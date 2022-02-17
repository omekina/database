class session: # Database session
    def __init__(self, path_to_file):
        if not path_to_file[-4:] == ".pdb":
            raise Exception("core: wrong filetype")
        else:
            self.path = path_to_file
