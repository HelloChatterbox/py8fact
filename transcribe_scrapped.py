from os import listdir
from os.path import join, dirname

# $ sudo apt install tesseract-ocr
# $ pip install instagram-scraper
# $ instagram-scraper 8fact

skips = [
    "16585455_697733803734680_1110860812567707648_a.jpg"  # logo
]

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# dataset follows a predictable pattern, these will often be transcribed by
# tesseract when parsing the logo
to_remove = [
    "@8FACT",
    "Oo", "oP)", "oO", "oF)"
]

facts = []


def normalize(inputString):
    norm = inputString.encode('ascii', 'ignore').decode('ascii').strip()
    for r in to_remove:
        norm = norm.replace(r, "").strip()
    if norm.startswith("0 ") or norm.startswith("O ") or norm.startswith(") "):
        norm = norm[2:]
    return norm.strip()


def ocr():
    global facts
    pic_folder = join(dirname(__file__), "8fact")

    for pic in listdir(pic_folder):
        if pic in skips or not pic.endswith(".jpg"):
            continue
        pic_path = join(pic_folder, pic)
        fact = pytesseract.image_to_string(Image.open(pic_path))
        lines = fact.split("\n")
        fact = normalize(" ".join(lines))
        if fact:
            facts.append(fact)


def dump():
    dialog = join(dirname(__file__), "py8fact", "res", "en", "facts.txt")

    with open(dialog, "w") as f:
        f.write("\n".join(facts))


def clean():
    dialog = join(dirname(__file__), "py8fact", "res", "en", "facts.txt")
    with open(dialog) as f:
        facts = f.read().split("\n")
    facts = [normalize(f) for f in facts]
    facts = [f.strip() for f in facts if f.strip()]
    with open(dialog, "w") as f:
        f.write("\n".join(facts))

clean()
exit()
ocr()
dump()