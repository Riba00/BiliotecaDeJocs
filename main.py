import os.path
from getpass import getuser

import xml.etree.ElementTree as ET


def menuInicial():
    bucleInici = 5
    while bucleInici > 0:
        bucleControlInici = 1
        while bucleControlInici > 0:
            print("BIBLIOTECA DE JOCS")
            print()
            print("1- Afegir joc")
            print("2- Llistar jocs")
            print("3- Mostrar dades d'un joc")
            print("4- Modificar un joc")
            print("5- Eliminar joc")
            print("6- Sortir")
            print()
            respostaInicial = int(input("Resposta: "))
            if 1 <= respostaInicial <= 6:
                bucleControlInici = 0
            else:
                print("Resposta incorrecta")
                print()

        if respostaInicial == 1:
            afegirJoc()

        if respostaInicial == 2:
            llistarJocs()

        if respostaInicial == 3:
            idMostrarGame = int(input("ID joc a mostrar: "))
            mostrarDadesJoc(idMostrarGame)

        if respostaInicial == 4:
            modificarJoc()

        if respostaInicial == 5:
            eliminarJoc()

        if respostaInicial == 6:
            print("Adeu, fins la pròxima")
            bucleInici = 0


def afegirJoc():
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
    generarFitxer()
    escriureJocFitxer(seguentId(), nomJoc, yearJoc, sistemesJoc, desenvolupadorJoc, genereJoc, descripcioJoc,
                      urlImatgeJoc)
    print()
    print("Joc afegit correctament")
    print()


def generarCarpetaPrograma():
    pathCarpetaPrograma = "/home/" + getuser() + "/BibliotecaDeJocs"
    existeixPathPrograma = os.path.exists(pathCarpetaPrograma)

    if not existeixPathPrograma:
        os.mkdir(pathCarpetaPrograma)


def generarFitxer():
    pathFitxer = "/home/" + getuser() + "/BibliotecaDeJocs/dades.xml"
    if not os.path.exists(pathFitxer):
        arrel = ET.fromstring("<data></data>")
        tree = ET.ElementTree(arrel)
        tree.write(pathFitxer)


def existeixFitxer():
    if os.path.exists("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml"):
        return True
    return False


def escriureJocFitxer(idJoc, nameInsert, yearInsert, systemInsert, developerInsert, genreInsert, descriptionInsert,
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

    game.set("id", str(idJoc))

    arrel.append(game)
    tree.write("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")


def seguentId():
    tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs" + "/dades.xml")
    root = tree.getroot()
    idMesGran = 0
    for game in root.findall("game"):
        if int(game.get("id")) > int(idMesGran):
            idMesGran = game.get("id")

    return int(idMesGran) + 1


def llistarJocs():
    if existeixFitxer():
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
    else:
        print("No hi ha cap joc creat")
        print()


def mostrarDadesJoc(idMostrar):
    if existeixFitxer():

        tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
        arrel = tree.getroot()
        for game in arrel.findall("game"):
            id = game.get("id")
            if int(id) == int(idMostrar):
                nomMostrarJoc = game.find("name").text.strip()
                yearMostrarJoc = game.find("year").text.strip()
                sistemesMostrarJoc = game.find("systems").text.strip()
                desenvolupadorMostrarJoc = game.find("developer").text.strip()
                genereMostrarJoc = game.find("genre").text.strip()
                descripcioMostrarJoc = game.find("description").text.strip()
                urlImatgeMostrarJoc = game.find("imageURL").text.strip()

                print("DADES JOC")
                print("---------")
                print("ID -------------> " + str(idMostrar))
                print("Nom ------------> " + nomMostrarJoc)
                print("Any ------------> " + yearMostrarJoc)
                print("Sistemes -------> " + sistemesMostrarJoc)
                print("Desenvolupador -> " + desenvolupadorMostrarJoc)
                print("Genere ---------> " + genereMostrarJoc)
                print("Descripcio -----> " + descripcioMostrarJoc)
                print("URL Imatge -----> " + urlImatgeMostrarJoc)
                print()
    else:
        print("No hi ha cap joc creat")
        print()


def modificarJoc():
    if existeixFitxer():
        print("MODIFICAR JOC")
        print("-------------")
        idModificarJoc = input("ID del joc a modificar: ")
        modificarAtributs(idModificarJoc)
        nomJoc = input("Nom: ")
        yearJoc = input("Any: ")
        sistemesJoc = input("Sistemes: ")
        desenvolupadorJoc = input("Desenvolupador: ")
        genereJoc = input("Gènere: ")
        descripcioJoc = input("Descripció: ")
        urlImatgeJoc = input("URL imatge: ")
        escriureJocFitxer(idModificarJoc, nomJoc, yearJoc, sistemesJoc, desenvolupadorJoc, genereJoc, descripcioJoc,
                          urlImatgeJoc)
        print()
        print("Joc modificat correctament")
        print()

    else:
        print("No hi ha cap joc creat")
        print()


def modificarAtributs(idModificar):
    if existeixFitxer():
        tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
        arrel = tree.getroot()

        for game in arrel.findall("game"):
            id = game.get("id")
            if int(id) == int(idModificar):
                arrel.remove(game)
        tree.write("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
        print()


def eliminarJoc():
    print("ELIMINAR JOC")
    print("------------")
    idEliminarJoc = input("ID del joc a eliminar: ")
    eliminarJocFitxer(idEliminarJoc)


def eliminarJocFitxer(idEliminar):
    if existeixFitxer():
        tree = ET.parse("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
        arrel = tree.getroot()

        for game in arrel.findall("game"):
            id = game.get("id")
            if int(id) == int(idEliminar):
                arrel.remove(game)
        tree.write("/home/" + getuser() + "/BibliotecaDeJocs/dades.xml")
        print("Joc eliminat correctament")
        print()
    else:
        print("No hi ha cap joc creat")
        print()


"""MAIN"""
menuInicial()
