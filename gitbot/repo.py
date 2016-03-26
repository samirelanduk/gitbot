import os
from .exceptions import *
from .objects import *

class Repository:

    def __init__(self, location):
        self.location = os.path.abspath(location)
        if ".git" not in os.listdir(self.location):
            raise NotARepositoryError(self.location)
        self.objects_directory = os.path.sep.join([self.location, ".git", "objects"])

        self.objects = self.get_loose_objects() + self.get_packed_objects()


    def __repr__(self):
        return "<Repository (%i objects)>" % len(self.objects)


    def get_loose_objects(self):
        loose_objects = []
        loose_directories = [
         d for d in os.listdir(self.objects_directory) if len(d) == 2
        ]
        for loose_directory in loose_directories:
            path = self.objects_directory + os.path.sep + loose_directory
            for obj in os.listdir(path):
                loose_objects.append(path + os.path.sep + obj)

        return [GitObject(path, self) for path in loose_objects]


    def get_packed_objects(self):
        return []
