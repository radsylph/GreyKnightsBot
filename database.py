from pymongo import MongoClient
from pymongo.server_api import ServerApi
import random


url = (
    "mongodb+srv://test1:123@cluster0.gpskocw.mongodb.net/?retryWrites=true&w=majority"
)


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

def ship_participantes() -> str:
    try:
        participantes = list(collection.find())
        
        if not participantes or len(participantes) < 2:
            return "No hay suficientes participantes en el grupo"
        
        random.shuffle(participantes)
        
        couple = random.sample(participantes, 2)
    
        nombres = [participante["nombre"] for participante in couple]
        return f"La pareja seleccionada es: {nombres[0]} y {nombres[1]}"
    
    except Exception as e:
        return "No se pudo consultar los participantes: " + str(e)
        
print(ship_participantes())
#print(consultar_participantes())