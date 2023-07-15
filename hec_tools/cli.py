"""Console script for hec_tools."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for hec_tools."""
    click.echo("Replace this message by putting your code into "
               "hec_tools.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
