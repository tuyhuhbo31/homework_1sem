import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

from wk.wiki import tg


def rd(fn):
    c = Counter()
    n = 0
    with open(fn, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            n += 1
            v = (row.get("steps") or "").strip()
            if not v or v == "None":
                c["fail"] += 1
            else:
                c[int(v)] += 1
    return c, n


def main():
    rt = Path(__file__).resolve().parents[1]
    fn = rt / "data" / "res.csv"
    out = rt / "data" / "hist.png"

    c, n = rd(fn)
    if n == 0:
        print("no data")
        return

    ks = [k for k in c.keys() if k != "fail"]
    ks = sorted(ks)
    lbl = ["fail"] + [str(k) for k in ks]
    val = [c["fail"]] + [c[k] for k in ks]

    plt.figure(figsize=(8, 4.5))
    plt.bar(lbl, val, edgecolor="black")
    plt.title(tg)
    plt.xlabel("переходы")
    plt.ylabel("кол-во")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.show()
    print("saved:", out)


if __name__ == "__main__":
    main()