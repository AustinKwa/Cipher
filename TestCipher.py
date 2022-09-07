#  File: TestCipher.py

#  Description: A program to encode and decode a string into encrypted text and vise-versa

#  Student's Name: Austin Kwa

#  Student's UT EID: ak38754
 
#  Partner's Name: N/A

#  Partner's UT EID: ak38754

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/3/2022

#  Date Last Modified: 2/4/2022

from audioop import reverse
import code
from pydoc import text
import sys

#   Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#   Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    text = list(strng)
    ticket = []
    j = 0
    for i in range(len(text)):
        if j == 0:
            reverse = False
        elif j == key - 1:
            reverse = True
        
        if reverse == False:
            ticket.append(j)
            j += 1
        else:
            ticket.append(j)
            j -= 1

    code = ''
    for j in range(key):
        for i in range(len(ticket)):
            if ticket[i] == j:
                code += text[i]
    return code

#   Input: strng is a string of characters and key is a positive
#         	integer 2 or greater and strictly less than the length
#         of strng
#   Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    text = list(strng)
    row_count = []
    for i in range(key):
        row_count.append(0)

    j = 0
    for i in range(len(text)):
        row_count[j] += 1
        if j == 0:
            reverse = False
        elif j == key - 1:
            reverse = True

        if reverse == False:
            j += 1
        else:
            j -= 1
    
    split_text = []
    for i in range(key):
        segment = []

        for j in range(row_count[i]):
            segment.append(text[j])

        split_text.append(segment)
        for j in range(row_count[i]):
            text.pop(0)
        
    code = ''
    text = list(strng)
    j = 0
    for i in range(len(text)):
        if j == 0:
            reverse = False
        elif j == key - 1:
            reverse = True

        if reverse == False:
            code += split_text[j][0]
            split_text[j].pop(0)
            j += 1
        else:
            code += split_text[j][0]
            split_text[j].pop(0)
            j -= 1

    return code

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    strng = strng.lower()
    text = list(strng)
    filtered = ''
    count = 0
    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122:
            filtered += text[i]
    return filtered

#  Input: p is a character in the pass phrase and s is a character
#         	in the plain text
#  Output: function returns a single character encoded using the
#          	Vigenere algorithm. You may not use a 2-D list
def encode_character (p, s):
    return chr(ord(p) + ord(s) - 97)

#  Input: p is a character in the pass phrase and s is a character
#         	in the plain text
#  Output: function returns a single character decoded using the
#          	Vigenere algorithm. You may not use a 2-D list
def decode_character (p, s):
	return chr((ord(s) - ord(p)) % 26 + 97)

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          	Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    text = list(strng)
    phrase_list = list(phrase)
    pass_phrase = []
    j = 0
    for i in range(len(text)):
        if j < len(phrase_list) - 1:
            pass_phrase.append(phrase_list[j])
            j += 1
        else:
            pass_phrase.append(phrase_list[j])
            j = 0
    
    #building alphabet grid
    grid = []
    step = 0
    for i in range(26):
        row = []
        for j in range(26):
            row.append(chr((j + step) % 26 + 97))
        grid.append(row)
        step += 1
    
    code = ''
    for i in range(len(text)):
        code += grid[ord(pass_phrase[i]) - 97][ord(text[i]) - 97]
    return code

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          	Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    text = list(strng)
    phrase_list = list(phrase)
    pass_phrase = []
    j = 0
    for i in range(len(text)):
        if j < len(phrase_list) - 1:
            pass_phrase.append(phrase_list[j])
            j += 1
        else:
            pass_phrase.append(phrase_list[j])
            j = 0
    
    #building alphabet grid
    grid = []
    step = 0
    for i in range(26):
        row = []
        for j in range(26):
            row.append(chr((j + step) % 26 + 97))
        grid.append(row)
        step += 1
    
    code = ''
    for i in range(len(text)):
        for j in range(26):
            for k in range(26):
                if (grid[j][k] == text[i]) and (k == ord(pass_phrase[i]) - 97):
                    code += chr(j + 97)
    return code

def main():
    decrypted_rail_fence = sys.stdin.readline()
    decrypted_rail_fence = decrypted_rail_fence.strip()
    de_num_lines = int(sys.stdin.readline())
    print(rail_fence_encode(decrypted_rail_fence, de_num_lines))

    encrypted_rail_fence = sys.stdin.readline()
    encrypted_rail_fence = encrypted_rail_fence.strip()
    en_num_lines = int(sys.stdin.readline())
    print(rail_fence_decode(encrypted_rail_fence, en_num_lines))

    decrypted_vigenere = sys.stdin.readline()
    decrypted_vigenere = decrypted_vigenere.strip()
    de_key = sys.stdin.readline()
    de_key = de_key.strip()
    print(vigenere_encode(decrypted_vigenere, de_key))

    encrypted_vigenere = sys.stdin.readline()
    encrypted_vigenere = encrypted_vigenere.strip()
    en_key = sys.stdin.readline()
    en_key = en_key.strip()
    print(vigenere_decode(encrypted_vigenere, en_key))

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()