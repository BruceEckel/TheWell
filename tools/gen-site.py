import re, html, pathlib

ROOT = pathlib.Path(r"C:\git\Novel3")
MS = ROOT / "manuscript"
OUT = ROOT / "docs"
OUT.mkdir(exist_ok=True)

ORDER = [
    ("I", ["act1-ch01-the-funeral", "act1-ch02-the-prophet", "act1-ch03-the-love",
            "act1-ch04-the-heresy", "act1-ch05-the-city", "act1-ch06-the-collapse",
            "act1-ch07-the-visitor", "act1-ch08-the-door"]),
    ("II", ["act2-ch01-the-recurrence", "act2-ch02-the-stranger-who-knows",
             "act2-ch03-the-tests", "act2-ch04-the-mission-partly-told",
             "act2-ch05-the-circling", "act2-ch06-the-teacher", "act2-ch07-the-refusal",
             "act2-ch08-the-drift", "act2-ch09-the-return", "act2-ch10-the-choice"]),
    ("III", ["act3-ch01-the-tales", "act3-ch02-the-hardening",
              "act3-ch03-the-teachers-orbit", "act3-ch04-the-death-of-despair",
              "act3-ch05-the-return-to-wren", "act3-ch06-the-novice",
              "act3-ch07-the-small-acceptances", "act3-ch08-the-reliquary",
              "act3-ch09-the-campaign-amara", "act3-ch10-the-campaign-sefa",
              "act3-ch11-the-campaign-havel", "act3-ch12-the-choice-point-awake"]),
]

LAMP = '''<button class="lamp" aria-label="the lamp" title="the lamp">
<svg viewBox="0 0 24 24" aria-hidden="true">
<circle class="glow" cx="12" cy="10.5" r="7.5"/>
<path class="flame" d="M12 4.5 C14.8 8 15.6 10.4 12 14.5 C8.4 10.4 9.2 8 12 4.5 Z"/>
<path class="base" d="M7.5 18.5 H16.5" fill="none" stroke-width="1.4" stroke-linecap="round"/>
</svg></button>'''

HERO = '''<svg class="hero" viewBox="0 0 600 340" role="img"
aria-label="A door standing open in the dark, lamplight lying across the landing floor in a long quiet stripe, a thin brass seam at its edge.">
<defs>
<linearGradient id="slit" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#f7d489" stop-opacity="0.95"/>
<stop offset="0.7" stop-color="#dfae55"/>
<stop offset="1" stop-color="#b97d2c"/>
</linearGradient>
<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#e9b95f" stop-opacity="0.55"/>
<stop offset="1" stop-color="#e9b95f" stop-opacity="0.04"/>
</linearGradient>
<linearGradient id="seam" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#b97d2c" stop-opacity="0"/>
<stop offset="0.5" stop-color="#e0b060"/>
<stop offset="1" stop-color="#b97d2c" stop-opacity="0"/>
</linearGradient>
<filter id="soft" x="-80%" y="-80%" width="260%" height="260%">
<feGaussianBlur stdDeviation="7"/>
</filter>
</defs>
<rect x="0" y="0" width="600" height="340" rx="4" fill="#171310"/>
<rect x="293" y="36" width="14" height="206" fill="url(#slit)" filter="url(#soft)" opacity="0.55"/>
<rect x="296.5" y="38" width="7" height="202" fill="url(#slit)"/>
<polygon points="296,240 304,240 452,306 148,306" fill="url(#floor)"/>
<rect x="70" y="305" width="460" height="1.6" fill="url(#seam)"/>
<rect x="297" y="302.5" width="6" height="6" transform="rotate(45 300 305.5)" fill="#e0b060"/>
</svg>'''

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="stylesheet" href="style.css">
<script src="well.js" defer></script>
</head>
<body>
'''

def convert(md_text):
    lines = md_text.split("\n")
    title_line = next(l for l in lines if l.startswith("# "))
    title = title_line[2:].strip()
    blocks, cur = [], []
    for l in lines:
        if l.startswith("# "):
            continue
        if l.strip() == "":
            if cur:
                blocks.append(" ".join(cur)); cur = []
        else:
            cur.append(l.strip())
    if cur:
        blocks.append(" ".join(cur))
    out, first_done, after_break = [], False, False
    for b in blocks:
        if b == "*":
            out.append('<div class="break" aria-hidden="true">&middot; &middot; &middot;</div>')
            after_break = True
            continue
        t = html.escape(b, quote=False)
        t = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", t)
        cls = ""
        if not first_done:
            cls = ' class="first"'; first_done = True
        elif after_break:
            cls = ' class="afterbreak"'
        after_break = False
        out.append(f"<p{cls}>{t}</p>")
    return title, "\n".join(out)

def short_title(full):
    return full.split(":", 1)[1].strip() if ":" in full else full

def navlink(href, label, name, cls):
    return (f'<a class="{cls}" href="{href}"><span class="label">{label}</span>{name}</a>')

chapters = []  # (fname, act, chnum, short)
for act, names in ORDER:
    for i, n in enumerate(names, 1):
        chapters.append((n, act, i, None))
chapters.append(("coda", None, None, None))

resolved = []
for n, act, i, _ in chapters:
    md = (MS / f"{n}.md").read_text(encoding="utf-8")
    full, body = convert(md)
    short = "Coda" if n == "coda" else short_title(full)
    resolved.append((n, act, i, short, body))

for idx, (n, act, i, short, body) in enumerate(resolved):
    eyebrow = "Coda" if act is None else f"Act {act} &middot; Chapter {i}"
    prev_html = next_html = ""
    if idx == 0:
        prev_html = navlink("index.html", "&lsaquo; title page", "The Well", "prev")
    else:
        p = resolved[idx - 1]
        prev_html = navlink(f"{p[0]}.html", "&lsaquo; previous", p[3], "prev")
    if idx < len(resolved) - 1:
        nx = resolved[idx + 1]
        next_html = navlink(f"{nx[0]}.html", "next &rsaquo;", nx[3], "next")
    page = HEAD.format(title=f"{short} &middot; The Well",
                       desc="The Well, a novel crafted by Bruce Eckel.")
    page += LAMP + '\n<main class="page">\n'
    page += f'<div class="runhead"><a href="index.html">The Well</a></div>\n'
    page += f'<div class="eyebrow">{eyebrow}</div>\n'
    page += f'<h1 class="chapter">{short}</h1>\n<hr class="seam">\n'
    page += f'<div class="prose">\n{body}\n</div>\n'
    page += f'<nav class="chapnav">{prev_html}{next_html}</nav>\n'
    page += "</main>\n</body>\n</html>\n"
    (OUT / f"{n}.html").write_text(page, encoding="utf-8")

# ---- index ----
toc = ""
k = 0
for act, names in ORDER:
    toc += f'<h2>Act {act}</h2>\n<ol>\n'
    for i, n in enumerate(names, 1):
        short = resolved[k][3]; k += 1
        toc += (f'<li><span class="num">{i}</span>'
                f'<a href="{n}.html">{short}</a></li>\n')
    toc += "</ol>\n"
toc += '<h2>&nbsp;</h2>\n<ol><li><span class="num">&#10087;</span>'
toc += '<a href="coda.html">Coda</a></li></ol>\n'

index = HEAD.format(title="The Well &middot; a novel crafted by Bruce Eckel",
                    desc="The Well, a novel crafted by Bruce Eckel. A man climbs down a well on purpose, and takes three lifetimes to learn why.")
index += LAMP + '\n<main class="page">\n'
index += HERO + "\n"
index += '<h1 class="book">THE WELL</h1>\n'
index += '<div class="byline">a novel crafted by Bruce Eckel</div>\n'
index += ('<p class="epigraph">The fire does not hate the ore. What burns away was never '
          'yours. Hold still in the burning, and remember what you came to do.</p>\n')
index += '<div class="epigraph-source">The Sixth Gathering</div>\n'
index += f'<div class="toc">\n{toc}</div>\n'
index += '<footer>The Well &middot; Bruce Eckel</footer>\n'
index += "</main>\n</body>\n</html>\n"
(OUT / "index.html").write_text(index, encoding="utf-8")
(OUT / ".nojekyll").write_text("", encoding="utf-8")

print(f"wrote {len(resolved) + 1} pages to {OUT}")
