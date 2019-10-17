from bs4 import BeautifulSoup
import requests
import urllib.request
import time

from Functions.parseCSV import parseToCSV

from Functions.createPropertiesFile import removeFileProperties,createFileProperties

from Functions.createTTLFile import removeFileTTL,createFileTTL

from Functions.makeSH import makeSH

from Functions.makeMetadata import removeFileJSON,createFileJSON

from Functions.getDataFromJson import getJsonData

from Functions.createYarml import removeFileYML,createFileYML



removeFileJSON()

documentJSON=open("csv-metadata.json", "a+")

documentJSON.write("""{
"@context": "http://www.w3.org/ns/csvw",
"skipRows": 8,
"tables":[]}
""")

documentJSON.close()


urlContinents = "https://energyplus.net/weather"
responseContinents = requests.get(urlContinents,timeout=10)
continent = BeautifulSoup(responseContinents.content, "html.parser")

# Primer for para continentes

for continent in continent.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
    continentLink = continent['href']
    # print ("Found the URL of continent:", continentLink)
    
    urlCountries = "https://energyplus.net" + continentLink
    responseCountries = requests.get(urlCountries,timeout=10)
    countries = BeautifulSoup(responseCountries.content,"html.parser")

    # Segundo for para paises

    for country in countries.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
        countryLink = country['href']
        # print("Found the URL of country:",countryLink)

        urlCities = "https://energyplus.net" + countryLink
        responseCities = requests.get(urlCities,timeout=10)
        cities = BeautifulSoup(responseCities.content,"html.parser")

        # Tercer for para ciudades

        for city in cities.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
            cityLink = city['href']
            # print("Found the URL of city:",cityLink)

            urlDownloadEPW = "https://energyplus.net" + cityLink
            responseDownloadEPW = requests.get(urlDownloadEPW,timeout=10)
            downloads = BeautifulSoup(responseDownloadEPW.content,"html.parser")

            #Cuarto for para descargas

            for download in downloads.find_all('a', attrs={"class": "btn btn-default left-justify blue-btn"}, href=True):
                downloadLink = download['href']

                if download.text == 'epw':
                    downloadLinkName = downloadLink.split('/')
                    downloadLinkName = downloadLinkName[-1]
                    print("Found the URL of download:",downloadLink)
                    download_url = "https://energyplus.net"+ downloadLink
                    responseData = requests.get(download_url,"html.parser")
                    data = responseData.text # Aquí tenemos los datos para eliminar
                    dataset = data.splitlines() # En dataset lo tenemos como líneas

                    city = createFileJSON(dataset)

                    headers,numberRowstoSkip = getJsonData(city)

                    headers = str(str(headers).strip('[]').replace("'","").split(', ')).strip('[]').replace(", ",",")

                    headers = str(headers).strip('[]').replace("'","").replace(", ",",")

                    parseToCSV(dataset,numberRowstoSkip,headers) # Parse to CSV

                    removeFileProperties(city)
                    propertiesFile = createFileProperties(city)

                    removeFileTTL(city)
                    createFileTTL(city)

                    removeFileYML(city)
                    createFileYML(city)

                    makeSH(propertiesFile)



