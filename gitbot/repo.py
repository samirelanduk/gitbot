import os
from .exceptions import *

class Repository:

    def __init__(self, location):
        self.location = os.path.abspath(location)
        if ".git" not in os.listdir(self.location):
            raise NotARepositoryError(self.location)
