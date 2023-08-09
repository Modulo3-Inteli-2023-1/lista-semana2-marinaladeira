#  Se achar necessario, faça import de outras bibliotecas
def is_anagram(palavra1, palavra2):
    for i in palavra1:
        if i not in palavra2:
            return False
    return True

print(is_anagram("banana", "banana"))
print(is_anagram("banana", "maçã")) 
print(is_anagram("amor", "roma"))
print(is_anagram("pedra", "padre")) 
print(is_anagram("pedra", "pedro")) 
print(is_anagram("perda", "pedra")) 
print(is_anagram("perda", "pedro")) 
print(is_anagram("perda", "padre") )