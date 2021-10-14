import random
import time
fruits = []
animals = []
objs = []
theme = [fruits, animals, objs]


def Read_file(arquiveName, list):
    file = open(arquiveName, 'r')

    for element in file:
        element.split(" ")
        list.append(element)


Read_file('fruits.txt', fruits)
Read_file('animals.txt', animals)
Read_file('objects.txt', objs)

print(''''
>>>>>>> Jogo da Forca <<<<<<<<<<<<
Olá seja bem vindo
Escolha um tema para o jogo
0 - Frutas
1 - Animais 
2 - Objetos
''')

theme_chooice = int(input('> '))

secret_word = random.choice(theme[theme_chooice])
numbers_of_letters = len(secret_word)
display = []
letters = ''

for letra in range(numbers_of_letters):
    display.append('_')

hits = 0
errors = 0
attempts = 6

while hits < numbers_of_letters and errors < attempts:
    print(f'{display}                                  ({letters})')
    chosen_letter = input('> ').lower()
    letters += chosen_letter + ', '

    if chosen_letter not in display:
        cont = 0
        hits = False

        for letter in secret_word:
            if chosen_letter == letter:
                display[cont] = letter
                hits = hits + 1
                hits = True

            cont = cont + 1
        if hits == False:
            errors += 1
            print('Errouuuu!!!')
            if errors == 1:
                print(
                    f'''
                       _________                    ({letters})             
                      |     |
                      |    ʘ‿ʘ
                      |
                '''
                )
            elif errors == 2:
                print(f'''
                       _________                    ({letters})
                      |     |
                      |    ಠ‿ಠ
                      |     |
                      |     |
                      |     
                      |
                      
              ''')

            elif errors == 3:
                print(f'''
                     _________                      ({letters})  
                    |   |
                    |  ⊙﹏⊙
                    |  /|
                    | / |
                    |   


              ''')
            elif errors == 4:
                print(f'''                             ({letters})  

                    ________
                    |   |
                    |  ⊙﹏⊙
                    |  /|\ 
                    |   | 
                    
              ''')

            elif errors == 5:
                print(f'''
                ________                                ({letters})  
               |    |
               | (´･_･`)
               |   /|\ 
               |  / | \ 
               |   / 



              ''')
            elif errors == 6:
                print(f'''
                _________                               ({letters})  
                |    |
                | （ ﾟДﾟ）
                |   /| \ 
                |  / |  \ 
                |    |
                |   / \ 



              ''')
    else:
        print('Essa letra vc já acertou')


if hits >= numbers_of_letters:
    print('Parabéns você acertou')
    print(display)
else:
    print('Se FU')
    print('A plavra era...')
    time.sleep(1)
    print(secret_word)
