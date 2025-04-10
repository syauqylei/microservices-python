### Microservices Python

This project built moslty using FastAPI for simplicity and fast development. Choosing FastAPI comes down with the builtin openapi and swagger support at the getgo.
Therefore, we can have documentation as well.

### Structure of this project

```
\common
  \ports
    \user_service_port.py
    \listing_service_port.py
  \types
    schemas.py
\user-service
\listing-service
\public-service
```

The project consist of 3 core services, `user-service`, `listing-service` and `public-service` is a api application built in python frameworks.
`common` the otherhand acts as a utility where common `ports` and `schema` are store. This package is shared across the project.
The `ports` is an interface of existing rest api so we can use in other project if we want to intergrate the api with this port.

### How to run APIs

#### listing service

```
# enter the directory of listing service
cd listing service

# Locate the path for the Python 3 installation
which python3

# Create the virtual environment in a folder named "env" in the current directory
virtualenv env --python=<path_to_python_3>

# Start the virtual environment
source env/bin/activate

# Install the required dependencies/libraries
pip install -r python-libs.txt
```

#### install poetry

Some of the service is set up using poetry. Therefore, you should install the poetry.
You can install using this documentation

https://python-poetry.org/docs/

#### user service

```
# enter the directory of listing service
cd user-service

poetry lock

poetry install

poetry run uvicorn main:app --port=8001

```

#### public service

```
# enter the directory of listing service
cd public-service

poetry lock

poetry install

poetry run uvicorn main:app --port=8001

```
