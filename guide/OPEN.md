**English | [Русский](OPEN.ru.md)**

[← Hyperbolic Field Saccharomyces Cerevisiae Study](../README.md) · [Guide index](README.md)

<div align="center">

# Open questions

</div>

These are inconsistencies and gaps found inside the repository. None has been fixed: the source files are unchanged and each item names where it sits.

## Inconsistencies inside the repository

| # | What does not agree | Where | What would settle it |
|---|---|---|---|
| 1 | The preregistration file contains an already-obtained result ("found: raises cell count ×1.6–1.8") and was first committed on 2026-06-10, after the data (2026-04-19 to 2026-04-22) and the density report; the earlier README of 2026-04-09 listed fermentation outcomes as primary, the file lists cell count, occupancy and LLM scoring | `OSF_PREREGISTRATION.md:33` | the frozen April text of the OSF page |
| 2 | The README says the effect is "reproducible"; the report says "not yet a reproducible effect" | earlier README `README.md:402` against `reports/2026-06-09_density-analysis/report_en.md` (Conclusion) | owner decision on the wording; the report is the stricter source |
| 3 | Stain strength is written as "0.1% MB + 0.01% sodium citrate" in the metrics table and as "0.1 mg/mL in 2% sodium citrate dihydrate" in the protocol | `README.md:100` against `README.md:231` and `reports/experiment_protocol_en.md` | the lab's actual recipe |
| 4 | The journal note speaks of "acceleration of the 19th frequency" (in Russian) while the README states the channel numbers are control-software identifiers, not physical frequencies | `data/photos/journal-note.txt:5` against `README.md:681` | a statement from the hardware lead |
| 5 | The combined group CH17+CH19 is in the README (H9 to H11, the design table) but not in the OSF file conditions, the journal mapping or the data; N = 25–50 matches five groups, the data has four | `README.md:187` | whether that arm was run |
| 6 | `data/README.md` says 198 photos and 180 HEIC and that it does "NOT attribute photos", which contradicts `data/photos/README.md` (<!--n:images_total-->990<!--/n--> images) and the journal mapping | `data/README.md:44` | updating the data hub |
| 7 | The pilot blind runs (24 images, three "analysts") presume a methylene-blue-type stain; the researcher later confirmed there was no stain | `results/llm_blind/blind_run_2.json:13` | marking the pilots as superseded |
| 8 | The OSF registration title ("... Cell Dynamics and Morphology") differs from the README subtitle ("... Fermentation Dynamics") | `OSF_PREREGISTRATION.md` against `README.md:1` | which title is the registered one |
| 9 | The README gives a hypothesis precedent for CH17 as "found in blue whale research"; nothing in the repository sources it | `README.md:204` | a citation |
| 10 | "Randomized double-blind" is stated; blinding is applied at scoring only, channel attribution comes from a handwritten journal, and there is no randomisation record | `README.md:187`, `scripts/llm_analysis/prompts.py` | the randomisation log, if it exists |

## Things that need access outside the repository

- The OSF page itself (what exactly was registered on 2026-04-04, and the registration DOI, still "TBD - pending").
- The status of the Kazakhstan application KZ 2025/1095.1 and its applicants; this repository states only the number and "Substantive Exam".
- The handwritten lab journal (three pages): the repository holds a transcription at 99.5% coverage, not the originals.
- The raw HEIC originals: they are in `data/photos/original/` and were not opened for this page.

## Open scientific steps

- **At least 5 cycles** under one imaging protocol, to confirm or drop the density signal; cycle 1 currently reverses the order.
- **Time-lapse and per-cell morphometry** to test the CH19 division-rate hypothesis; a single snapshot cannot show it.
- **Staining and OD600** (viability, doubling time) and the registered fermentation outcomes: nothing exists yet.
- **A scale bar and a common imaging protocol**, so that densities become absolute and imaging confounds (focus, dilution, session) can be excluded.
- **The full CV pipeline scripts** listed in the roadmap.

## Notes on reading the evidence

- The headline numbers were recomputed from the CSV files: this verifies the arithmetic and the join, not the imaging.
- The group CH19 reading ("count equals control") is the *expected* outcome of the protocol, not a null; its test is morphology, which does not support the hypothesis on this batch.
- The earlier README names eight contributors; two are laboratory assistants and are not named on these pages.
