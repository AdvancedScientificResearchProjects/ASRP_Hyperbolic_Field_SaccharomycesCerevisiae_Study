#!/usr/bin/env python3
"""Folder tree for guide/NAVIGATION*.md, built from the real tree and the computed facts.

`render(lang, F)` walks the files git knows about (tracked or not ignored), checks that every path of the
spec exists, and aborts when a tracked top-level entry is missing from the spec, so the printed tree
cannot drift from the repository. Comments are in `en` / `ru`; `{key}` placeholders are facts.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (path, English comment, Russian comment, children)
SPEC = [
    ("README.md", "front page (English)", "главная страница (английская)"),
    ("README.ru.md", "front page (Russian)", "главная страница (русская)"),
    ("guide/", "detail pages X.md + X.ru.md; assets/ = generated SVG", "страницы-детали X.md + X.ru.md; assets/ = сгенерированные SVG"),
    ("archive/", "the previous README, kept byte for byte", "прежний README, сохранён байт в байт"),
    ("tools/", "showcase tooling: facts, visuals, excerpts, no-loss check", "инструменты витрины: факты, визуалы, выдержки, проверка без потерь"),
    ("tests/", "regression gate for the showcase", "регрессионный гейт витрины"),
    ("OSF_PREREGISTRATION.md", "in-repository copy of the preregistration (disputed, see Open questions)", "копия предрегистрации в репозитории (спорна, см. Открытые вопросы)"),
    ("en/README.md", "English-only mirror of the earlier README", "англоязычное зеркало прежнего README"),
    ("ru/README.md", "Russian-only mirror of the earlier README", "русскоязычное зеркало прежнего README"),
    ("data/", "raw observational data: {images_total} images, journal mapping, placeholders", "сырые наблюдательные данные: {images_total} снимков, сопоставление по журналу, заглушки", [
        ("data/README.md", "data hub (partly stale)", "хаб данных (частично устарел)"),
        ("data/photos/", "flat photo set: manifest, journal mapping, original/ (HEIC, PNG), jpg/ ({jpg_previews} previews)", "плоский набор фото: манифест, сопоставление, original/ (HEIC, PNG), jpg/ ({jpg_previews} превью)"),
        ("data/equipment/", "equipment-setup photographs", "фото установки"),
        ("data/microscopy/", "microscopy and staining photographs", "фото микроскопии и окрашивания"),
        ("data/control-01/", "placeholder bins {placeholder_bins}: control-NN, sample-chXX", "пустые корзины {placeholder_bins}: control-NN, sample-chXX"),
    ]),
    ("results/", "analysis outputs", "результаты анализа", [
        ("results/cv_analysis/", "cyto2 counts, morphometry, occupancy (CSV + JSON)", "счёт cyto2, морфометрия, занятость (CSV + JSON)"),
        ("results/llm_blind/", "{blind_runs} pilot blind runs + key", "{blind_runs} пилотных слепых прогона + ключ"),
        ("results/llm_full/", "final LLM scoring, {llm_fields} fields", "итоговая оценка LLM, {llm_fields} полей"),
    ]),
    ("reports/", "protocol (EN, RU) and the density report", "протокол (EN, RU) и отчёт по плотности", [
        ("reports/experiment_protocol_en.md", "experiment protocol", "протокол эксперимента"),
        ("reports/2026-06-09_density-analysis/", "report v2 EN + RU, {charts_report} charts, chart script", "отчёт v2 EN + RU, {charts_report} графиков, скрипт графиков"),
    ]),
    ("scripts/", "{scripts_py} Python files: cv_analysis/, llm_analysis/", "{scripts_py} файлов Python: cv_analysis/, llm_analysis/"),
    ("charts/", "{charts_mermaid} rendered diagrams of the earlier README", "{charts_mermaid} отрисованные схемы прежнего README", [
        ("charts/mermaid/", "root_1 to root_3, retry_1 (PNG)", "root_1 — root_3, retry_1 (PNG)"),
    ]),
    ("protocols/", "empty placeholder", "пустая заглушка"),
]
IGNORED_TOP = {".git", ".gitignore", ".gitattributes", ".DS_Store"}


def tracked():
    out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], capture_output=True, text=True,
                         cwd=ROOT).stdout.split("\n")
    return [x for x in out if x]


def render(lang, F):
    files = tracked()
    tops = {x.split("/")[0] for x in files}
    spec_tops = {e[0].rstrip("/").split("/")[0] for e in SPEC}
    missing = sorted(t for t in tops - spec_tops if t not in IGNORED_TOP)
    if missing:
        raise SystemExit("tools/tree.py: tracked top-level entries missing from SPEC: %s" % missing)
    col = 1 if lang == "en" else 2
    rows = []

    def exists(path):
        q = path.rstrip("/")
        return any(f == q or f.startswith(q + "/") for f in files) or os.path.exists(os.path.join(ROOT, q))

    def emit(entries, prefix, top):
        for i, e in enumerate(entries):
            last = i == len(entries) - 1
            if not exists(e[0]):
                raise SystemExit("tools/tree.py: path in SPEC does not exist: %s" % e[0])
            name = e[0] if top else e[0].rstrip("/").split("/")[-1] + ("/" if e[0].endswith("/") else "")
            rows.append((prefix + ("└── " if last else "├── "), name, e[col].format(**F)))
            if len(e) > 3 and e[3]:
                emit(e[3], prefix + ("    " if last else "│   "), False)

    rows.append(("", "ASRP_Hyperbolic_Field_SaccharomycesCerevisiae_Study/", ""))
    emit(SPEC, "", True)
    width = max(len(a) + len(b) for a, b, c in rows if c) + 2
    out = []
    for a, b, c in rows:
        out.append((a + b).ljust(width) + "# " + c if c else a + b)
    return "\n".join(out)
