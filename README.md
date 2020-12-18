# Usage

### Installation from pip3

```shell
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --verbose subtitlecore
```

### Excutable usage

* Parse srtfile into sentences with timestamp

```shell
parse2sens --srtfile test.srt --lang en
```

* Parse srtfile into plain text
```shell
parse2text --srtfile test.srt --lang en
```

### Package usage
```
from subtitlecore import Subtitle
import sys
import click

def parse2sens(srtfile, lang):
  st = Subtitle(srtfile, lang)
  content_sens = st.sentenize(True)
  for e in content_sens:
    print(e)

def parse2text(srtfile, lang):
  st = Subtitle(srtfile, lang)
  text = st.plaintext()
  print(text)
```

# Development

### Clone project
```
git clone https://github.com/qishe-nlp/subtitlecore.git
```

### Install [poetry](https://python-poetry.org/docs/)

### Install dependencies
```
poetry update
```

### Execute
```
poetry run parse2sens --help
poetry run parse2text --help
```

### Build
* Change `version` in `pyproject.toml` and `content_processor/__init__.py`
* Build python package by `poetry build`

### Publish
* Set pypi test environment variables in poetry, refer to [poetry doc](https://python-poetry.org/docs/repositories/)
* Publish to pypi test by `poetry publish -r test`


# TODO

### Test and Issue
* `tests/*`

### Github action to publish package
* pypi test repo
* pypi repo
