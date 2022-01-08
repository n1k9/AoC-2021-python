def read_file(filename: str) -> list:
    with open(filename, 'r') as f:
        return list(map(int, f.readlines()))
