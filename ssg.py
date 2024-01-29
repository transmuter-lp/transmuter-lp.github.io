import os
import subprocess

import cog


def _split_join(input_: str, sections: list[int] = []) -> str:
    if len(sections) == 0:
        input_ = input_.replace("<!--***-->\n", "")
    else:
        input_ = "".join(map(input_.split("<!--***-->\n").__getitem__, sections))

    return input_


def component_name() -> str:
    return os.path.splitext(os.path.basename(cog.inFile))[0]


def generate_component(filename: str, sections: list[int] = [], **kwargs: str) -> str:
    args = ["cog", "-d", "-I", os.path.dirname(__file__)]

    for arg in kwargs.items():
        args.append("-D")
        args.append(f"{arg[0]}={arg[1]}")

    args.append(filename)
    component = subprocess.run(args, capture_output=True, check=True, encoding="UTF-8").stdout
    return _split_join(component, sections).rstrip()


def load_component(filename: str, sections: list[int] = []) -> str:
     with open(filename, encoding="UTF-8") as file:
        return _split_join(file.read(), sections).rstrip()


def format_template(filename: str, sections: list[int] = [], **kwargs: str) -> None:
    with open(filename, encoding="UTF-8") as file:
        template = _split_join(file.read(), sections)
        cog.out(eval(f'f"""{template}"""', kwargs))
