import os

class GitObject:

    def __init__(self, path, repository):
        with open(path, "rb") as f:
            self.data = f.read()
            self.hashcode = "".join(path.split(os.path.sep)[-2:])
            self.repository = repository
