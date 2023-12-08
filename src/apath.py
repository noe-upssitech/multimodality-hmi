from os import path

assets_dir = path.abspath(path.join(path.dirname(__file__), "../assets"))

def get_asset_path(filename: str):
    return path.join(assets_dir, filename)