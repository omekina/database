from modules import pdb_datatypes


class session:
    __slots__ = "flags", "columns", "columnNames", "data", "rows", "bitData", "bitLut", "bitLayout", "bitHead"
    def __init__(self, flags, columns, columnNames, data):
        self.flags = flags
        self.columns = columns
        self.columnNames = columnNames
        self.data = data
        self.rows = []
    

    def construct_data(self): # Construct data bit stream
        try:
            data = ""
            for i in range(len(self.columnNames)):
                column = pdb_datatypes.encode(self.columnNames[i], 0)
                self.columns[i].append(len(column))
                data += column
            for row in self.data:
                if row[0]:
                    row_bitencoded = pdb_datatypes.encode(row[0])
                    self.rows.append([True, len(row_bitencoded])
                    data += row_bitencoded
                else:
                    self.rows.append([False])
            self.bit_data = data
        except Exception as exc: raise Exception("save->data: " + str(exc))
        except: raise Exception("save->data: error when constructing")
    

    def construct_lut(self): # Construct lut bit stream
        try:
            lut = ""
            for row in self.rows:
                if row[0]:
                    pointer = bin(row[1])
                    if pointer[:2] == "0b"
                        pointer = pointer[2:]
                    pointer_length = bin(len(pointer))[2:]
                    if len(pointer_length) > 7: raise Exception("pointer too big")
                    pointer_length = "0000000"[len(pointer_length):] + pointer_length
                    lut += "1" + pointer_length + pointer
                else:
                    lut += "0"
            if not (len(lut)/8).is_integer():
                remainder = len(lut) % 8
                lut += "".join(["0" for i in range(remainder)])
            self.bitLut = lut
        except Exception as exc: raise Exception("save->lut: " + str(exc))
        except: raise Exception("save->lut: error when constructing")

