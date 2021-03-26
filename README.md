### Installation from pip3

```shell
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --verbose subtitlecore
```

# Usage

### Excutable usage

* Get subtitle content

```shell
get_subtitle_content --srtfile test.srt --lang en
``` 

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

def get_subtitle_content(srtfile, lang):
  st = Subtitle(srtfile, lang)
  for line_info in st.content:
    print(line_info)

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

### Check the documentation locally
```
python -m http.server -d docs/build/html
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

### Test and Issue
```
poetry run pytest -rP
```
which run tests under `tests/*`

### Execute
```
poetry run get_subtitle_content --help
poetry run parse2sens --help
poetry run parse2text --help
```

### Create sphix docs
```
poetry shell
cd docs
sphinx-apidoc -f -o source ../subtitlecore
make html
python -m http.server -d build/html
```

### Build
* Change `version` in `pyproject.toml` and `content_processor/__init__.py`
* Build python package by `poetry build`

### Publish
* Set pypi test environment variables in poetry, refer to [poetry doc](https://python-poetry.org/docs/repositories/)
* Publish to pypi test by `poetry publish -r test`

# TODO

### Github action to publish package
* pypi test repo
* pypi repo
