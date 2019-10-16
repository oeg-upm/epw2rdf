import os

def removeFile(document):
    if os.path.exists("" + document):
        os.remove("" + document)
        return
    else:
        return


def createFile(document):
    documentCTD=open("" + document, "a+")
    return documentCTD # Document Created


def openFile(document):
    documentOPD=open(document,'r')
    return documentOPD # Document Opened