"""Custom domain exceptions."""


class DataLoadError(Exception):
    """Raised when a file cannot be found or read."""

    pass


class ValidationError(Exception):
    """Raised when data structure is invalid or lacks numeric columns."""

    pass
