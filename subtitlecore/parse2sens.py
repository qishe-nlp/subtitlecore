from subtitlecore.subtitle import Subtitle
import sys
import click

@click.command()
@click.option("--srtfile", prompt="srt file", help="Specify a srt file")
@click.option("--lang", default="en", prompt="language", help="Specify language")
def run(srtfile, lang):
  st = Subtitle(srtfile, lang)
  content_sens = st.sentenize()
  for e in content_sens:
    print(e)
