from invoke import task
import os

COMPOSE_BASE = "docker-compose -f development/docker-compose-base.yml"
COMPOSE_DEV = f"{COMPOSE_BASE} -f development/docker-compose-dev.yml"

@task
def build(c):
    """Build the plugin Docker image."""
    python_ver = os.getenv("PYTHON_VER", "3.11")
    nautobot_ver = os.getenv("NAUTOBOT_VER", "2.0.0")
    dockerhub_user = os.getenv("DOCKERHUB_USER")
    dockerhub_token = os.getenv("DOCKERHUB_TOKEN")
    image_name = os.getenv("DOCKER_IMAGE", f"docker.io/{dockerhub_user}/nautobot-plugin-example:latest")

    if not dockerhub_user or not dockerhub_token:
        print("Error: DOCKERHUB_USER and DOCKERHUB_TOKEN environment variables must be set.")
        return

    build_cmd = (
        f"docker build "
        f"--build-arg PYTHON_VER={python_ver} "
        f"--build-arg NAUTOBOT_VER={nautobot_ver} "
        f"--build-arg DOCKERHUB_USER={dockerhub_user} "
        f"--build-arg DOCKERHUB_TOKEN={dockerhub_token} "
        f"-t {image_name} "
        f"-f development/Dockerfile ."
    )
    c.run(build_cmd)

@task
def start(c):
    """Start the plugin environment."""
    c.run(f"{COMPOSE_DEV} up -d")

@task
def stop(c):
    """Stop the plugin environment."""
    c.run(f"{COMPOSE_DEV} down")

@task
def logs(c):
    """Show logs of all containers."""
    c.run(f"{COMPOSE_DEV} logs -f")

@task
def test(c):
    """Run tests with pytest."""
    c.run("pytest nautobot_plugin_example/tests")

@task
def docker_login(c, username=None, password=None, registry="docker.io"):
    """Login to private Docker registry."""
    if not username or not password:
        print("Usage: inv docker_login --username <user> --password <pat>")
        return
    c.run(f"docker login {registry} -u {username} -p {password}")

@task
def docker_push(c):
    """Push image to private Docker registry."""
    dockerhub_user = os.getenv("DOCKERHUB_USER")
    image_name = os.getenv("DOCKER_IMAGE", f"docker.io/{dockerhub_user}/nautobot-plugin-example:latest")
    c.run(f"docker push {image_name}")

@task
def docker_pull(c):
    """Pull image from private Docker registry."""
    dockerhub_user = os.getenv("DOCKERHUB_USER")
    image_name = os.getenv("DOCKER_IMAGE", f"docker.io/{dockerhub_user}/nautobot-plugin-example:latest")
    c.run(f"docker pull {image_name}")

