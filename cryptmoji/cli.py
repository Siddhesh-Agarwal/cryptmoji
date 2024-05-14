from rich.console import Console
from typer import Typer, prompt

from cryptmoji.main import decrypt, encrypt
from cryptmoji.version import __version__

app = Typer()
console = Console()


@app.command("encrypt")
def cli_encrypt(text: str):
    """Encrypts a string as a string of emojis."""
    key = prompt("Enter key", default=None)
    console.print(encrypt(text, key=key))


@app.command("decrypt")
def cli_decrypt(text: str):
    """Decrypts a string of emojis."""
    key = prompt("Enter key", default=None)
    console.print(decrypt(text, key=key))


@app.command("--version")
def cli_version():
    """Prints the version of the library."""
    version = ".".join(str(i) for i in __version__)
    console.print(f"cryptmoji v{version}")


if __name__ == "__main__":
    app()
