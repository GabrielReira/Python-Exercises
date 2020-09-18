user_words = list()

n = int(input('Quantas palavras você deseja informar? '))

for i in range(n):
    word = (input('Digite a palavra (sem acentos): '))
    user_words.append(word.lower())

for word in user_words:
    print(f'\nNa palavra "{word}", temos: ', end='')
    for letter in word:
        if letter in 'aeiou':
            print(letter, end=' ')