# Classy Env

## About

Classy Env is a lightweight python package for managing environment variables in OOP way.

## Requirements

This package requires python >= 3.11

## Installation

Classy Env is available on pip and can be installed by running the following command:

```shell
pip install classy-env
```

## Usage

Create a `ClassyEnv` subclass and declare its attributes with `EnvVar` function:

```python
from classyenv import ClassyEnv, EnvVar


class Settings(ClassyEnv):
    database_user = EnvVar("DB_USER")
    database_password = EnvVar("DB_PASSWORD")
    api_secret_key = EnvVar("SECRET_KEY")
```

`EnvVar` function takes a name of the environment variable as an argument. Value of that variable will be assigned to the corresponding attribute.

Then, create an object of your subclass and access environment variables by object attributes:

```python
settings = Settings()

database_connection = connect(
    user=settings.database_user,
    password=settings.database_password,
)
```

Note! TODO make an MD note
At the object's creation, classy env will perform checks if environment variables provided to `EnvVar` functions are set. If not, an exception will be raised.

### Mutating the `ClassyEnv` instances and subclasses

At this moment, mutating the instances of `ClassyEnv` class is not supported:

```python
settings.database_user = "Roe_Jogan123" # this will raise an exception
```

Same with mutating the class attributes of `ClassyEnv` subclasses:

```python
Settings.database_user = "Roe_Jogan123" # this will raise an exception
```

## License

This project is licensed under the terms of the MIT license.
