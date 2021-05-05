import os
import PIL
import numpy as np
from json import load
from requests import get
from random import choice
from textwrap import wrap
from platform import system
from string import printable
from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__
__version__		= "1.1"
__date__		= "16.10.2020"
__status__		= "Development"
__license__		= "GPL v1"

# 
exec(open("Scripts/Utils.pyw").read())		# import Scripts/Utils.py
print("Setting up utils...")

exec(open("Scripts/Title.pyw").read())		# import Scripts/Title.py
print("Creating title...")

exec(open("Scripts/Content.pyw").read())	# import Scripts/Content.py
print("Creating content...")

exec(open("Scripts/Picture.pyw").read())	# import Scripts/Picture.py
print("Creating image...")

exec(open("Scripts/Paste.pyw").read())		# import Scripts/Paste.py
print("Applying contents...")

__Path = "Images/{0}_{1}.{2}"

Demotivational_Crop.save(__Path.format(
	Config()["Content"]["Title" if Config()["Content"]["Title"] != "" else "Text"].\
		replace(" ", "_").\
		replace("\\", "_").\
		replace("/", "_").\
		replace(":", "_").\
		replace("*", "_").\
		replace("?", "_").\
		replace("<", "_").\
		replace(">", "_").\
		replace("|", "_").\
		encode().decode("utf-8", errors = "strict"),
	Random_String(8), "jpg"), quality = Config()["Quality"]
	)

print("Done!")