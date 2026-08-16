

class SalesAnalyticError(Exception):
    """ base exception for the application."""
    pass


class FileLoadError(SalesAnalyticError):
    """ raise when a csv can not be loaded. """
    pass

class DataValidationError(SalesAnalyticError):
    """ raise when data validation fails. """
    pass

