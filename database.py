from pymongo import MongoClient
from pymongo.server_api import ServerApi


url = "mongodb+srv://radsylph:30683643@cluster0.kt6qv0l.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(
    url,
    server_api=ServerApi("1"),
    connectTimeoutMS=30000,
    socketTimeoutMS=None,
    connect=False,
    maxPoolsize=1,
)

db = client["bot_emperador"]
collection = db["integrantes"]


def agregar_participante(nombre: str) -> str:
    if nombre == "":
        return "No se pueden agregar campos vacios"

    if collection.find_one({"nombre": nombre}):
        return "Ya existe el usuario en el grupo"
    try:
        nuevo_participante = {
            "nombre": nombre,
        }
        collection.insert_one(nuevo_participante)
        return f"Se agrego el participante {nombre} de forma satisfactoria"
    except Exception as e:
        return "No se pudo agregar el participante" + str(e)


def eliminar_participante(nombre: str) -> str:
    if nombre == "":
        return "No se pueden agregar campos vacios"

    if collection.find_one({"nombre": nombre}) is None:
        return "No existe el usuario en el grupo"
    try:
        collection.delete_one({"nombre": nombre})
        return f"Se elimino el participante {nombre} de forma satisfactoria"
    except:
        return "No se pudo eliminar el participante"


def consultar_participantes() -> str:
    try:
        participantes = collection.find()
        if participantes is None:
            return "No hay participantes en el grupo"
        mensaje = " Atencion: \n"
        for participante in participantes:
            mensaje += f"{participante['nombre']} \n"
        return mensaje
    except:
        return "No se pudo consultar los participantes"


def borrar_todo(grupo: str) -> str:
    if grupo == "":
        return "No se pueden agregar campos vacios"

    participantes = collection.find({"grupo": grupo})
    if participantes is None:
        return "No hay participantes en el grupo"

    for participante in participantes:
        collection.delete_one({"nombre": participante["nombre"], "grupo": grupo})
    return (
        f"Se borraron todos los participantes del grupo {grupo} de forma satisfactoria"
    )
