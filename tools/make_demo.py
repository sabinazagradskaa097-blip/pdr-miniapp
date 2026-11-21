# Собирает demo/index.html из index.html: без проверки Telegram ID, своё хранилище, примеры данных.
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / 'index.html').read_text(encoding='utf8')
seed_p = root / 'tools' / 'demo_seed.json'
seed = seed_p.read_text(encoding='utf8') if seed_p.exists() else 'null'
def rep(a, b):
    global s
    assert s.count(a) == 1, a
    s = s.replace(a, b)
rep("const LS = 'pdr:';", "const LS = 'pdrdemo:';")
rep("const cloud = inTg &&", "const cloud = null && inTg &&")
rep("async function allowed() {", "async function allowed() { return true;")
rep("  ingest(lsAll());\n", "  if (!Object.keys(lsAll()).length && DEMO_SEED) { const m = {}; const sh = Date.now() - 3600e3 - Math.max(...DEMO_SEED.cars.map(c => c.t)); ['orders','insps','cars'].forEach(n => (DEMO_SEED[n] || []).forEach(o => { o.t += sh; if (o.doneAt) o.doneAt += sh; })); m.settings = JSON.stringify(DEMO_SEED.settings || {}); ['orders','insps','cars'].forEach((n, j) => (DEMO_SEED[n] || []).forEach(o => m[['o_','i_','c_'][j] + o.id] = JSON.stringify(o))); lsReplace(m); }\n  ingest(lsAll());\n")
rep("const ALLOWED =", "const DEMO_SEED = " + seed + ";\nconst ALLOWED =")
rep("</body>", "<div style=\"position:fixed;left:50%;bottom:calc(env(safe-area-inset-bottom,0px) + 76px);transform:translateX(-50%);z-index:99;background:rgba(255,206,110,.95);color:#1a1300;font:600 12px/1.3 system-ui;padding:6px 12px;border-radius:999px;pointer-events:none;white-space:nowrap\">Демо-версия · данные выдуманные</div>\n</body>")
(root / 'demo' / 'index.html').write_text(s, encoding='utf8')
print('ok', len(s))
