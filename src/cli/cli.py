from argparse import Namespace
import argparse

class Cli:
    def __init__(self, version: str) -> None:
        self.version = version


    def setup(self) -> Namespace:
        parser = argparse.ArgumentParser(prog="fs", description="a fuzzy search for files and diretories")
        parser.add_argument("-v", "--version", action="version", version=f"%(prog)s v{self.version}")
        parser.add_argument("dir", type=str, help="the directory to search in")
        parser.add_argument("pattern", type=str, help="the pattern to search for in the file name")

        return parser.parse_args()