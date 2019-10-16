
import os

def removeFileProperties(document):
    if os.path.exists(""  + document + "EPW-batch.morph.properties"):
        os.remove(""  + document + "EPW-batch.morph.properties")
        return
    else:
        return



def createFileProperties(document):
    documentCTD=open("" + document + "_EPW-batch.morph.properties", "a+")
    propertiesFile = "" + document + "_EPW-batch.morph.properties"

    documentCTD.write("""mappingdocument.file.path="""+ document +"""_EPW.r2rml.ttl
output.file.path=""" + document + """_EPW-batch-result-csv.nt
output.rdflanguage=N-TRIPLE

csv.file.path = """ + document + """.csv
no_of_database=1
database.name[0]=morphcsv
database.driver[0]=org.h2.Driver
database.url[0]=jdbc:h2:mem:morphcsv
database.user[0]=sa
database.pwd[0]=
database.type[0]=CSV""")

    documentCTD.close()

    return propertiesFile



# document = 'ABU DHABI'


# removeFileProperties(document)
# createFileProperties(document)
