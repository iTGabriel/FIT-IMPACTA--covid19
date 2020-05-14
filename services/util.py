def custom_data(texto):
    data_split = texto.split("T")[0].split('-')
    data_br = f"{data_split[2]}/{data_split[1]}/{data_split[0]}"
    # print(data_br)
    return data_br

def custom_numero(texto):
    texto = str(texto)
    if len(texto) == 4:
        texto = f"{texto}k"
    elif len(texto) == 5:
        texto = f"{texto[:2]}.{texto[2:]}k"
    elif len(texto) == 6:
        texto = f"{texto[:3]}.{texto[3:]}k"
    elif len(texto) == 7:
        texto = f"{texto[:1]}.{texto[1:4]}.{texto[4:]}k"
    return texto