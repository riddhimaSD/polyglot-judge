"""Write every solution variant to solutions/<problem>/<lang>/<variant>.<ext> so each bug can be read as a file."""
from pathlib import Path

from .catalog import S, source
from .runners import EXT

if __name__ == "__main__":
    for (p, lang), vs in S.items():
        for v in vs:
            name = "Main" if lang == "java" else v
            d = Path("solutions") / p / lang / (v if lang == "java" else "")
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{name}{EXT[lang]}").write_text(source(p, lang, v), encoding="utf-8", newline="\n")
    print("exported")
