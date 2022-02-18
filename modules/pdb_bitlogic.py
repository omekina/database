def octets_to_bits(octets): # Decode octets to string of bits
    octet_stream = octets
    bits = ""
    try:
        while len(octet_stream) > 0:
            translate_octet = bin(octet_stream[0])[2:]
            bits += "00000000"[len(translate_octet):] + translate_octet
            octet_stream = octet_stream[1:]
        return bits
    except: raise Exception("pdb_bitlogic: error when decoding octets")


def bits_to_octets(bits): # Encode bits to octets (bytes)
    bit_stream = bits
    octets = b''
    if not (len(bits)/8).is_integer(): raise Exception("pdb_bitlogic: input is not in valid octet length")
    try:
        while len(bit_stream) > 0:
            octet = int(bit_stream[:8], base=2).to_bytes(1, byteorder="little")
            octets += octet
            bit_stream = bit_stream[8:]
        return octets
    except: raise Exception("pdb_bitlogic: error when encoding bits")
