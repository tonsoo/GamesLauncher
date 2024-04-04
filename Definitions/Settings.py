from pathlib import Path
import os
import os.path
from tkinter import *
from PIL import ImageTk, Image

def BuildPath(path:str, start:str = '') -> str:
    if(start):
        start = f"{start}{os.sep}"

    return f"{start}{path.replace('/', os.sep)}"

def IsFile(path:str) -> bool:
    fixedPath = BuildPath(path)

    return os.path.isfile(fixedPath)

def DynamicImport(structure:str, module:str):
    try:
        importFile = __import__(f"{structure}.{module}", fromlist=[module])
        fileClass = getattr(importFile, module)

        return fileClass
    except:
        print(f'Não foi possivel incluir "{structure}.{module}"')
    
    return None

ROOT_DIR = Path(__file__).parent.parent
FILES_DIR = BuildPath(f"Files", start=ROOT_DIR)
PAGES_DIR = BuildPath(f"Classes/Generics/Pages/", start=ROOT_DIR)
GAMES_DIR = BuildPath(f"Classes/Games/", start=ROOT_DIR)

GAMES_API_URL = 'https://games.nareke.com.br/'

COLORS = {
    '1':'#030301',
    '1-1':'#80817F',
    '2':'#19647E',
    '2-1':'#0E3440',
    '3':'#EDAE49',
    '4':'#AB81CD',
    '5':'#FCFFFD',
}

def LoadImage(path:str, x:int=100, y:int=100):
    imagePath = BuildPath(path, start=FILES_DIR)
    imageFile = Image.open(imagePath).resize((x,y))
    print(f"rendering: {imagePath}")
    return ImageTk.PhotoImage(imageFile)