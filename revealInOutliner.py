import maya.cmds as cmds
import maya.mel as mel
import maya.utils

__version__=1.01
__author__="Sanjeev Kumar"
__contact__="asksan@live.ca"



def GraphMatSelObj():
    mel.eval('evalDeferred "hyperShadePanelGraphCommand hyperShadePanel1 graphMaterials"')

def run(mod=None):
    """
    import revealInOutliner.run() to reveal selected object in complex scene.
    press ctrl while clicking on shelfbar button to open hypershade and graph
    the selected objects material and shading network.
    """
    mod = cmds.getModifiers()
    if mod == 4:
        print("Ctrl pressed", mod)
        # show hypershade
        if 'hyperShadePanel1' in cmds.getPanel(vis=1):
            GraphMatSelObj()
        else:
            print("Hypershade is not open")
            cmds.HypershadeWindow()
            GraphMatSelObj()

    else:
        # show Outliner
        OpenOutliner()





def OpenOutliner():

    outliners =cmds.getPanel(typ='outlinerPanel')
    panl=str(outliners[0])
    if 'outlinerPanel1' in cmds.getPanel(vis=1):
        cmds.evalDeferred("import maya.cmds as cmds;cmds.outlinerEditor('"+panl+"', e=1, sc=1);")
    else:
        cmds.OutlinerWindow()
        cmds.evalDeferred("import maya.cmds as cmds;cmds.outlinerEditor('"+panl+"', e=1, sc=1);")
        cmds.evalDeferred("cmds.outlinerEditor('"+panl+"', e=1, sc=1);")







print("\nRevealInOutliner script by Sanjeev Kumar)