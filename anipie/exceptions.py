class AnipieException(Exception):
    """Base exception for all Anipie errors"""
    
    pass

class TitleNotFoundError(AnipieException):
    """Requested title was not found"""

    pass
