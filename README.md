# revealInOutliner 
==================
![Reveal In Outliner or hypershade]
(https://img.shields.io/badge/revealInOutliner-Ver: 0.2-green.svg?style=flat-square)

![Python Version]
(https://img.shields.io/badge/Python-2.7-green.svg?style=flat-square)




![Maya - Python]
(http://www.creativecrash.com/system/photos/000/246/872/246872/big/740071361.png?1348471615)

# What it does ?
================
Reveals selected object in maya outliner massive tree with just single click.
This script does the same thing as doing opening outliner, click on Display > Reveal selected,
except this script does these 3 steps in just one click.

In addition, you can also press CTRL key while clicking on shelfbar button to open hypershade  and graph
the selected objects material and shading network.


# Install Instruction
=====================
1. copy the downloaded revealInOutliner.py in maya scripts folder
2. In maya create a python button in shelf with the below 6 lines.

	```python
	try:
		reload(revealInOutliner)
		revealInOutliner.run()
	except NameError:
		import revealInOutliner
		revealInOutliner.run()
	```

