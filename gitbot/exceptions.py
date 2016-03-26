class NotARepositoryError(Exception):

    def __init__(self, path):
        Exception.__init__(self, "'%s' is not a git repository" % path)
