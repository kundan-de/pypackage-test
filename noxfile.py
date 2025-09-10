import nox

nox.options.sessions = ["lint"]
nox.options.default_venv_backend = "uv|virtualenv"
nox.options.reuse_venv = 'Yes'


@nox.session(reuse_venv=True)
def lint(session):
    """Apply the pre-commits."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-file", *session.posargs)

@nox.session(reuse_venv=True)
def print(session):
    """Print the current version."""
    session.install(".")
    session.run("python", "-V", *session.posargs)