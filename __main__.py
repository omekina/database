from os import listdir
from load import session
from os.path import isdir, isfile


def autoParse(filename):
    database = session(filename)
    database.load()
    database.parse_head()
    database.parse_layout()
    database.parse_lut()
    database.parse_data()
    return database


if __name__ == "__main__":
    database = autoParse("test2.pdb")
    print(database.data)
