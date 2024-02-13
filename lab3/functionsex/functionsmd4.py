def reverse_sentence(sentence):
    words = sentence.split()     # разбиваем строку sentence которую мы ввели на слова!
    reversed_words = words[::-1] # список слов words переворачиается благодаря [::-1], сохранил ее в новой переменной
    reversed_sentence = ' '.join(reversed_words) # с помощью метода join() cлова из реверсед вордс обьеднияются в строку и сохраняются в reversed sentence 
    return reversed_sentence

sentence = input()
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)


def revsentence(soilem):
    sozder = soilem.split()
    keri_sozder = sozder[::-1]
    keri_soilem = " ".join(keri_sozder)
    return keri_soilem

soilem = input()
keri_soilem = revsentence(soilem)
print(keri_soilem)
    
