# FastAPI pipeline for Image Captioning Model

This project uses Python and poetry. Remember to run below commands in the root directory of your project where the `pyproject.toml` file is located. Here are the main elements you need to know to get started:

## Model
[nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)

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

- ***[pipx Installation](https://github.com/pypa/pipx)***
- ***[Poetry Installation](https://python-poetry.org/docs/#installing-with-pipx)***
- ***[Poe The Poet Installation](https://poethepoet.natn.io/installation.html)***

### Build on local

- ***If you have Docker installed, you can just:***

```docker
docker compose up --build
```

- ***Otherwise:***

In a Python project managed with Poetry, dependencies are listed in a `pyproject.toml` file. When you run `poetry install`, Poetry reads the `pyproject.toml` file, resolves the dependencies, and installs them:

```bash
poetry install
```
OR
```bash
pip install -r requirements.txt
```

This command reads the `pyproject.toml` file and installs all the dependencies listed in it. 
***To add additional dependencies/packages to your project, use:***
```bash
pip install [dependencies/packages]
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

# References
- [Python pip equivalent of node's package.json](https://stackoverflow.com/questions/48941116/does-python-pip-have-the-equivalent-of-nodes-package-json)
- [Poetry Documentation](https://python-poetry.org/)
- [Poe The Poet Documentation](https://poethepoet.natn.io/installation.html)
- [Image Captioning Blog from Ankur Kumar](https://ankur3107.github.io/blogs/the-illustrated-image-captioning-using-transformers/)
