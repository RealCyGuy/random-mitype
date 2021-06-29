import json
import os
import importlib.resources as pkg_resources
import random

import click

from version import __version__


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, "-v", "--version")
@click.argument("words", default=10)
def cli(words):
    """Start a typing test with number of WORDS."""
    if words < 1:
        return click.echo("WORDS must be higher than 0.")
    elif words > 10000:
        return click.echo("WORDS must be lower than 10000.")
    word_list = json.loads(pkg_resources.read_text("words", "english.json"))
    text = " ".join(random.choices(word_list, k=words))
    name = f"{words} random words"
    with open(name, "w") as f:
        f.write(text)
    os.system(f"mitype -f \"{name}\"")
    os.remove(name)
