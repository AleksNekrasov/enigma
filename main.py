
ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
          2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
          3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
          4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
          5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
          6: 'JPGVOUMFYQBENHZRDKASXLICTW',
          7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
          8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
          'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
          'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
          }
REFLEC = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
          2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
          3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
          4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
          }


def coder(char: str, shift: list, rotors: list, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> str:
    len_shift = len(shift)
    len_alphabet = len(alphabet)

    for i in range(len_shift):  # если reverse = False  то по факту получаем(0,4,1) иначе (0,4,-1)
        index = rotors[i].find(char)  # индекс сдвига и поиска нужного символа
        index = (index - shift[i]) % len_alphabet  # индекс 1 сдвига ( нахождение индекса символа в алфавите)
        char = alphabet[index]  # запись нового символа, найденного в роторе
    return char


def encoder(char: str, shift: list, rotors: list, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> str:
    len_shift = len(shift)
    len_alphabet = len(alphabet)

    for i in range(len_shift):  # если reverse = False  то по факту получаем(0,4,1) иначе (0,4,-1)
        index = alphabet.find(char)  # индекс сдвига и поиска нужного символа
        index = (index + shift[i]) % len_alphabet  # индекс 1 сдвига ( нахождение индекса символа в алфавите)
        char = rotors[i][index]  # запись нового символа, найденного в роторе
    return char


def clean_and_uppercase(s):
    # Оставляем только буквы, убираем всё остальное
    cleaned = ''.join(char for char in s if char.isalpha())
    # Переводим в верхний регистр
    return cleaned.upper()


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    # your code
    new_text = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    REFLEC = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
              2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
              3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
              4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
              }

    text = clean_and_uppercase(text)
    # это шаги сдвигов, до реф слева-направо, после реф: справа-налево *(-1)
    shift = [shift3, shift2 - shift3, shift1 - shift2, 0 - shift1]
    rotors = [ROTORS[rot3], ROTORS[rot2], ROTORS[rot1], REFLEC[ref]]

    for t in text:
        ch = encoder(t, shift, rotors)
        index = REFLEC[ref].find(ch)
        ch = alphabet[index]
        ch = coder(ch, shift[::-1], rotors[::-1])
        new_text += ch
    return new_text


f = enigma('AYIQQLXZMFHQUHQCH', 1, 1, -1, 2, 2, 3, -1)
print(f)

