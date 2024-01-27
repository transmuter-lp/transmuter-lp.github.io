import os
import subprocess

import cog


def component_name() -> str:
    return os.path.splitext(os.path.basename(cog.inFile))[0]


def include_component(filename: str, **kwargs: dict[str, str]) -> str:
    args = ["cog", "-I", os.path.dirname(__file__)]

    for arg in kwargs.items():
        args.append("-D")
        args.append(f"{arg[0]}={arg[1]}")

    args.append(filename)
    return (
        subprocess.run(args, capture_output=True, check=True, encoding="UTF-8")
        .stdout.replace("<!--[[[cog", "<!--")
        .replace("<!--[[[end]]]-->", "<!---->")
        .replace("]]]-->", "-->")
    )


def format_template(filename: str, **kwargs: dict[str, str]) -> None:
    with open(filename, encoding="UTF-8") as file:
        cog.outl()
        cog.outl(file.read().format(**kwargs))
