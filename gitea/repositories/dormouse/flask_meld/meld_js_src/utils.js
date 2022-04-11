export var socketio = io();
/*
    Handles calling the message endpoint and merging the results into the document.
    */
export function sendMessage(component) {
  // Prevent network call when there isn't an action
  if (component.actionQueue.length === 0) {
    return;
  }

  // Prevent network call when the action queue gets repeated
  if (component.currentActionQueue === component.actionQueue) {
    return;
  }

  component.currentActionQueue = component.actionQueue;
  component.actionQueue = [];

  socketio.emit('meld-message', {'id': component.id, 'actionQueue': component.currentActionQueue, 'componentName': component.name, 'data': component.data});
}

/**
 * Handles loading elements in the component.
 * @param {Component} component Component.
 * @param {Element} targetElement Targetted element.
 */
export function handleLoading(component, targetElement) {
  targetElement.handleLoading();

  // Look at all elements with a loading attribute
  component.loadingEls.forEach((loadingElement) => {
    if (loadingElement.target) {
      let targetedEl = $(`#${loadingElement.target}`, component.root);

      if (!targetedEl) {
        component.keyEls.forEach((keyElement) => {
          if (!targetedEl && keyElement.key === loadingElement.target) {
            targetedEl = keyElement.el;
          }
        });
      }

      if (targetedEl) {
        if (targetElement.el.isSameNode(targetedEl)) {
          if (loadingElement.loading.hide) {
            loadingElement.hide();
          } else if (loadingElement.loading.show) {
            loadingElement.show();
          }
        }
      }
    } else if (loadingElement.loading.hide) {
      loadingElement.hide();
    } else if (loadingElement.loading.show) {
      loadingElement.show();
    }
  });
}

/*
Traverse the DOM looking for child elements.
*/
export function walk(el, callback) {
  var walker = document.createTreeWalker(el, NodeFilter.SHOW_ELEMENT, null, false);

  while (walker.nextNode()) {
    // TODO: Handle sub-components
    callback(walker.currentNode);
  }
}

/*
A simple shortcut for querySelector that everyone loves.
*/
export function $(selector, scope) {
  if (scope == undefined) {
    scope = document;
  }

  return scope.querySelector(selector);
}

/**
 * Checks if a string has the search text.
 */
export function contains(str, search) {
  if (!str) {
    return false;
  }

  return str.indexOf(search) > -1;
}

/**
 * Checks if an object has a value.
 */
export function hasValue(obj) {
  return !isEmpty(obj);
}

/**
 * Checks if an object is empty. Useful to check if a dictionary has a value.
 */
export function isEmpty(obj) {
  return (
    typeof obj === "undefined" ||
    obj === null ||
    (Object.keys(obj).length === 0 && obj.constructor === Object)
  );
}

/*
    Allow python print
    */
export function print(msg) {
  var args = [].slice.apply(arguments).slice(1);
  console.log(msg, ...args);
}

/**
 * Returns a function, that, as long as it continues to be invoked, will not
 * be triggered. The function will be called after it stops being called for
 * N milliseconds. If `immediate` is passed, trigger the function on the
 * leading edge, instead of the trailing.
 * Derived from underscore.js's implementation in https://davidwalsh.name/javascript-debounce-function.
 */
export function debounce(func, wait, component, immediate) {
  let timeout;

  if (typeof immediate === "undefined") {
    immediate = true;
  }

  return (...args) => {
    const context = this;

    const later = () => {
      timeout = null;
      if (!immediate) {
        if (component.activeDebouncers === 1){
          component.activeDebouncers = 0;
          func.apply(context, args);
        }
        else{
          component.activeDebouncers -= 1;
        }
      }
    };

    const callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);

    if (callNow) {
      func.apply(context, args);
    }
  };
}
