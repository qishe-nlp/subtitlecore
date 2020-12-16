Installation
============

```shell
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --verbose subtitlecore
```

Usage
=====

* Parse srtfile into sentences with timestamp

```shell
parse2sens --srtfile test.srt --lang en
```

* Parse srtfile into plain text
```shell
parse2text --srtfile test.srt --lang en
```
