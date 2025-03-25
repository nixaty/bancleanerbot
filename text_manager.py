import json
import os
from pathlib import Path


langs_path = Path(__file__).parent.joinpath("lang")
langs_files = os.listdir(langs_path)
langs = {}
for lang_file in langs_files:
    if lang_file.endswith(".json"):
        with open(langs_path.joinpath(lang_file), "r", encoding="utf-8") as f:
            langs[lang_file.rsplit(".", 1)[0]] = json.load(f)


def get_by_lang_code(key: str, language_code: str):
    if language_code in langs and key in langs[language_code.lower()]:
        text = langs[language_code.lower()].get(key)
    else:
        text = langs["en"].get(key)
    return text
