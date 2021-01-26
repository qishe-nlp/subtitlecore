from subtitlecore import Subtitle
import sys
import click

@click.command()
@click.option("--srtfile", prompt="srt file", help="Specify a srt file")
@click.option("--lang", default="en", prompt="language", help="Specify language")
@click.option("--dstfile", prompt="Output json file", help="Specify output file")
def parse2sens(srtfile, lang, dstfile):
  sens = []
  st = Subtitle(srtfile, lang)
  content_sens = st.sentenize(True)
  for e in content_sens:
    for s in e["sens"]:
      sens.append(s["text"])
  print(sens)
  import json
  with open(dstfile, 'w') as f:
    json.dump(sens, f) 
    

@click.command()
@click.option("--srtfile", prompt="srt file", help="Specify a srt file")
@click.option("--lang", default="en", prompt="language", help="Specify language")
def parse2text(srtfile, lang):
  st = Subtitle(srtfile, lang)
  text = st.plaintext()
  print(text)
