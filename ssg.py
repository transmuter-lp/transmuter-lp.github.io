import os
import subprocess

import cog


def component_name() -> str:
    return os.path.splitext(os.path.basename(cog.inFile))[0]


def generate_component(filename: str, sections: list[int] = [], **kwargs: str) -> str:
    args = ["cog", "-I", os.path.dirname(__file__)]

    for arg in kwargs.items():
        args.append("-D")
        args.append(f"{arg[0]}={arg[1]}")

    args.append(filename)
    component = subprocess.run(args, capture_output=True, check=True, encoding="UTF-8").stdout

    if len(sections) == 0:
        component = component.replace("<!--***-->\n", "<!--*-->\n")
    else:
        component = "<!--*-->\n".join(map(component.split("<!--***-->\n").__getitem__, sections))

    return component.replace("<!--[[[cog", "<!--").replace("<!--[[[end]]]-->", "<!---->").replace("]]]-->", "-->").rstrip()


def format_template(filename: str, sections: list[int] = [], **kwargs: str) -> None:
    with open(filename, encoding="UTF-8") as file:
        template = file.read()

        if len(sections) == 0:
            template = template.replace("<!--***-->\n", "<!--*-->\n")
        else:
            template = "<!--*-->\n".join(map(template.split("<!--***-->\n").__getitem__, sections))

        cog.out(template.format(**kwargs))
