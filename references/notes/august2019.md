# august2019

August, Elias; Sabani, Besmira; Memeti, Nurdzane (2019). Using Colour Images for Online Yeast Growth Estimation. Sensors 19:894.

- DOI or link: https://doi.org/10.3390/s19040894
- Identity check: DOI resolved in Crossref 2026-11-20; title, authors and year compared ; PubMed/Europe PMC record PMID 30795509
- What was read: Full text (Europe PMC open-access XML, PMC6412256), Methods and Results. The PDF could not be fetched automatically.
- How the study uses it: implied

## What the source says

- "When employing leave-one-out cross validation ... the mean of the residuals is roughly 0.01, and R2=0.81" (section 3.3).
- "R2=0.80 for images from location 1 only and R2=0.89 for those from location 2 only" (section 3.3).
- "We use two different smartphones, iPhone 7 and iPhone 6S" (section 2).

## Sample and design

18 shake-flask cultivations of S. cerevisiae, more than 340 paired measurements (photo of the flask plus a spectrophotometer OD reading every 30 minutes for 9.5 h); a log-log regression from CIELAB colour values to OD, leave-one-experiment-out validation.

## What the ASRP text says

- `guide/DATA.md:46`: "Turbidity (OD600 proxy) | CIELAB regression (OpenCV) | R²=0.81 on S. cerevisiae with iPhone" (planned, not run).

## Verdict: overstated

The number, the organism and the phone all match this paper, which is why it is taken to be the unnamed source (an inference: the study cites nothing). But the paper photographs whole shake flasks of growing culture in rich medium and calibrates every model against a spectrophotometer. It says nothing about Petri dishes or microscope fields, and without a spectrophotometer there is nothing to calibrate against. As a rationale for a turbidity proxy in this study the line promises more than the source gives.

## Use for the crowdfunding page

Not for the campaign page. For the repeat it argues for the simpler option already in the plan: if a spectrophotometer exists, read OD600 directly.
