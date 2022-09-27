import os.path
from getpass import getuser

import xml.etree.ElementTree as ET


def menuInicial():
    bucleInici = 5
    while bucleInici > 0:
        print("BIBLIOTECA DE JOCS")
        print()
        print("1- Insertar joc")
        print("2- Llistar jocs")
        print("3- Mostrar dades d'un joc")
        print("4- Modificar un joc")
        print("5- Eliminar joc")
        print("6- Sortir")
        respostaInicial = int(input("Resposta: "))

        if respostaInicial == 1:
            insertarJoc()

        if respostaInicial == 2:
            llistarJocs()

        if respostaInicial == 3:
            mostrarDadesJoc()

        if respostaInicial == 5:
            eliminarJoc()

        if respostaInicial == 6:
            print("Adeu, fins la pròxima")
            bucleInici = 0


def mostrarDadesJoc():
    tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
    arrel = tree.getroot()
    print("DADES DEL JOC")
    print("-------------")
    idMostrarJoc = input("ID del joc a mostrar: ")
    for game in arrel.findall("game"):
        id = game.get("id")
        if int(id) == int(idMostrarJoc):
            nomMostrarJoc = game.find("name").text.strip()
            yearMostrarJoc = game.find("year").text.strip()
            sistemesMostrarJoc = game.find("systems").text.strip()
            desenvolupadorMostrarJoc = game.find("developer").text.strip()
            genereMostrarJoc = game.find("genre").text.strip()
            descripcioMostrarJoc = game.find("description").text.strip()
            urlImatgeMostrarJoc = game.find("imageURL").text.strip()
            print(id, nomMostrarJoc, yearMostrarJoc, sistemesMostrarJoc, desenvolupadorMostrarJoc, genereMostrarJoc,
                  descripcioMostrarJoc, urlImatgeMostrarJoc)


def eliminarJoc():
    print("ELIMINAR JOC")
    print("------------")
    idEliminarJoc = input("ID del joc a eliminar: ")
    eliminarJocFitxer(idEliminarJoc)
    print("Joc eliminat")


def llistarJocs():
    tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
    arrel = tree.getroot()
    print("LLISTA DELS JOCS")
    print("----------------")
    for game in arrel.findall("game"):
        id = game.get("id")
        name = game.find("name").text.strip()
        year = game.find("year").text.strip()
        developer = game.find("developer").text.strip()
        print(id, name, year, developer)
    print()


def insertarJoc():
    print("DADES DEL JOC")
    print("-------------")
    nomJoc = input("Nom: ")
    yearJoc = input("Any: ")
    sistemesJoc = input("Sistemes: ")
    desenvolupadorJoc = input("Desenvolupador: ")
    genereJoc = input("Gènere: ")
    descripcioJoc = input("Descripció: ")
    urlImatgeJoc = input("URL imatge: ")

    generarCarpetaPrograma()
    comprovarFitxer()
    escriureJocFitxer(nomJoc, yearJoc, sistemesJoc, desenvolupadorJoc, genereJoc, descripcioJoc, urlImatgeJoc)
    print()
    print("Joc afegit correctament")
    print()


def comprovarFitxer():
    pathFitxer = "/home/" + getuser() + "/BibliotecaDeJocs/dades.xml"
    if not os.path.exists(pathFitxer):
        arrel = ET.fromstring("<data></data>")
        tree = ET.ElementTree(arrel)
        tree.write(pathFitxer)


def escriureJocFitxer(nameInsert, yearInsert, systemInsert, developerInsert, genreInsert, descriptionInsert,
                      urlImageInsert):
    tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
    arrel = tree.getroot()

    game = ET.Element("game")
    nom = ET.SubElement(game, "name")
    nom.text = nameInsert
    year = ET.SubElement(game, "year")
    year.text = yearInsert
    systems = ET.SubElement(game, "systems")
    systems.text = systemInsert
    developer = ET.SubElement(game, "developer")
    developer.text = developerInsert
    genre = ET.SubElement(game, "genre")
    genre.text = genreInsert
    description = ET.SubElement(game, "description")
    description.text = descriptionInsert
    urlImage = ET.SubElement(game, "imageURL")
    urlImage.text = urlImageInsert

    game.set("id", str(seguentId()))

    arrel.append(game)
    tree.write("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")


def eliminarJocFitxer(idEliminar):
    tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
    arrel = tree.getroot()

    for game in arrel.findall("game"):
        id = game.get("id")
        if int(id) == int(idEliminar):
            arrel.remove(game)
    tree.write("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")


def seguentId():
    tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs" + "/dades.xml")
    root = tree.getroot()

    return len(root) + 1


def generarCarpetaPrograma():
    pathCarpetaPrograma = "/home/" + getuser() + "/BibliotecaDeJocs"

    existeixPathPrograma = os.path.exists(pathCarpetaPrograma)

    if not existeixPathPrograma:
        os.mkdir(pathCarpetaPrograma)


"""MAIN"""
menuInicial()
