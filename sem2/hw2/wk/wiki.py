import time
from collections import deque
from urllib.parse import unquote

import requests as rq
from bs4 import BeautifulSoup as bs

bsu = "https://ru.wikipedia.org"
hdr = {"User-Agent": "edu-hw2/1.0"}
tg = "Теорема о движении центра масс системы"


def t2u(t):
    return f"{bsu}/wiki/{t.replace(' ', '_')}"


def ok_h(h):
    if not h.startswith("/wiki/"):
        return False
    t = h[6:]
    if not t or "#" in t or ":" in t:
        return False
    if t.startswith("Заглавная_страница"):
        return False
    return True


def h2t(h):
    return unquote(h[6:]).replace("_", " ")


def rnd_t():
    r = rq.get(f"{bsu}/wiki/Special:Random", headers=hdr, timeout=25, allow_redirects=True)
    r.raise_for_status()
    s = bs(r.text, "lxml")
    h = s.find("h1")
    return h.get_text(strip=True) if h else None


def lnk(t, ml=60):
    r = rq.get(t2u(t), headers=hdr, timeout=25)
    r.raise_for_status()
    s = bs(r.text, "lxml")
    c = s.find("div", id="mw-content-text")
    if not c:
        return []
    out, seen = [], set()
    for a in c.find_all("a", href=True):
        h = a["href"]
        if not ok_h(h):
            continue
        tt = h2t(h)
        if tt == t or tt in seen:
            continue
        seen.add(tt)
        out.append(tt)
        if len(out) >= ml:
            break
    return out


def bfs(st, md=6, ml=60, sl=0.0, mx=5000):
    q = deque([st])
    dep = {st: 0}
    par = {st: None}
    n = 0

    while q:
        t = q.popleft()
        d = dep[t]
        if t == tg:
            p = []
            x = t
            while x is not None:
                p.append(x)
                x = par[x]
            p.reverse()
            return d, p

        if d >= md:
            continue

        try:
            nb = lnk(t, ml=ml)
        except Exception:
            nb = []

        for x in nb:
            if x in dep:
                continue
            dep[x] = d + 1
            par[x] = t
            q.append(x)

        n += 1
        if n >= mx:
            break
        if sl:
            time.sleep(sl)

    return None, [st]