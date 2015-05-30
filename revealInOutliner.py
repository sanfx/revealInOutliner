# -*-coding: utf8-*-
# file: revealInOutliner.py
# Date: 2009

""" To reveal the selected object in outliser when scene in maya veiwport is
	very complex. press ctrl while clicking on shelfbar button to open hypershade
	and graph the selected objects material and shading network.

	If you find it useful, please share your comments on asksan@live.ca
"""

import maya.cmds as cmds
import maya.mel as mel

__version__ = "0.2"
__author__ = "Sanjeev Kumar"
__contact__ = "asksan@live.ca"



def _graphMatSelObj():
	mel.eval('evalDeferred "hyperShadePanelGraphCommand hyperShadePanel1 graphMaterials"')

def run(mod=None):
	"""	open outlier and select the node in outliner that is selected in veiwport.
		if Control Key is pressed on keyboard then open hypershade and graphs the material
		of selected object.

		Kwargs:
			:param mod: key modifer pressed
			:type mod: int
	"""
	mod = cmds.getModifiers()
	if mod == 4:
		print "Ctrl pressed", mod
		# show hypershade
		if _isobjectInList(cmds.getPanel(vis=1), 'hyperShade'):
			_graphMatSelObj()
		else:
			print "Hypershade is not open"
			cmds.HypershadeWindow()
			_graphMatSelObj()

	else:
		# show Outliner
		_openOutliner()

def _isobjectInList(lst, name, criterion='startswith'):
	""" Find item in the list  startrting or ending with name passed.

		Args:
			:param lst: list of items/ objects
			:type lst: list

			:param name: name starting or ending with.
			:type name: string

		Kwargs:
			:param criterion: function of string obect whether startswith or endswith
			:type criterion: method of str object
	"""
	for itemfound in lst:
		if getattr(itemfound, criterion)(name):
			return True

def _openOutliner():

	outliners = cmds.getPanel(typ='outlinerPanel')
	panl = str(outliners[0])
	if _isobjectInList(cmds.getPanel(vis=1), 'outliner'):
		cmds.evalDeferred("import maya.cmds as cmds;cmds.outlinerEditor('%s', e=1, sc=1);" % panl)
	else:
		cmds.OutlinerWindow()
		cmds.evalDeferred("import maya.cmds as cmds; cmds.outlinerEditor('%s', e=1, sc=1);" % panl)
		cmds.evalDeferred("cmds.outlinerEditor('%s', e=1, sc=1);" % panl)







print "\nRevealInOutliner script by Sanjeev Kumar"
