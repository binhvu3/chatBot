<!--https://www.readme-templates.com/  -->
<h1 align="center"> ChatBot </h1> <br>
<p align="center">
  <a href="">
    <img alt="Robot" title="Robot" src="https://static.vecteezy.com/system/resources/previews/000/271/349/original/chatbot-web-banner-vector.jpg" width="550">
  </a>
</p>

<p align="center">
  "Embracing the prowess of AI, we delve into the realm of personalized conversation, harnessing its capabilities to foster meaningful interactions."
</p>


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction
Goal is to produced ChatGPT like chatbot with open source LLM and linking everything together with API.

## Features

* API integration with Flask
* Jinja template for dynamic HTML site
* Basic CSS to enhance bare bone site
* Built in databse with sqlite3
* Notification message to user
* Fillable form w/ post automatic display
* Logging user interactions

## Installation
```bash
pip install flask
python -m flask --app website run
```
Retrieve current enviroment setup
```
import os
from dotenv import load_dotenv
load_dotenv()
# True
print(os.getenv("ENVIROMENT"))
# Development
```

Before sqlite3 databse:
``` python
import secrets
secrets.token_hex()
```

Start/reinitialize the sqlite3 database
```
python -m flask --app website init-db
```
## Acknowledgments

Thanks to [RealPython](https://realpython.com/flask-project/) for guide.
