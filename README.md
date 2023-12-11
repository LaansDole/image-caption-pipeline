# FastAPI pipeline for Image Captioning Model

This project uses Python 3.10. Remember to run below commands in the root directory of your project where the `pyproject.toml` file is located. Here are the main elements you need to know to get started:
- Model: 
[nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning)

## Virtual Environment
Note that for this the package venv is to be used.

In short, a virtual environment will help us manage an isolated version of python interpreter. And so too installed packages. In this way. Different project will not have to depends on the same packages installation and have to conflict. Read the link above explain and show it well.

## Build on local
### Docker Build
```docker
docker compose up --build
```
### Poetry or Pip
```bash
# Create a virtual environment, navigate to your root directory and run:
python -m venv .venv
# Activate the environment, use:
source .venv/bin/activate
pip install -r requirements
```
- In a Python project managed with Poetry, dependencies are listed in a `pyproject.toml` file, make sure that `[tool.poetry] name = "bloomsage-backend"`:
```bash
poetry install --no-root
```
***To add additional dependencies/packages to your project, use:***
- With `poetry`
```bash
poetry add [dependencies/packages]
```
- With `pip`
```bash
pip install [dependencies/packages]
```
- Once you have done with your session
```bash
# To export the requirements.txt
pip install -r requirements
poetry export -f requirements.txt --output requirements.txt --without-hashes --without=dev
# Deactivate the environment once done, use:
deactivate
```
### To run locally

- ***To start the server at http://0.0.0.0:8000***
```bash
poe compose
```
- ***To check the type in python files***
```bash
poe typecheck
```

# References
- [Python pip equivalent of node's package.json](https://stackoverflow.com/questions/48941116/does-python-pip-have-the-equivalent-of-nodes-package-json)
- [Poetry Documentation](https://python-poetry.org/)
- [Poe The Poet Documentation](https://poethepoet.natn.io/installation.html)
- [Image Captioning Blog from Ankur Kumar](https://ankur3107.github.io/blogs/the-illustrated-image-captioning-using-transformers/)
- [pipx Installation](https://github.com/pypa/pipx)
