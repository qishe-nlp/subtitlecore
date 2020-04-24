import spacy

class ENCaptionMarker:

  @classmethod
  def mark(self, line):
    """
    e.g,
    return [{text: '', confidence: 1.0}, {text: '', confidence: 0.5}]
    """
    nlp = spacy.load("en_core_web_md")
    _line = line.replace("\n", " ").replace("-", " ")
    doc = nlp(_line)
    _temp = list(doc.sents)
    sens = []
    for s in _temp:
      e = {"text": s, "confidence": 1.0}
      sens.append(e)
    return sens 

