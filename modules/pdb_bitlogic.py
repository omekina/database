def octets_to_bits(octets): # Decode octets to string of bits
    bits = ""
    try:
        for octet in octets:
            translate_octet = bin(octet)[2:]
            bits += translate_octet + "00000000"[len(translate_octet):]
    except: raise Exception("pdb_bitlogic: error when decoding octets")
    return bits


def bits_to_octets(bits): # Encode bits to octets (bytes)
    octets = b''
    if not (len(bits)/8).is_integer(): raise Exception("pdb_bitlogic: input is not in valid octet length")
    try:
        for i in range(0, len(bits), 8):
            octets += int(bits[i:i+8], base=2).to_bytes(1, byteorder="little")
    except: raise Exception("pdb_bitlogic: error when encoding bits")
