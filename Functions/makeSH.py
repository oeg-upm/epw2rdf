import os

def makeSH(propertiesFile):

    command = "java -cp .:morph-rdb.jar:dependency/* es.upm.fi.dia.oeg.morph.r2rml.rdb.engine.MorphCSVRunner . " + propertiesFile + ""

    os.system(command)