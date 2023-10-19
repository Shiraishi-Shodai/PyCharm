import requests
from bs4 import BeautifulSoup
from pathlib import Path
import tkinter as tk
import PIL.Image
import PIL.ImageTk
import os
import glob
import tkinter.filedialog as fd


dir_path = "C:/Users/shodai/Pictures/Screenshots/"
file_list = glob.glob("tkImage/*.png")
print(file_list)

for i in file_list:
    newImage = PIL.Image.open(i).convert("L")
    newImage.save(i)


