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
def mergelist():
    list_merge = questionary.text("Which lists would you like to merge?").ask()
    click.echo(f"Merged: {list_merge}")


@main.command()
def namelist():
    list_name = questionary.text("What would you like to name your list?").ask()
    click.echo(f"Created: {list_name}")


@main.command()
def searchlist():
    list_access = questionary.text("Which list would you like to access?").ask()
    click.echo(f"Here you go, found it! {list_access}")


@main.command()
def deletelist():
    list_delete = questionary.text("Which list would you like to delete?").ask()
    click.echo(f"Deleted: {list_delete}")


@main.command()
def renamelist():
    list_rename = questionary.text("Which list would you like to rename?").ask()
    click.echo(f"Renamed: {list_rename}")


if __name__ == "__main__":
    main()
