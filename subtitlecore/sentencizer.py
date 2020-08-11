from importlib import import_module

class Sentencizer:
  def __init__(self, lang):
    module = import_module("subtitlecore.{}_caption_marker".format(lang.lower()))
    self.marker = getattr(module, "{}CaptionMarker".format(lang.upper()))

  def mark(self, content, choice):
    marked_content = content.copy()
    for e in marked_content:
      e["sens"] = self.marker.mark(e["text"], choice)
    return marked_content

