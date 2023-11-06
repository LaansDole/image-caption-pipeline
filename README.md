# FastAPI Production Setup with Poe The Poet

Refer to ***[TODO](./TODO.md)*** to see the future propects of the project 

This project uses Python and poetry, the modern Python package installer. Remember to run this command in the root directory of your project where the `pyproject.toml` file is located. Here are the main elements you need to know to get started:

## DevOps Quick Start Guide

DevOps CI/CD Quick Start Guide with GitHub Actions 🛠️🐙⚡️

[![codecov](https://codecov.io/gh/dpills/devops-quick-start-guide/graph/badge.svg?token=jwraAw5pYK)](https://codecov.io/gh/dpills/devops-quick-start-guide)

## Virtual Environment

Note that for this the package venv is to be used.

To know well the what is it and the why check this out https://docs.python.org/3/tutorial/venv.html

In short, a virtual environment will help us manage an isolated version of python interpreter. And so too installed packages. In this way. Different project will not have to depends on the same packages installation and have to conflict. Read the link above explain and show it well.

## Usage

- To create a virtual environment, navigate to your root directory and run:

```bash
python3 -m venv virtual-env
```

- To activate the environment, use:

```bash
source virtual-env/bin/activate
```

- To deactivate the environment, use:
```bash
deactivate
```

### ***Alternatively***
There is another way to create a virtual environment in python using miniconda
- [Miniconda Installation](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)
- To create a virtual environment in a specific python version:
```python
conda create --name env-python3 python=3.11
```
- To activate the environment:
```python
conda activate env-python3
```
- To deactivate the environment:
```python
conda deactivate
```
## Build

### Prerequisites

- ***[Poetry Installation](https://python-poetry.org/docs/#installing-with-pipx)***
- On MacOS, you can just run:
```bash
brew install poetry
```
- ***[Poe The Poet Installation](https://poethepoet.natn.io/installation.html)***

### Build on local

The Poetry equivalent of `pip install -r requirements.txt` is `poetry install`.

In a Python project managed with Poetry, dependencies are listed in a `pyproject.toml` file. When you run `poetry install`, Poetry reads the `pyproject.toml` file, resolves the dependencies, and installs them:

```bash
poetry install
```

This command reads the `pyproject.toml` file and installs all the dependencies listed in it. 
***To add additional dependencies/packages to your project, use:***
```bash
poetry add --dev [dependencies]
poetry run [dependency]
```

### To run locally

- ***To start the server at http://0.0.0.0:8000***
```bash
poe compose
```

- ***To run format on project***
```bash
poe format
```

- ***To prettier the python files***
```bash
poe lint
```

- ***To check the type in python files***
```bash
poe typecheck
```

## Requirements.txt

- To export the requirements.txt
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes --without=dev
```

- To see the project dependencies
```bash
poetry show --tree --without dev
```

It should look like this:

```bash
fastapi 0.103.2 FastAPI framework, high performance, easy to learn, fast to code, ready for production
├── anyio >=3.7.1,<4.0.0
│   ├── idna >=2.8 
│   └── sniffio >=1.1 
├── pydantic >=1.7.4,<1.8 || >1.8,<1.8.1 || >1.8.1,<2.0.0 || >2.0.0,<2.0.1 || >2.0.1,<2.1.0 || >2.1.0,<3.0.0
│   ├── annotated-types >=0.4.0 
│   ├── pydantic-core 2.10.1 
│   │   └── typing-extensions >=4.6.0,<4.7.0 || >4.7.0 
│   └── typing-extensions >=4.6.1 (circular dependency aborted here)
├── starlette >=0.27.0,<0.28.0
│   └── anyio >=3.4.0,<5 
│       ├── idna >=2.8 
│       └── sniffio >=1.1 
└── typing-extensions >=4.5.0
uvicorn 0.23.2 The lightning-fast ASGI server.
├── click >=7.0
│   └── colorama * 
├── colorama >=0.4
├── h11 >=0.8
├── httptools >=0.5.0
├── python-dotenv >=0.13
├── pyyaml >=5.1
├── uvloop >=0.14.0,<0.15.0 || >0.15.0,<0.15.1 || >0.15.1
├── watchfiles >=0.13
│   └── anyio >=3.0.0 
│       ├── idna >=2.8 
│       └── sniffio >=1.1 
└── websockets >=10.4
```
# References
- [Python pip equivalent of node's package.json](https://stackoverflow.com/questions/48941116/does-python-pip-have-the-equivalent-of-nodes-package-json)
- [Poetry Documentation](https://python-poetry.org/)
- [Poe The Poet Documentation](https://poethepoet.natn.io/installation.html)
