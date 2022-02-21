from modules import pdb_bitlogic


class dt0: # String
    def decode(raw_data):
        data = raw_data.decode("utf-8", "ignore")
        return data
    def encode(data):
        raw_data = data.encode("utf-8", "ignore")
        return raw_data
class dt1: # SInt
    def decode(raw_data):
        if raw_data[0] == "0":
            data = int(raw_data[1:], base=2)
        else:
            data = -(int(raw_data[1:], base=2))
        return data
    def encode(data):
        raw_data = bin(data)
        if raw_data[0] == "-":
            raw_data = raw_data[3:]
        else:
            raw_data = raw_data[2:]
        return raw_data


def decode(raw_data, datatype):
    try:
        if datatype == 0: # String
            bytes_data = pdb_bitlogic.bits_to_octets(raw_data)
            decoded = dt0.decode(bytes_data)
        elif datatype == 1: # SInt
            decoded = dt1.decode(raw_data)
        else: raise Exception("datatype not supported") # Datatype not supported
        return decoded
    except Exception as exc: raise Exception("datatype_decode: " + str(exc))
    except: raise Exception("datatype_decode: error when decoding data")

def encode(raw_data):
    try:
        if type(raw_data) is str: # String
            bytes_data = dt0.encode(raw_data)
            encoded = pdb_bitlogic.octets_to_bits(bytes_data)
        elif type(raw_data) is int: # SInt
            bytes_data = dt1.encode(raw_data)
        else: raise Exception("datatype not supported") # Datatype not supported
        return encoded
    except Exception as exc: raise Exception("datatype_encode: " + str(exc))
    except: raise Exception("datatype_encode: error when encoding data")

