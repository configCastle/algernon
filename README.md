# Algernon project

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Algernon - the code name of the project. This is a tribute to the science fiction novel, [Flowers for Algernon](https://en.wikipedia.org/wiki/Flowers_for_Algernon).

## Table of contents

* [Technical description](#technical-description)
* [Run application](#run-application)
  * [Docker](#docker)
  * [Native](#native)

## Technical description

The project is written using aiohttp as a means of providing api for client applications of one kind or another.

As a linter flake8 is used. With addon: wemake-python-styleguide

If you want to enable the linter in vs code add the line to .vscode / settings.json:

```"python.linting.flake8Enabled": true```

## Run application

### Docker

If you want to start the project using Docker, then you can use the following command:

```docker run -p 8080:8080 --name <put your name> -d leocoan/algernon```

### Native

1. If you want to run the project outside the docker, then clone the project using the command: ```git clone https://github.com/leocoan/algernon.git```

2. After that install pipenv: ```pip install pipenv```

3. And after use the command: ```pipenv shell```

4. Install ```mongodb 4.2```

5. Run project using the command: ```python algernon/app.py```
