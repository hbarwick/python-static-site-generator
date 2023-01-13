from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(self, path: Path, source: Path, dest: Path)
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

