import os
import random

import click

from .version import __version__
from .words.english import word_list


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, "-v", "--version")
@click.argument("words", default=10)
def cli(words):
    """Start a typing test with number of WORDS."""
    if words < 1:
        return click.echo("WORDS must be higher than 0.")
    elif words > 10000:
        return click.echo("WORDS must be lower than 10000.")
    text = " ".join(random.choices(word_list, k=words))
    name = f"{words} random words"
    with open(name, "w") as f:
        f.write(text)
    os.system(f"mitype -f \"{name}\"")
    os.remove(name)
