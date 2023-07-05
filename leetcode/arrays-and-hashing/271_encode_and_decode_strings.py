def encode(self, strs):
    string = ""

    for word in strs:
        string = str(len(word)) + "#" + word

    return string

def decode(self, str):
    array = []
    i = 0

    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        array.append(str[j + 1:j + 1 + length])
        i = j + 1 + length