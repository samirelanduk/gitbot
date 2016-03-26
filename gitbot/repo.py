import os
from .exceptions import *

class Repository:

    def __init__(self, location):
        self.location = os.path.abspath(location)
        if ".git" not in os.listdir(self.location):
            raise NotARepositoryError(self.location)

        self.objects = self.get_loose_objects() + self.get_packed_objects()


    def __repr__(self):
        return "<Repository (%i objects)>" % len(self.objects)


    def get_loose_objects(self):
        return []


    def get_packed_objects(self):
        return []
