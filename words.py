# Вывести последнюю букву в слове
word1 = 'Архангельск'
print(f"Последняя буква: {word1[-1]}")


# Вывести количество букв а в слове
word2 = 'Архангельск'
print (len(word2))


# Вывести количество гласных букв в слове

word3 = "Архангельск"
vowels = 0
for i in word3:
    letter = i.lower()
    if letter == "а" or letter == "е":
        vowels += 1
    
print((vowels))


# Вывести количество слов в предложении
sentence4 = 'Мы приехали в гости'
print(f"Слова: {len(sentence4.split())}")


# Вывести первую букву каждого слова на отдельной строке
sentence1 = 'Мы приехали в гости'
sentence3 = sentence1.split()
for letters in sentence3:
        print (letters[0])




# Вывести усреднённую длину слова.
sentence2 = 'Мы приехали в гости'
razdelenie = sentence2.split()

razdelenie0 = int(len(razdelenie[0]))/len(sentence2)
print(razdelenie0)

razdelenie1 = int(len(razdelenie[1]))/len(sentence2)
print(razdelenie1)

razdelenie2 = int(len(razdelenie[2]))/len(sentence2)
print(razdelenie2)

razdelenie3 = int(len(razdelenie[3]))/len(sentence2)
print(razdelenie3)
