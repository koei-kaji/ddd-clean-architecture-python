class InjectionException(Exception):
    ...


class AdapterNotFoundError(InjectionException):
    ...


class InteractorNotFoundError(InjectionException):
    ...
