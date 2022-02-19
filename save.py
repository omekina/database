from modules import pdb_datatypes


class session:
    __slots__ = "flags", "columns", "columnNames", "data"
    def __init__(self, flags, columns, columnNames, data):
        self.flags = flags
        self.columns = columns
        self.columnNames = columnNames
        self.data = data
    def parse_data(self):
        data = ""

