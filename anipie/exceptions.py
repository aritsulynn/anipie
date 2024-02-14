class AnipieException(Exception):
    """Base exception for all Anipie errors"""
    
    pass

class TitleNotFoundError(AnipieException):
    """Requested title was not found"""

    def __init__(self, message: str, /, *, title: str) -> None:
        super().__init__(message)
        self.title = title

class QueryTypeError(AnipieException):
    """Invalid query type"""

    def __init__(self, message: str, /, *, type: str) -> None:
        super().__init__(message)
        self.type = type
