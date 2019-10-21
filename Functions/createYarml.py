
import os


def removeFileYML(document):
    if os.path.exists("Data/" + document + "_EPW.yml"):
        os.remove("Data/" + document + "_EPW.yml")
        return
    else:
        return



def createFileYML(document):
    documentCTD=open("Data/" + document + ".yml", "a+")

    documentCTD.write("""prefixes:
  ex: "http://example.com/"
  rr: <http://www.w3.org/ns/r2rml#> .
  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
  @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
  @prefix owl: <http://www.w3.org/2002/07/owl#> .
  @prefix dcterms: <http://purl.org/dc/terms/> .
  @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
  @prefix fno: <http://w3id.org/function/ontology#> .
  @prefix sql: <http://dchaves.oeg-upm.net/resources/function/sql.ttl#> .
  @prefix bv: <http://bio2rdf.org/bio2rdf_vocabulary:> .
  @prefix homogv: <http://bio2rdf.org/homologene_vocabulary:> .
  @prefix epw: <http://epw.linkeddata.es/vocab#> .
  @prefix epw""" + document.lower() +  """: <http://epw.linkeddata.es/resources/""" + document.lower() +  """/> .

  mappings:
  """+ document + """:
    sources:
      - ['"""+ document + """.csv'~csv]
    s: http://epw.linkeddata.es/resources/""" + document.lower() +  """/$(year)-$(month)-$(day)-$(hour)-$(minute)
    po:
      - [a, epw:EPW]
      - [epw:city, http://dbpedia.org/resource/""" + document.lower().title() + """]
      - [epw:year, $(year), xsd:integer]
      - [epw:month, $(month), xsd:integer]
      - [epw:day, $(day), xsd:integer]
      - [epw:hour, $(hour), xsd:integer]
      - [epw:minute, $(minute), xsd:integer]
      - [epw:dataSourceAndUncertaintyFlags, $(datasourceanduncertaintyflags), xsd:string]
      - [epw:dryBulbTemperature, $(drybulbtemperature), xsd:decimal]
      - [epw:dewPointTemperature, $(dewpointtemperature), xsd:decimal]
      - [epw:relativeHumidity, $(relativehumidity), xsd:decimal]
      - [epw:atmosphericStationPressure, $(atmosphericstationpressure), xsd:decimal]
      - [epw:extraterrestrialHorizontalRadiation, $(extraterrestrialhorizontalradiation),xsd:decimal]
      - [epw:extraterrestrialDirectNormalRadiation, $(extraterrestrialdirectnormalradiation),xsd:decimal]
      - [epw:horizontalInfraredRadiationIntensity, $(horizontalinfraredradiationintensity), xsd:decimal]
      - [epw:globalHorizontalRadiation, $(globalhorizontalradiation), xsd:decimal]
      - [epw:directNormalRadiation, $(directnormalradiation), xsd:decimal]
      - [epw:diffuseHorizontalRadiation, $(diffusehorizontalradiation), xsd:decimal]
      - [epw:globalHorizontalIlluminance, $(globalhorizontalilluminance), xsd:decimal]
      - [epw:directNormalIlluminance, $(directnormalilluminance), xsd:decimal]
      - [epw:diffuseHorizontalIlluminance, $(diffusehorizontalilluminance), xsd:decimal]
      - [epw:zenithLuminance, $(zenithluminance), xsd:decimal]
      - [epw:windDirection, $(winddirection), xsd:decimal]
      - [epw:windSpeed, $(windspeed), xsd:decimal]
      - [epw:totalSkyCover, $(totalskycover), xsd:decimal]
      - [epw:opaqueSkyCover, $(opaqueskycover), xsd:decimal]
      - [epw:visibility, $(visibility), xsd:decimal]
      - [epw:ceilingHeight, $(ceilingheight), xsd:decimal]
      - [epw:presentWeatherObservation, $(presentweatherobservation), xsd:decimal]
      - [epw:presentWeatherCodes, $(presentweathercodes), xsd:decimal]
      - [epw:precipitableWater, $(precipitablewater), xsd:decimal]
      - [epw:aerosolOpticalDepth, $(aerosolopticaldepth), xsd:decimal]
      - [epw:snowDepth, $(snowdepth), xsd:decimal]
      - [epw:daysSinceLastSnowfall, $(dayssincelastsnowfall), xsd:decimal]
      - [epw:albedo, $(albedo), xsd:decimal]
      - [epw:liquidPrecipitationDepth, $(liquidprecipitationdepth), xsd:decimal]
      - [epw:liquidPrecipitationQuantity, $(liquidprecipitationquantity), xsd:decimal]
""".replace("'",'"'))

    documentCTD.close()