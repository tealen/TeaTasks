import click
import questionary


@click.group()
def main():
    """TeaTasks is a cute CLI todo manager."""


@main.command()
def greet():
    name = questionary.text("What's your first name?").ask()
    click.echo(f"Hello {name}")


if __name__ == "__main__":
    main()
