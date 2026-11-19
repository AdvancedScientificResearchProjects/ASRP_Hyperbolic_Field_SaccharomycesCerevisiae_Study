#!/usr/bin/env python3
"""Generates the showcase visuals of the yeast study (never hand-edit the SVG output; edit this file).

    python3 tools/build_visuals.py

Output (English and Russian twin for every picture)
    guide/assets/banner/hero-banner.{en,ru}.svg           generated illustration, not a screenshot
    guide/assets/diagrams/programme-map.{en,ru}.svg       registered programme vs the one analysed batch
    guide/assets/diagrams/density-results.{en,ru}.svg     cell count by channel, cycles 2-3, and the cycle-1 reversal
    guide/assets/diagrams/claimed-vs-shown.{en,ru}.svg    what the README says vs what the data and code show
    guide/assets/diagrams/analysis-flow.{en,ru}.svg       journal -> mapping -> photos -> three methods -> report
    guide/assets/diagrams/timeline.{en,ru}.svg            plan (old diagram) vs what the repository records
    guide/assets/diagrams/ecosystem-flow.{en,ru}.svg      what this study depends on and what depends on it
    guide/assets/icons/*.svg                              navigation icons

Every number printed on a picture comes from tools/facts.py (computed from the repository at build
time). Every date on the timeline is checked against the repository text or git history it is taken from,
and the build aborts when it is missing. Rules (ASRP visual standard): <title>, <desc>, viewBox on every
SVG; text is measured and must fit its container (the build aborts otherwise); a status is a word paired
with a shape, never colour alone; one token set (tools/svgkit.py).
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit import *  # noqa: E402,F401,F403  (tokens, text(), Canvas, write(), ...)
import facts as factsmod  # noqa: E402

F = factsmod.facts()
CH_COLORS = {"0": MUTED, "17": TEAL, "19": VIOLET, "21": AMBER}


def fmt(s):
    return s.format(**F)


# a state is always a word paired with a shape (never colour alone)
STATE = {
    "en": {"shown": ("■ SHOWN", GREEN), "prelim": ("◧ PRELIMINARY", GOLD), "absent": ("✕ NOT DONE", AMBER),
           "disputed": ("◇ DISPUTED", VIOLET), "planned": ("◇ PLANNED ONLY", VIOLET), "partly": ("◧ PARTLY", GOLD),
           "analysed": ("■ ANALYSED", GREEN), "pending": ("◇ PENDING", VIOLET), "app": ("◇ APPLICATION", VIOLET)},
    "ru": {"shown": ("■ ПОКАЗАНО", GREEN), "prelim": ("◧ ПРЕДВАРИТЕЛЬНО", GOLD), "absent": ("✕ НЕ СДЕЛАНО", AMBER),
           "disputed": ("◇ СПОРНО", VIOLET), "planned": ("◇ ТОЛЬКО ПЛАН", VIOLET), "partly": ("◧ ЧАСТИЧНО", GOLD),
           "analysed": ("■ ПРОАНАЛИЗИРОВАНО", GREEN), "pending": ("◇ В ОЖИДАНИИ", VIOLET), "app": ("◇ ЗАЯВКА", VIOLET)},
}


def foot(cv, parts, bottom, color=MUTED, weight=400):
    lines = []
    for p in ([parts] if isinstance(parts, str) else parts):
        lines += wrap(p, FS_SMALL, cv.w - 48, weight >= 600)
    y = bottom - 20 * (len(lines) - 1)
    for i, ln in enumerate(lines):
        cv.label(24, y + 20 * i, ln, FS_SMALL, color, weight=weight, box=cv.w - 48)
    return len(lines)


def bars(cv, x, y, w, h, series, vmax, unit_fmt, label_box=90):
    """Vertical bars. series = [(label, value, colour)]; baseline at y+h; heights scale to vmax."""
    n = len(series)
    gap = 18
    bw = (w - gap * (n - 1)) / n
    cv.o.append("<line x1='%s' y1='%s' x2='%s' y2='%s' stroke='%s' stroke-width='1.5'/>" % (x - 6, y + h, x + w + 6, y + h, LINE))
    for i, (lab, val, col) in enumerate(series):
        bh = max(2.0, h * val / vmax)
        bx = x + i * (bw + gap)
        cv.o.append("<rect x='%.1f' y='%.1f' width='%.1f' height='%.1f' rx='6' fill='%s' fill-opacity='0.85'/>" % (bx, y + h - bh, bw, bh, col))
        cv.o.append(text("%.1f" % (bx + bw / 2), "%.1f" % (y + h - bh - 8), unit_fmt(val), FS_BODY, INK, "middle", 700, 0, bw + gap))
        cv.o.append(text("%.1f" % (bx + bw / 2), y + h + 22, lab, FS_SMALL, MUTED, "middle", 600, 0, bw + gap))


# --- hero banner -----------------------------------------------------------------------------
BANNER = {
    "en": {
        "title": "Hyperbolic Field × Yeast",
        "kicker": "SACCHAROMYCES CEREVISIAE STUDY",
        "tag": "PUBLIC REPO · RESULTS PRELIMINARY",
        "sub": ["Does a structured field change how yeast", "divides? One imaging batch so far"],
        "chart": "mean cells per 100× field, cycles 2–3",
        "chips": ["{images_total} images", "{cycles} experiment cycles", "{hypotheses} hypotheses"],
        "foot": "first analysed batch; fermentation kinetics not yet measured",
        "desc": ("Generated illustration, not a screenshot. Left: four bars, mean cells per 100x microscope field in cycles 2 and 3 "
                 "(control {mean_ch0}, channel 17 {mean_ch17}, channel 19 {mean_ch19}, channel 21 {mean_ch21}), a preliminary "
                 "density result. Right: the title, a one-line question and three figures computed from the repository: "
                 "{images_total} microscopy images, {cycles} experiment cycles, {hypotheses} registered hypotheses."),
    },
    "ru": {
        "title": "Гиперболическое поле × дрожжи",
        "kicker": "ИССЛЕДОВАНИЕ SACCHAROMYCES CEREVISIAE",
        "tag": "ПУБЛИЧНЫЙ РЕПО · РЕЗУЛЬТАТЫ ПРЕДВАРИТЕЛЬНЫЕ",
        "sub": ["Меняет ли структурированное поле деление", "дрожжей? Пока один пакет снимков"],
        "chart": "средний счёт клеток на поле 100×, циклы 2–3",
        "chips": ["{images_total} снимков", "{cycles} цикла эксперимента", "{hypotheses} гипотез"],
        "foot": "первый проанализированный пакет; кинетика ферментации ещё не измерена",
        "desc": ("Сгенерированная иллюстрация, не скриншот. Слева четыре столбца: средний счёт клеток на поле микроскопа 100× в циклах "
                 "2 и 3 (контроль {mean_ch0}, канал 17 {mean_ch17}, канал 19 {mean_ch19}, канал 21 {mean_ch21}), предварительный "
                 "результат по плотности. Справа заголовок, вопрос в одну строку и три числа, посчитанные по репозиторию: "
                 "{images_total} снимков микроскопии, {cycles} цикла эксперимента, {hypotheses} зарегистрированных гипотез."),
    },
}


def banner(lang):
    c = BANNER[lang]
    W, H = 1200, 330
    o = [svg_open(W, H, c["title"], fmt(c["desc"]))]
    cv = Canvas.__new__(Canvas)
    cv.w, cv.h, cv.o, cv._markers = W, H, o, set()
    series = [("CH0", int(F["mean_ch0"]), CH_COLORS["0"]), ("CH17", int(F["mean_ch17"]), CH_COLORS["17"]),
              ("CH19", int(F["mean_ch19"]), CH_COLORS["19"]), ("CH21", int(F["mean_ch21"]), CH_COLORS["21"])]
    o.append(text(40, 50, c["chart"], FS_KICKER, TEAL, "start", 700, 0, 440))
    bars(cv, 50, 80, 400, 170, series, 215, lambda v: str(v))
    tx = 520
    box = W - tx - 36
    o.append(text(tx, 86, c["kicker"], FS_KICKER, TEAL, "start", 700, 2, box))
    o.append(text(W - 36, 36, c["tag"], FS_SMALL, MUTED, "end", 700, 2, 560))
    o.append(text(tx, 146, c["title"], 46 if lang == "en" else 32, INK, "start", 800, 0, box))
    for i, line in enumerate(c["sub"]):
        o.append(text(tx, 188 + 28 * i, line, 21, MUTED, "start", 400, 0, box))
    x = tx
    for i, chip in enumerate(c["chips"]):
        chip = fmt(chip)
        w = text_width(chip, FS_KICKER, True) + 28
        if x + w > W - 30:
            raise SystemExit("chips overflow the banner: %r" % chip)
        col = [GOLD, TEAL, GREEN][i]
        o.append("<rect x='%.1f' y='252' width='%.1f' height='38' rx='19' fill='%s' fill-opacity='0.08' stroke='%s'/>" % (x, w, col, col))
        o.append(text("%.1f" % (x + w / 2), 277, chip, FS_KICKER, INK, "middle", 700))
        x += w + 12
    o.append(text(24, H - 14, c["foot"], FS_SMALL, MUTED, "start", 400, 0, 600))
    o.append("</svg>\n")
    return "\n".join(o)


# --- programme map ---------------------------------------------------------------------------
PROG = {
    "en": {
        "title": "Registered programme and the one analysed batch",
        "desc": ("Three cards. Fermentation kinetics: the registered primary programme (gas production, turbidity and time to onset, indices "
                 "FAI, FDI, FPI), no data in the repository, not done. Viability stain: methylene blue protocol registered; the first batch "
                 "used no stain, pending. Density imaging: {images_total} microscopy images in {cycles} cycles, cell count and occupancy by "
                 "channel, analysed and preliminary. Below, the registered design: {hypotheses} hypotheses, groups control, CH19, CH21, CH17 "
                 "and CH17+CH19; the data holds four of the five groups."),
        "sub": "What was registered is wider than what was measured",
        "tag": "PROGRAMME",
        "cards": [
            ("Fermentation kinetics", ["Registered primary track: gas, turbidity, time to onset; indices FAI, FDI, FPI",
                                       "No fermentation, gas or OD600 data in the repository"], "absent", AMBER),
            ("Viability stain", ["Methylene blue protocol registered for 24 h and 48 h",
                                 "The first batch used no stain: density only, not live/dead"], "pending", VIOLET),
            ("Density imaging", ["{images_total} microscopy images, {cycles} cycles, three methods: count, occupancy, blind LLM",
                                 "Report of 2026-06-09: a preliminary signal, not confirmatory"], "prelim", GOLD),
        ],
        "design": ("Registered design", ["{hypotheses} hypotheses; groups: control CH0, CH19, CH21, CH17, CH17+CH19",
                                         "The data holds four groups (CH0, CH17, CH19, CH21): the combined group CH17+CH19 is not in the data",
                                         "Double-blind RCT, N = 25–50 is the registered plan; blinding in practice is at scoring only"]),
        "foot": "Sources: README (archive), reports/experiment_protocol_en.md, reports/2026-06-09_density-analysis/report_en.md.",
    },
    "ru": {
        "title": "Программа и один проанализированный пакет",
        "desc": ("Три карточки. Кинетика ферментации: зарегистрированный первичный трек (газообразование, мутность и время до начала, "
                 "индексы FAI, FDI, FPI), данных в репозитории нет, не сделано. Окрашивание: протокол метиленового синего зарегистрирован; "
                 "первый пакет без окрашивания, в ожидании. Плотность по снимкам: {images_total} снимков микроскопии в {cycles} циклах, "
                 "счёт клеток и занятость по каналам, проанализировано, предварительно. Ниже зарегистрированный дизайн: {hypotheses} "
                 "гипотез, группы контроль, CH19, CH21, CH17 и CH17+CH19; в данных четыре группы из пяти."),
        "sub": "Зарегистрировано шире, чем измерено",
        "tag": "ПРОГРАММА",
        "cards": [
            ("Кинетика ферментации", ["Зарегистрированный первичный трек: газ, мутность, время до начала; индексы FAI, FDI, FPI",
                                      "Данных по ферментации, газу и OD600 в репозитории нет"], "absent", AMBER),
            ("Окрашивание жизнеспособности", ["Протокол метиленового синего зарегистрирован на 24 ч и 48 ч",
                                              "Первый пакет без окрашивания: только плотность, не живые/мёртвые"], "pending", VIOLET),
            ("Плотность по снимкам", ["{images_total} снимков микроскопии, {cycles} цикла, три метода: счёт, занятость, слепой LLM",
                                      "Отчёт 2026-06-09: предварительный сигнал, не подтверждение"], "prelim", GOLD),
        ],
        "design": ("Зарегистрированный дизайн", ["{hypotheses} гипотез; группы: контроль CH0, CH19, CH21, CH17, CH17+CH19",
                                                 "В данных четыре группы (CH0, CH17, CH19, CH21): комбинированной группы CH17+CH19 в данных нет",
                                                 "Двойное слепое РКИ, N = 25–50 — зарегистрированный план; на практике ослепление только при оценке"]),
        "foot": "Источники: README (архив), reports/experiment_protocol_ru.md, reports/2026-06-09_density-analysis/report_ru.md.",
    },
}


def programme(lang):
    c = PROG[lang]
    W, H = 1200, 520
    cv = Canvas(W, H, c["title"], fmt(c["desc"]), c["title"], c["sub"], c["tag"])
    st = STATE[lang]
    bw, gap = 372, 18
    for i, (t, body, state, col) in enumerate(c["cards"]):
        cv.box(24 + i * (bw + gap), 100, bw, t, [fmt(b) for b in body], status=[st[state]], stroke=col, h=190, valign="top")
    t, body = c["design"]
    cv.box(24, 312, W - 48, t, [fmt(b) for b in body], stroke=BLUE, h=150, valign="top")
    foot(cv, c["foot"], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- density results ---------------------------------------------------------------------------
RES = {
    "en": {
        "title": "Cell density by channel: two cycles agree, cycle 1 reverses",
        "desc": ("Left: mean cell count per 100x field, cycles 2 and 3 pooled, cyto2 segmentation: control {mean_ch0} (n {n_ch0}), CH17 "
                 "{mean_ch17} ({pct_ch17} percent, n {n_ch17}), CH19 {mean_ch19} ({pct_ch19} percent, n {n_ch19}), CH21 {mean_ch21} "
                 "({pct_ch21} percent, n {n_ch21}). Right: cycle 1, occupancy only, the fraction of the image covered by cells: control "
                 "{occ1_ch0}, CH17 {occ1_ch17}, CH19 {occ1_ch19}, CH21 {occ1_ch21}; CH21 is the densest ({occ1_pct_ch21} percent), the opposite "
                 "of cycles 2 and 3. CH17 ranks first and CH21 last in both cycles that have counts."),
        "sub": "Preliminary: N = 2 cycles with counts, descriptive only",
        "tag": "RESULTS SO FAR",
        "left": "CELL COUNT, 100×, CYCLES 2–3",
        "right": "CYCLE 1: OCCUPANCY, THE OPPOSITE ORDER",
        "lnote": ["Per cycle (CH0 / CH17 / CH19 / CH21):", "cycle 2: {cyc2_ch0} / {cyc2_ch17} / {cyc2_ch19} / {cyc2_ch21}",
                  "cycle 3: {cyc3_ch0} / {cyc3_ch17} / {cyc3_ch19} / {cyc3_ch21}"],
        "rnote": ["Occupancy = fraction of the image covered by cells.", "CH21 is {occ1_pct_ch21}% vs control here; CH17 only {occ1_pct_ch17}%."],
        "foot": ["Same pixels, three methods agree per field (rho 0.81–0.89), but this is not independent replication.",
                 "Source: reports/2026-06-09_density-analysis/report_en.md; numbers recomputed from results/cv_analysis/*.csv."],
    },
    "ru": {
        "title": "Плотность по каналам: цикл 1 обратный",
        "desc": ("Слева: средний счёт клеток на поле 100×, циклы 2 и 3 вместе, сегментация cyto2: контроль {mean_ch0} (n {n_ch0}), CH17 "
                 "{mean_ch17} ({pct_ch17} процентов, n {n_ch17}), CH19 {mean_ch19} ({pct_ch19} процентов, n {n_ch19}), CH21 {mean_ch21} "
                 "({pct_ch21} процентов, n {n_ch21}). Справа: цикл 1, только занятость, доля снимка, занятая клетками: контроль "
                 "{occ1_ch0}, CH17 {occ1_ch17}, CH19 {occ1_ch19}, CH21 {occ1_ch21}; CH21 самый плотный ({occ1_pct_ch21} процентов), "
                 "обратно циклам 2 и 3. CH17 первый, CH21 последний в обоих циклах со счётом."),
        "sub": "Предварительно: N = 2 цикла со счётом, только описательно",
        "tag": "РЕЗУЛЬТАТЫ ПОКА",
        "left": "СЧЁТ КЛЕТОК, 100×, ЦИКЛЫ 2–3",
        "right": "ЦИКЛ 1: ЗАНЯТОСТЬ, ОБРАТНЫЙ ПОРЯДОК",
        "lnote": ["По циклам (CH0 / CH17 / CH19 / CH21):", "цикл 2: {cyc2_ch0} / {cyc2_ch17} / {cyc2_ch19} / {cyc2_ch21}",
                  "цикл 3: {cyc3_ch0} / {cyc3_ch17} / {cyc3_ch19} / {cyc3_ch21}"],
        "rnote": ["Занятость = доля снимка, занятая клетками.", "CH21 здесь {occ1_pct_ch21}% к контролю; CH17 лишь {occ1_pct_ch17}%."],
        "foot": ["Те же пиксели, три метода согласуются по кадрам (rho 0,81–0,89), но это не независимая репликация.",
                 "Источник: reports/2026-06-09_density-analysis/report_ru.md; числа пересчитаны из results/cv_analysis/*.csv."],
    },
}


def results(lang):
    c = RES[lang]
    W, H = 1200, 600
    cv = Canvas(W, H, c["title"], fmt(c["desc"]), c["title"], c["sub"], c["tag"])
    cv.panel(24, 96, 570, 380, c["left"], BLUE)
    cv.panel(606, 96, 570, 380, c["right"], BLUE)
    left = [("CH0", int(F["mean_ch0"]), CH_COLORS["0"]), ("CH17", int(F["mean_ch17"]), CH_COLORS["17"]),
            ("CH19", int(F["mean_ch19"]), CH_COLORS["19"]), ("CH21", int(F["mean_ch21"]), CH_COLORS["21"])]
    bars(cv, 70, 160, 480, 200, left, 215, lambda v: str(v))
    right = [("CH0", float(F["occ1_ch0"]), CH_COLORS["0"]), ("CH17", float(F["occ1_ch17"]), CH_COLORS["17"]),
             ("CH19", float(F["occ1_ch19"]), CH_COLORS["19"]), ("CH21", float(F["occ1_ch21"]), CH_COLORS["21"])]
    bars(cv, 652, 160, 480, 200, right, 0.27, lambda v: "%.3f" % v)
    for i, ln in enumerate(c["lnote"]):
        cv.label(48, 420 + 19 * i, fmt(ln), FS_SMALL, INK if i == 0 else MUTED, weight=600 if i == 0 else 400, box=520)
    for i, ln in enumerate(c["rnote"]):
        cv.label(630, 420 + 19 * i, fmt(ln), FS_SMALL, MUTED, box=520)
    foot(cv, c["foot"], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- claimed vs shown ------------------------------------------------------------------------
# every row has a source path in the repository (page guide/EVIDENCE shows the same rows with file and line)
CLAIM = {
    "en": {
        "title": "What is claimed and what was shown",
        "desc": ("Seven rows: topic, what the README or protocol says, what the files show, and a state word. Fermentation kinetics claimed as "
                 "primary; no such data (not done). Direction of the density effect: CH17 more cells, CH21 fewer; shown in two cycles, "
                 "cycle 1 reverses (preliminary). Replication: README says reproducible; the report says not yet (preliminary). Preregistered "
                 "before data: the in-repository file was added on 2026-06-10, after the data (disputed). CH19 faster division: not "
                 "supported on this batch (not shown). Blinded randomised design: blinding at scoring only (partly). Patent: an "
                 "application number only (application)."),
        "sub": "Left: the claim as written. Right: what the repository files show",
        "tag": "CLAIMED VS SHOWN",
        "cols": ["TOPIC", "CLAIMED", "SHOWN IN THE REPOSITORY", "STATE"],
        "rows": [
            ("Primary outcome", "Fermentation rate, gas, onset; indices FAI, FDI, FPI", "No fermentation, gas or OD600 data; only microscopy photos", "absent"),
            ("Density signal", "CH17 raises, CH21 lowers cell count", "{pct_ch17}% / {pct_ch21}% in cycles 2–3 (n = 2 cycles); cycle 1 reverses", "prelim"),
            ("Replication", "README: 'reproducible directional effect'", "Report: 'not yet a reproducible effect'; needs 5 or more cycles", "prelim"),
            ("Preregistration", "Hypotheses registered before data collection", "OSF_PREREGISTRATION.md first added 2026-06-10, after the data", "disputed"),
            ("CH19 division rate", "CH19 accelerates division", "Not supported on this batch: count equals control, cells rounder, budding flat", "absent"),
            ("Design", "Randomised double-blind RCT, N = 25–50", "Blinding at scoring only; no randomisation log; 4 groups of 5", "partly"),
            ("Patent", "KZ 2025/1095.1, substantive exam", "An application number only; applicant not stated; not granted", "app"),
        ],
        "foot": ["A claim is filed as shown only when a file in the repository carries it. Full rows with file and line: guide/EVIDENCE.md."],
    },
    "ru": {
        "title": "Что заявлено и что показано",
        "desc": ("Семь строк: тема, что говорят README или протокол, что показывают файлы, и слово-состояние. Кинетика ферментации заявлена "
                 "как первичная; таких данных нет (не сделано). Направление эффекта плотности: CH17 больше клеток, CH21 меньше; показано в "
                 "двух циклах, цикл 1 обратный (предварительно). Репликация: README говорит воспроизводимо; отчёт говорит пока нет "
                 "(предварительно). Предрегистрация до данных: файл в репозитории добавлен 2026-06-10, после данных (спорно). Ускорение "
                 "деления CH19: на этом пакете не подтверждено (не сделано). Рандомизированный слепой дизайн: ослепление только при "
                 "оценке (частично). Патент: только номер заявки (заявка)."),
        "sub": "Слева заявление как написано. Справа что показывают файлы репозитория",
        "tag": "ЗАЯВЛЕНО И ПОКАЗАНО",
        "cols": ["ТЕМА", "ЗАЯВЛЕНО", "ПОКАЗАНО В РЕПОЗИТОРИИ", "СОСТОЯНИЕ"],
        "rows": [
            ("Первичный исход", "Скорость ферментации, газ, начало; индексы FAI, FDI, FPI", "Данных по ферментации, газу, OD600 нет; только фото микроскопии", "absent"),
            ("Сигнал плотности", "CH17 повышает, CH21 снижает счёт клеток", "{pct_ch17}% / {pct_ch21}% в циклах 2–3 (n = 2 цикла); цикл 1 обратный", "prelim"),
            ("Репликация", "README: «воспроизводимый направленный эффект»", "Отчёт: «пока не воспроизводимый эффект»; нужно 5 и более циклов", "prelim"),
            ("Предрегистрация", "Гипотезы зарегистрированы до сбора данных", "OSF_PREREGISTRATION.md добавлен 2026-06-10, после данных", "disputed"),
            ("Скорость деления CH19", "CH19 ускоряет деление", "На этом пакете не подтверждено: счёт как у контроля, клетки круглее, почкование без изменений", "absent"),
            ("Дизайн", "Рандомизированное двойное слепое РКИ, N = 25–50", "Ослепление только при оценке; журнала рандомизации нет; 4 группы из 5", "partly"),
            ("Патент", "KZ 2025/1095.1, экспертиза по существу", "Только номер заявки; заявитель не указан; не выдан", "app"),
        ],
        "foot": ["Утверждение считается показанным, только если его несёт файл репозитория. Полные строки с файлом и строкой: guide/EVIDENCE.ru.md."],
    },
}


def claimed(lang):
    c = CLAIM[lang]
    st = STATE[lang]
    W, H = 1200, 836
    cv = Canvas(W, H, c["title"], fmt(c["desc"]), c["title"], c["sub"], c["tag"])
    x0, x1, x2, x3 = 24, 190, 560, 1000
    w1, w2, w3 = 370, 440, 176
    ytop = 98
    for x, w, i in ((x0, 160, 0), (x1, w1, 1), (x2, w2, 2), (x3, w3, 3)):
        cv.label(x, ytop + 10, c["cols"][i], FS_KICKER, TEAL, weight=700, box=w)
    rh, gap = 84, 8
    for i, (topic, claim, shown, state) in enumerate(c["rows"]):
        y = ytop + 26 + i * (rh + gap)
        label, col = st[state]
        for k, ln in enumerate(wrap(topic, FS_BODY, 156, True)):
            cv.label(x0, y + rh / 2 + 5 + 19 * (k - (len(wrap(topic, FS_BODY, 156, True)) - 1) / 2), ln, FS_BODY, INK, weight=700, box=160)
        cv.box(x1, y, w1 - 12, None, [fmt(claim)], stroke=BLUE, h=rh)
        cv.box(x2, y, w2 - 12, None, [fmt(shown)], stroke=col, h=rh)
        cv.box(x3, y, w3, None, [], status=[(label, col)], stroke=col, h=rh, center=True)
    foot(cv, c["foot"], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- analysis flow ---------------------------------------------------------------------------
FLOW = {
    "en": {
        "title": "From handwritten journal to the report",
        "desc": ("Left to right: the handwritten lab journal, transcribed into journal-mapping.csv ({mapping_rows} rows, {mapping_images} images, "
                 "{cycles} cycles); the photo set ({images_total} files, {images_heic} HEIC and {images_png} PNG); then three methods run "
                 "without the channel label: cyto2 cell count on {count_fields} fields, texture occupancy on {occupancy_fields} fields and "
                 "blind LLM scoring of {llm_fields} fields; the channel is joined back only at aggregation; the output is one report."),
        "sub": "The channel of every photo comes from a handwritten journal",
        "tag": "ANALYSIS FLOW",
        "cards": [
            ("Lab journal", ["Handwritten, three pages: photo number to channel, medium, replicate, magnification"], GOLD),
            ("Mapping CSV", ["{mapping_rows} rows, {mapping_images} images, {cycles} cycles", "confidence: {conf_high} high, {conf_med} medium, {conf_low} low"], GOLD),
            ("Photo set", ["{images_total} files: {images_heic} HEIC and {images_png} PNG", "{images_dated} carry a date, {images_undated} do not"], TEAL),
        ],
        "methods": [
            ("cyto2 cell count", ["{count_fields} fields at 100×", "counts cells; undercounts"], TEAL),
            ("Texture occupancy", ["{occupancy_fields} fields", "no segmentation"], VIOLET),
            ("Blind LLM scoring", ["{llm_fields} fields", "neutral file names"], GREEN),
        ],
        "join": ("Aggregation by channel", ["The channel is revealed here, by joining the mapping", "Unit of replication: the cycle, not the photo"]),
        "out": ("Report v2, 2026-06-09", ["Preliminary signal, not confirmatory"]),
        "foot": "Reading: the journal is the only link between a photo and its channel; the analysis cannot be better than the transcription.",
    },
    "ru": {
        "title": "От рукописного журнала до отчёта",
        "desc": ("Слева направо: рукописный лабораторный журнал, переписанный в journal-mapping.csv ({mapping_rows} строк, {mapping_images} "
                 "снимков, {cycles} цикла); набор фото ({images_total} файлов, {images_heic} HEIC и {images_png} PNG); затем три метода "
                 "без метки канала: счёт клеток cyto2 на {count_fields} полях, занятость текстуры на {occupancy_fields} полях и слепая "
                 "оценка LLM {llm_fields} полей; канал присоединяется только при агрегации; на выходе один отчёт."),
        "sub": "Канал каждого снимка известен из рукописного журнала",
        "tag": "ПОТОК АНАЛИЗА",
        "cards": [
            ("Лабораторный журнал", ["Рукописный, три страницы: номер снимка в канал, среду, повтор, увеличение"], GOLD),
            ("CSV-сопоставление", ["{mapping_rows} строк, {mapping_images} снимков, {cycles} цикла", "уверенность: {conf_high} высокая, {conf_med} средняя, {conf_low} низкая"], GOLD),
            ("Набор фото", ["{images_total} файлов: {images_heic} HEIC и {images_png} PNG", "дата у {images_dated}, без даты {images_undated}"], TEAL),
        ],
        "methods": [
            ("Счёт клеток cyto2", ["{count_fields} полей при 100×", "считает клетки; занижает"], TEAL),
            ("Занятость текстуры", ["{occupancy_fields} полей", "без сегментации"], VIOLET),
            ("Слепая оценка LLM", ["{llm_fields} полей", "нейтральные имена файлов"], GREEN),
        ],
        "join": ("Агрегация по каналам", ["Канал раскрывается здесь, через сопоставление", "Единица репликации: цикл, а не снимок"]),
        "out": ("Отчёт v2, 2026-06-09", ["Предварительный сигнал, не подтверждение"]),
        "foot": "Вывод: журнал — единственная связь снимка с каналом; анализ не точнее переписи журнала.",
    },
}


def flow(lang):
    c = FLOW[lang]
    W, H = 1200, 640
    cv = Canvas(W, H, c["title"], fmt(c["desc"]), c["title"], c["sub"], c["tag"])
    bw, gap, y, h = 372, 18, 100, 108
    xs = [24 + i * (bw + gap) for i in range(3)]
    for x, (t, body, col) in zip(xs, c["cards"]):
        cv.box(x, y, bw, t, [fmt(b) for b in body], stroke=col, h=h, valign="top")
    cv.arrow([(xs[0] + bw + 2, y + h / 2), (xs[1] - 2, y + h / 2)], GOLD)
    cv.arrow([(xs[1] + bw + 2, y + h / 2), (xs[2] - 2, y + h / 2)], GOLD)
    ym, trunk = 262, 236
    for x, (t, body, col) in zip(xs, c["methods"]):
        cv.box(x, ym, bw, t, [fmt(b) for b in body], stroke=col, h=92, valign="top")
        pts = [(xs[2] + bw / 2, y + h + 3), (xs[2] + bw / 2, trunk), (x + bw / 2, trunk), (x + bw / 2, ym - 3)]
        cv.arrow(pts if x != xs[2] else [pts[0], pts[-1]], TEAL)
    yj = 402
    t, body = c["join"]
    cv.box(24, yj, W - 48, t, [fmt(b) for b in body], stroke=BLUE, h=92, valign="top")
    for x in xs:
        cv.arrow([(x + bw / 2, ym + 92 + 3), (x + bw / 2, yj - 3)], BLUE)
    t, body = c["out"]
    cv.box(24, yj + 92 + 30, W - 48, t, [fmt(b) for b in body], stroke=GREEN, h=70, valign="top")
    cv.arrow([(W / 2, yj + 92 + 3), (W / 2, yj + 92 + 27)], GREEN)
    foot(cv, c["foot"], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- timeline --------------------------------------------------------------------------------
# (date shown, text, source, needle). source: a repository path (needle must occur in it) or "git" (needle =
# a commit hash whose author date must equal the date shown)
TIMELINE_PLAN = [
    ("Mar 28", {"en": "Team assembled, protocol defined", "ru": "Команда собрана, протокол определён"}),
    ("Mar 29", {"en": "Emitter upgrade 0.7 W to 60 W / 144 W", "ru": "Модернизация излучателя 0,7 Вт до 60 / 144 Вт"}),
    ("Mar 31", {"en": "Microscopy and staining validated", "ru": "Микроскопия и окрашивание валидированы"}),
    ("Apr 4", {"en": "OSF preregistration submitted", "ru": "OSF: предрегистрация подана"}),
    ("Apr 7", {"en": "OSF registration accepted", "ru": "Регистрация OSF принята"}),
    ("Q2 2026", {"en": "Irradiation experiments begin", "ru": "Начало экспериментов по облучению"}),
    ("Q3–Q4 2026", {"en": "Data collection and CV analysis", "ru": "Сбор данных и CV-анализ"}),
    ("Q3–Q4 2026", {"en": "Publication preparation", "ru": "Подготовка публикации"}),
]
TIMELINE_REC = [
    ("2026-03-28", {"en": "Repository created (first commit)", "ru": "Репозиторий создан (первый коммит)"}, "git", "28b0485"),
    ("2026-04-04", {"en": "OSF project osf.io/vxkum registered", "ru": "OSF: проект osf.io/vxkum"}, "archive/README_2026-11-19_pre-showcase.md", "Apr 4, 2026"),
    ("2026-04-19", {"en": "First photos observed ({images_dated} dated, to {date_last})", "ru": "Первые снимки ({images_dated} с датой, до {date_last})"}, "data/photos/manifest.json", "2026-04-19"),
    ("2026-05-06", {"en": "Photo hub and manifest added to the repository", "ru": "В репозиторий добавлен хаб фото и манифест"}, "git", "05fcfd7"),
    ("2026-06-09", {"en": "Density report v2: preliminary signal", "ru": "Отчёт v2 по плотности: лишь сигнал"}, "reports/2026-06-09_density-analysis/report_en.md", "2026-06-09"),
    ("2026-06-10", {"en": "Preregistration file first committed, results already in it", "ru": "Файл предрегистрации впервые закоммичен, результаты уже в нём"}, "git", "0461da9"),
    ("2026-07-18", {"en": "Last change: README aligned to the house template", "ru": "Последнее изменение: README по шаблону дома"}, "git", "5942aa8"),
    ("2026-11-19", {"en": "Showcase restructuring (this change)", "ru": "Новая структура README (это изменение)"}, None, None),
]
TL = {
    "en": {
        "title": "Plan versus what the repository records",
        "desc": ("Two lanes of eight events, in order, not to scale. Lane one, the plan drawn in the old README: {plan}. Lane two, what the "
                 "repository records: {rec}."),
        "sub": "Not to scale; recorded dates come from git history or repository files",
        "tag": "TIMELINE",
        "lanes": ["THE PLAN (diagram of the old README)", "RECORDED IN THE REPOSITORY"],
        "note": "Irradiation, fermentation and publication steps of the plan have no recorded result yet.",
    },
    "ru": {
        "title": "План и то, что записано в репозитории",
        "desc": ("Две дорожки по восемь событий, по порядку, без масштаба. Первая, план со схемы прежнего README: {plan}. Вторая, что "
                 "записано в репозитории: {rec}."),
        "sub": "Без масштаба; даты записи взяты из истории git и файлов репозитория",
        "tag": "ХРОНОЛОГИЯ",
        "lanes": ["ПЛАН (схема прежнего README)", "ЗАПИСАНО В РЕПОЗИТОРИИ"],
        "note": "Шаги плана по облучению, ферментации и публикации пока без записанного результата.",
    },
}


def git_date(h):
    return subprocess.run(["git", "show", "-s", "--format=%ad", "--date=short", h], cwd=factsmod.ROOT,
                          capture_output=True, text=True).stdout.strip()


def check_dates():
    for date, _t, src, needle in TIMELINE_REC:
        if src is None:
            continue
        if src == "git":
            if git_date(needle) != date:
                raise SystemExit("timeline: commit %s is dated %s, not %s" % (needle, git_date(needle), date))
        elif needle not in factsmod.read(src):
            raise SystemExit("timeline date %s (%r) is not in %s" % (date, needle, src))


def timeline(lang):
    check_dates()
    c = TL[lang]
    desc = c["desc"].format(plan="; ".join("%s %s" % (d, t[lang]) for d, t in TIMELINE_PLAN),
                            rec="; ".join("%s %s" % (d, fmt(t[lang])) for d, t, _, _ in TIMELINE_REC))
    W, H = 1200, 590
    cv = Canvas(W, H, c["title"], desc, c["title"], c["sub"], c["tag"])
    n, gap = 8, 8
    bw = (W - 48 - gap * (n - 1)) / n
    lanes = ((TIMELINE_PLAN, GOLD, 112, c["lanes"][0], 124), (TIMELINE_REC, TEAL, 312, c["lanes"][1], 175))
    for events, col, y, lab, bh in lanes:
        cv.label(24, y, lab, FS_KICKER, col, weight=800, box=600)
        cv.o.append("<line x1='24' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2' stroke-opacity='0.6'/>" % (y + 18, W - 24, y + 18, col))
        for i, ev in enumerate(events):
            date, t = ev[0], ev[1]
            x = 24 + i * (bw + gap)
            cv.o.append("<circle cx='%.1f' cy='%d' r='6' fill='%s'/>" % (x + bw / 2, y + 18, col))
            cv.box(x, y + 34, bw, date, [fmt(t[lang])], stroke=col, h=bh, title_size=14, pad=10, valign="top")
            if events is TIMELINE_REC and ev[2] is None:
                cv.o.append("<rect x='%.1f' y='%d' width='%.1f' height='%d' rx='%d' fill='none' stroke='%s' stroke-width='4'/>" % (x, y + 34, bw, bh, RADIUS, BG0))
                cv.o.append("<rect x='%.1f' y='%d' width='%.1f' height='%d' rx='%d' fill='none' stroke='%s' stroke-width='2' stroke-dasharray='6 5'/>" % (x, y + 34, bw, bh, RADIUS, col))
    foot(cv, c["note"], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- ecosystem flow --------------------------------------------------------------------------
ECO = {
    "en": {
        "title": "What this study depends on",
        "desc": ("Centre: the yeast study. It depends on the blood plasma study for the meaning of channels 19 and 21, on the emitter programs "
                 "repository for the hardware control, and on a patent application KZ 2025/1095.1 for the hardware family. Sibling studies "
                 "of the same field, plants and crystals, are only listed. {portfolio_patents} patent applications appear in the portfolio "
                 "table of the old README; none is stated as granted."),
        "sub": "Dependencies as stated in this repository, not checked elsewhere",
        "tag": "ECOSYSTEM",
        "centre": ("Yeast study", ["this repository", "{images_total} images, {cycles} cycles"], "prelim"),
        "left": [("Blood plasma study", ["Source of the CH19 and CH21 directional hypotheses", "osf.io/8q42f"], VIOLET),
                 ("Emitter programs", ["Control software of the emitters", "this study logs channel identifiers only"], TEAL)],
        "right": [("Patent application", ["KZ 2025/1095.1, substantive exam", "same hardware family; not a granted patent"], AMBER),
                  ("Sibling studies", ["Agricultural (plants, seeds) and crystal studies", "listed only, nothing is imported"], MUTED)],
        "up": "channel meaning", "up2": "hardware", "foot": "The repository does not name the applicants; an application is not a granted patent.",
    },
    "ru": {
        "title": "От чего зависит это исследование",
        "desc": ("В центре исследование дрожжей. Оно зависит от исследования плазмы крови в смысле каналов 19 и 21, от репозитория "
                 "программ излучателей в части управления аппаратурой и от патентной заявки KZ 2025/1095.1 по аппаратному семейству. "
                 "Смежные исследования того же поля, растения и кристаллы, только перечислены. В таблице портфеля прежнего README "
                 "{portfolio_patents} патентных заявок; ни одна не названа выданной."),
        "sub": "Зависимости как указано в этом репозитории, вне его не проверены",
        "tag": "ЭКОСИСТЕМА",
        "centre": ("Исследование дрожжей", ["этот репозиторий", "{images_total} снимков, {cycles} цикла"], "prelim"),
        "left": [("Исследование плазмы крови", ["Источник гипотез направления CH19 и CH21", "osf.io/8q42f"], VIOLET),
                 ("Программы излучателей", ["ПО управления излучателями", "это исследование логирует только идентификаторы каналов"], TEAL)],
        "right": [("Патентная заявка", ["KZ 2025/1095.1, экспертиза по существу", "то же аппаратное семейство; не выданный патент"], AMBER),
                  ("Смежные исследования", ["Сельскохозяйственное (растения, семена) и кристаллов", "только перечислены, ничего не импортируется"], MUTED)],
        "up": "смысл каналов", "up2": "аппаратура", "foot": "Репозиторий заявителей не называет; заявка — не выданный патент.",
    },
}


def ecosystem(lang):
    c = ECO[lang]
    st = STATE[lang]
    W, H = 1200, 460
    cv = Canvas(W, H, c["title"], fmt(c["desc"]), c["title"], c["sub"], c["tag"])
    cw, cx = 340, (W - 340) / 2
    t, body, state = c["centre"]
    cv.box(cx, 190, cw, t, [fmt(b) for b in body], status=[st[state]], stroke=GOLD, h=130, valign="top")
    lw = 380
    for i, (t, body, col) in enumerate(c["left"]):
        y = 100 + i * 170
        cv.box(24, y, lw, t, [fmt(b) for b in body], stroke=col, h=130, valign="top")
        cv.arrow([(24 + lw + 3, y + 65), (cx - 3, 255 + (i - 0.5) * 40)], col)
    for i, (t, body, col) in enumerate(c["right"]):
        y = 100 + i * 170
        cv.box(W - 24 - lw, y, lw, t, [fmt(b) for b in body], stroke=col, h=130, valign="top", )
        cv.arrow([(cx + cw + 3, 255 + (i - 0.5) * 40), (W - 24 - lw - 3, y + 65)] if i == 1 else [(W - 24 - lw - 3, y + 65), (cx + cw + 3, 255 + (i - 0.5) * 40)], col, dashed=(i == 1), animate=False)
    foot(cv, c["foot"], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- redraws of the four earlier mermaid PNGs (charts/mermaid/*.png) ----------------------------
DECL = {"en": ("◇ DECLARED", VIOLET), "ru": ("◇ ЗАЯВЛЕНО", VIOLET)}

GROUPS = {
    "en": {
        "title": "Treatment and control groups as planned",
        "desc": ("Redrawn from the earlier diagram charts/mermaid/root_1.png. Four treatment groups, CH17, CH19, CH21 and CH17+CH19, and one "
                 "control group, each stated as 5-10 samples, flow into measurements and then results."),
        "sub": "Earlier diagram, redrawn; group sizes are as that diagram states",
        "tag": "DESIGN · REDRAWN",
        "t_panel": "TREATMENT GROUPS", "c_panel": "CONTROL GROUP",
        "groups": [("CH17", TEAL), ("CH19", VIOLET), ("CH21", AMBER), ("CH17+CH19", BLUE)], "control": "Control",
        "n": "5-10 samples", "meas": "Measurements", "res": "Results",
        "foot": "Declared in the earlier README diagram; the sample counts are not checked against the data here.",
    },
    "ru": {
        "title": "Группы воздействия и контроль по плану",
        "desc": ("Перерисовано с прежней схемы charts/mermaid/root_1.png. Четыре группы воздействия, CH17, CH19, CH21 и CH17+CH19, и одна "
                 "контрольная группа, в каждой заявлено 5-10 образцов, ведут к измерениям и затем к результатам."),
        "sub": "Прежняя схема, перерисована; размеры групп как на ней",
        "tag": "ДИЗАЙН · ПЕРЕРИСОВАНО",
        "t_panel": "ГРУППЫ ВОЗДЕЙСТВИЯ", "c_panel": "КОНТРОЛЬНАЯ ГРУППА",
        "groups": [("CH17", TEAL), ("CH19", VIOLET), ("CH21", AMBER), ("CH17+CH19", BLUE)], "control": "Контроль",
        "n": "5-10 образцов", "meas": "Измерения", "res": "Результаты",
        "foot": "Заявлено на схеме прежнего README; число образцов здесь не сверено с данными.",
    },
}


def groups(lang):
    c = GROUPS[lang]; st = DECL[lang]
    W, H = 1200, 540
    cv = Canvas(W, H, c["title"], c["desc"], c["title"], c["sub"], c["tag"])
    pw = 4 * 200 + 3 * 14 + 32
    cv.panel(24, 96, pw, 124, c["t_panel"], LINE)
    for i, (t, col) in enumerate(c["groups"]):
        cv.box(24 + 16 + i * 214, 132, 200, t, [c["n"]], stroke=col, h=76, center=True)
    cx = 24 + pw + 20
    cv.panel(cx, 96, W - 24 - cx, 124, c["c_panel"], LINE)
    cv.box(cx + 16, 132, W - 24 - cx - 32, c["control"], [c["n"]], stroke=MUTED, h=76, center=True)
    mw = 320; mx = (W - mw) / 2
    cv.box(mx, 300, mw, c["meas"], [], stroke=TEAL, h=60, center=True)
    cv.arrow([(24 + pw / 2, 223), (24 + pw / 2, 262), (mx + 60, 262), (mx + 60, 297)], TEAL, animate=False)
    cv.arrow([((cx + W - 24) / 2, 223), ((cx + W - 24) / 2, 262), (mx + mw - 60, 262), (mx + mw - 60, 297)], TEAL, animate=False)
    cv.box(mx, 400, mw, c["res"], [], stroke=GREEN, h=60, center=True)
    cv.arrow([(W / 2, 363), (W / 2, 397)], TEAL, animate=False)
    foot(cv, [c["foot"]], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


PIPE = {
    "en": {
        "title": "Planned analysis stack",
        "desc": ("Redrawn from the earlier diagram charts/mermaid/root_2.png. A phone camera image is restored with Cellpose3, then an image-type "
                 "decision splits it. Microscopy goes to YeastSAM cell segmentation and morphometry (size, budding index). A macro Petri dish goes "
                 "to OpenCV turbidity and colony measurement, then CIELAB to OD600 and HSV viability. Both branches feed AMiGA growth curves, then "
                 "LME and ANOVA statistics, then results."),
        "sub": "Earlier diagram, redrawn; this is the plan, not the analysed batch",
        "tag": "PLANNED STACK · REDRAWN",
        "phone": ("Phone camera", []), "cp": ("Cellpose3", ["Restore / denoise"]), "dec": ["Image type"],
        "b1": "Microscopy", "b2": "Macro Petri",
        "ys": ("YeastSAM", ["Cell segmentation"]), "mo": ("Morphometry", ["size, budding index"]),
        "cv": ("OpenCV", ["Turbidity + colony"]), "ci": ("CIELAB -> OD600", ["Viability / HSV"]),
        "am": ("AMiGA", ["Growth curves"]), "lme": ("LME + ANOVA", ["Statistics"]), "res": ("Results", []),
        "foot": ["Planned tools as drawn earlier. The analysed batch used cyto2 cell count, texture occupancy and blind LLM scoring (see Analysis flow)."],
    },
    "ru": {
        "title": "Планируемый стек анализа",
        "desc": ("Перерисовано с прежней схемы charts/mermaid/root_2.png. Снимок с камеры телефона восстанавливается Cellpose3, затем выбор типа "
                 "изображения разводит потоки. Микроскопия идёт в сегментацию клеток YeastSAM и морфометрию (размер, индекс почкования). Макро "
                 "чашки Петри идёт в мутность и колонии OpenCV, затем CIELAB в OD600 и жизнеспособность HSV. Обе ветви ведут к кривым роста "
                 "AMiGA, затем к статистике LME и ANOVA и к результатам."),
        "sub": "Прежняя схема, перерисована; это план, а не проанализированная серия",
        "tag": "ПЛАН СТЕКА · ПЕРЕРИСОВАНО",
        "phone": ("Камера телефона", []), "cp": ("Cellpose3", ["Шумоподавление"]), "dec": ["Тип", "изображения"],
        "b1": "Микроскопия", "b2": "Макро чашка",
        "ys": ("YeastSAM", ["Сегментация клеток"]), "mo": ("Морфометрия", ["размер, индекс почкования"]),
        "cv": ("OpenCV", ["Мутность + колонии"]), "ci": ("CIELAB -> OD600", ["Жизнеспособность HSV"]),
        "am": ("AMiGA", ["Кривые роста"]), "lme": ("LME + ANOVA", ["Статистика"]), "res": ("Результаты", []),
        "foot": ["Планируемые инструменты как на схеме. Проанализированная серия использовала счёт клеток cyto2, занятость текстуры и слепую оценку LLM (см. Поток анализа)."],
    },
}


def pipeline(lang):
    c = PIPE[lang]; st = DECL[lang]
    W, H = 1200, 690
    cv = Canvas(W, H, c["title"], c["desc"], c["title"], c["sub"], c["tag"])
    ym = 270

    def b(x, cy, w, key, stroke=TEAL, planned=True):
        t, body = c[key]
        cv.box(x, cy - 58, w, t, body, status=[st] if planned else [], stroke=stroke, h=116, center=True)
    b(24, ym, 130, "phone", MUTED, False)
    b(172, ym, 160, "cp")
    # decision diamond
    dx, dh, dw = 420, 62, 76
    cv.add("<polygon points='%d,%d %d,%d %d,%d %d,%d' fill='%s' stroke='%s' stroke-width='1.6'/>"
           % (dx, ym - dh, dx + dw, ym, dx, ym + dh, dx - dw, ym, PANEL, GOLD))
    for i, ln in enumerate(c["dec"]):
        cv.label(dx, ym + 5 + (i - (len(c["dec"]) - 1) / 2) * 18, ln, 14, INK, "middle", 700, box=2 * dw - 30)
    cv.arrow([(156, ym), (169, ym)], TEAL, animate=False)
    cv.arrow([(334, ym), (dx - dw - 3, ym)], TEAL, animate=False)
    y1, y2 = 170, 370
    cv.label(520, y1 - 66, c["b1"].upper(), 13, GOLD, weight=800, box=170)
    cv.label(520, y2 - 66, c["b2"].upper(), 13, GOLD, weight=800, box=170)
    b(520, y1, 200, "ys"); b(740, y1, 200, "mo")
    b(520, y2, 200, "cv"); b(740, y2, 200, "ci")
    cv.arrow([(dx + dw + 3, ym), (508, ym), (508, y1), (517, y1)], GOLD, animate=False)
    cv.arrow([(508, ym), (508, y2), (517, y2)], GOLD, animate=False)
    cv.arrow([(722, y1), (737, y1)], TEAL, animate=False)
    cv.arrow([(722, y2), (737, y2)], TEAL, animate=False)
    ax, aw = 970, 206
    b(ax, ym, aw, "am")
    cv.arrow([(942, y1), (956, y1), (956, ym - 20), (967, ym - 20)], TEAL, animate=False)
    cv.arrow([(942, y2), (956, y2), (956, ym + 20), (967, ym + 20)], TEAL, animate=False)
    b(ax, 430, aw, "lme")
    cv.arrow([(ax + aw / 2, ym + 61), (ax + aw / 2, 369)], TEAL, animate=False)
    b(ax, 570, aw, "res", GREEN, False)
    cv.arrow([(ax + aw / 2, 491), (ax + aw / 2, 509)], TEAL, animate=False)
    foot(cv, c["foot"], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


PLAN = {
    "en": {
        "title": "Milestone plan as the earlier README drew it",
        "desc": ("Redrawn from the earlier diagram charts/mermaid/root_3.png. Eight steps in order: Mar 28 team assembled and protocol defined; "
                 "Mar 29 emitter upgrade 0.7 W to 60 W / 144 W; Mar 31 microscopy and staining validated; Apr 4 OSF preregistration submitted; "
                 "Apr 7 OSF registration accepted; Q2 2026 irradiation experiments begin; Q3-Q4 2026 data collection and CV analysis; "
                 "Q3-Q4 2026 publication preparation."),
        "sub": "Earlier diagram, redrawn; dates are as that diagram states them",
        "tag": "PLAN · REDRAWN",
        "steps": [("Mar 28", "Team assembled, protocol defined"), ("Mar 29", "Emitter upgrade 0.7W→60W/144W"),
                  ("Mar 31", "Microscopy & staining validated"), ("Apr 4", "OSF preregistration submitted"),
                  ("Apr 7", "OSF registration accepted"), ("Q2 2026", "Irradiation experiments begin"),
                  ("Q3–Q4 2026", "Data collection & CV analysis"), ("Q3–Q4 2026", "Publication preparation")],
        "foot": "Dated record against this plan: the Timeline picture. The first five dates are the earlier README's statements; the last three are plans.",
    },
    "ru": {
        "title": "План вех, как его рисовал прежний README",
        "desc": ("Перерисовано с прежней схемы charts/mermaid/root_3.png. Восемь шагов по порядку: 28 марта команда и протокол; 29 марта "
                 "модернизация излучателя 0,7 Вт до 60 Вт / 144 Вт; 31 марта валидация микроскопии и окрашивания; 4 апреля подана предрегистрация "
                 "OSF; 7 апреля регистрация OSF принята; 2 кв. 2026 начало экспериментов по облучению; 3-4 кв. 2026 сбор данных и CV-анализ; "
                 "3-4 кв. 2026 подготовка публикации."),
        "sub": "Прежняя схема, перерисована; даты как на ней",
        "tag": "ПЛАН · ПЕРЕРИСОВАНО",
        "steps": [("28 марта", "Команда собрана, протокол определён"), ("29 марта", "Модернизация излучателя 0,7 Вт→60 Вт/144 Вт"),
                  ("31 марта", "Микроскопия и окрашивание валидированы"), ("4 апреля", "Предрегистрация OSF подана"),
                  ("7 апреля", "Регистрация OSF принята"), ("2 кв. 2026", "Начало экспериментов по облучению"),
                  ("3–4 кв. 2026", "Сбор данных и CV-анализ"), ("3–4 кв. 2026", "Подготовка публикации")],
        "foot": "Датированная запись против этого плана: картина «Хронология». Первые пять дат — утверждения прежнего README; последние три — планы.",
    },
}


def plan(lang):
    c = PLAN[lang]
    st_d = DECL[lang]; st_p = STATE[lang]["planned"]
    W, H = 1200, 500
    cv = Canvas(W, H, c["title"], c["desc"], c["title"], c["sub"], c["tag"])
    bw, gap, h = 264, 32, 128
    pos = []
    for i, (d, t) in enumerate(c["steps"]):
        x = 24 + (i % 4) * (bw + gap); y = 100 if i < 4 else 290
        cv.box(x, y, bw, d, [t], status=[st_d if i < 5 else st_p], stroke=VIOLET if i < 5 else AMBER, h=h, valign="top")
        pos.append((x, y))
    for i in range(7):
        if i == 3:
            x4 = pos[3][0] + bw / 2; x5 = pos[4][0] + bw / 2
            cv.arrow([(x4, 100 + h + 3), (x4, 259), (x5, 259), (x5, 287)], TEAL, animate=False)
        else:
            (x, y), (x2, _) = pos[i], pos[i + 1]
            cv.arrow([(x + bw + 2, y + h / 2), (x2 - 3, y + h / 2)], TEAL, animate=False)
    foot(cv, [c["foot"]], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


PAT = {
    "en": {
        "title": "Patent connection as the earlier README drew it",
        "desc": ("Redrawn from the earlier diagram charts/mermaid/retry_1.png. The application KZ 2025/1095.1, Fractal Biomedical Hyperbolic Field "
                 "System, status Substantive Exam, leads to the Hyperbolic Field emitter technology, which leads to four studies: this study "
                 "(Saccharomyces cerevisiae), the blood plasma study, the agricultural study and the DAAT crystal study."),
        "sub": "Earlier diagram, redrawn; an application is not a granted patent",
        "tag": "IP · REDRAWN",
        "app": ("KZ 2025/1095.1", ["Fractal Biomedical Hyperbolic Field System", "Substantive Exam"]),
        "tech": ("Hyperbolic Field emitter technology", []),
        "kids": [("This study", ["Saccharomyces cerevisiae"], TEAL), ("Blood plasma study", [], MUTED),
                 ("Agricultural study", [], MUTED), ("DAAT crystal study", [], MUTED)],
        "foot": "As the earlier README states it; the repository holds no filing text and does not name the applicants.",
    },
    "ru": {
        "title": "Связь с патентом, как её рисовал прежний README",
        "desc": ("Перерисовано с прежней схемы charts/mermaid/retry_1.png. Заявка KZ 2025/1095.1, Fractal Biomedical Hyperbolic Field System, "
                 "статус Substantive Exam, ведёт к технологии излучателей гиперболического поля, а она к четырём исследованиям: это исследование "
                 "(Saccharomyces cerevisiae), исследование плазмы, сельскохозяйственное и исследование кристаллов DAAT."),
        "sub": "Прежняя схема, перерисована; заявка — не выданный патент",
        "tag": "ИС · ПЕРЕРИСОВАНО",
        "app": ("KZ 2025/1095.1", ["Fractal Biomedical Hyperbolic Field System", "Substantive Exam"]),
        "tech": ("Технология излучателей гиперболического поля", []),
        "kids": [("Это исследование", ["Saccharomyces cerevisiae"], TEAL), ("Исследование плазмы", [], MUTED),
                 ("Исследование растений", [], MUTED), ("Исследование кристаллов DAAT", [], MUTED)],
        "foot": "Как утверждает прежний README; текста подачи в репозитории нет, заявители не названы.",
    },
}


def patent(lang):
    c = PAT[lang]; st = STATE[lang]["app"]
    W, H = 1200, 510
    cv = Canvas(W, H, c["title"], c["desc"], c["title"], c["sub"], c["tag"])
    aw = 480; ax = (W - aw) / 2
    t, body = c["app"]
    cv.box(ax, 96, aw, t, body, status=[st], stroke=GOLD, h=118, center=True)
    t, body = c["tech"]
    cv.box(ax, 244, aw, t, body, stroke=BLUE, h=56, center=True)
    cv.arrow([(W / 2, 217), (W / 2, 241)], GOLD, animate=False)
    bw, gap = 276, 16
    for i, (t, body, col) in enumerate(c["kids"]):
        x = 24 + i * (bw + gap)
        cv.box(x, 350, bw, t, body, stroke=col, h=70, center=True)
        cv.arrow([(W / 2, 303), (W / 2, 326), (x + bw / 2, 326), (x + bw / 2, 347)], BLUE, animate=False)
    foot(cv, [c["foot"]], H - 14)
    return "\n".join(cv.o + ["</svg>\n"])


# --- icons -----------------------------------------------------------------------------------
def icon(col, body, title):
    return ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 64 64\" width=\"64\" height=\"64\" role=\"img\">\n"
            "<title>%s</title>\n<desc>Navigation icon: %s.</desc>\n<rect x=\"2\" y=\"2\" width=\"60\" height=\"60\" rx=\"12\" fill=\"#101826\" "
            "stroke=\"%s\" stroke-width=\"3\"/>\n<g fill='none' stroke='%s' stroke-width='2.6' stroke-linecap='round' "
            "stroke-linejoin='round'>%s</g>\n</svg>\n" % (title, title, col, col, body))


ICONS = {
    "study": (TEAL, "<circle cx='32' cy='32' r='16'/><circle cx='32' cy='32' r='5'/><path d='M32 12v8M32 44v8M12 32h8M44 32h8'/>", "the study"),
    "design": (GOLD, "<rect x='14' y='14' width='36' height='36' rx='4'/><path d='M14 26h36M26 26v24M20 20h.1M32 20h.1'/>", "hypotheses and design"),
    "data": (BLUE, "<ellipse cx='32' cy='18' rx='16' ry='6'/><path d='M16 18v28c0 3 7 6 16 6s16-3 16-6V18M16 32c0 3 7 6 16 6s16-3 16-6'/>", "data and methods"),
    "results": (GREEN, "<path d='M14 50V14M14 50h38'/><rect x='20' y='32' width='7' height='18'/><rect x='31' y='20' width='7' height='30'/><rect x='42' y='38' width='7' height='12'/>", "results so far"),
    "evidence": (AMBER, "<circle cx='28' cy='28' r='13'/><path d='M38 38l12 12M23 28l4 4 7-8'/>", "evidence"),
    "ecosystem": (BLUE, "<circle cx='32' cy='32' r='6'/><circle cx='32' cy='14' r='4'/><circle cx='48' cy='41' r='4'/>"
                        "<circle cx='16' cy='41' r='4'/><path d='M32 26V18M37 35l8 4M27 35l-8 4'/>", "ecosystem and IP"),
    "navigation": (GREEN, "<path d='M20 14v36M20 22h10M20 34h10M20 46h10'/><rect x='30' y='17' width='20' height='10' rx='2'/>"
                          "<rect x='30' y='29' width='20' height='10' rx='2'/><rect x='30' y='41' width='20' height='10' rx='2'/>", "navigation"),
    "open": (GOLD, "<circle cx='32' cy='32' r='18'/><path d='M26 27a6 6 0 1 1 9 5c-2 1-3 2-3 4M32 43v2'/>", "open questions"),
    "ethics": (AMBER, "<rect x='17' y='29' width='30' height='21' rx='4'/><path d='M23 29v-6a9 9 0 0 1 18 0v6M32 38v6'/>", "ethics and security"),
    "glossary": (VIOLET, "<rect x='16' y='12' width='32' height='40' rx='4'/><path d='M23 22h18M23 30h18M23 38h10'/>", "glossary"),
    "figures": (TEAL, "<rect x='12' y='14' width='40' height='36' rx='4'/><circle cx='24' cy='26' r='4'/><path d='M12 44l12-10 9 7 8-9 11 10'/>", "figures"),
    "archive": (MUTED, "<rect x='12' y='14' width='40' height='11' rx='3'/><path d='M16 25v25h32V25M26 34h12'/>", "archive"),
}


def main():
    for lang in ("en", "ru"):
        write("guide/assets/banner/hero-banner.%s.svg" % lang, banner(lang))
        write("guide/assets/diagrams/programme-map.%s.svg" % lang, programme(lang))
        write("guide/assets/diagrams/density-results.%s.svg" % lang, results(lang))
        write("guide/assets/diagrams/claimed-vs-shown.%s.svg" % lang, claimed(lang))
        write("guide/assets/diagrams/analysis-flow.%s.svg" % lang, flow(lang))
        write("guide/assets/diagrams/timeline.%s.svg" % lang, timeline(lang))
        write("guide/assets/diagrams/ecosystem-flow.%s.svg" % lang, ecosystem(lang))
        write("guide/assets/diagrams/design-groups.%s.svg" % lang, groups(lang))
        write("guide/assets/diagrams/planned-pipeline.%s.svg" % lang, pipeline(lang))
        write("guide/assets/diagrams/plan-milestones.%s.svg" % lang, plan(lang))
        write("guide/assets/diagrams/patent-connection.%s.svg" % lang, patent(lang))
    for name, (col, body, title) in ICONS.items():
        write("guide/assets/icons/%s.svg" % name, icon(col, body, title))


if __name__ == "__main__":
    main()
