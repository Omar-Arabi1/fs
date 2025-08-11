from argparse import Namespace

from cli.cli import Cli
from . import __version__

def main():
    cli: Cli = Cli(version=__version__)
    args: Namespace = cli.setup()


if __name__ == "__main__":
    main()
