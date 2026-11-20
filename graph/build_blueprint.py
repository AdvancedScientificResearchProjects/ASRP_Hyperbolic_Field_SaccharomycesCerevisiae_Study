#!/usr/bin/env python3
"""Build the Cytoscape.js / Kumu.io JSON blueprint of the Hyperbolic Field
Saccharomyces cerevisiae Study: the study, its runs, datasets, claims, roles,
devices, ASRP records and the external sources in references/sources.json.

Derived from Banchenko_Dream_Research_Study/graph/build_blueprint.py (same E()/C()
mechanics, same shared TYPE_ICONS vocabulary, same validation block).

Honesty policy: every `fact` node carries `confidence` and `source`. A number
recomputed from the repository's own files is `high` (the arithmetic is verified,
not the imaging). An ASRP reading that an external source does not carry is `low`
and has a `contradicts` edge from the fact that records what the source says.

ID compatibility: ids that already exist in asrp.memory/brain/entities.yaml are
reused unchanged (hyperbolic-saccharomyces, hyperbolic-blood-plasma,
hyperbolic-emitter-generator, channel-17, channel-19-21-taxonomy, fbhfs-patent,
osf, asrp). People appear as roles, never by name; authors of cited works are
named only inside the citation of their own paper.

Output: hyperbolic-saccharomyces_kumu.json (fed to preview.html; also Kumu import).
"""
import json
from pathlib import Path

OUTPUT_NAME = "hyperbolic-saccharomyces_kumu.json"
HERE = Path(__file__).parent
SOURCES_JSON = HERE.parent / "references" / "sources.json"

elements = []
connections = []
_seen_ids = set()

# Shared vocabulary across ASRP graphs: extended (four keys at the end), nothing renamed.
TYPE_ICONS = {
    "legal-entity":      "🏢",
    "person · team":     "👤",
    "person · external": "👥",
    "project":           "🚀",
    "patent":            "📜",
    "publication":       "📄",
    "channel":           "📡",
    "outreach":          "🤝",
    "institution":       "🏛️",
    "event":             "📅",
    "theory-anchor":     "💡",
    "tooling-class":     "🛠️",
    "cluster":           "🎯",
    "funding-source":    "💰",
    "accreditation":     "🏅",
    "fact":              "🧪",
    "phenomenon":        "🛸",
    "source":            "📜",
    "hypothesis":        "🧬",
    # added for study graphs (20 Nov 2026)
    "dataset":           "🗂️",
    "device":            "📟",
    "role":              "🎭",
    "campaign":          "📣",
}

_dup_definitions = []


def E(eid, label, etype, label_ru=None, description_ru=None, **kwargs):
    """Emit one element. De-duplicates by id (first definition wins)."""
    if eid in _seen_ids:
        _dup_definitions.append({"id": eid, "type": etype, "label": label,
                                 "description": kwargs.get("description", "")[:100]})
        return
    _seen_ids.add(eid)
    e = {"id": eid, "label": label, "type": etype, "icon": TYPE_ICONS.get(etype, "•")}
    if label_ru:
        e["labelRu"] = label_ru
    if description_ru:
        e["descriptionRu"] = description_ru
    e.update(kwargs)
    elements.append(e)


def C(efrom, eto, ctype="related-to", direction="directed", **kwargs):
    """Emit one connection."""
    c = {"from": efrom, "to": eto, "type": ctype, "direction": direction}
    c.update(kwargs)
    connections.append(c)


# ════════════════════════════════════════════════════════════════════════════
# 0. ANCHOR NODES: ids shared with asrp.memory/brain/entities.yaml
# ════════════════════════════════════════════════════════════════════════════

E("asrp", "ASRP (Advanced Scientific Research Projects)", "legal-entity",
  label_ru="ASRP (Перспективные научно-исследовательские разработки)",
  description="Independent research group that runs the study and built the emitter.",
  description_ru="Независимая исследовательская группа, которая ведёт исследование и построила излучатель.")

E("hyperbolic-saccharomyces", "Hyperbolic Field Saccharomyces cerevisiae Study", "project",
  label_ru="Исследование дрожжей Saccharomyces cerevisiae в гиперболическом поле",
  description="Pilot of April 2026: baker's yeast in Petri dishes, two liquids, a control and three emitter settings (17, 19, 21), three rounds; 972 eyepiece photos, 398 of them counted. Status in the study's own words: preliminary, not confirmatory.",
  description_ru="Пилот апреля 2026: пекарские дрожжи в чашках Петри, две жидкости, контроль и три настройки излучателя (17, 19, 21), три раунда; 972 фото через окуляр, из них посчитано 398. Статус по словам самого исследования: предварительно, не подтверждено.",
  url="https://github.com/AdvancedScientificResearchProjects/Hyperbolic_Field_SaccharomycesCerevisiae_Study")

E("hyperbolic-blood-plasma", "Hyperbolic Field Blood Plasma Study", "project",
  label_ru="Исследование плазмы крови в гиперболическом поле",
  description="Companion ASRP study. The yeast texts name it as the origin of the meanings of settings 19 and 21.",
  description_ru="Родственное исследование ASRP. Тексты по дрожжам называют его источником смысла настроек 19 и 21.")

E("hyperbolic-emitter-generator", "ASRP emitter (hyperbolic field generator)", "device",
  label_ru="Излучатель ASRP (генератор гиперболического поля)",
  description="As written in the protocol: 6 nodes, 60 W average / 144 W peak, clean sine wave. Internal design not public; the emitted field is not specified in physical units anywhere in the study.",
  description_ru="По протоколу: 6 узлов, 60 Вт средняя / 144 Вт пиковая, чистая синусоида. Внутреннее устройство не опубликовано; излучаемое поле нигде в исследовании не задано в физических единицах.",
  source="reports/experiment_protocol_en.md:87")

E("channel-17", "Emitter setting 17 (CH17)", "channel",
  label_ru="Настройка излучателя 17 (CH17)",
  description="A priori 'unknown effect' (hypothesis H7). The setting behind the +83 % headline.",
  description_ru="Заранее «эффект неизвестен» (гипотеза H7). Настройка, с которой связан заголовок +83 %.",
  source="reports/experiment_protocol_en.md:27")

E("channel-19-21-taxonomy", "Emitter settings 19 and 21 ('time acceleration' / 'time deceleration')", "channel",
  label_ru="Настройки излучателя 19 и 21 («ускорение времени» / «замедление времени»)",
  description="The protocol's names for settings 19 and 21. The study says the numbers are control-software identifiers, not physical frequencies.",
  description_ru="Названия настроек 19 и 21 в протоколе. Исследование говорит, что номера — идентификаторы управляющей программы, а не физические частоты.",
  source="reports/experiment_protocol_en.md:28")

E("fbhfs-patent", "Patent application KZ 2025/1095.1 (Fractal Biomedical Hyperbolic Field System)", "patent",
  label_ru="Патентная заявка KZ 2025/1095.1 (Fractal Biomedical Hyperbolic Field System)",
  description="An application, not a granted patent; applicants are not named in the study repository. Not checked against the register.",
  description_ru="Заявка, а не выданный патент; заявители в репозитории исследования не названы. По реестру не проверялось.",
  source="guide/ECOSYSTEM.md:54", connected=False)

E("osf", "OSF (Open Science Framework)", "institution",
  label_ru="OSF (Open Science Framework)",
  description="Registry that hosts the ASRP registrations cited by the study.",
  description_ru="Реестр, где размещены регистрации ASRP, на которые ссылается исследование.")

E("campaign-yeast-result-that-flipped", "Kickstarter campaign draft 'The Result That Flipped: an open lab notebook'", "campaign",
  label_ru="Черновик кампании Kickstarter «The Result That Flipped: открытый лабораторный журнал»",
  description="Draft of 20 Nov 2026 in the crowdfunding repository (campaigns/yeast-replication-study/). Funds a blinded repeat and a printed notebook. Not launched.",
  description_ru="Черновик от 20 ноября 2026 в репозитории краудфандинга (campaigns/yeast-replication-study/). Финансирует слепое повторение и печатный журнал. Не запущена.",
  status="draft, not launched")

# ════════════════════════════════════════════════════════════════════════════
# 1. FRAGMENTS
# ════════════════════════════════════════════════════════════════════════════

FRAGMENTS = [
    "fragments/study.py",      # runs, datasets, tools, roles, claims
    "fragments/sources.py",    # one node per record of references/sources.json
]

for frag in FRAGMENTS:
    path = HERE / frag
    exec(path.read_text(encoding="utf-8"))

# ════════════════════════════════════════════════════════════════════════════
# 2. BRIDGES between anchors
# ════════════════════════════════════════════════════════════════════════════

C("asrp", "hyperbolic-saccharomyces", ctype="runs")
C("asrp", "hyperbolic-emitter-generator", ctype="built")
C("asrp", "campaign-yeast-result-that-flipped", ctype="runs")
C("hyperbolic-saccharomyces", "hyperbolic-emitter-generator", ctype="uses-device")
C("hyperbolic-emitter-generator", "channel-17", ctype="has-setting")
C("hyperbolic-emitter-generator", "channel-19-21-taxonomy", ctype="has-setting")
C("fbhfs-patent", "hyperbolic-emitter-generator", ctype="covers")
C("hyperbolic-blood-plasma", "channel-19-21-taxonomy", ctype="named-as-origin-of")
C("hyperbolic-saccharomyces", "campaign-yeast-result-that-flipped", ctype="used_by_campaign")
C("osf", "src-asrp2026chrono_osf", ctype="hosts")
C("osf", "src-asrp2026yeast_osf", ctype="hosts")

# ════════════════════════════════════════════════════════════════════════════
# 3. NORMALIZE + VALIDATE
# ════════════════════════════════════════════════════════════════════════════

for el in elements:
    el.setdefault("tags", [el["type"]])

known_ids = {el["id"] for el in elements}
dangling = [(c["from"], c["to"], c["type"]) for c in connections
            if c["from"] not in known_ids or c["to"] not in known_ids]
orphan_ids = known_ids - {c["from"] for c in connections} - {c["to"] for c in connections}

conf_breakdown = {"high": 0, "medium": 0, "low": 0, "unspecified": 0}
for el in elements:
    if el["type"] == "fact":
        c = el.get("confidence", "unspecified")
        conf_breakdown[c if c in conf_breakdown else "unspecified"] += 1

ru_label_count = sum(1 for el in elements if el.get("labelRu"))
ru_desc_count = sum(1 for el in elements if el.get("descriptionRu"))

# ════════════════════════════════════════════════════════════════════════════
# 4. WRITE JSON
# ════════════════════════════════════════════════════════════════════════════

out_path = HERE / OUTPUT_NAME
out_path.write_text(json.dumps({
    "elements": elements,
    "connections": connections,
}, ensure_ascii=False, indent=2))

print(f"Wrote {out_path}")
print(f"  elements   : {len(elements)}")
print(f"  connections: {len(connections)}")
if _dup_definitions:
    print(f"  duplicate-id skips: {len(_dup_definitions)}")
    for d in _dup_definitions:
        print(f"    SKIPPED {d['id']:<22} ({d['type']}): {d['label'][:60]}")
print(f"  orphans    : {len(orphan_ids)}  {'(' + ', '.join(sorted(orphan_ids)) + ')' if orphan_ids else ''}")
print(f"  dangling C : {len(dangling)}")
for f, t, k in dangling[:20]:
    miss = f if f not in known_ids else t
    print(f"    {f} -[{k}]-> {t}   (missing: {miss})")
print("  facts:")
for k, v in conf_breakdown.items():
    print(f"    confidence={k:<12} : {v}")
print(f"  RU label coverage      : {ru_label_count}/{len(elements)} = {100*ru_label_count/len(elements):.1f}%")
print(f"  RU description coverage: {ru_desc_count}/{len(elements)} = {100*ru_desc_count/len(elements):.1f}%")

type_counts = {}
for el in elements:
    type_counts[el["type"]] = type_counts.get(el["type"], 0) + 1
print("  type breakdown:")
for t, n in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"    {t:<22} : {n}")
edge_counts = {}
for c in connections:
    edge_counts[c["type"]] = edge_counts.get(c["type"], 0) + 1
print("  edge breakdown:")
for t, n in sorted(edge_counts.items(), key=lambda x: -x[1]):
    print(f"    {t:<22} : {n}")

assert not dangling, f"{len(dangling)} dangling connection(s)"
assert not orphan_ids, f"{len(orphan_ids)} orphan element(s)"
assert ru_label_count == len(elements) and ru_desc_count == len(elements), "RU coverage below 100 %"
