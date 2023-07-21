import typer

from commands.command_builder import CommandBuilder
from config import config

app = typer.Typer()


@app.command()
def main(path: str):
    CommandBuilder().clone_git(config.base_git_project, config.git_branch,
                               path).install_deps(path, config.pip_packages).run()


if __name__ == "__main__":
    app()
