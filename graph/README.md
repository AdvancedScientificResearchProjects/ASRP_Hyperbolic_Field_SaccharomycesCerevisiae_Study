# Hyperbolic Field Yeast Study: study, claims and sources graph / Граф исследования, утверждений и источников

**EN:** A bilingual property graph of this study: the study and its three rounds, the datasets, the scoring tools, people as roles (no names), the emitter and its settings, ASRP's own documents, the claims with what supports and what contradicts them, and one node for every record in [`../references/sources.json`](../references/sources.json). Each source node carries its verdict and the path of its reading note. It renders in the browser with Cytoscape.js and imports into Kumu. Same format as the sibling ASRP graphs.

**RU:** Двуязычный граф этого исследования: само исследование и три его раунда, наборы данных, инструменты оценки, люди как роли (без имён), излучатель и его настройки, собственные документы ASRP, утверждения с тем, что их подкрепляет и что им противоречит, и по одному узлу на каждую запись из [`../references/sources.json`](../references/sources.json). Узел источника содержит вердикт и путь к заметке. Отрисовывается в браузере через Cytoscape.js и импортируется в Kumu. Формат тот же, что в соседних графах ASRP.

## Quick start / Быстрый старт

```bash
# from this directory / из этого каталога
python3 build_blueprint.py            # (re)generate the JSON / (пере)собрать JSON
python3 -m http.server 8765
# open http://127.0.0.1:8765/preview.html
```

## Structure / Структура

```
graph/
├── README.md
├── build_blueprint.py                  ← anchors + fragment loader + validation
├── hyperbolic-saccharomyces_kumu.json  ← generated (do not hand-edit) / сгенерирован
├── preview.html                        ← viewer, copied from the sibling graphs; only the JSON name and the title changed
├── libs/                               ← vendored Cytoscape + layouts (copied verbatim)
└── fragments/
    ├── study.py                        ← runs, datasets, tools, roles, hypotheses, claims
    └── sources.py                      ← reads ../references/sources.json, one node per record
```

Size on 20 November 2026: 98 nodes, 178 edges (37 external sources, 3 ASRP records, 20 facts, 4 hypotheses, 4 runs, 6 datasets, 6 roles).

## Ids / Идентификаторы

**EN:** Ids that already exist in the shared memory (`asrp.memory/brain/entities.yaml`) are reused unchanged: `hyperbolic-saccharomyces`, `hyperbolic-blood-plasma`, `hyperbolic-emitter-generator`, `channel-17`, `channel-19-21-taxonomy`, `fbhfs-patent`, `osf`, `asrp`. New ids are prefixed by type: `src-` (source; the rest is the id in `sources.json`), `f-` fact, `hyp-` hypothesis, `ev-` run, `ds-` dataset, `tool-`, `dev-` device, `role-`, `pub-` ASRP document. The campaign node is `campaign-yeast-result-that-flipped`.

**RU:** Идентификаторы, уже существующие в общей памяти (`asrp.memory/brain/entities.yaml`), используются без изменений (список выше). Новые идентификаторы начинаются с типа: `src-` (источник; далее id из `sources.json`), `f-` факт, `hyp-` гипотеза, `ev-` раунд, `ds-` набор данных, `tool-`, `dev-` устройство, `role-`, `pub-` документ ASRP. Узел кампании: `campaign-yeast-result-that-flipped`.

## Edges / Рёбра

| Edge | Meaning |
|---|---|
| `cites` | the study names the work |
| `uses-tool-from`, `uses-method-from` | the study names a tool or method, not its paper |
| `leans-on` | the study or the campaign page uses the idea without naming a source |
| `field-context` | background the study does not cite |
| `sourced-from` | where a fact is written |
| `measured_in` | the dataset or run a number comes from |
| `supports`, `contradicts` | a fact for or against a hypothesis or another fact |
| `replicates` | a repeat of an earlier experiment (the planned repeat of the pilot; Gos 1997 of Grundler 1983) |
| `used_by_campaign` | used on the Kickstarter draft "The Result That Flipped" |

## Honesty policy / Политика добросовестности

**EN:** Every `fact` has `confidence` and `source`. `high` means the number was recomputed from the repository's own files or read directly in the source; it verifies arithmetic and wording, not the imaging. `medium` means reported and not recomputed here. `low` marks a reading the cited source does not carry; each of these has a `contradicts` edge from the fact that records what the source says. Four additions were made to the shared type list (`dataset`, `device`, `role`, `campaign`); the viewer shows them in its default colour.

**RU:** У каждого узла `fact` есть `confidence` и `source`. `high` — число пересчитано из файлов репозитория или прочитано прямо в источнике; проверены арифметика и формулировка, а не съёмка. `medium` — заявлено и здесь не пересчитывалось. `low` — трактовка, которой нет в указанном источнике; к каждому такому узлу идёт ребро `contradicts` от факта с тем, что говорит источник. В общий список типов добавлены четыре (`dataset`, `device`, `role`, `campaign`); просмотрщик показывает их цветом по умолчанию.

## Build invariants / Инварианты сборки

0 orphans, 0 dangling connections, 0 duplicate ids, 100 % `labelRu` and `descriptionRu` coverage. The build fails if any of these breaks.
