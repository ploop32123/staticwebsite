


def extract_title(markdown):
    splited = markdown.split("\n")
    for line in splited:
        if line.startswith("# "):
            striped = line[2:]
            return striped
    raise ValueError("No Markdown")