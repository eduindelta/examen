frase = "El curso de programacion en logros es muy bueno"

lista_palabras = frase.split()

if not lista_palabras:
    print("La frase está vacía.")
else:
    palabra_mas_larga = lista_palabras[0]
    
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    print(f"La frase es: '{frase}'")
    print(f"La palabra más larga encontrada es: '{palabra_mas_larga}'")