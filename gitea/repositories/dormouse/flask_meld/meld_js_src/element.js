import { print, hasValue} from "./utils.js";
import { Attribute } from "./attribute.js";

/**
 * Encapsulate DOM element for Meld-related information.
 */
export class Element {
  constructor(el, component) {
    this.el = el;
    this.component = component
    this.init();
  }

  /**
   * Check if another `Element` is the same as this `Element`.
   * @param {Element} other
   */
  isSame(other) {
    // Use isSameNode (not isEqualNode) because we want to check the nodes reference the same object
    return this.el.isSameNode(other.el);
  }

  /**
   * Gets the value from the element.
   */
  getValue() {
    let { value } = this.el;
    let component = this.component

    if (this.el.type) {
      if (this.el.type.toLowerCase() === "checkbox") {
        let modelValue = component.data[this.model.name]
        // Handle checkbox
        if (Array.isArray(modelValue)) {
          modelValue = this.mergeCheckboxValueIntoArray(this.el, modelValue)
          return modelValue;
        }
        if (this.el.value != "on"){
          if (!this.el.checked){
            return ""
          }
          return this.el.value
        }
        return this.el.checked;
      } else if (this.el.type.toLowerCase() === "select-multiple") {
        // Handle multiple select options
        value = [];
        for (let i = 0; i < this.el.selectedOptions.length; i++) {
          value.push(this.el.selectedOptions[i].value);
        }
      }
    }

    return value;
  }
    mergeCheckboxValueIntoArray(el, arrayValue) {
        if (el.checked) {
          return arrayValue.concat(el.value)
        }

        return arrayValue.filter(item => item !== el.value)
    }
  /**
   * Get the element's next parent that is a meld element.
   *
   * Returns `null` if no meld element can be found before the root.
   */
  getMeldParent() {
    let parentElement = this.parent;

    while (parentElement && !parentElement.isMeld) {
      parentElement = parentElement.parent;
    }

    return parentElement;
  }

  /**
   * Init the element.
   */
  init() {
    this.id = this.el.id;
    this.isMeld= false;
    this.attributes = [];
    this.parent = null;

    if (this.el.parentElement) {
      this.parent = new Element(this.el.parentElement);
    }

    this.model = {};
    this.poll = {};
    this.loading = {};
    this.actions = [];
    this.db = {};
    this.field = {};
    this.target = null;
    this.key = null;
    this.errors = [];

    if (!this.el.attributes) {
      return;
    }

    for (let i = 0; i < this.el.attributes.length; i++) {
      const attribute = new Attribute(this.el.attributes[i]);
      this.attributes.push(attribute);

      if (attribute.isMeld) {
        this.isMeld= true;
      }

      if (attribute.isModel) {
        this.model.name = attribute.value;
        this.model.eventType = attribute.modifiers.lazy ? "blur" : "input";
        this.model.isLazy = !!attribute.modifiers.lazy;
        this.model.isDefer = !!attribute.modifiers.defer;
        this.model.debounceTime = attribute.modifiers.debounce
          ? parseInt(attribute.modifiers.debounce, 10) || -1
          : -1;
      } else if (attribute.isField) {
        this.field.name = attribute.value;
        this.field.eventType = attribute.modifiers.lazy ? "blur" : "input";
        this.field.isLazy = !!attribute.modifiers.lazy;
        this.field.isDefer = !!attribute.modifiers.defer;
        this.field.debounceTime = attribute.modifiers.debounce
          ? parseInt(attribute.modifiers.debounce, 10) || -1
          : -1;
      } else if (attribute.isDb) {
        this.db.name = attribute.value;
      } else if (attribute.isPK) {
        this.db.pk = attribute.value;
      } else if (attribute.isPoll) {
        this.poll.method = attribute.value ? attribute.value : "refresh";
        this.poll.timing = 2000;

        const pollArgs = attribute.name.split("-").slice(1);

        if (pollArgs.length > 0) {
          this.poll.timing = parseInt(pollArgs[0], 10) || 2000;
        }
      } else if (attribute.isLoading) {
        if (attribute.modifiers.attr) {
          this.loading.attr = attribute.value;
        } else if (attribute.modifiers.class && attribute.modifiers.remove) {
          this.loading.removeClasses = attribute.value.split(" ");
        } else if (attribute.modifiers.class) {
          this.loading.classes = attribute.value.split(" ");
        } else if (attribute.modifiers.remove) {
          this.loading.hide = true;
        } else {
          this.loading.show = true;
        }
      } else if (attribute.isTarget) {
        this.target = attribute.value;
      } else if (attribute.eventType) {
        const action = {};
        action.name = attribute.value;
        action.eventType = attribute.eventType;
        action.isPrevent = false;
        action.isStop = false;

        if (attribute.modifiers) {
          Object.keys(attribute.modifiers).forEach((modifier) => {
            if (modifier === "prevent") {
              action.isPrevent = true;
            } else if (modifier === "stop") {
              action.isStop = true;
            } else {
              action.key = modifier;
            }
          });
        }

        this.actions.push(action);
      }

      if (attribute.isKey) {
        this.key = attribute.value;
      }
    }
  }
  /**
   * Hide the element.
   */
  hide() {
    this.el.hidden = "hidden";
  }

  /**
   * Show the element.
   */
  show() {
    this.el.hidden = null;
  }

  /**
   * Handle loading for the element.
   */
  handleLoading() {
    this.handleInterfacer("loading");
  }

  /**
   * Handle interfacers for the element.
   * @param {string} interfacerType The type of interfacer. Either "dirty" or "loading".
   * @param {bool} revert Whether or not the revert the interfacer.
   */
  handleInterfacer(interfacerType, revert) {
    revert = revert || false;

    if (hasValue(this[interfacerType])) {
      if (this[interfacerType].attr) {
        if (revert) {
          this.el.removeAttribute(this[interfacerType].attr);
        } else {
          this.el.setAttribute(
            this[interfacerType].attr,
            this[interfacerType].attr
          );
        }
      }

      if (this[interfacerType].classes) {
        if (revert) {
          this.el.classList.remove(...this[interfacerType].classes);

          // Remove the class attribute if it's empty so that morphdom sees the node as equal
          if (this.el.classList.length === 0) {
            this.el.removeAttribute("class");
          }
        } else {
          this.el.classList.add(...this[interfacerType].classes);
        }
      }

      if (this[interfacerType].removeClasses) {
        if (revert) {
          this.el.classList.add(...this[interfacerType].removeClasses);
        } else {
          this.el.classList.remove(...this[interfacerType].removeClasses);
        }
      }
    }
  }
}
