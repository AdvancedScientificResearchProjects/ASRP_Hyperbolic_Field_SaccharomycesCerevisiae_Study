**English | [Русский](README.ru.md)**

<div align="center">

# References

![Sources](https://img.shields.io/badge/Sources-40-1f6feb?style=flat-square)
![Verified](https://img.shields.io/badge/Verified-38-2ea043?style=flat-square)
![Reading notes](https://img.shields.io/badge/Reading%20notes-26-8250df?style=flat-square)
![OA PDFs fetched](https://img.shields.io/badge/OA%20PDFs%20fetched-9-8250df?style=flat-square)

</div>

This folder holds the machine-readable literature base for the Hyperbolic Field Saccharomyces cerevisiae Study. It was built on 20 November 2026. Before that date the study's texts named four papers (in one paragraph of the density report) and gave no reference list.

| File | Purpose |
|---|---|
| `sources.json` | One record per source: `id`, `title`, `authors`, `year`, `doi`, `url`, `theme`, `evidence_level` (L1 ASRP model / L2 contested / L3 mainstream), `open_access`, `oa_pdf_url` (legal open-access copies only), `verified`, `note`, plus short `why_en`/`why_ru` relevance notes. Four fields were added for this study: `relation`, `cited_in`, `verdict`, `note_file` (explained in the file's `extra_fields`). |
| `bibliography.bib` | BibTeX for every verified entry. Keys match the `id` values in `sources.json`. |
| `notes/<id>.md` | Reading notes: what the source says (short quotes with page or section), sample and design, what the ASRP text says about it (`path:line`), a verdict, and whether it can be used on the crowdfunding page. |
| `pdf/` | **Not tracked by git.** Created by `scripts/fetch_literature.py`, which downloads open-access PDFs and writes `pdf/MANIFEST.json` (SHA-256, size, source URL). |

## How a source got into the list

The `relation` field says how the study depends on each source.

| `relation` | Meaning | Count |
|---|---|---|
| `cited_explicitly` | the study names the work | 7 |
| `tool_named` | the study names a software tool, not its paper | 6 |
| `method_named` | the study names a statistical or image method, not its paper | 6 |
| `implied` | the study or the campaign page leans on the idea and names no source | 14 |
| `context_not_cited` | background on electromagnetic fields and yeast that the study does not cite | 7 |

The seven `context_not_cited` records are not evidence for the study and none of them tests the ASRP emitter. They are listed because the study's texts contain no literature on field effects in yeast at all.

## Verdicts

| Verdict | Count | Sources |
|---|---|---|
| `matches` | 8 | kato2021, pachitariu2022cellpose2, midani2021amiga, lazic2018, lazic2010, holman2015, nosek2018, lakens2017 |
| `overstated` | 3 | schmidtglenewinkel2014, stringer2025cellpose3, august2019 |
| `misreported` | 1 | asrp2026chrono_osf |
| `not checked (no full text)` | 21 | paywalled papers, records without an abstract, and the two ASRP records that cannot be read from outside |
| `n/a (context, no ASRP claim)` | 7 | the field-effect background records |

## Rules

- **Never commit PDFs.** `references/pdf/` is in `.gitignore`. Paywalled papers are cited by DOI only.
- **Never add a reference from memory.** Resolve the DOI (Crossref) or PMID (PubMed) and compare the title, authors and year before adding it. If a source cannot be confirmed, set `verified: false` and explain why in `note`.
- **When adding a source**, edit `sources.json`, then add the matching BibTeX entry and, if the source carries a claim, a note in `notes/`.
- Quotes from external sources stay short (a sentence or two). Numbers that are not in a source are written as NOT FOUND.

## Fetching open-access PDFs

```bash
python3 scripts/fetch_literature.py --dry-run   # list what would be downloaded
python3 scripts/fetch_literature.py             # download into references/pdf/
python3 scripts/fetch_literature.py --only kato2021 --force
```

The script uses only the Python standard library. It sends the User-Agent `ASRP-literature-fetcher/1.0`, retries with backoff and pauses between requests. It keeps a file only if the response really is a PDF. If Python cannot verify TLS certificates on the machine, it repeats the request through the system `curl`, with certificate checks on.

On 20 November 2026 it fetched 9 of 17 listed PDFs. The other 8 are served behind an access check (Europe PMC's PDF renderer and bioRxiv); those PDFs have to be downloaded by a person from the listed URL. For four of the eight (`kato2021`, `august2019`, `midani2021amiga`, `lakens2017`) the text was read instead through Europe PMC's open full-text XML service, so their notes give sections, not page numbers. `nosek2018`, `wernerwashburne1993`, `gray2004` and `zhao2025yeastsam` were read as abstracts only.

---

<div align="center">

Last Updated: 20 November 2026 · Standard: UNIFIED_ASRP_STANDARD v6.1

</div>
