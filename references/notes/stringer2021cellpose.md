# stringer2021cellpose

Stringer, Carsen; Wang, Tim; Michaelos, Michalis; Pachitariu, Marius (2021). Cellpose: a generalist algorithm for cellular segmentation. Nature Methods 18:100-106.

- DOI or link: https://doi.org/10.1038/s41592-020-01018-x
- Identity check: DOI resolved in Crossref 2026-11-20; title, authors and year compared ; PubMed/Europe PMC record PMID 33318659
- What was read: Abstract (PubMed 33318659) and a keyword search of the bioRxiv preprint PDF (17 pages). The journal version is paywalled.
- How the study uses it: tool_named

## What the source says

- "a generalist, deep learning-based segmentation method called Cellpose, which can precisely segment cells from a wide range of image types and does not require model retraining or parameter adjustments" (Abstract)
- "Cellpose was trained on a new dataset of highly varied images of cells, containing over 70,000 segmented objects." (Abstract)

## Sample and design

Method paper: a neural network trained on a mixed image set, compared with other segmentation methods on held-out images. The word "yeast" does not occur in the preprint text.

## What the ASRP text says

- `reports/2026-06-09_density-analysis/report_en.md:44`: "CV cell count (cyto2) — Cellpose `cyto2` instance segmentation, diameter calibrated to the cells".
- `reports/2026-06-09_density-analysis/report_en.md:187`: "cyto2 misses ~40 % of cells in dense fields, but systematically".

## Verdict: not checked (no full text)

The tool is real and widely used. Nothing in the abstract or the preprint covers yeast photographed through an eyepiece with a phone, so the paper cannot vouch for the counts in this study. The study's own figure "misses ~40 %" has no stated ground truth in the repository (NOT FOUND: who counted by hand, on how many fields).

## Use for the crowdfunding page

The page may say the pilot counts were made by an open-source segmentation program (Cellpose). It should not present the program as validated for these photos.
