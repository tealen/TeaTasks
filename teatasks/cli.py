import click
import questionary


@click.group()
def main():
    """TeaTasks is a cute CLI todo manager."""


@main.command()
def greet():
    name = questionary.text("What's your first name?").ask()
    click.echo(f"Hello {name}")


@main.command()
def createlist():
    list_name = questionary.text("What would you like to name your list?").ask()
    click.echo(f"Created: {list_name}")


if __name__ == "__main__":
    main()
