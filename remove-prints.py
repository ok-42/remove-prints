import sys


def remove_print(path: str) -> None:
    """Remove lines that start with ``print`` from a file inplace.

    :param path: full path to a file
    :return: None
    """
    result: list[str] = []
    with open(path, 'r', encoding='utf-8') as file:
        lines: list[str] = file.readlines()
        for line in lines:
            if not line.lstrip().startswith('print'):
                result.append(line)
    with open(path, 'w', encoding='utf-8') as out:
        out.writelines(result)


if __name__ == '__main__':
    remove_print(sys.argv[1])
