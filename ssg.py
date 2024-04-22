import os
import subprocess

import cog


def name() -> str:
    return os.path.splitext(os.path.basename(cog.inFile))[0]

def init(filename: str, **kwargs: str) -> str:
    args = ["cog", "-d", "-I", os.path.dirname(__file__), "-p", "import ssg; init = True"]

    for arg in kwargs.items():
        args.append("-D")
        args.append(f"{arg[0]}={arg[1]}")

    args.append(filename)
    return subprocess.run(args, capture_output=True, check=True, encoding="UTF-8").stdout.rstrip()

def text(filename: str) -> str:
    with open(filename, encoding="UTF-8") as file:
        return file.read().rstrip()

def format(**kwargs: str) -> None:
    cog.out(eval(f'f"""{cog.previous}"""', kwargs))
