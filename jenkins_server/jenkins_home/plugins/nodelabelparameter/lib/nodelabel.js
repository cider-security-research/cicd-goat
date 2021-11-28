// https://developer.mozilla.org/en-US/docs/Glossary/IIFE to make sure clean scope
(function () {
	function ready(fn) {
		if (document.readyState != 'loading') {
			fn();
		} else {
			document.addEventListener('DOMContentLoaded', fn);
		}
	};

	// https://caniuse.com/matchesselector
	function matches(el, selector) {
		return (el.matches || el.matchesSelector || el.msMatchesSelector || el.mozMatchesSelector || el.webkitMatchesSelector || el.oMatchesSelector).call(el, selector);
	};

	function show(el) {
		if (el == null) {
			return;
		}
		el.style.display = '';
	};

	function hide(el) {
		if (el == null) {
			return;
		}
		el.style.display = 'none';
	};

	ready(function () {
		var concurrentBuild = document.querySelector("input[type='checkbox'][name='_.concurrentBuild']");
		checkConcurrentExecutionValuesNode();
		checkConcurrentExecutionValuesLabel();

		concurrentBuild.addEventListener('change', function () {
			checkConcurrentExecutionValuesNode();
			checkConcurrentExecutionValuesLabel();
		});

		document.querySelector('input[type="radio"][name$=triggerIfResult]').addEventListener('change', function () {
			checkConcurrentExecutionValuesNode();
			checkConcurrentExecutionValuesLabel();
		});

		function checkConcurrentExecutionValuesNode() {
			if (matches(concurrentBuild, ":checked") && (document.querySelector('input[type="radio"][name$=triggerIfResult]:checked').value != "allowMultiSelectionForConcurrentBuilds")) {
				show(document.querySelector("#allowmultinodeselection"));
			} else if (!matches(concurrentBuild, ":checked") && (document.querySelector('input[type="radio"][name$=triggerIfResult]:checked').value == "allowMultiSelectionForConcurrentBuilds")) {
				show(document.querySelector("#allowmultinodeselection"));
			} else {
				hide(document.querySelector("#allowmultinodeselection"));
			}
		}

		function checkConcurrentExecutionValuesLabel() {
			if (matches(concurrentBuild, ":checked") && (document.querySelector('input[type="radio"][name$=triggerIfResult]:checked').value != "allCases")) {
				show(document.querySelector("#allowmultinodeselection_label"));
			} else {
				hide(document.querySelector("#allowmultinodeselection_label"));
			}
		}
	});
})();
