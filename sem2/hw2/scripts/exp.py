import csv
from pathlib import Path

from wk.wiki import rnd_t, bfs, tg


def main(n=30, md=7, ml=60, sl=0.0):
    rt = Path(__file__).resolve().parents[1]
    df = rt / "data"
    df.mkdir(exist_ok=True)
    fn = df / "res.csv"

    res = []
    ok = 0
    for i in range(1, n + 1):
        st = None
        while not st:
            st = rnd_t()
        k, _ = bfs(st, md=md, ml=ml, sl=sl)
        res.append((st, k))
        if k is not None:
            ok += 1
        print(i, "/", n, "steps:", k)

    with open(fn, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["start", "steps"])
        w.writerows(res)

    print(tg)
    print("n =", n)
    print("ok =", ok)
    print("fail =", n - ok)


if __name__ == "__main__":
    main()