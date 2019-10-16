
# Función para saltar filas y para añadir encabezados
from Functions.skip_add_Rows import skipRows_addHeader


# Funciones para borrar y crear los documentos csv
from Functions.remove_create_open import removeFile, createFile, openFile

# Función para recoger todos los documentos pertenecientes a la extensión epw
# from glob import glob

# documents = glob("Documents/*.epw") # Cogemos todos los documentos pertenecientes a la extensión epw

def parseToCSV(dataset,numberRowstoSkip,headers):

    firstLine = dataset[0]
    firstLine = firstLine.split(',')
    cityName = firstLine[1].replace('/',' ').replace(' ','_').replace('__','')

    contents = skipRows_addHeader(numberRowstoSkip,dataset,headers)

    city = ''+ cityName +'.csv'
    
    removeFile(city)
    documentCTD = createFile(city)

    for line in contents:
        line = line.strip('\n').split(',')
        line = str(line).strip('[]').replace("'","")
        documentCTD.write(line + '\n') 

    documentCTD.close()
