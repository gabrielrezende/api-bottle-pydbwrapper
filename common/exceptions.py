class HTTPResponseError(Exception):

    def __init__(self, code, message):
        super(HTTPResponseError, self).__init__()
        self.code = code
        self.message = message


class NotFoundError(HTTPResponseError):

    def __init__(self, message):
        super(NotFoundError, self).__init__(404, message)


class UnauthorizedError(HTTPResponseError):

    def __init__(self, message):
        super(UnauthorizedError, self).__init__(401, message)


class BadRequestError(HTTPResponseError):

    def __init__(self, message):
        super(BadRequestError, self).__init__(400, message)


class ConflictError(HTTPResponseError):

    def __init__(self, message):
        super(ConflictError, self).__init__(409, message)


class ForbbidenError(HTTPResponseError):

    def __init__(self, message):
        super(ForbbidenError, self).__init__(403, message)


class EntityError(HTTPResponseError):

    def __init__(self, message):
        super(EntityError, self).__init__(422, message)


class IntegrationError(Exception):

    def __init__(self, message):
        super(IntegrationError, self).__init__()
        self.message = message
