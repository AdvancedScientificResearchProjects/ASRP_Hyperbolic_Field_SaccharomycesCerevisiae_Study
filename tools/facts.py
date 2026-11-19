#!/usr/bin/env python3
"""Every number on the showcase pages and diagrams is computed here, from the repository itself.

    python3 tools/facts.py            # print all facts

`facts()` returns a flat dict of strings. tools/build_facts.py writes them into the pages
(markers `<!--n:key-->value<!--/n-->`); tools/build_visuals.py draws the diagrams from the same dict.
Nothing is copied from older prose: image counts come from data/photos/manifest.json, the per-channel
cell counts and the cycle-1 occupancy are recomputed from results/cv_analysis/*.csv joined to the
handwritten-journal mapping data/photos/journal-mapping.csv, hypotheses are counted in the archived
README. The build fails when a source a number depends on has changed shape. Standard library only.
"""
import csv
import glob
import json
import os
import re
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AS_OF = "2026-11-19"  # date of this showcase restructuring
CHANNELS = ("0", "17", "19", "21")


def p(*a):
    return os.path.join(ROOT, *a)


def read(rel):
    return open(p(rel), encoding="utf-8").read()


def md_files(*parts):
    out = []
    for dp, dn, fn in os.walk(p(*parts)):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
        out += [os.path.join(dp, f) for f in fn if f.endswith(".md")]
    return sorted(out)


def must(pattern, text, what, flags=0):
    m = re.search(pattern, text, flags)
    if not m:
        raise SystemExit("facts.py: cannot find %s (pattern %r) - the source changed" % (what, pattern))
    return m


def ru_plural(n, one, few, many):
    n = abs(int(n))
    if n % 10 == 1 and n % 100 != 11:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


def pct(a, b):
    """Signed percent change of a against b, rounded, with a real minus sign."""
    v = round((a / b - 1) * 100)
    return ("+%d" if v >= 0 else "−%d") % abs(v)


def img_no(name):
    return int(re.match(r"IMG_(\d+)", name).group(1))


def csv_rows(rel):
    with open(p(rel), encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def facts():
    f = {"as_of": AS_OF}

    # --- image set (manifest) ---------------------------------------------------------------
    man = json.load(open(p("data", "photos", "manifest.json"), encoding="utf-8"))
    f["images_total"] = str(len(man))
    f["images_heic"] = str(sum(1 for m in man if m["format"] == "HEIC"))
    f["images_png"] = str(sum(1 for m in man if m["format"] == "PNG"))
    dated = [m for m in man if m.get("date_observed")]
    f["images_dated"] = str(len(dated))
    f["images_undated"] = str(len(man) - len(dated))
    dates = sorted({m["date_observed"] for m in dated})
    f["date_first"], f["date_last"] = dates[0], dates[-1]
    f["jpg_previews"] = str(len(glob.glob(p("data", "photos", "jpg", "*.jpg"))))

    # --- journal mapping ----------------------------------------------------------------------
    mp = csv_rows("data/photos/journal-mapping.csv")
    f["mapping_rows"] = str(len(mp))
    f["mapping_images"] = str(sum(int(r["img_count"]) for r in mp))
    sets = {}
    for r in mp:
        sets[r["set"]] = sets.get(r["set"], 0) + 1
    f["cycles"] = str(len(sets))
    f["set1_rows"], f["set2_rows"], f["set3_rows"] = (str(sets[k]) for k in ("1", "2", "3"))
    f["mapping_blank_rows"] = str(sum(1 for r in mp if r["img_count"] == "0"))
    conf = {}
    for r in mp:
        conf[r["confidence"]] = conf.get(r["confidence"], 0) + 1
    f["conf_high"], f["conf_med"], f["conf_low"] = (str(conf.get(k, 0)) for k in ("high", "med", "low"))

    def group_of(n):
        for r in mp:
            if int(r["img_count"]) and int(r["img_start"]) <= n <= int(r["img_end"]):
                return r
        return None

    # --- cell counts, 100x, cycles 2-3 (cyto2) ------------------------------------------------
    wc = csv_rows("results/cv_analysis/white_counts.csv")
    f["count_fields"] = str(len(wc))
    by_ch, by_cyc = {}, {}
    for r in wc:
        g = group_of(img_no(r["file"]))
        if not g:
            continue
        by_ch.setdefault(g["channel"], []).append(float(r["cell_count"]))
        by_cyc.setdefault((g["set"], g["channel"]), []).append(float(r["cell_count"]))
    mean = {c: statistics.mean(by_ch[c]) for c in CHANNELS}
    for c in CHANNELS:
        f["n_ch" + c] = str(len(by_ch[c]))
        f["mean_ch" + c] = str(round(mean[c]))
    for c in ("17", "19", "21"):
        f["pct_ch" + c] = pct(mean[c], mean["0"])
    f["ratio_ch17"] = "%.1f" % (mean["17"] / mean["0"])
    for cyc in ("2", "3"):
        for c in CHANNELS:
            f["cyc%s_ch%s" % (cyc, c)] = str(round(statistics.mean(by_cyc[(cyc, c)])))
    # ranks per cycle: CH17 first, CH21 last in both cycles with counts
    for cyc in ("2", "3"):
        order = sorted(CHANNELS, key=lambda c: -statistics.mean(by_cyc[(cyc, c)]))
        f["rank_first_c%s" % cyc], f["rank_last_c%s" % cyc] = "CH" + order[0], "CH" + order[-1]

    # --- occupancy, cycle 1 and by magnification ------------------------------------------------
    occ = csv_rows("results/cv_analysis/occupancy_full.csv")
    f["occupancy_fields"] = str(len(occ))
    c1 = {}
    for r in occ:
        g = group_of(img_no(r["file"]))
        if g and g["set"] == "1":
            c1.setdefault(g["channel"], []).append(float(r["texture_occupancy"]))
    m1 = {c: statistics.mean(c1[c]) for c in CHANNELS}
    for c in CHANNELS:
        f["occ1_ch" + c] = "%.3f" % m1[c]
    f["occ1_pct_ch21"] = pct(m1["21"], m1["0"])
    f["occ1_pct_ch17"] = pct(m1["17"], m1["0"])
    f["occ1_first"] = "CH" + max(CHANNELS, key=lambda c: m1[c])

    # --- LLM scoring ------------------------------------------------------------------------
    llm = json.load(open(p("results", "llm_full", "llm_full.json"), encoding="utf-8"))
    recs = llm if isinstance(llm, list) else llm.get("records") or llm.get("results") or []
    f["llm_fields"] = str(len(recs)) if recs else "?"

    # --- hypotheses, outcomes, documents --------------------------------------------------------
    arch = read("archive/README_2026-11-19_pre-showcase.md")
    f["hypotheses"] = str(len(re.findall(r"^### H\d+:", arch, re.M)))
    f["indices"] = str(len(re.findall(r"^\| \*\*F[ADP]I ", arch, re.M)))
    f["team_listed"] = str(len(re.findall(r"^\| \*\*[^|]+\*\* \| [^|]+ \| [^|]+ \|$", arch.split("## RESEARCH TEAM")[1].split("## SECURITY")[0], re.M)))
    f["eco_repos"] = str(len(re.findall(r"github\.com/AdvancedScientificResearchProjects/", arch.split("### Related Research Repositories")[1].split("### Patent Portfolio")[0])))
    f["portfolio_patents"] = str(len(set(re.findall(r"github\.com/denisbanchenko/Kazpatent_[\w-]+", arch))))
    f["report_pages"] = str(len(glob.glob(p("reports", "*", "report_en.md"))))
    f["charts_report"] = str(len(glob.glob(p("reports", "*", "charts", "*.png"))))
    f["charts_mermaid"] = str(len(glob.glob(p("charts", "mermaid", "*.png"))))
    f["scripts_py"] = str(len([x for x in glob.glob(p("scripts", "**", "*.py"), recursive=True) if not x.endswith("__init__.py")]))
    f["blind_runs"] = str(len(glob.glob(p("results", "llm_blind", "blind_run_*.json"))))
    f["placeholder_bins"] = str(len(glob.glob(p("data", "control-*"))) + len(glob.glob(p("data", "sample-*"))))
    f["md_content_pages"] = str(len([x for x in md_files() if "/guide/" not in x and "/archive/" not in x
                                     and not os.path.basename(x).startswith("README")]) + 3)  # +3: root/en/ru READMEs
    return f


def badges(lang, F):
    """Computed shields.io badges for the README header (the URL carries the numbers)."""
    from urllib.parse import quote
    names = {"en": ("images analysed", "experiment cycles", "CH17 cell count"),
             "ru": ("снимков", "циклов эксперимента", "CH17 счёт клеток")}[lang]
    items = [(names[0], F["images_total"], "1f6feb", "Images"), (names[1], F["cycles"], "8957e5", "Cycles"),
             (names[2], F["pct_ch17"].replace("−", "-") + "%_(prelim.)", "f59e0b", "CH17")]
    return "\n".join("![%s](https://img.shields.io/badge/%s-%s-%s?style=flat-square)"
                     % (alt, quote(label.replace("-", "--").replace(" ", "_"), safe="_-"),
                        quote(msg.replace("-", "--").replace(" ", "_"), safe="_-%.()+"), col)
                     for label, msg, col, alt in items)


if __name__ == "__main__":
    for k, v in facts().items():
        print("%-28s %s" % (k, v))
