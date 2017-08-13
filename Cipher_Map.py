def recall_password(cipher_grille, ciphered_password):
    decrypted_word = ""
    def rotate_90degree(matrix):
        rotated90 = list(zip(*matrix[::-1]))
        return rotated90
    def convert_to_matrix(data):
        # Creates a list containing 4 lists, each of 4 items, all set to 0
        row, column = len(cipher_grille), len(cipher_grille[0])
        matrix = [[0 for x in range(row)] for y in range(column)]
        row = 0
        column = 0
        for words in data:
            for letter in words:
                matrix[row][column] = letter
                column +=1
            row += 1
            column = 0
        return matrix

    def decrypt(grille, template, hole='X'):
        decoded_word = ""
        row = 0
        column = 0
        for x in grille:
            for y in x:
                if y == hole:
                    decoded_word += template[row][column]
                column +=1
            row += 1
            column = 0   
        return decoded_word
    

    word_matrix = convert_to_matrix(ciphered_password)
    ciphered_matrix = convert_to_matrix(cipher_grille)
    for i in range(4):
        decrypted_word += decrypt(ciphered_matrix, word_matrix)
        ciphered_matrix = rotate_90degree(ciphered_matrix)
    print(decrypted_word)       
    return decrypted_word




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

    # Rank 2
    assert recall_password(
        ('.X...X.',
         'X.....X',
         '.......',
         '...X...',
         '.......',
         'X.....X',
         '.X...X.'),
        ('loremip',
         'sumdolo',
         'rsitame',
         'tconsec',
         'teturad',
         'ipiscin',
         'gelitqu')) == "oisonineqoisonineqoisonineqoisonineq", "R2"

    # Rank 3
    assert recall_password(
        ('.X...',
         '.X...',
         '..X..',
         '.X...',
         '.X...'),
        ('QWERT',
         'ASDFG',
         'ZXCVB',
         'YUIOP',
         'GHJKL')) == "WSCUHCYUOPRFCOKASFGC", "R3"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
