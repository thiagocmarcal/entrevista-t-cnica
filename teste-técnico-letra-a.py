def verificar_letra_a(texto):
    texto_lower = texto.lower()

    quantidade_a = texto_lower.count('a')

    if quantidade_a > 0:
        return f"A letra 'a' aparece {quantidade_a} vezes na string."
    else:
        return "A letra 'a' não aparece na string."
    
entrada_usuario = input("Digite uma string: ")
resultado = verificar_letra_a(entrada_usuario)

print(resultado)
