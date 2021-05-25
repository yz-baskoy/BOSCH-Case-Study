KEYBOARD_MATRIX = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]


def getCharacterCoord(c, array):
    # function taken from this <link> and modified to handle lowercase to uppercase
    # link: https://github.com/wsong/Typo-Distance/blob/d5bb17d24154e5c5762416060cfed487cdb5e4ef/typodistance.py#L67L77
    row = -1
    column = -1
    c = c.upper()
    for r in array:
        if c in r:
            row = array.index(r)
            column = r.index(c)
            return (row, column)
    raise ValueError(c + " not found in given keyboard layout")


def calculate_adjacency(sentence):
    total_error_rate = 0
    for i in range(len(sentence)-1):
        total_error_rate += adjacency_rate(sentence[i], sentence[i+1], i, sentence)
    return total_error_rate


def adjacency_rate(letter, nextletter, index, sentence):
    try:
        row, column = getCharacterCoord(letter, KEYBOARD_MATRIX)
    except ValueError:
        return 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            # handle indexerror if user call element that not exist in matrix
            try:
                if row + i >= 0 and column + j > 0:
                    if KEYBOARD_MATRIX[row+i][column+j] == nextletter.upper():
                        print(f"Adjacency Found in {sentence}: {index}({letter},{nextletter})")
                        return 1
            except IndexError:
                continue
    return 0

#Application section
first_sen = 'Quality is much better than quantity. One home run is much better than two doubles'
second_sen = "Qwuality isd mucxh bettedr than quanmtity. Oıne homke run is much bvetter than two doubnles"

print("="*120)
adj_rate_1 = calculate_adjacency(first_sen)
print("="*120, end="\n\n")

print("="*120)
adj_rate_2 = calculate_adjacency(second_sen)
print("="*120, end="\n\n")

print("="*120)
print(f"{first_sen}: (Error Rate: {adj_rate_1})")
print(f"{second_sen}: (Error Rate: {adj_rate_2})")
print("="*120)
