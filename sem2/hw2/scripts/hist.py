import csv
from pathlib import Path

import matplotlib.pyplot as plt

from wk.wiki import tg


def rd(fn):
    ks = []
    n = 0
    with open(fn, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            n += 1
            v = (row.get("steps") or "").strip()
            if not v or v == "None":
                continue
            ks.append(int(v))
    return ks, n


def main():
    rt = Path(__file__).resolve().parents[1]
    fn = rt / "data" / "res.csv"
    out = rt / "data" / "hist.png"

    ks, n = rd(fn)
    if not ks:
        print("no successful runs")
        return

    mn, mx = min(ks), max(ks)
    bins = list(range(mn, mx + 2))

    plt.figure(figsize=(8, 4.5))
    plt.hist(ks, bins=bins, edgecolor="black")
    plt.title(tg)
    plt.xlabel("переходы")
    plt.ylabel("кол-во")
    plt.text(0.99, 0.95, f"успех: {len(ks)}/{n}", transform=plt.gca().transAxes, ha="right", va="top")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.show()


if __name__ == "__main__":
    main()