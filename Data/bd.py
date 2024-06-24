from appwrite import query
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from appwrite.id import ID
from enum import Enum
from Model.log import Log

class Table(Enum):
    Obra='65e8b328f0121bbe4444'

databaseId = '65dfa13ca9b5455eaf4a'

client=Client()

client.set_endpoint('http://195.35.18.156/v1')
client.set_project('657093958a9218d22389')

client.set_key('d97bb8d06410a6f27f69be358bd46d5e11c48cc9104965e0248013ea70ab8ec6691b5d35b71424cf86848e00293dfb69dbcff63e1ca9c556317bb9e5fd0b8648e8624c86de7f76560dc66914d1f7363f613c1324b88c54487cafcf2d9b4f9e894ca772230cf80ff588b2e56af36848866869169c779baf0283befd8f026e5902')

databases = Databases(client)

def createFile(file)->dict:
    try:
        storage = Storage(client)
        result= storage.create_file(file=file)
        return result
    except Exception as e:
        Log.Registrar(f"Appwrite Error:|{e}|")
        return None

def createDocument(table:Table,document:dict)->dict:
    try:
        result= databases.create_document(databaseId,table.value,ID.unique(),data=document)
        return result
    except Exception as e:
         Log.Registrar(f"Appwrite Error:|{e}|")
         return None
        
def updateDocument(table:Table,documentId:str,document:dict)->dict:
    try:
        result= databases.update_document(databaseId,table.value,documentId,document)
        return result
    except Exception as e:
        Log.Registrar(f"Appwrite Error:|{e}|")
        return None

def deleteDocument(table:Table,documentId:str)->str:
    try:
        result= databases.delete_document(databaseId,table.value,documentId)
        return result["$id"]
    except Exception as e:
        Log.Registrar(f"Appwrite Error:|{e}|")
        return None

def getDocument(table:Table,documentId:str)->dict:
    try:
        result= databases.get_document(databaseId,table.value,documentId)
        return result
    except Exception as e:
        Log.Registrar(f"Appwrite Error:|{e}|")
        return None

def getDocumentByField(table:Table,filter:list=[])->dict:
    try:
        if filter == []:
            result= databases.list_documents(databaseId,table.value)
        else:
            result= databases.list_documents(databaseId,table.value,filter)
        return result["documents"][0]
    except Exception as e:
        Log.Registrar(f"Appwrite Error:|{e}|")
        return None

def listDocuments(table:Table,filter:list=[])->list:
    try:
        if filter == []:
            result= databases.list_documents(databaseId,table.value)
        else:
            result= databases.list_documents(databaseId,table.value,filter)

        return result["documents"]    
    except Exception as e:
        return Log.Registrar(f"Appwrite Error:|{e}|")
        return None
        
    




