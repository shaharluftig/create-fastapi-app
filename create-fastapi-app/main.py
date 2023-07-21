import typer

app = typer.Typer()


@app.command()
def say_bye(name: str):
    print(f"bye {name}")


@app.command()
def say_hello(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
