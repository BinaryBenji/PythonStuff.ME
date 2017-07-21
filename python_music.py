import winsound
import string

#Converts a char string into binary string.
#Fill automaticaly 8 digits for each sound
def string_bin(string):
    return ' '.join(format(ord(c), 'b').zfill(8) for c in string)

print("### BINARY PIANO ###\n")
print("Use letters + space, ?,!,.\n")
string = input("Enter your text : ")
string = str(string)
sounds = string_bin(string)
print("Binary : " + sounds + "\n")
print("~~~~~ TUTUUTUTUTUTUTUTUUTTUTUTUUUUUU ~~~~~~")

for note in sounds.split():
    if note == "01000001" or note == "01100001": # A or a
        freq = 237
        rate = 500
    elif note == "01000010" or note == "01100010": # B or b
        freq = 262
        rate = 500
    elif note == "01000011" or note == "01100011": # C or c
        freq = 294
        rate = 500
    elif note == "01000100" or note == "01100100": # D or d
        freq = 330
        rate = 500
    elif note == "01000101" or note == "01100101": # E or e
        freq = 349
        rate = 500
    elif note == "01000110" or note == "01100110": # F or f
        freq = 392
        rate = 500
    elif note == "01000111" or note == "01100111": # G or g
        freq = 440
        rate = 500
    elif note == "01001000" or note == "01101000": # H or h
        freq = 494
        rate = 500
    elif note == "01001001" or note == "01101001": # I or i
        freq = 523
        rate = 500
    elif note == "01001010" or note == "01101010": # J or j
        freq = 523
        rate = 1000
    elif note == "01001011" or note == "01101011": # K ot k
        freq = 494
        rate = 1000
    elif note == "01001100" or note == "01101100": # L or l
        freq = 440
        rate = 1000
    elif note == "01001101" or note == "01101101": # M or m
        freq = 392
        rate = 1000
    elif note == "01001110" or note == "01101110": # N or n
        freq = 349
        rate = 1000
    elif note == "01001111" or note == "01101111": # O or o
        freq = 330
        rate = 1000
    elif note == "01010000" or note == "01110000": # P or p
        freq = 294
        rate = 1000
    elif note == "01010001" or note == "01110001": # Q or q
        freq = 262
        rate = 1000
    elif note == "01010010" or note == "01110010": # R or r
        freq = 237
        rate = 1000
    elif note == "01010011" or note == "01110011": # S or s
        freq = 262
        rate = 1500
    elif note == "01010100" or note == "01110100": # T or t
        freq = 294
        rate = 1500
    elif note == "01010101" or note == "01110101": # U or u
        freq = 330
        rate = 1500
    elif note == "01010110" or note == "01110110": # V or v
        freq = 349
        rate = 1500
    elif note == "01010111" or note == "01110111": # W or w
        freq = 392
        rate = 1500
    elif note == "01011000" or note == "01111000": # X or x
        freq = 440
        rate = 1500
    elif note == "01011001" or note == "01111001": # Y or y
        freq = 523
        rate = 1500
    elif note == "01011010" or note == "01111010": # Z or z
        freq = 523
        rate = 2000
    elif note == "00100000": # Space
        freq = 50
        rate = 200
    elif note == "00111111": # ?
        freq = 1000
        rate = 200
    elif note == "00100001": # !
        freq = 750
        rate = 200
    elif note == "00101110": # .
        freq = 300
        rate = 200
    else : #unknown
        freq = 440
        rate = 200
    winsound.Beep(freq, rate)
