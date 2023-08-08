def conta_palavras_unicas(words):
    unicas = []
    if isinstance(words, str):
         words = words.split(' ')
    for word in words:
            if word not in unicas:
                unicas.append(word) 
    return len(unicas)

# Teste a sua função aqui (caso ache necessário)

print(conta_palavras_unicas("banana maçã banana maçã laranja maçã banana"))









