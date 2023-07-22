import typer

from cfa.commands import command_builder
from cfa.config import config

app = typer.Typer()


@app.command()
def create_fastapi_app(path: str):
    command_builder.CommandBuilder().clone_git(config.base_git_project, config.git_branch,
                                               path).install_deps(path, config.pip_packages).run()


def main_cli():
    app()


if __name__ == "__main__":
    main_cli()
