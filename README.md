# Datadog APM Echo Server

This is a very simple local http server which can be used to capture Datadog APM trace requests in local development.

Example usage:
```
pipenv install
pipenv shell

PORT=8000 python server.py
```