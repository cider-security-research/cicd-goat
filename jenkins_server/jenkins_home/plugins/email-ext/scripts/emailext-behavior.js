
function hideElement(elmID)
{
	var elm = document.getElementById(elmID);
	elm.style.display = "none";
}

function showElement(elmID)
{
	var elm = document.getElementById(elmID);
	elm.style.display = "";
}

function swapEdit(swapName)
{
	var editID = swapName+"edit";
	var hideID = swapName+"hide";
	var elmID = swapName+"elm";
	var elm = document.getElementById(elmID);
	
	
	if(elm.style.display == "none")
	{
		showElement(hideID);
		showElement(elmID);
		hideElement(editID);
	}
	else
	{
		hideElement(hideID);
		hideElement(elmID);
		showElement(editID);
	}
}

function switchElementContainer(oldParent,newParent,child)
{
	if(!child)
		return;
	oldParent.removeChild(child);
	newParent.appendChild(child);
}

function selectTrigger(selectElement,secId)
{
	var selInd = selectElement.selectedIndex;
	
	if(selInd == 0)
		return;
	
	var triggerOption = selectElement.options[selInd];
	var mailerId = triggerOption.value;
	
	selectElement.selectedIndex = 0;

	addTrigger(mailerId,secId);
}

function addTrigger(mailerId,secId)
{
	var configId = secId+"mailer."+mailerId+".configured";
	mailerId = secId + mailerId;
	var nonConfigTriggers = document.getElementById(secId+"non-configured-email-triggers");
	var triggerRow = document.getElementById(mailerId);
	var configTriggers = document.getElementById(secId+"configured-email-triggers");
	var afterThisElement = document.getElementById(secId+"after-last-configured-row");
	
	if(!triggerRow || !document.getElementById(configId))
		return;
	
	nonConfigTriggers.removeChild(triggerRow);
	configTriggers.insertBefore(triggerRow,afterThisElement);
	triggerRow.style.display="";
	
	var triggerHelp = document.getElementById(mailerId+"help");
	nonConfigTriggers.removeChild(triggerHelp);
	configTriggers.insertBefore(triggerHelp,afterThisElement);
	
	var triggerAdv = document.getElementById(mailerId+"elm");
	nonConfigTriggers.removeChild(triggerAdv);
	configTriggers.insertBefore(triggerAdv,afterThisElement);
	
	var nonConfigOptions = document.getElementById(secId+"non-configured-options");
	var configOptions = document.getElementById(secId+"configured-options");
	var option = document.getElementById(mailerId + "option");
	switchElementContainer(nonConfigOptions,configOptions,option);
	
	document.getElementById(configId).value = "true";
}

function removeTrigger(mailerId,secId)
{
	document.getElementById(secId+"mailer."+mailerId+".configured").value = "false";
	mailerId = secId + mailerId;

	var nonConfigTriggers = document.getElementById(secId+"non-configured-email-triggers");
	var triggerRow = document.getElementById(mailerId);
	var configTriggers = document.getElementById(secId+"configured-email-triggers"); 
	switchElementContainer(configTriggers,nonConfigTriggers,triggerRow);

	var triggerHelp = document.getElementById(mailerId+"help");
	switchElementContainer(configTriggers,nonConfigTriggers,triggerHelp);

	var triggerAdv = document.getElementById(mailerId+"elm");
	switchElementContainer(configTriggers,nonConfigTriggers,triggerAdv);

	var nonConfigOptions = document.getElementById(secId+"non-configured-options");
	var configOptions = document.getElementById(secId+"configured-options");
	var option = document.getElementById(mailerId + "option");
	configOptions.removeChild(option);

	// Reinsert in alphabetical order (skipping the generic 'select' option at the top).
	var before = null;
	for (var i = 1; i < nonConfigOptions.options.length; i++) {
		var curOption = nonConfigOptions.options[i];
		if (curOption.id && curOption.value > option.value) {
			before = nonConfigOptions.options[i];
			break;
		}
	}
	nonConfigOptions.insertBefore(option, before);
	
	if(triggerAdv.style.display != "none")
		swapEdit(mailerId);
	
	if(triggerHelp.style.display != "none")
		triggerHelp.style.display="none";
		
	nonConfigOptions.selectedIndex = 0;
}

function toggleMailHelp(mailerId)
{
	var mailHelpRow = document.getElementById(mailerId+"help");
	mailHelpRow.style.display = (mailHelpRow.style.display=="none") ? "" : "none";
}

function toggleContentTokenHelp(secId)
{
	var mailHelp = document.getElementById(secId+"contentTokenHelpConf");
	mailHelp.style.display = (mailHelp.style.display=="none") ? "block" : "none";
}
