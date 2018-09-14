import unicodedata


def clean_curso(data):
    articles = ["el", "y", "la", "los", "tu", "las", "de","al", "para", "ellos", "de", "del", "una", "a", "tu"
                                                                                                     "EL", "Y", "LA",
                "LOS", "TU", "LAS", "DE","AL", "PARA", "ELLOS", "DE", "DEL", "UNA", "A", "TU"]
    special = ["¿", "?", "!", "¡", "(", ")", ",", ".", ";", ":", "_", "{", "}", "[", "]", "+", "/", "*", "<",
               ">"]
    data_aux = ""
    # Deleting special characters
    for i in range(0, len(data)):
        if data[i] not in special:
            data_aux = data_aux + data[i]

    #   Deleting articles
    words = data_aux.split(" ")
    new_data = ""
    for word in words:
        if word not in articles:
            new_data += word + " "
    new_data = new_data[0:len(new_data)-1]
    return strip_accents(new_data)


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')
