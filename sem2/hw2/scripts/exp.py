import csv
from pathlib import Path

from wk.wiki import rnd_t, bfs, tg


def main(n=50, md=6, ml=30, sl=0.2):
    rt = Path(__file__).resolve().parents[1]
    df = rt / "data"
    df.mkdir(exist_ok=True)
    fn = df / "res.csv"

    res, ok = [], []
    for _ in range(n):
        st = None
        while not st:
            st = rnd_t()
        k = bfs(st, md=md, ml=ml, sl=sl)
        res.append((st, k))
        if k is not None:
            ok.append(k)

    with open(fn, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["start", "steps"])
        w.writerows(res)

    print(tg)
    print("n =", n)
    print("ok =", len(ok))
    print("fail =", n - len(ok))
    if ok:
        print("min =", min(ok))
        print("max =", max(ok))
        print("avg =", sum(ok) / len(ok))


if __name__ == "__main__":
    main()