texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
cambio = texto.split("#")
for i, cambios in enumerate(cambio):
    cambio[i] = cambios.capitalize()
    if i == 0:
        cambio[i] = cambio [i] +"..."
    else:
        cambio [i] = "- " + cambio[i] + "."
for cambios in cambio:
    print(cambios)