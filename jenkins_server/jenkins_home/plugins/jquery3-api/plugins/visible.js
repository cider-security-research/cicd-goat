/*
 * Visible.js -- jQuery Visible/Unvisible Plug-in.
 *
 * Version 2.0.3.
 *
 * Copyright (c) 2017-2018 Dmitry Zavodnikov.
 *
 * Licensed under the MIT License.
 */
(function($) {

    var BECAME_VISIBLE_MESSAGE   = 'becameVisible';
    var BECAME_UNVISIBLE_MESSAGE = 'becameUnvisible';

    var unvisibleSet = [];

    function isVisible(element) {
        return $(element).is(':visible');
    }

    function inUnvisibleSet(element) {
        return unvisibleSet.indexOf(element) !== -1;
    }

    function isElement(element) {
        return element.nodeType === 1;
    }

    function addToUnvisibleSet(element) {
        if (!inUnvisibleSet(element) && isElement(element)) {
            unvisibleSet.push(element);
        }
    }

    function removeFromUnvisibleSet(element) {
        var idx = unvisibleSet.indexOf(element);
        if (idx != -1) {
            unvisibleSet.splice(idx, 1);
        }
    }

    function initUnvisibleSet(element) {
        element.childNodes.forEach(function(child) {
            if (!isVisible(child)) {
                sendMessage(child, BECAME_UNVISIBLE_MESSAGE);

                addToUnvisibleSet(child);
            } else {
                sendMessage(child, BECAME_VISIBLE_MESSAGE);

                initUnvisibleSet(child);
            }
        });
    }

    function sendMessage(element, msg) {
        $(element).trigger(msg);
    }

    function sendTreeMessage(element, msg) {
        sendMessage(element, msg);

        element.childNodes.forEach(function(child) {
            sendTreeMessage(child, msg);
        });
    }

    function becameVisible(element) {
        removeFromUnvisibleSet(element);

        sendTreeMessage(element, BECAME_VISIBLE_MESSAGE);
    }

    function becameUnvisible(element) {
        addToUnvisibleSet(element);

        sendTreeMessage(element, BECAME_UNVISIBLE_MESSAGE);
    }

    function bindVisibleUnvisible() {
        /* See:
         *      http://blog.whiteoctober.co.uk/2012/12/07/keeping-track-of-dom-manipulation/
         *      https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver?redirectlocale=en-US&redirectslug=DOM%2FDOM_Mutation_Observers
         */
        // Select the target element.
        var target = document.getElementsByTagName('body')[0];

        // Choose browser-specific MutationObserver.
        var MutationObserver = window.MutationObserver || window.WebKitMutationObserver || window.MozMutationObserver;

        // Create an observer instance.
        var observer = new MutationObserver(function(mutations) {
            mutations.map(function(mutation) {
                return mutation.target;
            }).forEach(function(element) {
                if (inUnvisibleSet(element)) {
                    if (isVisible(element)) {
                        becameVisible(element);
                    }
                } else {
                    if (!isVisible(element)) {
                        becameUnvisible(element);
                    }
                }
            });
        });

        // Configuration of the observer.
        var config = {
            childList:              false,
            attributes:             true,
            characterData:          false,
            subtree:                true,
            attributeOldValue:      false,
            characterDataOldValue:  false,
            attributeFilter:        ['class', 'style']
        };

        // Pass in the target element, as well as the observer options.
        observer.observe(target, config);
    }

    document.addEventListener('DOMContentLoaded', function() {
        initUnvisibleSet(document.getElementsByTagName('body')[0]);

        bindVisibleUnvisible();
    });
}(jQuery));
