**English | [Русский](GLOSSARY.ru.md)**

[← Hyperbolic Field Saccharomyces Cerevisiae Study](../README.md) · [Guide index](README.md)

<div align="center">

# Glossary

</div>

Plain-language reference for the technical terms used in the pages and the linked reports.

## Quick reader's guide

*A plain-language key to the terms used in the results.*

- **n.s.** — not significant: the difference is too small to prove it is real.
- **p-value** — probability the result is due to chance; p < 0.05 = less than 5% chance (e.g. 6e-5 = 0.00006).
- **ρ (rho)** — method-agreement score from 0 to 1; ρ = 0.88 = very strong agreement.
- **pseudoreplication** — photos from the same dish count as 1 replicate, not many; this is why the p-values are descriptive only.
- **N=2 cycles** — the count result rests on only 2 independent experiment runs.
- **descriptive** — p-values shown for scale and direction only, not as formal proof.
- **sign-flip** — cycle 1 showed the opposite ordering from cycles 2–3.
- **endpoint** — a single-moment photo, not a time-series film of the cells.
- **CH0/CH17/CH19/CH21** — emitter settings; CH0 = emitter off (control), CH17/19/21 = three field configurations.
- **occupancy** — fraction of the image area covered by cells (0 = empty, 1 = full).

## Terms

### Statistics

| **Term** | Meaning |
|---|---|
| **n.s.** | Not statistically significant — the difference between groups is too small to rule out chance |
| **p / p-value** | A number (0–1) measuring the probability that an observed difference arose by chance. p < 0.05 = less than 5% chance it is random. Scientific notation: 6e-5 = 0.00006 (smaller = less likely to be chance) |
| **descriptive p-value** | The p-value is shown for scale/direction only, not as a formal significance test, because the independent-samples assumption is violated (see pseudoreplication) |
| **pseudoreplication** | Treating multiple photos from the same biological dish as independent observations; it inflates sample size and makes p-values artificially small. True replicates here are the 3 experiment cycles, not individual photos |
| **N=2 cycles** | The cell-count result rests on only 2 independent experiment repetitions; too few to test statistically at the cycle level |
| **ρ (rho) / Spearman correlation** | A number (−1 to +1) measuring how consistently two methods rank the same fields. ρ = 0.88 = very strong agreement |
| **Kruskal–Wallis** | A statistical test comparing 3+ groups without assuming a bell-curve distribution |
| **Δ (delta)** | Difference between two values (e.g. Δ ecc = 0.016 means eccentricity differs by 0.016 units) |
| **LME (Linear Mixed-Effects Model)** | A statistical model for repeated-measurement data; separates treatment effects from random sample variation |
| **Tukey HSD** | A post-hoc test comparing every pair of groups after an overall difference is found, controlling for false positives |
| **Bonferroni** | A correction for running many statistical tests at once; divides the significance threshold by the number of tests |
| **Cohen's d** | Effect size: how many standard deviations apart two group means are (d ≥ 0.8 large, ≈0.5 medium, ≈0.2 small) |
| **partial eta squared** | Effect size: fraction of total data variation explained by the treatment (0–1; larger = stronger) |
| **AUC (Area Under the Curve)** | The total area under a time-series curve; measures total fermentation activity over the whole period |
| **sign-flip** | The direction of an effect reversed between conditions (cycle 1 showed the opposite ordering from cycles 2–3) |
| **a priori** | Known or predicted before the experiment; CH17 was "a priori unknown" = no prediction was made for it |
| **R²** | R-squared: how well a model fits the data (0–1). R² = 0.81 = 81% of variation explained |

### Computer vision and imaging

| **Term** | Meaning |
|---|---|
| **Cellpose / cyto2** | Open-source AI software that automatically finds and outlines individual cells in microscopy photos; "cyto2" = its neural-network model trained for cell-body images |
| **segmentation / instance segmentation** | Identifying which image pixels belong to each cell and drawing its boundary; "instance" = each cell outlined separately |
| **CNN (Convolutional Neural Network)** | The type of AI used to recognize cells, trained from many example images |
| **occupancy / texture occupancy** | Fraction of image area covered by cells (0 = empty, 1 = full), measured from pixel-brightness patterns without outlining each cell |
| **Otsu** | An algorithm that automatically finds the brightness threshold separating cell pixels from background |
| **Canny** | An edge-detection algorithm that finds cell outlines; used here to count edges as a density proxy |
| **field (microscopy field / FOV)** | One photograph taken through the microscope (990 fields = 990 photos) |
| **eccentricity** | Cell-shape metric (0–1): 0 = perfect circle, 1 = line; higher = more elongated |
| **aspect ratio (major:minor axis)** | Longest diameter divided by shortest diameter of an ellipse fitted to the cell; 1.0 = circle, larger = more elongated |
| **solidity** | Shape metric (0–1) for how "compact" the cell boundary is; a budding cell has lower solidity |
| **blob detection** | Finding cells as rounded filled regions, without neural-network segmentation |
| **downscale** | Reducing image pixel count before processing; standardizes cell size in pixels and speeds analysis |
| **100× / 10× magnification** | Objects appear 100× or 10× larger than real size; at 100× individual cells (~5–8 µm) are visible, at 10× only population density |
| **HEIC** | Apple iPhone photo format; here, photos taken through the microscope eyepiece with a smartphone |
| **YeastSAM** | AI segmentation tool specialized for budding-yeast microscopy; more accurate than Cellpose on budding cells |
| **AMiGA** | Software for fitting microbial growth curves (growth rate, lag phase) using a Gaussian Process |
| **CIELAB / b\* channel** | A color-description system; the b\* channel measures blue-yellow shift, used to detect methylene-blue dye uptake |

### AI and LLM method

| **Term** | Meaning |
|---|---|
| **blind LLM scoring** | An AI model (Claude Opus 4.8) scored each photo without knowing which channel it came from — preventing bias; "blind" = scorer does not know the group |
| **group-agnostic** | The method does not see channel labels until the final grouping step |
| **diagnostic vs consistent** | "Consistent with" = compatible with the hypothesis but not proof; "diagnostic" = uniquely identifies one cause, ruling out others |

### Biology

| **Term** | Meaning |
|---|---|
| **budding index / budding fraction** | Percentage of yeast cells actively dividing at the moment of imaging, seen as a small "bud" on the mother cell; higher = more division |
| **Whi5 / G1-sizer** | Whi5 is a protein that brakes division; the G1-sizer lets cells "measure" their size before dividing. Cells passing the "Start" point while small make small daughters |
| **Start (cell cycle)** | The molecular decision point after which a yeast cell is committed to dividing |
| **G2/M arrest** | Cells stuck just before the division step; they look ready to divide (may show buds) but never finish — hard to tell from fast division in one photo |
| **time-lapse microscopy** | Filming the same cells repeatedly over hours; directly measures division rate, unlike a single snapshot |
| **OD600 / doubling time** | OD600 = cloudiness of the liquid at 600 nm light; as cells multiply it gets cloudier. Doubling time = time for the population to double; faster division = shorter doubling time |
| **stationary phase** | When nutrients run out, yeast stop dividing and rest; such cells are smaller and could mimic the predicted CH19 shrinkage |
| **quiescent cells** | Individual non-dividing, dormant cells; smaller than actively growing cells |
| **viability / vital stain** | A dye that distinguishes live from dead cells; methylene blue stains dead cells blue, live cells stay clear. NOT used in the first analysed batch |
| **kinetic effect** | An effect on the speed/rate of cell division (not on the number of cells) |
| **morphological effect** | An effect on the physical shape or size of cells |
| **morphometry** | Quantitative measurement of cell shape, size, and geometry (area, elongation, roundness) |
| **endpoint / static endpoint** | A single measurement taken at one moment (not a time-series); shows only the cells' state at the photograph, not how they changed |
| **confound / imaging confound** | An uncontrolled factor other than the treatment that could explain a difference (e.g. different focus, dilution, or lighting between channels) |

### Study design

| **Term** | Meaning |
|---|---|
| **CH0 / CH17 / CH19 / CH21 (channels)** | Specific configurations of the emitter hardware; CH0 = emitter off (control), CH17/19/21 = three different settings. The numbers are control-software identifiers, not physical frequencies |
| **cycles 001 / 002 / 003** | Three independent repetitions of the whole experiment (biological replicates), each with freshly prepared yeast |
| **biological replicate** | An independent repetition with freshly prepared samples (distinct from re-measuring the same sample) |
| **preregistration / OSF** | A public, time-stamped declaration of hypotheses and analysis plan made before data collection; prevents adjusting the analysis to fit results. OSF (Open Science Framework) is the free public registry that timestamps it |
| **double-blind** | Neither the analyst nor the scoring system (LLM) knows which sample belongs to which condition during scoring |
