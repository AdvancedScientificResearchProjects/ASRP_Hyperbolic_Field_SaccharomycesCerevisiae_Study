# ════════════════════════════════════════════════════════════════════
# SOURCES: one node per record of references/sources.json
# ════════════════════════════════════════════════════════════════════
# exec()'d inside build_blueprint.py: E(), C(), SOURCES_JSON are already defined.
# Node id = "src-" + the id in sources.json. Each node links to its reading note.

_EDGE_BY_RELATION = {
    "cited_explicitly":  "cites",
    "tool_named":        "uses-tool-from",
    "method_named":      "uses-method-from",
    "implied":           "leans-on",
    "context_not_cited": "field-context",
}
_srcs = json.loads(SOURCES_JSON.read_text(encoding="utf-8"))["sources"]
for _s in _srcs:
    _sid = "src-" + _s["id"]
    _first = _s["authors"][0].split(",")[0] if _s["authors"] else "?"
    _short = f'{_first}{" et al." if len(_s["authors"]) > 1 else ""} {_s["year"]}'
    if _s["theme"] == "asrp_primary":
        _short = {"asrp2026chrono_osf": "ASRP OSF registration GWA9E (2026)",
                  "asrp2026yeast_osf": "ASRP OSF registration vxkum (2026, not public)",
                  "asrp2025kzpatent": "Patent application KZ 2025/1095.1 (record)"}[_s["id"]]
    _extra = {}
    if _s.get("doi"):
        _extra["doi"] = _s["doi"]
    if _s.get("note_file"):
        _extra["note"] = "references/" + _s["note_file"]
    _note_en = f' Reading note: references/{_s["note_file"]}' if _s.get("note_file") else " No reading note."
    _note_ru = f' Заметка: references/{_s["note_file"]}' if _s.get("note_file") else " Заметки нет."
    E(_sid, _short, "publication" if _s["theme"] == "asrp_primary" else "source",
      label_ru=_short,
      description=f'{_s["title"]}. {_s["venue"]}. Verdict: {_s["verdict"]}. {_s["why_en"]}' + _note_en,
      description_ru=f'{_s["title"]}. {_s["venue"]}. Вердикт: {_s["verdict"]}. {_s["why_ru"]}' + _note_ru,
      url=_s.get("url"), verdict=_s["verdict"], verified=_s["verified"], relation=_s["relation"],
      theme=_s["theme"], evidence_level=_s["evidence_level"], **_extra)
    C("hyperbolic-saccharomyces", _sid, ctype=_EDGE_BY_RELATION[_s["relation"]])
    if any(ref.startswith("[crowdfunding repo]") for ref in _s.get("cited_in", [])):
        C(_sid, "campaign-yeast-result-that-flipped", ctype="used_by_campaign")

# ── source-to-source and source-to-claim edges ───────────────────────
C("src-gos1997", "src-grundler1983", ctype="replicates")            # repeat with concurrent controls
C("f-gos-null", "src-gos1997", ctype="sourced-from")
C("src-lakens2017", "src-schuirmann1987", ctype="cites")
C("src-lazic2018", "src-hurlbert1984", ctype="cites")
C("src-lazic2010", "src-hurlbert1984", ctype="cites")
C("src-zhao2026yeastsam", "src-zhao2025yeastsam", ctype="journal-version-of")
C("src-asrp2026chrono_osf", "hyperbolic-blood-plasma", ctype="registration-of")
C("src-asrp2026yeast_osf", "hyperbolic-saccharomyces", ctype="registration-of")
C("src-asrp2025kzpatent", "fbhfs-patent", ctype="record-of")
