from modules import pdb_bitlogic


class dt0: # String
    def decode(raw_data):
        data = raw_data.decode("utf-8", "ignore")
        return data
    def encode(data):
        raw_data = data.encode("utf-8", "ignore")
        return raw_data


def decode(raw_data, datatype):
    try:
        bytes_data = pdb_bitlogic.bits_to_octets(raw_data)
        if datatype == 0: # String
            decoded = dt0.decode(bytes_data)
        else: raise Exception("datatype not supported") # Datatype not supported
        return decoded
    except Exception as exc: raise Exception("datatype_decode: " + str(exc))
    except: raise Exception("datatype_decode: error when decoding data")

def encode(raw_data, datatype):
    try:
        if datatype == 0: # String
            bytes_data = dt0.encode(raw_data)
            encoded = pdb_bitlogic.octets_to_bits(bytes_data)
        else: raise Exception("datatype not supported") # Datatype not supported
        return encoded
    except Exception as exc: raise Exception("datatype_encode: " + str(exc))
    except: raise Exception("datatype_encode: error when encoding data")

