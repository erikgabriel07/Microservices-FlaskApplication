from invoke import task


@task
def install_requirements(c):
    c.run('pip freeze > requirements.txt')


@task
def commit(c):
    c.run('git add .')
    c.run('git commit -m "Updated files"')
    c.run('git push')


@task(pre=[install_requirements])
def deploy(c):
    c.run('python Flask/main.py')