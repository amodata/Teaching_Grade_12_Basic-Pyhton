import click
import wikipedia

from mylib.bot import scrape


def scrape(name="wikipedia", length=1):
    result = wikipedia.summary(name, sentences=length)
    return result


print(scrape())


@click.command()
@click.option("--name", help="Web page we want to scrape")
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", fg="white"))


if __name__ == "__main__":
    cli()
