# Nautobot Plugin Example (Production Ready)

This repository contains a production-ready Nautobot plugin with the following features:

- Poetry for packaging and dependency management
- Multi-file Docker Compose setup:
  - Base Nautobot service with Celery, Redis, and Postgres
  - Dev override with volume mounts and debug settings
  - Separate Postgres and Redis compose files
- Invoke tasks to build, start, stop, view logs, test the plugin
- Docker login, push, and pull tasks integrated for personal Docker registry/artifactory
- Plugin app structured per Nautobot plugin best practices
- Development Nautobot config file with DB and plugin registration

## Usage

1. Install Poetry and Invoke (pip install poetry invoke)
2. Run poetry shell to enter the environment
3. Run poetry install to install dependencies
4. Copy development/creds.example.env to development/creds.env and configure credentials
5. Use invoke build to build Docker images and push to your Docker registry
6. Use invoke start to bring up Docker containers for development
7. Use invoke stop to tear down containers
8. Use invoke logs to view logs
9. Develop plugin code inside 
autobot_plugin_example/
10. Add the plugin to your Nautobot config as demonstrated

## Docker Registry Setup

Modify 	asks.py docker_login, docker_push, and docker_pull tasks with your personal Docker registry URL and credentials.

