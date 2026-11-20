# pachitariu2022cellpose2

Pachitariu, Marius; Stringer, Carsen (2022). Cellpose 2.0: how to train your own model. Nature Methods 19:1634-1641.

- DOI or link: https://doi.org/10.1038/s41592-022-01663-4
- Identity check: DOI resolved in Crossref 2026-11-20; title, authors and year compared ; PubMed/Europe PMC record PMID 36344832
- What was read: Full text (Europe PMC XML and the publisher PDF, 19 pages), keyword search plus the abstract and introduction.
- How the study uses it: tool_named

## What the source says

- "Cellpose 2.0, a new package that includes an ensemble of diverse pretrained models as well as a human-in-the-loop pipeline for rapid prototyping of new custom models" (Abstract, p. 1)
- "models pretrained on the Cellpose dataset can be fine-tuned with only 500-1,000 user-annotated regions of interest (ROI)" (Abstract, p. 1)

## Sample and design

Method paper; benchmarks on the TissueNet and LiveCell datasets. Neither "cyto2" nor "yeast" occurs in the text.

## What the ASRP text says

- `reports/2026-06-09_density-analysis/report_en.md:66`: "Cellpose cyto2 | CNN instance segmentation | Cell count @ 100× | MouseLand, cellpose 3.x".
- `guide/GLOSSARY.md:56`: "\"cyto2\" = its neural-network model trained for cell-body images".

## Verdict: matches

The study describes the tool correctly as a pretrained general model. The paper's own advice points the other way from how the study used it: for images unlike the training set it recommends fine-tuning on a few hundred hand-annotated cells, which the study did not do. The model name cyto2 is documented in the Cellpose software, not in this paper.

## Use for the crowdfunding page

For the repeat: the paper is a citable reason to hand-annotate a few hundred cells from the new chamber photos and fine-tune before the automatic secondary count.
