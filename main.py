def return_rotor(pos) -> str:
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
    return ROTORS[pos]


def return_reflector(pos) -> str:
    REFLEC = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
              2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
              3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
              4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
              }
    return REFLEC[pos]


def clean_and_uppercase(s):
    # Оставляем только буквы, убираем всё остальное
    cleaned = ''.join(char for char in s if char.isalpha())
    # Переводим в верхний регистр
    return cleaned.upper()


def return_index(char, rotor):
    return rotor.find(char)


def return_char(index, rotor):
    return rotor[index]


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    # your code

    text = clean_and_uppercase(text)  # подготавливаем строку
    message = ''  # закодированное сообщение

    # смещения роторов
    shift_rotor3 = shift3
    shift_rotor2 = shift2 - shift3
    shift_rotor1 = shift1 - shift2
    shift_reflector = 0 - shift1

    for char in text:
        ch = char

        # rotor3
        rotor = return_rotor(0)
        index = return_index(ch, rotor)
        index = (index + shift_rotor3) % len(rotor)
        rotor = return_rotor(rot3)
        ch = return_char(index, rotor)  # буква 3 ротора

        # rotor2
        rotor = return_rotor(0)
        index = return_index(ch, rotor)
        index = (index + shift_rotor2) % len(rotor)
        rotor = return_rotor(rot2)
        ch = return_char(index, rotor)  # буква 2 ротора

        # rotor1
        rotor = return_rotor(0)
        index = return_index(ch, rotor)
        index = (index + shift_rotor1) % len(rotor)
        rotor = return_rotor(rot1)
        ch = return_char(index, rotor)  # буква 1 ротора

        # reflector
        rotor = return_rotor(0)
        index = return_index(ch, rotor)
        index = (index + shift_reflector) % len(rotor)
        rotor = return_reflector(ref)
        ch = return_char(index, rotor)  # буква рефлектора

        # reflector добавочный
        rotor = return_rotor(0)
        index = return_index(ch, rotor)
        index = (index - shift_reflector) % len(rotor)
        rotor = return_reflector(0)
        ch = return_char(index, rotor)  # буква рефлектора

        # rotor1
        rotor = return_rotor(rot1)
        index = return_index(ch, rotor)
        index = (index - shift_rotor1) % len(rotor)
        rotor = return_rotor(0)
        ch = return_char(index, rotor)

        # rotor2
        rotor = return_rotor(rot2)
        index = return_index(ch, rotor)
        index = (index - shift_rotor2) % len(rotor)
        rotor = return_rotor(0)
        ch = return_char(index, rotor)

        # rotor3
        rotor = return_rotor(rot3)
        index = return_index(ch, rotor)
        index = (index - shift_rotor3) % len(rotor)
        rotor = return_rotor(0)
        ch = return_char(index, rotor)

        message += ch

    return message


f = enigma('AYIQQLXZMFHQUHQCH', 1, 1, -1, 2, 2, 3, -1)
print(f)

