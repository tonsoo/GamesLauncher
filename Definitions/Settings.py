from pathlib import Path
import os
import os.path

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
        print(f'Não foi possivel incluir "{importFile}"')
    
    return None

ROOT_DIR = Path(__file__).parent.parent
FILES_DIR = BuildPath(f"Files", start=ROOT_DIR)
PAGES_DIR = BuildPath(f"Classes/Generics/Pages/", start=ROOT_DIR)
GAMES_DIR = BuildPath(f"Classes/Games/", start=ROOT_DIR)

GAMES_API_URL = 'https://games.nareke.com.br/'