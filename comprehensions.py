def devowel(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels = [letter
                 for letter in sentence
                 if letter not in vowels]
    return ''.join(no_vowels)

print(devowel('List Comprehensions are the Greatest!'))
