from rich.console import Console
from typer import Typer

from cryptmoji.main import decrypt, encrypt

app = Typer()
console = Console()


@app.command("encrypt")
def cli_encrypt(text: str):
    """Encrypts a string as a string of emojis."""
    key = console.input(
        "Key (optional): ",
        markup=False,
        emoji=False,
        password=True,
    )

    console.print(encrypt(text, key=key if key else None))


@app.command("decrypt")
def cli_decrypt(text: str):
    """Decrypts a string of emojis."""
    key = console.input(
        "Key (optional): ",
        markup=False,
        emoji=False,
        password=True,
    )
    console.print(decrypt(text, key=key if key else None))
