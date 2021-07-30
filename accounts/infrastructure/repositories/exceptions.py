class RepositoryError(Exception):
    pass


class NotFoundError(RepositoryError):

    def __init__(self, message: str = 'Entity not found'):
        self.message = message
