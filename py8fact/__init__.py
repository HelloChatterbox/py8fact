from os.path import join, dirname
import random


class UnsupportedLanguage(ValueError):
    """ Facts not translated yet """


SUPPORTED_LANGS = ["en"]

_FACTS = {}


def _load(lang="en"):
    if lang not in SUPPORTED_LANGS:
        raise UnsupportedLanguage
    facts_path = join(dirname(__file__), "res", lang, "facts.txt")
    with open(facts_path) as f:
        _FACTS[lang] = f.readlines()
    _FACTS[lang] = [f.strip() for f in _FACTS[lang]]


def random_fact(lang="en"):
    lang = lang.lower().split("-")[0].strip()
    if lang not in _FACTS:
        _load(lang)
    return random.choice(_FACTS[lang])


def get_facts(n=10, lang="en"):
    lang = lang.lower().split("-")[0].strip()
    if lang not in _FACTS:
        _load(lang)
    random.shuffle(_FACTS[lang])
    if n >= len(_FACTS[lang]):
        n = len(_FACTS[lang]) - 1
    if n < 0:
        return _FACTS[lang]
    return _FACTS[lang][:n]


def total_facts(lang="en"):
    lang = lang.lower().split("-")[0].strip()
    if lang not in _FACTS:
        _load(lang)
    return len(_FACTS[lang])
