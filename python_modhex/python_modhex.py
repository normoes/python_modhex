import re

ALPHABET = "cbdefghijklnrtuv"

def from_hex(data):
    p = re.compile("^[a-fA-F0-9]+$")

    # if (! /^[a-fA-F0-9]+$/.test(hex)) {
    if not p.match(data):
        raise ValueError("Invalid characters in hex input.")

    if len(data) % 2:
        data = "0" + data
    result = []
    # for (var bytes = [], c = 0; c < hex.length; c += 2) {
    for i in range(0,len(data), 2):
        result.append(int(data[i:i+2], 16))
    return result;

def to_hex(data):
    result = []
    for l in data:
        result.append(hex(int(l, 16) >> 4)[2:])
        result.append(hex(int(l, 16) & int("0xf", 16))[2:])
    return "".join(result)

def from_modhex(data):
    result = []
    toggle = False
    keep = 0

    for i, l in enumerate(data):
        ch = data[i:i+1]
        n = ALPHABET.find(ch)
        if n == -1:
            raise ValueError(f"{data} is not properly encoded.")
        toggle = not toggle
        if toggle:
            keep = n
        else:
            # bytes.push((keep << 4) | n);           
            result.append(hex((keep << 4) | n)[2:])
    # Use 'to_hex' on the array.
    return to_hex(result)

def to_modhex(data):
    result = []
    for l in from_hex(data):
        index = (l>>4) & int("0xf", 16)
        result.append(ALPHABET[index])
        index = l & int("0xf", 16)
        result.append(ALPHABET[index])
    return "".join(result)


if __name__ == "__main__":
    modhex = "cccccccgklgcvnkcvnnegrnhgrjkhlkfhdkclfncvlgj"
    hex_ = "000000059a50fb90fbb35cb65c896a946290a4b0fa58"
    # Convert from modhex.
    hex__ = from_modhex(modhex)
    print(hex__)
    assert hex__ == hex_, "conversion failed"
    # Convert to modhex.
    modhex_ = to_modhex(hex_)
    print(modhex_)
    assert modhex_ == modhex, "conversion failed"

    try:
        # Invalid character 'a'.
        from_modhex("acccccccgklgcvnkcvnnegrnhgrjkhlkfhdkclfncvlgj")
    except (ValueError) as e:
        print(str(e))

    try:
        # Invalid character 'a'.
        to_modhex("0000000q59a50fb90fbb35cb65c896a946290a4b0fa58")
    except (ValueError) as e:
        print(str(e))


