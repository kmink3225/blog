import json
import nbformat
from nbformat import read
from pathlib import Path

ROOT = Path("c:/Users/kmkim/Desktop/projects/blog/docs/blog/posts/Agent/18-LangGraph")

EXTS = ["01-Core-Features", "02-Structures", "03-Use-Cases"]


def convert_notebook(nb_path: Path):
    with nb_path.open("r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    parts = []

    title = nb_path.stem.replace('-', ' ')

    # YAML header
    header = ["---\n",
              f"title: \"{title}\"\n",
              "format:\n",
              "  html:\n",
              "    code-fold: true\n",
              "    toc: true\n",
              "    number-sections: true\n",
              "---\n\n"]
    parts.extend(header)

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            src = ''.join(cell.source)
            parts.append(src + "\n\n")
        elif cell.cell_type == 'code':
            # try to detect language from metadata
            lang = 'python'
            parts.append(f"```{{python}}\n")
            parts.append(''.join(cell.source) + "\n")
            parts.append("```\n\n")
        else:
            # other types, skip
            continue

    out_path = nb_path.with_suffix('.qmd')
    with out_path.open('w', encoding='utf-8') as f:
        f.writelines(parts)

    return out_path


def main():
    converted = []
    for sub in EXTS:
        for nb in (ROOT / sub).rglob('*.ipynb'):
            try:
                out = convert_notebook(nb)
                converted.append(out)
            except Exception as e:
                print(f'Failed: {nb}: {e}')
    print('Converted:', len(converted))


if __name__ == '__main__':
    main()
