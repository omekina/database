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