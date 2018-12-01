#!/bin/python3

digits = [
    [  1,
     1,  1,
       0,
     1,  1,
       1,  ],

    [  0,
     0,  1,
       0,
     0,  1,
       0,  ],

    [  1,
     0,  1,
       1,
     1,  0,
       1,  ],

    [  1,
     0,  1,
       1,
     0,  1,
       1,  ],

    [  0,
     1,  1,
       1,
     0,  1,
       0,  ],

    [  1,
     1,  0,
       1,
     0,  1,
       1,  ],

    [  1,
     1,  0,
       1,
     1,  1,
       1,  ],

    [  1,
     0,  1,
       0,
     0,  1,
       0,  ],

    [  1,
     1,  1,
       1,
     1,  1,
       1,  ],

    [  1,
     1,  1,
       1,
     0,  1,
       1,  ],
]

def get_braille(left_side):
    braille = 0x2800
    if left_side[0]:
        braille += 0x01
    if left_side[1]:
        braille += 0x02
    if left_side[2]:
        braille += 0x04
    if left_side[3]:
        braille += 0x40
    return chr(braille)

def encode_digit(num):
    data = digits[num]
    left = get_braille([data[i] for i in [0, 1, 4, 6]])
    right = get_braille([data[i] for i in [0, 2, 5, 6]])
    out = left
    if data[0]:
        out += chr(0x0340)
    if data[3]:
        out += chr(0x0335)
    if data[6]:
        out += chr(0x0331)
    out += right
    return out

if __name__ == '__main__':
    import sys
    out = ''
    for arg in sys.argv[1:]:
        for c in arg:
            if ord(c) >= 48 and ord(c) < 58:
                out += encode_digit(int(c))
            else:
                out += c
        out += ' '
    print(out)
