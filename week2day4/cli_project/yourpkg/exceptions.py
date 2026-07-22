"""Custom exceptions for the package."""


class FileProcessingError(Exception):
    """raised when a file does not exist or cannot be read"""


class ValidationError(Exception):
    """custom exception for data validation and formatting errors"""

    pass
