text = ''
pattern = ''
diccionario_alfabeto = ''
list_pattern = []
funcion_hash = 0

def Read_alphabet():
    global text
    global pattern
    text = input('Introduce un texto: ')
    pattern = input('Introduce un patron: ')

def Convert_to_list(converted):
    list1 = []
    list1[:0] = converted
    return list1


def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return unique_list

def Process_alphabet(sample):
    text_in_array = Convert_to_list(sample)
    alphabet = unique(text_in_array)
    # Lo volvemos un diccionario para facilidad de manejo y para agregarle un valor a cada letra del alfabeto
    diccionario = {letra: index + 1 for index, letra in enumerate(alphabet)}
    return diccionario


def FuncionHash(patron):
    hash_value = 0
    for index, letra in enumerate(patron):
        hash_value = hash_value + diccionario_alfabeto[letra] * pow(len(diccionario_alfabeto), len(patron)-(index + 1))
    return hash_value

def Inicio():
    global diccionario_alfabeto
    global list_pattern
    global funcion_hash
    Read_alphabet()
    diccionario_alfabeto = Process_alphabet(text)
    list_pattern = Convert_to_list(pattern)
    funcion_hash = FuncionHash(list_pattern)

    text_list = Convert_to_list(text)
    for index, letter in enumerate(text_list):
        if(FuncionHash(text_list[index:len(list_pattern) + index]) == funcion_hash):
            print(f"El texto '{pattern}' esta en el index {index}")
        #print(FuncionHash(text_list[0 + index:len(list_pattern) + index]))

Inicio()
