import {$, walk, hasValue, isEmpty, sendMessage, print, debounce, socketio, handleLoading} from "./utils.js";
import { Element } from "./element.js";

export class Component {
  constructor(args) {
    this.id = args.id;
    this.name = args.name;
    this.messageUrl = args.messageUrl;
    this.csrfTokenHeaderName = args.csrfTokenHeaderName;

    if (this.name.includes(".")) {
      const names = this.name.split(".");
      this.name = names[names.length - 2];
    }

    this.data = args.data;

    this.document = args.document || document;
    this.walker = args.walker || walk;

    this.root = undefined;
    this.modelEls = [];
    this.keyEls = [];
    this.loadingEls = [];

    this.actionQueue = [];
    this.activeDebouncers = 0

    this.actionEvents = {};
    this.attachedEventTypes = [];
    this.attachedModelEvents = [];
    this.attachedCustomEvents = [];

    this.init();
    this.refreshEventListeners();
  }

  checkComponentDefer(element, action){
      if (element.model.isDefer) {
          let foundAction = false;

          // Update the existing action with the current value
          this.actionQueue.forEach((a) => {
            if (a.payload.name === element.model.name) {
              a.payload.value = element.getValue();
              foundAction = true;
            }
          });

          // Add the action if not already in the queue
          if (!foundAction) {
            this.actionQueue.push(action);
          }
          return;
      }
    else{
      this.actionQueue.push(action);
      this.queueMessage(element.model);
    }
  }

  addModelEventListener(component, el, eventType) {
    el.addEventListener(eventType, (event) => {
      const element = new Element(event.target, component);

      const action = {
        type: "syncInput",
        payload: {
          name: element.model.name,
          value: element.getValue(),
        },
      };

      this.checkComponentDefer(element, action);
    });
  }

  /**
   * Adds an action event listener to the document for each type of event (e.g. click, keyup, etc).
   * Added at the document level because validation errors would sometimes remove the
   * events when attached directly to the element.
   * @param {Component} component Component that contains the element.
   * @param {string} eventType Event type to listen for.
   */
  addActionEventListener(component, eventType) {
    component.document.addEventListener(eventType, (event) => {
      let targetElement = new Element(event.target, component);

      // Make sure that the target element is a meld element.
      if (targetElement && !targetElement.isMeld) {
        targetElement = targetElement.getMeldParent();
      }

      if (
        targetElement &&
        targetElement.isMeld &&
        targetElement.actions.length > 0
      ) {
        component.actionEvents[eventType].forEach((actionEvent) => {
          const { action } = actionEvent;
          const { element } = actionEvent;

          if (targetElement.isSame(element)) {
            if (action.isPrevent) {
              event.preventDefault();
            }

            if (action.isStop) {
              event.stopPropagation();
            }

            var method = { type: "callMethod", payload: { name: action.name } };


            if (action.key) {
              if (action.key === event.key.toLowerCase()) {
                this.actionQueue.push(method);
                this.queueMessage(element.model);
                handleLoading(component, targetElement);
              }
            } else {
                this.actionQueue.push(method);
                this.queueMessage(element.model);
                handleLoading(component, targetElement);
            }
          }
        });
      }
    });
  }

  /**
   * Adds a custom event listener to the document for the given eventName.
   * @param {string} eventName Name of the custom meld-event to be listened for
   * @param {string} funcName Name of the method to call on the Python Component
   */
  addCustomEventListener(eventName, funcName) {
    this.document.addEventListener(eventName, (event) => {
      const element = new Element(event.target, this);
      var method = { type: "callMethod", payload: { name: funcName, message: event.detail } };
      this.actionQueue.push(method);
      this.queueMessage(element.model);
    });
  }

  queueMessage(model, callback) {
    this.activeDebouncers += 1
    if (model.debounceTime === -1) {
      debounce(sendMessage, 150, this, false)(this, callback);
    } else {
      debounce(sendMessage, model.debounceTime, this, false)(this, callback);
    }
  }



  /**
   * Initializes the Component.
   */
  init() {
    this.root = $(`[meld\\:id="${this.id}"]`, this.document);

    if (!this.root) {
      throw Error("No id found");
    }

    /**
     * Add the custom listeners from the python class
     * This separate helper function is needed because "this" doesn't
     * work in the socketio.emit callback (it refers to the socketio
     * object).
     */
    function addListeners(component, response) {
      Object.entries(response).forEach(([eventName, funcNames]) => {
        component.attachedCustomEvents.push(eventName)
        funcNames.forEach((funcName) => {
          component.addCustomEventListener(eventName, funcName)
        })
      })
    }

    socketio.emit(
      'meld-init', this.name,
      (response) => addListeners(this, response)
    )
  }

  refreshEventListeners() {
    this.actionEvents = {};
    this.modelEls = [];
    this.dbEls = [];

    walk(this.root, (el) => {
      if (el.isSameNode(this.root)) {
        // Skip the component root element
        return;
      }

      const element = new Element(el, this);

      if (element.isMeld) {
         if ( hasValue(element.model)) {
          if (!this.attachedModelEvents.some((e) => e.isSame(element))) {
            this.attachedModelEvents.push(element);
            this.addModelEventListener(this, element.el, element.model.eventType);
          }

          if (!this.modelEls.some((e) => e.isSame(element))) {
            this.modelEls.push(element);
          }
        } else if (hasValue(element.loading)) {
          this.loadingEls.push(element);

          // Hide loading elements that are shown when an action happens
          if (element.loading.show) {
            element.hide();
          }
        }

        if (hasValue(element.key)) {
          this.keyEls.push(element);
        }

        element.actions.forEach((action) => {
          if (this.actionEvents[action.eventType]) {
            this.actionEvents[action.eventType].push({ action, element });
          } else {
            this.actionEvents[action.eventType] = [{ action, element }];

            if (
              !this.attachedEventTypes.some((et) => et === action.eventType)
            ) {
              this.attachedEventTypes.push(action.eventType);
              this.addActionEventListener(this, action.eventType);
            }
          }
        });
      }
    });
  }
}

