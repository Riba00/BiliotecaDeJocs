from getpass import getuser

import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader

# Escollim el template
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("llistaJocs.html")

# Obrim el XML
tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
games = tree.getroot()

jocs = []
dades = {}
dadesTemp = {}

for games in tree.iter("game"):
    for child in games.iter():
        if child.tag != "game":
            dades[child.tag] = child.text
        else:
            dades['idJoc'] = child.get('id')

    dadesTemp = dades.copy()
    dades.clear()
    jocs.append(dadesTemp)

# FITXER FINAL ON APLIQUEM LES DADES I AGAFEM LA BASE DEL HTML
file = open("llistaFinal.html", "w")
# ESCRIVIM EL CONTINGUT FINAL
llistatJocs = {"jocs":jocs}
contingut = template.render(llistatJocs)
file.write(contingut)

file.close()
