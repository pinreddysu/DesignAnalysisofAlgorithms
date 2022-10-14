def RearrangingDataFiles(source, format):
    RearrangedData = []
    for i in range(len(source)):
        RearrangedData.append(source[format[i].index])
        #rearranging the data with the index position
    return RearrangedData