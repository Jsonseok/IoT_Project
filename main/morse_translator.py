import collections
import re

english_morse_dictionary = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '!': '-.-.--',
    '"': '.-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    '/': '-..-.',
    '+': '.-.-.',
    '-': '-....-',
    '$': '...-..-',
    '@': '.--.-.',
}
english_morse_cute_dictionary = {}
for k, v in english_morse_dictionary.items():
    english_morse_cute_dictionary[k] = ''.join(['•' if char == '.' else '‒' for char in v])


reversed_english_morse_cute_dictionary = dict(
    zip(english_morse_cute_dictionary.values(), english_morse_cute_dictionary.keys()))
reversed_english_morse_cute_dictionary


def translator(code: str) -> str:
    """Reads Morse code and converts it to plain text."""
    msg = ''
    for word in code.split('  '):
        msg += ''.join([reversed_english_morse_cute_dictionary.get(char) for char in word.split()])
        msg += ' '
    return msg.rstrip()


def encoder(msg: str) -> str:
    """Converts the given message into Morse code."""
    code = ''
    for word in msg.split():
        code += ' '.join([english_morse_cute_dictionary.get(char.upper()) for char in word])
        code += '  '  # To separate words
    return code.rstrip()
