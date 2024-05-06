class ApplicationException(Exception):
    """Base exception class for all application-specific errors."""

    def __init__(self, message="An error occurred", status_code=500):
        self.message = message
        self.status_code = status_code


class UserNotFoundException(ApplicationException):
    """Exception raised when a user is not found."""

    def __init__(self, message="User not found"):
        super().__init__(message, status_code=404)


class UserAlreadyExistsException(ApplicationException):
    """Exception raised when a user already exists."""

    def __init__(self, message="User already exists"):
        super().__init__(message, status_code=400)


class PostNotFoundException(ApplicationException):
    """Exception raised when a post is not found."""

    def __init__(self, message="Post not found"):
        super().__init__(message, status_code=404)


class PostCreationFailedException(ApplicationException):
    """Exception raised when post creation fails."""

    def __init__(self, message="Post creation failed"):
        super().__init__(message, status_code=500)


class PostUpdateFailedException(ApplicationException):
    """Exception raised when post update fails."""

    def __init__(self, message="Post update failed"):
        super().__init__(message, status_code=500)


class PostDeletionFailedException(ApplicationException):
    """Exception raised when post deletion fails."""

    def __init__(self, message="Post deletion failed"):
        super().__init__(message, status_code=500)


class CategoryNotFoundException(ApplicationException):
    """Exception raised when a category is not found."""

    def __init__(self, message="Category not found"):
        super().__init__(message, status_code=404)


class DatabaseOperationException(ApplicationException):
    """Exception raised for database operation failures."""

    def __init__(self, message="Database operation failed"):
        super().__init__(message, status_code=500)


class CommentNotFoundException(ApplicationException):
    """Exception raised when a comment is not found."""

    def __init__(self, message="Comment not found"):
        super().__init__(message, status_code=404)


class CommentCreationFailedException(ApplicationException):
    """Exception raised when comment creation fails."""

    def __init__(self, message="Comment creation failed"):
        super().__init__(message, status_code=500)


class CommentUpdateFailedException(ApplicationException):
    """Exception raised when comment update fails."""

    def __init__(self, message="Comment update failed"):
        super().__init__(message, status_code=500)

