from pathlib import Path
from pprint import pprint
import sys
import configparser
toto


def add_app_setting(file :str, app : str) -> bool:
    word_to_be_find = "INSTALLED_APPS = ["
    word_found = False
    installed_apps = ""
    lines = ""
    with open(file , "r") as f:
        lines = f.readlines()
        for line in lines:
            if word_to_be_find in line:
                word_found = True
                word_to_be_find = "]\n"
            if word_found:
                installed_apps += f"{line}"
                if line == word_to_be_find:
                    break
    installed_apps = installed_apps.replace("]\n",f"    '{app}',\n]\n")
    for line in installed_apps.split("\n"):
        print(line)


dossier_courant = Path.cwd()
file_manage = dossier_courant / "manage.py"

#verification si on est bien dans le mçme dossier que manage.py
if not file_manage.exists():
    print("Mauvais dossier, le script doit ses trouvé dans le même réperoire que manage.py")
    exit()

#recupération du nom de l'app
try:
    app = sys.argv[1]
except Exception:
    print("Erreur vous devez indiquez le nom d'une apps")
    exit()


# verification le dossier de l'app exist
dir_app = dossier_courant / app
if not dir_app.exists():
    print(f"le dossier '{dir_app}' de votre app n'existe pas")
    exit()

#recuperation du nom d projets dans manage.py
file_manage = dossier_courant / "manage.py"
with open(file_manage, "r") as f:
    lines = f.readlines()

for line in lines:
    if "os.environ.setdefault" in line:
        projet = line.replace("os.environ.setdefault('DJANGO_SETTINGS_MODULE', '","")
        projet = projet.replace(".settings')","")
        projet = projet.replace(" ","")
        projet = projet.replace("\n","")
        break

# creation des fichier et repertoire
file_a_creer = [
   {"path":dossier_courant / app / "urls.py" ,"data":
"""
from django.urls import path
from django.views.defaults import server_error
urlpatterns = [
    #path('', index, name="index")
]
""" ,"type":"file"},
   {"path":dossier_courant / app / "templates" / app,"data":"" ,"type":"dir"},
   {"path":dossier_courant / app / "static" / "css" / app ,"data":"" ,"type":"dir"},
   {"path":dossier_courant / app / "static" / "css" / app / "style.css","data":"" ,"type":"file"},
   {"path":dossier_courant / app / "static" / "script" / app,"data":"" ,"type":"dir"}
]

for file in file_a_creer:
    path = Path(file["path"])
    if not path.exists():
        print(f"création de '{path}'")
        if file["type"] == "file":
            path.touch()
            if file["data"]:
                path.write_text(file["data"])
        if file["type"] == "dir":
           path.mkdir(parents=True) 
    else:
        print(f"'{path}' existe déjà")
"""   
#modification du fichier setting
file_setting = dossier_courant / projet / "settings.py"
file_setting = dossier_courant / "settings.py"
#recherche de la lignes Templates

add_app_setting(file_setting,"newblog")
"""

