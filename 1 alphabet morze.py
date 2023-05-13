from typing import Dict, Any

print(
    """

 .----------------. .----------------. .----------------. .----------------. .----------------.   .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | | .--------------. | .--------------. | .--------------. | .--------------. |
| | ____    ____ | | |     ____     | | |  _______     | | |    _______   | | |  _________   | | | |     ______   | | |     ____     | | |  ________    | | |  _________   | |
| ||_   \  /   _|| | |   .'    `.   | | | |_   __ \    | | |   /  ___  |  | | | |_   ___  |  | | | |   .' ___  |  | | |   .'    `.   | | | |_   ___ `.  | | | |_   ___  |  | |
| |  |   \/   |  | | |  /  .--.  \  | | |   | |__) |   | | |  |  (__ \_|  | | |   | |_  \_|  | | | |  / .'   \_|  | | |  /  .--.  \  | | |   | |   `. \ | | |   | |_  \_|  | |
| |  | |\  /| |  | | |  | |    | |  | | |   |  __ /    | | |   '.___`-.   | | |   |  _|  _   | | | |  | |         | | |  | |    | |  | | |   | |    | | | | |   |  _|  _   | |
| | _| |_\/_| |_ | | |  \  `--'  /  | | |  _| |  \ \_  | | |  |`\____) |  | | |  _| |___/ |  | | | |  \ `.___.'\  | | |  \  `--'  /  | | |  _| |___.' / | | |  _| |___/ |  | |
| ||_____||_____|| | |   `.____.'   | | | |____| |___| | | |  |_______.'  | | | |_________|  | | | |   `._____.'  | | |   `.____.'   | | | |________.'  | | | |_________|  | |
| |              | | |              | | |              | | |              | | |              | | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------'   '----------------' '----------------' '----------------' '----------------' 

    """
)


def morse_alphabet():
    code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', '0': '-----'}
    return code


def morse_reverse():
    reverse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
               '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
               '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
               '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
               '-.--': 'Y', '--..': 'Z'}
    return reverse


def encode_word(word_for_encode, alph_morse):
    letter = 0
    try:
        while letter < len(word_for_encode):
            if word_for_encode[letter] != ' ':
                print(alph_morse[word_for_encode[letter]], end=' ')

            else:
                print('/', end=' ')

            letter += 1
    except KeyError:
        print('\nThis symbol is not in the alphabet morse')


def decode_word(word_for_decode, alph_reverse):
    letter = 0
    word_for_decode = word_for_decode.split()
    try:
        while letter < len(word_for_decode):
            if word_for_decode[letter] == ' ':
                print(' ', end=' ')

            else:
                print(alph_reverse[word_for_decode[letter]], end='')

            letter += 1
    except KeyError:
        print('\nThis symbol is not in the Morse alphabet')


morse_alph = morse_alphabet()
morse_alph_reverse = morse_reverse()

choice = input('\nYou want to encode the word or decode? Type "ENCODE" or "DECODE": ').upper()


while choice != "ENCODE" and choice != "DECODE":
    choice = input('you want to encode the word or decode? Type "ENCODE" or "DECODE": ').upper()

if choice == "ENCODE":
    word = input('Enter the cipher you want to decrypt: ').upper()
    encode_word(word_for_encode=word, alph_morse=morse_alph)


elif choice == "DECODE":
    word = input('Enter the word or phrase you want to decode: ').upper()
    decode_word(word_for_decode=word, alph_reverse=morse_alph_reverse)


