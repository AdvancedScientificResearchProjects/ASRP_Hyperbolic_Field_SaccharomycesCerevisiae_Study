# stringer2025cellpose3

Stringer, Carsen; Pachitariu, Marius (2025). Cellpose3: one-click image restoration for improved cellular segmentation. Nature Methods 22:592-599.

- DOI or link: https://doi.org/10.1038/s41592-025-02595-5
- Identity check: DOI resolved in Crossref 2026-11-20; title, authors and year compared ; PubMed/Europe PMC record PMID 39939718
- What was read: Full text (publisher PDF, 26 pages), keyword search and the passages on the one-click model.
- How the study uses it: tool_named

## What the source says

- "We refer to this as a 'one-click' model, as it can be run without specifying the degradation or dataset type." (p. 6)
- The restoration network is trained "by running the denoised images through the Cellpose 'cyto2' segmentation network" (p. 2).

## Sample and design

Method paper; restoration of noisy, blurred and undersampled images, tested on the Cellpose, nuclei and seven other datasets (yeast datasets among the training sets).

## What the ASRP text says

- `guide/DATA.md:43`: "Image denoising | Cellpose3 one-click restore | Handles phone-through-eyepiece noise, blur, vignetting" (planned, not run).

## Verdict: overstated

The paper shows restoration of synthetic noise, blur and downsampling on research-microscope images. It does not test phone-through-eyepiece photos or vignetting, so "handles" is a hope, not a finding. The line sits in a table the study itself marks as planned, not run.

## Use for the crowdfunding page

Not for the campaign page.
