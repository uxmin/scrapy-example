def get_path(file: object, depth: int) -> str:
    from os.path import abspath, dirname

    path = dirname(abspath(file))
    for _ in range(depth):
        path = dirname(path)
    return path
