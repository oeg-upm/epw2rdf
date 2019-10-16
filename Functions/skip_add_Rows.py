

def skipRows_addHeader(numberRowstoSkip,contents,headers):
    contents = contents[numberRowstoSkip:]
    contents.insert(0,headers)
    return contents