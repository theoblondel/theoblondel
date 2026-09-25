#!/usr/bin/env python3
"""Generate the animated SVGs used in the profile README.

Edit PALETTE / PROJECTS below, then run:  python3 scripts/build_assets.py
Everything lands in assets/. No dependencies.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

# ── DA ────────────────────────────────────────────────────────────────────
PALETTE = {
    "bg": "#07070d",
    "surface": "#0f0f1a",
    "line": "#1d1d2e",
    "text": "#f4f4fb",
    "muted": "#9a9ab5",
    "violet": "#8b5cf6",
    "sky": "#38bdf8",
    "pink": "#f472b6",
}
FONT = "'Inter','Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"

# ── Projects (name, tagline, tags, status, accent) ──────────────────────────
PROJECTS = [
    ("kauryui", "KauryUI", "Visual drag &amp; drop form builder for React — export JSX, Vue, HTML.",
     ["React", "TypeScript", "Tailwind", "Framer"], "LIVE", "violet"),
    ("hugoboost", "HugoBoost", "Productivity booster app for Windows. Less clicks, more flow.",
     ["Electron", "Node.js", "UX"], "BUILDING", "sky"),
    ("kinytimer", "KinyTimer", "Minimal focus timer for devs — zen mode, shortcuts, GitHub sync.",
     ["TypeScript", "React", "GitHub API"], "SHIPPED", "pink"),
    ("krypthash", "KryptHash", "Modern hash generator &amp; verifier — MD5, SHA-256, bcrypt.",
     ["React", "Tailwind", "crypto-js"], "SHIPPED", "violet"),
    ("pidrop", "DropPi", "Self-hosted LAN file &amp; note drop running on a Raspberry Pi.",
     ["TypeScript", "Node.js", "Raspberry Pi"], "SHIPPED", "sky"),
    ("kauth", "KAuth", "Local auth testing sandbox — play with flows without a backend.",
     ["TypeScript", "Auth", "Security"], "SHIPPED", "pink"),
]

P = PALETTE


def defs_gradients():
    return f"""
    <linearGradient id="brand" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{P['violet']}"/>
      <stop offset="50%" stop-color="{P['sky']}"/>
      <stop offset="100%" stop-color="{P['pink']}"/>
    </linearGradient>
    <linearGradient id="brandMove" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0%" stop-color="{P['violet']}"><animate attributeName="stop-color" dur="8s" repeatCount="indefinite" values="{P['violet']};{P['sky']};{P['pink']};{P['violet']}"/></stop>
      <stop offset="100%" stop-color="{P['sky']}"><animate attributeName="stop-color" dur="8s" repeatCount="indefinite" values="{P['sky']};{P['pink']};{P['violet']};{P['sky']}"/></stop>
    </linearGradient>"""


def header():
    w, h = 1200, 380
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Théo Blondel — Creative Technologist">
  <defs>{defs_gradients()}
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="{P['line']}" stroke-width="1"/>
    </pattern>
    <radialGradient id="fade" cx="50%" cy="50%" r="65%">
      <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
    <mask id="gridMask"><rect width="{w}" height="{h}" fill="url(#fade)"/></mask>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="24"/></clipPath>
  </defs>
  <style>
    .orb {{ transform-box: fill-box; transform-origin: center; }}
    .o1 {{ animation: drift1 14s ease-in-out infinite; }}
    .o2 {{ animation: drift2 18s ease-in-out infinite; }}
    .o3 {{ animation: drift3 16s ease-in-out infinite; }}
    @keyframes drift1 {{ 0%,100% {{ transform: translate(0,0) scale(1); }} 50% {{ transform: translate(180px,60px) scale(1.2); }} }}
    @keyframes drift2 {{ 0%,100% {{ transform: translate(0,0) scale(1.1); }} 50% {{ transform: translate(-200px,-40px) scale(.9); }} }}
    @keyframes drift3 {{ 0%,100% {{ transform: translate(0,0); }} 50% {{ transform: translate(-80px,70px); }} }}
    .up {{ opacity: 0; animation: up .9s cubic-bezier(.2,.8,.2,1) forwards; }}
    .d1 {{ animation-delay: .1s; }} .d2 {{ animation-delay: .35s; }} .d3 {{ animation-delay: .6s; }} .d4 {{ animation-delay: .85s; }}
    @keyframes up {{ from {{ opacity: 0; transform: translateY(18px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    .caret {{ animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .scan {{ animation: scan 6s linear infinite; }}
    @keyframes scan {{ from {{ transform: translateY(-40px); }} to {{ transform: translateY({h + 40}px); }} }}
    .pulse {{ animation: pulse 2s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
    @keyframes pulse {{ 0%,100% {{ opacity: 1; transform: scale(1); }} 50% {{ opacity: .4; transform: scale(1.6); }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .up {{ opacity: 1; }} }}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="{P['bg']}"/>
    <g filter="url(#blur)" opacity=".75">
      <circle class="orb o1" cx="220" cy="120" r="170" fill="{P['violet']}"/>
      <circle class="orb o2" cx="980" cy="270" r="190" fill="{P['sky']}" opacity=".7"/>
      <circle class="orb o3" cx="760" cy="40" r="120" fill="{P['pink']}" opacity=".55"/>
    </g>
    <rect width="{w}" height="{h}" fill="url(#grid)" mask="url(#gridMask)" opacity=".7"/>
    <rect class="scan" width="{w}" height="2" fill="url(#brand)" opacity=".25"/>

    <g font-family="{MONO}" font-size="15" fill="{P['muted']}">
      <text class="up d1" x="80" y="92"><tspan fill="{P['violet']}">~/</tspan>theoblondel <tspan fill="{P['sky']}">❯</tspan> whoami</text>
    </g>
    <text class="up d2" x="76" y="190" font-family="{FONT}" font-size="92" font-weight="800" letter-spacing="-3" fill="url(#brandMove)">Théo Blondel</text>
    <text class="up d3" x="80" y="240" font-family="{FONT}" font-size="26" font-weight="500" fill="{P['text']}">Creative technologist — design, code &amp; motion<tspan class="caret" fill="{P['sky']}">▍</tspan></text>

    <g class="up d4" font-family="{MONO}" font-size="14">{pills(80, 280, CHIPS)}</g>
    {orbit(960, 195)}

    <g class="up d4" font-family="{MONO}" font-size="14" fill="{P['muted']}">
      <circle class="pulse" cx="1004" cy="51" r="5" fill="#34d399"/>
      <text x="1018" y="56">open to collabs</text>
      <text x="1120" y="346" text-anchor="end">📍 Switzerland</text>
    </g>
    <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="24" fill="none" stroke="url(#brand)" stroke-opacity=".5"/>
  </g>
</svg>
"""


CHIPS = [("WEB APPS", "violet"), ("UI / UX", "sky"), ("BRANDING", "pink"), ("MOTION", "violet"), ("AUTOMATION", "sky")]


def pills(x, y, chips):
    out = []
    for label, color in chips:
        out.append(pill(x, y, label, P[color]))
        x += len(label) * 9.4 + 28 + 12
    return "".join(out)


def orbit(cx, cy):
    """Rotating rings with satellites — decorative, right side of the header."""
    rings = []
    for r, dur, color, dash, rev in [(108, 40, P["violet"], "2 10", False), (76, 26, P["sky"], "40 14", True), (46, 18, P["pink"], "1 7", False)]:
        spin = f'<animateTransform attributeName="transform" type="rotate" from="{360 if rev else 0} {cx} {cy}" to="{0 if rev else 360} {cx} {cy}" dur="{dur}s" repeatCount="indefinite"/>'
        rings.append(f'<g><circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-opacity=".45" stroke-dasharray="{dash}"/>'
                     f'<circle cx="{cx + r}" cy="{cy}" r="5" fill="{color}"/>{spin}</g>')
    core = (f'<text x="{cx}" y="{cy + 9}" text-anchor="middle" font-family="{MONO}" font-size="26" font-weight="700" fill="{P["text"]}" '
            f'fill-opacity=".9">&lt;/&gt;</text>')
    return f'<g class="up d4">{"".join(rings)}{core}</g>'


def pill(x, y, label, color):
    width = len(label) * 9.4 + 28
    return (f'<g transform="translate({x},{y})"><rect width="{width:.0f}" height="30" rx="15" fill="{color}" fill-opacity=".12" '
            f'stroke="{color}" stroke-opacity=".55"/><text x="{width / 2:.0f}" y="20" text-anchor="middle" fill="{color}" '
            f'letter-spacing="1">{label}</text></g>')


def card(slug, name, tagline, tags, status, accent, idx):
    w, h = 400, 190
    c = P[accent]
    tag_svg, x = [], 24
    for t in tags:
        tw = len(t) * 7.4 + 20
        tag_svg.append(f'<g transform="translate({x:.0f},140)"><rect width="{tw:.0f}" height="24" rx="6" fill="{P["line"]}"/>'
                       f'<text x="{tw / 2:.0f}" y="16.5" text-anchor="middle">{escape(t)}</text></g>')
        x += tw + 8
    # wrap tagline in 2 lines max (~46 chars)
    words, lines, cur = tagline.split(" "), [], ""
    for wd in words:
        if len((cur + " " + wd).replace("&amp;", "&")) > 46 and cur:
            lines.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    lines.append(cur)
    desc = "".join(f'<tspan x="24" dy="{0 if i == 0 else 20}">{ln}</tspan>' for i, ln in enumerate(lines[:2]))
    live = status in ("LIVE", "BUILDING")
    delay = idx * 0.6
    bw = len(status) * 7.8 + 36
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{name} — {escape(tagline.replace('&amp;', '&'))}">
  <defs>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c}"/><stop offset="100%" stop-color="{c}" stop-opacity=".05"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glow" cx="100%" cy="0%" r="80%">
      <stop offset="0%" stop-color="{c}" stop-opacity=".35"/><stop offset="100%" stop-color="{c}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="r"><rect width="{w}" height="{h}" rx="16"/></clipPath>
  </defs>
  <style>
    .shine {{ animation: sweep 5s ease-in-out {delay:.1f}s infinite; }}
    @keyframes sweep {{ 0% {{ transform: translateX(-{w}px); }} 45%,100% {{ transform: translateX({w}px); }} }}
    .dot {{ animation: pulse 1.8s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
    @keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .25; }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <g clip-path="url(#r)">
    <rect width="{w}" height="{h}" fill="{P['surface']}"/>
    <rect width="{w}" height="{h}" fill="url(#glow)"/>
    <rect class="shine" width="{w}" height="{h}" fill="url(#shine)"/>
    <text x="24" y="50" font-family="{FONT}" font-size="26" font-weight="800" letter-spacing="-.5" fill="{P['text']}">{name}</text>
    <g font-family="{MONO}" font-size="11" letter-spacing="1">
      <rect x="{w - 24 - bw:.0f}" y="30" width="{bw:.0f}" height="24" rx="12" fill="{c}" fill-opacity=".14"/>
      <circle class="{'dot' if live else ''}" cx="{w - 24 - bw + 14:.0f}" cy="42" r="3.5" fill="{c}"/>
      <text x="{w - 36:.0f}" y="46" text-anchor="end" fill="{c}">{status}</text>
    </g>
    <text x="24" y="86" font-family="{FONT}" font-size="15" fill="{P['muted']}">{desc}</text>
    <g font-family="{MONO}" font-size="12" fill="{P['text']}" fill-opacity=".85">{''.join(tag_svg)}</g>
    <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="16" fill="none" stroke="url(#edge)"/>
  </g>
</svg>
"""


def footer():
    import math
    w, h = 1200, 130
    period = 360  # px per wave; path is 2×w long so a translate of `period` loops seamlessly

    def path(amp, phase):
        pts = [f"{x},{60 + amp * math.sin(2 * math.pi * x / period + phase):.1f}" for x in range(0, 2 * w + 1, 12)]
        return "M" + " L".join(pts)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Create until your ideas feel real.">
  <defs>{defs_gradients()}
    <linearGradient id="edgeFade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".2" stop-color="#fff"/><stop offset=".8" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="m"><rect width="{w}" height="{h}" fill="url(#edgeFade)"/></mask>
  </defs>
  <style>
    .w1 {{ animation: slide 6s linear infinite; }}
    .w2 {{ animation: slide 9s linear infinite; }}
    .w3 {{ animation: slide 12s linear infinite; }}
    @keyframes slide {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-{period}px); }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>
  <g fill="none" stroke-linecap="round" mask="url(#m)">
    <path class="w1" d="{path(16, 0)}" stroke="{P['violet']}" stroke-width="2.5" opacity=".9"/>
    <path class="w2" d="{path(11, 1.4)}" stroke="{P['sky']}" stroke-width="2" opacity=".6"/>
    <path class="w3" d="{path(7, 2.8)}" stroke="{P['pink']}" stroke-width="1.5" opacity=".45"/>
  </g>
  <text x="{w / 2}" y="118" text-anchor="middle" font-family="{MONO}" font-size="14" letter-spacing="1" fill="{P['muted']}">“ create until your ideas feel real ”</text>
</svg>
"""


def divider(label):
    w, h = 1200, 44
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}">
  <defs>{defs_gradients()}</defs>
  <style>
    .bar {{ animation: grow 1.2s cubic-bezier(.2,.8,.2,1) forwards; transform-origin: 0 0; transform: scaleX(0); }}
    .run {{ animation: run 3.5s linear infinite; }}
    @keyframes grow {{ to {{ transform: scaleX(1); }} }}
    @keyframes run {{ from {{ transform: translateX(0); }} to {{ transform: translateX({w - 300}px); }} }}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} .bar {{ transform: none; }} }}
  </style>
  <text x="0" y="26" font-family="{MONO}" font-size="18" font-weight="700" letter-spacing="3" fill="url(#brand)">{escape(label.upper())}</text>
  <rect class="bar" x="{len(label) * 13.6 + 24:.0f}" y="19" width="{w - len(label) * 13.6 - 24:.0f}" height="1" fill="#2a2a40"/>
  <rect class="run" x="{len(label) * 13.6 + 24:.0f}" y="18" width="60" height="3" rx="1.5" fill="url(#brand)"/>
</svg>
"""


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "header.svg").write_text(header(), encoding="utf-8")
    (OUT / "footer.svg").write_text(footer(), encoding="utf-8")
    for i, p in enumerate(PROJECTS):
        (OUT / f"card-{p[0]}.svg").write_text(card(*p, idx=i), encoding="utf-8")
    for slug, label in [("about", "About me"), ("building", "Now building"), ("stack", "Stack"),
                        ("stats", "Activity"), ("connect", "Let's talk")]:
        (OUT / f"title-{slug}.svg").write_text(divider(label), encoding="utf-8")
    print("assets written to", OUT)


if __name__ == "__main__":
    main()
