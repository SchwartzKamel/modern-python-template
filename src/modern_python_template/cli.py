import click

from . import __version__
import modules.api as api

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def main():
    """Modern Python Template - A production-ready Python CLI template

    SYNOPSIS \n
        modern-python-template [COMMAND] [OPTIONS]

    DESCRIPTION \n
        This CLI provides a template for modern Python applications with
        proper packaging, testing, and documentation practices.
    """
    pass


@main.command()
@click.argument("input", required=False)
@click.option("--output", "-o", help="Output file path")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def process(input, output, verbose):
    """Process input data and generate output

    EXAMPLES

        modern-python-template process input.txt -o output.csv
        modern-python-template process --verbose
    """
    click.echo(f"Processing {input or 'default input'}...")


@main.command()
def config():
    """Show configuration settings"""
    click.echo("Current configuration:")
    click.echo("Version: " + __version__)
    click.echo("Python: 3.11+")


@main.command()
@click.argument("--name", required=False, help="Your name")
@click.argument("--api", required=False, help="API key for Randommer.io")
def helloWorld(name: str = "World") -> str:
    """Example of Hello World that has a paramater to display for auto-doc

    Args:
        name (str, optional): Name value. Defaults to "World".

    Returns:
        str: Returns "Hello World!" or "Hello {name}!" if a `name` is passed
    """
    click.echo(f"Hello {name}!")


def random_name(api_key: str) -> str:
    name = api.GET_page("https://randommer.io/api/Name", api_key=api_key)

    return name


if __name__ == "__main__":
    main()
