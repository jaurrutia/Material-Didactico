

string = 'ÁáÉéÍíÓóÚúÑñÜü'

print("\tCaracter\tValor\n" +
        "\t" + 25 * "-")                    # Notemos que también pudimos "multiplicar" la cadena, así como la sumamos
for i in range(len(string)-1):
    print("\t ", string[i], "\t\t", ord(string[i]),"\t\t", ord(string[i])-ord(string[i+1]) )
print("\t" + 25 * "-")         # Nota que la instrucción que no se
                                            # repite es la que no tiene una tabulación
