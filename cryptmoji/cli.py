from typing import Annotated, Union
from rich.console import Console
from typer import Typer, Option

from cryptmoji.main import decrypt, encrypt
from cryptmoji.version import __version__

app = Typer()
console = Console()

key_option_type = Option(
    "--key",
    help="This is an optional key that can be used to increase the complexity of the encryption.",
)


@app.command("encrypt")
def cli_encrypt(
    text: str,
    key: Annotated[Union[str, None], key_option_type] = None,
):
    """Encrypts a string as a string of emojis."""
    console.print(encrypt(text, key=key))


@app.command("decrypt")
def cli_decrypt(
    text: str,
    key: Annotated[Union[str, None], key_option_type] = None,
):
    """Decrypts a string of emojis."""
    console.print(decrypt(text, key=key))


@app.command("--version")
def cli_version():
    """Prints the version of the library."""
    version = ".".join(str(i) for i in __version__)
    console.print(f"cryptmoji v{version}")


if __name__ == "__main__":
    app()
