# Customização da data, passando-a para formato Br
def custom_data(texto):
    data_split = texto.split("T")[0].split('-')
    data_br = f"{data_split[2]}/{data_split[1]}/{data_split[0]}"
    return data_br


# Customização do totla, tornando legibilidade mais atrativa
def custom_numero(texto):
    texto = str(texto)
    if len(texto) == 4:
        texto = f"{texto}"
    elif len(texto) == 5:
        texto = f"{texto[:2]}.{texto[2:]}"
    elif len(texto) == 6:
        texto = f"{texto[:3]}.{texto[3:]}"
    elif len(texto) == 7:
        texto = f"{texto[:1]}.{texto[1:4]}.{texto[4:]}"
    return texto