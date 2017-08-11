def recall_password(cipher_grille, ciphered_password):
    def rotate_90degree(matrix):
        return 0
    def convert_to_matrix(data):
        return 0
    def decrypt(grille, template, hole='X'):
        return 0
    
    return ""


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