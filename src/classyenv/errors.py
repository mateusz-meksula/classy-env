from typing import Any


class ClassyEnvError(Exception):
    """Base Classy Env exception"""


class ClassyEnvClassInstantiatedError(ClassyEnvError):
    def __init__(self) -> None:
        message = "Cannot instantiate object of 'ClassyEnv' class"
        super().__init__(message)


class EnvVarNameTypeError(ClassyEnvError, ValueError):
    def __init__(self, envvar_name: Any) -> None:
        message = f"Invalid type {type(envvar_name)}, expected type: 'str'"
        super().__init__(message)


class EnvVarNameEmptyError(ClassyEnvError, ValueError):
    def __init__(self) -> None:
        message = "Cannot set empty string as environment variable"
        super().__init__(message)


class AttributeMutabilityError(ClassyEnvError, AttributeError):
    def __init__(self, attr_name: str, envvar_name: str) -> None:
        message = f"Cannot set {attr_name!r} attribute. This attribute corresponds to a {envvar_name!r} environment variable"
        super().__init__(message)


class EnvVarNotFoundError(ClassyEnvError, ValueError):
    def __init__(self, envvar_name: str) -> None:
        message = f"Cannot find the {envvar_name!r} environment variable"
        super().__init__(message)


class EnvVarsNotFoundError(ClassyEnvError, ValueError):
    def __init__(self, missing_envvars: list[str]) -> None:
        message = "Cannot find the following environment variables:\n"
        message += "\n".join(f"\t{envvar!r}" for envvar in missing_envvars)
        super().__init__(message)


class RepeatedEnvVarsError(ClassyEnvError, ValueError):
    def __init__(self, repeated_envvars: list[str]) -> None:
        message = "The following environment variables were declared more than once:\n"
        message += "\n".join(f"\t{envvar!r}" for envvar in repeated_envvars)
        super().__init__(message)
