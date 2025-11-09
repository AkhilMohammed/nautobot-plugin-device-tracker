from invoke import task

COMPOSE_BASE = 'docker-compose -f development/docker-compose-base.yml'
COMPOSE_DEV = f'{COMPOSE_BASE} -f development/docker-compose-dev.yml'

@task
def build(c):
    # Build nautobot and related containers
    c.run(f'{COMPOSE_BASE} build nautobot')

@task
def start(c):
    c.run(f'{COMPOSE_DEV} up -d')

@task
def stop(c):
    c.run(f'{COMPOSE_DEV} down')

@task
def logs(c):
    c.run(f'{COMPOSE_DEV} logs -f')

@task
def test(c):
    c.run('pytest nautobot_plugin_example/tests')
    
@task
def docker_login(c, registry='your-docker-registry.com', username=None, password=None):
    if not username or not password:
        print('Usage: inv docker_login --username youruser --password yourpass')
        return
    c.run(f'docker login {registry} -u {username} -p {password}')

@task
def docker_push(c, image='your-docker-registry.com/nautobot-plugin-example:latest'):
    c.run(f'docker push {image}')

@task
def docker_pull(c, image='your-docker-registry.com/nautobot-plugin-example:latest'):
    c.run(f'docker pull {image}')
