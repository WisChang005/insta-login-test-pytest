import pathlib


def get_path():
    return str(pathlib.Path(__file__).parent.absolute())
