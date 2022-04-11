import { Component } from "./component.js";
import { Element } from "./element.js";
import { Attribute } from "./attribute.js";
import { contains, hasValue, isEmpty, sendMessage, socketio, print } from "./utils.js";
import { morph } from "./morph.js"

export var Meld = (function () {
  var meld = {};  // contains all methods exposed publicly in the meld object
  var messageUrl = "meld-message";
  var csrfTokenHeaderName = 'X-CSRFToken';
  var data = {};
  const components = {};

  /*
    Initializes the meld object.
    */
  meld.init = function (_messageUrl) {
    messageUrl = _messageUrl;

    socketio.on('meld-response', function(responseJson) {
      if (!responseJson) {
        return
      }
      if (responseJson.error) {
        console.error(responseJson.error);
        return
      }
      if (!components[responseJson.id])
        return
      else if(components[responseJson.id].actionQueue.length > 0)
        return

      if (responseJson.redirect) {
        window.location.href = responseJson.redirect.url;
      }



      updateData(components[responseJson.id], responseJson.data);
      var dom = responseJson.dom;

      var morphdomOptions = {
        childrenOnly: false,
        getNodeKey: function (node) {
          // A node's unique identifier. Used to rearrange elements rather than
          // creating and destroying an element that already exists.
          if (node.attributes) {
            var key = node.getAttribute("meld:key") || node.id;
            if (key) {
              return key;
            }
          }
        },
      }
      var componentRoot = $('[meld\\:id="' + responseJson.id + '"]');
      morph(componentRoot, dom);
      components[responseJson.id].refreshEventListeners()
    });

    socketio.on('meld-event', function(payload) {
      var event = new CustomEvent(payload.event, { detail: payload.message })
      document.dispatchEvent(event)
    });
  }

function updateData(component, newData){
  data = JSON.parse(newData);
  for (var key in data) {
    component.data[key] = data[key];
  }
}

/**
 * Checks if a string has the search text.
 */
function contains(str, search) {
  if (!str) {
    return false;
  }

  return str.indexOf(search) > -1;
}


/*
    Initializes the component.
    */
meld.componentInit = function (args) {
  const component = new Component(args);
  components[component.id] = component;
};
function toKebabCase(str) {
  if (!str) {
    return "";
  }

  const match = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  if (!match) {
    return str;
  }

  return match.map((x) => x.toLowerCase()).join("-");
}

/*
    Get the CSRF token used by Django.
    */
function getCsrfToken() {
  var csrfToken = "";
  var csrfElements = document.getElementsByName('csrfmiddlewaretoken');

  if (csrfElements.length > 0) {
    csrfToken = csrfElements[0].getAttribute('value');
  }

  if (!csrfToken) {
    console.error("CSRF token is missing. Do you need to add {% csrf_token %}?");
  }

  return csrfToken;
}

/*
    Traverse the DOM looking for child elements.
    */
function walk(el, callback) {
  var walker = document.createTreeWalker(el, NodeFilter.SHOW_ELEMENT, null, false);

  while (walker.nextNode()) {
    // TODO: Handle sub-components
    callback(walker.currentNode);
  }
}

/*
    A simple shortcut for querySelector that everyone loves.
    */
function $(selector, scope) {
  if (scope == undefined) {
    scope = document;
  }

  return scope.querySelector(selector);
}

return meld;
}());
