from commands.command_builder import CommandBuilder


# app = typer.Typer()


def main(project_name: str):
    CommandBuilder().create_dir(project_name).run()


if __name__ == "__main__":
    main("tt")
