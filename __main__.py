from os import listdir
from load import session
from os.path import isdir, isfile


if __name__ == "__main__":
    database = session("modules/testbin.pdb")
    database.load()
    database.parse_head()
    database.parse_layout()
    database.parse_lut()
