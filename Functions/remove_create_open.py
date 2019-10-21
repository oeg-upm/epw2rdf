import os

def removeFile(document):
    if os.path.exists("Data/" + document):
        os.remove("Data/" + document)
        return
    else:
        return


def createFile(document):
    documentCTD=open("Data/" + document, "a+")
    return documentCTD # Document Created


def openFile(document):
    documentOPD=open("Data/" + document,'r')
    return documentOPD # Document Opened