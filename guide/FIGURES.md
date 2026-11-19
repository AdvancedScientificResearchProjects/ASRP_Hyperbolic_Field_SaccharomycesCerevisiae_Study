**English | [Русский](FIGURES.ru.md)**

[← Hyperbolic Field Saccharomyces Cerevisiae Study](../README.md) · [Guide index](README.md)

<div align="center">

# Figures: everything the repository holds

</div>

Every figure in the repository is reachable from here. The tables have no thumbnails: figure, what it shows, where it comes from. The redrawn schemas replaced the earlier mermaid PNGs on the pages; the original files stay in place and are listed in the first table.

## Redrawn schemas (the original PNG stays)

| Figure | What it shows | Original figure |
|---|---|---|
| [Treatment and control groups](assets/diagrams/design-groups.en.svg) | four treatment groups and one control, 5-10 samples each, to measurements and results | [`charts/mermaid/root_1.png`](../charts/mermaid/root_1.png) |
| [Planned analysis stack](assets/diagrams/planned-pipeline.en.svg) | phone camera, Cellpose3, image-type split, YeastSAM or OpenCV branches, AMiGA, LME + ANOVA | [`charts/mermaid/root_2.png`](../charts/mermaid/root_2.png) |
| [Milestone plan](assets/diagrams/plan-milestones.en.svg) | eight milestones from 28 March to publication preparation, Q3-Q4 2026 | [`charts/mermaid/root_3.png`](../charts/mermaid/root_3.png) |
| [Patent connection](assets/diagrams/patent-connection.en.svg) | application KZ 2025/1095.1 to the emitter technology to four studies (an application, not a granted patent) | [`charts/mermaid/retry_1.png`](../charts/mermaid/retry_1.png) |

## Guide diagrams

| Figure | What it shows | Page |
|---|---|---|
| [Programme map](assets/diagrams/programme-map.en.svg) | registered programme against the one analysed batch | [The study](STUDY.md) |
| [Timeline](assets/diagrams/timeline.en.svg) | the plan lane against what git history and the files record | [The study](STUDY.md) |
| [Analysis flow](assets/diagrams/analysis-flow.en.svg) | journal, mapping, photos, three methods, one report | [Data and methods](DATA.md) |
| [Density results](assets/diagrams/density-results.en.svg) | cell count by channel, cycles 2-3, and the cycle-1 reversal | [Results so far](RESULTS.md) |
| [Claimed versus shown](assets/diagrams/claimed-vs-shown.en.svg) | what the earlier README says against what the data and code show | [Evidence](EVIDENCE.md) |
| [Ecosystem flow](assets/diagrams/ecosystem-flow.en.svg) | what this study depends on and what is only listed | [Ecosystem](ECOSYSTEM.md) |
| [Hero banner](assets/banner/hero-banner.en.svg) | generated illustration, not a screenshot | [README](../README.md) |

## Density report charts

| Figure | What it shows | Source |
|---|---|---|
| [Cell count by channel, 100x](../reports/2026-06-09_density-analysis/charts/chart_counts_100x.png) | mean cells per field for control, CH17, CH19, CH21 (cyto2) | [report](../reports/2026-06-09_density-analysis/report_en.md) |
| [Field effect against control](../reports/2026-06-09_density-analysis/charts/chart_relative_effect.png) | percent change of the cell count against control, 100x | [report](../reports/2026-06-09_density-analysis/report_en.md) |
| [Occupancy by channel and magnification](../reports/2026-06-09_density-analysis/charts/chart_occupancy_by_magnification.png) | texture occupancy (density proxy) at 10x and 100x, 787 magnification-labelled fields | [report](../reports/2026-06-09_density-analysis/report_en.md) |
| [Cell count per experiment cycle](../reports/2026-06-09_density-analysis/charts/chart_counts_by_cycle.png) | the same count split by cycle; shows that cycle 1 disagrees | [report](../reports/2026-06-09_density-analysis/report_en.md) |
| [CV against LLM agreement](../reports/2026-06-09_density-analysis/charts/chart_cv_vs_llm.png) | per-field scatter of cyto2 count against blind LLM estimate, Spearman rho | [report](../reports/2026-06-09_density-analysis/report_en.md) |

## Photographs and working images

| Folder or file | What is there | Page |
|---|---|---|
| [`data/equipment/`](../data/equipment/) | 3 photographs: a yeast sachet (front and back) and a hand sketch of the sensor layout (sample dish, DHT11, ADC) | [Data and methods](DATA.md) |
| [`data/microscopy/`](../data/microscopy/) | 3 photographs: an eyepiece view of yeast concentrate and two photos of a labelled three-field slide (live, plus ethanol, plus ethanol and colour) | [Data and methods](DATA.md) |
| [`data/microscopy/staining/`](../data/microscopy/staining/) | 3 phone-screen captures of stained yeast under the microscope | [Data and methods](DATA.md) |
| [`results/SEMANTICS_objectives_photo.jpg`](../results/SEMANTICS_objectives_photo.jpg) | screenshot of a shop listing of microscope objectives, eyepieces and a phone holder | [Data and methods](DATA.md) |
| [`data/photos/`](../data/photos/) | raw data, not figures: the 972 + 18 sample photographs (990 files) of the analysed experiment, mapped to channels by journal-mapping.csv | [Data and methods](DATA.md) |

The equipment and microscope images are unedited phone shots and screenshots; files whose names contain a person's name are not listed by name here (private persons), open the folder instead.
