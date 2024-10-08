def conta_a(string):
    string_lower = string.lower()

    contando = string_lower.count('a')

    if contando > 0:
        return f"A letra 'a' aparece {contando} vezes na string."
    else:
        return "não existe letra 'a' na string."
    

string = input("digite uma string: ")
print(conta_a(string))