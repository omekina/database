import program_data
from modules import pdb_bitlogic


class session: # Database session
    def __init__(self, path_to_file):
        if not path_to_file[-4:] == ".pdb":
            raise Exception("load: wrong filetype")
        else:
            self.path = path_to_file
    

    def load(self): # Load file into RAM
        try:
            file = open(self.path, "rb")
            read = file.read()
            file.close()
            self.head, self.body = read[:10], read[10:]
        except: raise Exception("load: error when loading file")
    
# ----- PARSED FILE -----
# head (string)
# body (string)
# -----------------------

    def parse_head(self): # Parse head from file data
        try:
            head = pdb_bitlogic.octets_to_bits(self.head)
            if not len(head) == 80: raise Exception("length error")
            version, head = int(head[:12], base=2), head[12:]
            if not version == program_data.version_id: raise Exception("versions do not match")
            self.flags, head = head[:16], head[16:]
            self.layoutLength, head = int(head[:12], base=2), head[12:]
            self.lutLength, head = int(head[:36], base=2), head[36:]
            self.lutPaddingLength = int(head, base=2) 
        except Exception as exc: raise Exception("load->head: " + str(exc))
        except: raise Exception("load->head: error when parsing")

# ----- PARSED HEAD -----
# flags (string)
# layoutLength (int)
# lutLength (int)
# lutPaddingLength (int)
# -----------------------

    def parse_layout(self): # Preparse layout from file data
        try:
            if not (self.layoutLength/16).is_integer(): raise Exception("length error")
            if not len(self.body) >= self.layoutLength: raise Exception("length discrepancy")
            self.totalColumns = self.layoutLength//16
            self.columns = []
            self.verifyBodyLength = 0
            for i in range(self.totalColumns):
                column, self.body = self.body[:16], self.body[16:]
                isKey, column = bool(int(column[:1], base=2)), column[1:]
                isAutoIncrement, column = bool(int(column[:1], base=2)), column[1:]
                dataType, column = int(column[:6], base=2), column[6:]
                nameLength = int(column, base=2)
                self.verifyBodyLength += nameLength
                self.columns.append([isKey, isAutoIncrement, dataType, nameLength])
        except Exception as exc: raise Exception("load->layout: " + str(exc))
        except: raise Exception("load->layout: error when parsing")

# ----- prePARSED LAYOUT -----
# isKey (bool)
# isAutoIncrement (bool)
# dataType (int)
# nameLength (int)
#
# verifyBodyLength
# ----------------------------

    def parse_lut(self): # Parse LUT from file data
        try:
            if not len(self.body) >= self.lutLength: raise Exception("length error")
            if not self.lutPaddingLength <= self.lutLength: raise Exception("padding length error")
            self.lutActualLength = self.lutLength - self.lutPaddingLength
            if not len(self.body) >= self.lutActualLength: raise Exception("length error")
            lut, self.body = self.body[:self.lutActualLength], self.body[self.lutActualLength:]
            self.rows = []
            i = 0
            while len(lut) > 0:
                if i >= len(lut): break
                if lut[i] == "1":
                    lut = lut[1:]
                    pointerLength, lut = int(lut[:7], base=2), lut[7:]
                    pointer, lut = int(lut[:pointerLength], base=2), lut[pointerLength:]
                    self.rows.append([True, pointer])
                else:
                    lut = lut[1:]
                    self.rows.append([False])
        except Exception as exc: raise Exception("load->lut: " + str(exc))
        except: raise Exception("load->lut: error when parsing") 
