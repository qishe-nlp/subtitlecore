import spacy

class ENCaptionMarker:

  @classmethod
  def mark(self, line, choice):
    """
    e.g,
    return [{text: '', confidence: 1.0}, {text: '', confidence: 0.5}]
    """
    print("Analyze: {}".format(line))
    sens = []
    if choice:
      nlp = spacy.load("en_core_web_md")
      doc = nlp(line, disable=["tagger", "ner"])
      _temp = list(doc.sents)
      for s in _temp:
        e = {"text": s.text, "confidence": 1.0}
        sens.append(e)
    else:
      sens = [{"text": line, "confidence": 1.0}]
    print(sens)
    return sens 
