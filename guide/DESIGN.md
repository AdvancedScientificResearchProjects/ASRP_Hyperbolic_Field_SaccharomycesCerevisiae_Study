**English | [Русский](DESIGN.ru.md)**

[← Hyperbolic Field Saccharomyces Cerevisiae Study](../README.md) · [Guide index](README.md)

<div align="center">

# Hypotheses and design

</div>

This page is the **registered plan**: what the study set out to test and how. It is not a record of what was measured; for that see [Results so far](RESULTS.md) and [Evidence](EVIDENCE.md). The in-repository copy of the preregistration is itself disputed (see [Open questions](OPEN.md)).

## Key metrics

| Parameter | Value |
|---|---|
| **Model organism** | *Saccharomyces cerevisiae* (Dr. Oetker dry yeast, 7g, batch L329 M68) |
| **Study type** | Randomized Controlled Experiment, double-blind (as registered) |
| **Irradiation duration** | 80 minutes (1h 20m) per session |
| **Channels** | CH17, CH19, CH21, CH17+CH19 |
| **Samples per condition** | 5-10 independent samples |
| **Total sample size** | N = 25-50 |
| **Blinding** | Double-blind: coded identifiers, researchers unaware of conditions during analysis |
| **Randomization** | Simple random assignment via RNG |
| **Emitter power** | 60W avg / 144W peak (6 nodes, clean sine wave) |
| **Temperature** | 10 C (basement) / 18 C (lab) |
| **Viability assay** | Methylene blue staining (0.1% MB + 0.01% sodium citrate); see the note on the stain strength below |
| **Logging interval** | 1 measurement per minute (~80 per session) |
| **OSF registration** | [osf.io/vxkum](https://osf.io/vxkum) (Apr 4, 2026) |
| **Patent** | Application KZ 2025/1095.1, Fractal Biomedical Hyperbolic Field System (an application, not a granted patent) |

## Hypotheses

*All hypotheses are stated as preregistered on OSF ([osf.io/vxkum](https://osf.io/vxkum)) prior to data collection. The repository's own copy of the registration was first committed after the data; see [Open questions](OPEN.md).*

### H1: Primary Hypothesis

Exposure of *Saccharomyces cerevisiae* to hyperbolic field modulation will produce measurable differences in fermentation dynamics compared to non-exposed control samples.

### H2: Channel-Specific Effects

Different hyperbolic field configurations (CH19, CH21, CH17) will produce distinct and measurable effects on fermentation dynamics compared to control conditions.

### H3: Directional Channel Hypothesis

Based on prior observations in plasma systems (companion Blood Plasma Study, osf.io/8q42f, DOI 10.17605/OSF.IO/GWA9E), it is hypothesised that CH19 exposure will be associated with increased fermentation activity (e.g., faster metabolic dynamics — i.e. accelerated division rate / dynamics, NOT an increase in biomass or cell count; count ≈ control is the expected outcome for CH19; the count increase belongs to CH17), while CH21 exposure will be associated with reduced or delayed activity relative to control samples.

### H4: Temporal Dynamics

If hyperbolic field effects persist beyond the exposure period, differences between experimental conditions will increase over time, becoming more pronounced at later observation points (e.g., 12 hours post-exposure).

### H5: Transient Effect

If the effect is limited to the exposure period, differences between conditions will be observable during or immediately after exposure but will not significantly increase after the field is turned off.

### H6: Immediate Morphological Effect

Hyperbolic field exposure may induce immediate observable changes in sample properties (e.g., turbidity, texture, or visible morphology) during or immediately after exposure.

### H7: CH17 Uncertainty

The effect of CH17 is currently unknown. It may (a) produce a weaker directional effect similar to CH19, (b) induce qualitatively different changes (e.g., morphological alterations), or (c) produce no measurable effect compared to control.

### H8: Exploratory Variability

Exposure may alter the variability and consistency of fermentation dynamics across samples, reflecting potential non-linear or system-level responses.

### H9: Combined Channel Interaction

Simultaneous exposure to multiple hyperbolic field configurations (e.g., CH17 + CH19) may produce interaction effects on fermentation dynamics that differ from the effects of individual channels.

### H10: Additive vs Non-Linear Effects

Combined exposure may result in (a) additive effects (sum of individual channel effects), (b) synergistic amplification, or (c) antagonistic interactions, leading to outcomes that are not predictable from single-channel conditions.

### H11: Directional Combination

If CH19 is associated with increased activity and CH17 exhibits a similar or intermediate effect, combined exposure (CH17 + CH19) may lead to enhanced fermentation dynamics compared to either channel alone.


## Experimental design

### Design type

| Parameter | Value |
|---|---|
| **Type** | Randomized, double-blind, controlled |
| **Groups** | Control, CH19, CH21, CH17, CH17+CH19 |
| **Samples per group** | 5-10 independent samples |
| **Total N** | 25-50 |
| **Blinding** | Coded sample identifiers; researchers unaware of conditions during analysis |
| **Randomization** | Simple random assignment via RNG at sample level |

### Sample groups

<div align="center">
<a href="../charts/mermaid/root_1.png"><img src="../charts/mermaid/root_1.png" width="50%" alt="Earlier diagram: four treatment groups CH17, CH19, CH21 and CH17+CH19 and one control group, 5-10 samples each, flowing to measurements and results"></a>
</div>

The data holds four of these five groups: the combined group CH17+CH19 is not in the journal mapping or in the photographs ([Evidence](EVIDENCE.md)).

### Channel predictions

| Channel | Effect | Plasma Precedent |
|---|---|---|
| **CH19** | Accelerated fermentation phases | Most coagulated + lysis |
| **CH21** | Delayed fermentation phases | Lagged behind control |
| **CH17** | Unknown -- 3 scenarios (H7) | Found in blue whale research |
| **CH17+CH19** | Interaction effects (H9, H10, H11) | Not tested in plasma |

### Environment

| Parameter | Value |
|---|---|
| **Location** | Basement (-1 floor) |
| **Lighting** | Complete darkness during irradiation |
| **Temperature** | 10 C (basement); 18 C (3rd floor lab) |
| **Light monitoring** | Photoresistors |

### Observation schedule

| Timepoint | Action |
|---|---|
| Before irradiation | Photograph + microscopy |
| Immediately after | Photograph + microscopy |
| 3h post-exposure | Photograph |
| 6h | Photograph |
| 12h | Photograph + microscopy |
| 24h | Photograph + microscopy + staining |
| 48h | Photograph + microscopy + staining |

### Viability assay

**Methylene blue staining:**
- 100 uL cell suspension + 100 uL methylene blue (0.1 mg/mL in 2% sodium citrate dihydrate)
- 5 min incubation at room temperature
- Dead cells stain blue (cannot reduce dye)
- Live cells remain unstained (reduce dye)
- Budding cells with slight staining count as live

> **Note:** This is the *registered* viability protocol. The **first analysed microscopy batch (2026-06-09, 990 total images — 972 HEIC eyepiece microscopy fields + 18 PNG digital microscopy) used NO viability stain** (researcher-confirmed; the blue cast in those images is medium/illumination), so that batch reports cell **density only**, not live/dead viability. Staining / OD600 / fermentation outcomes remain pending.

The stain strength is written two ways in the earlier README: "0.1% MB + 0.01% sodium citrate" in the metrics table and "0.1 mg/mL in 2% sodium citrate dihydrate" in the protocol (see [Open questions](OPEN.md)).

## Outcome variables

### Primary outcomes

| Variable | Measurement |
|---|---|
| **Fermentation activity (rate)** | Observable gas production and turbidity changes over time |
| **Time to fermentation onset** | Time from start to visible signs of activity |
| **Fermentation progression dynamics** | Temporal evolution across predefined timepoints |
| **Qualitative morphology (exploratory)** | Turbidity patterns, texture, growth characteristics |

### Derived indices

| Index | Formula | Description |
|---|---|---|
| **FAI (Fermentation Activity Index)** | AUC_condition / AUC_control | Relative fermentation activity |
| **FDI (Fermentation Delay Index)** | lag_condition - lag_control | Lag phase difference |
| **FPI (Fermentation Progression Index)** | umax_condition / umax_control | Maximum growth rate ratio |

### Control variables

Temperature, medium composition, container type, time from preparation to exposure.

## Statistical analysis

### Primary analysis

Linear Mixed-Effects Model (LME) comparing fermentation dynamics across conditions:

```
log(OD) ~ Condition * Timepoint + (1 | SampleID)
```

- **Between-subject factor:** Exposure condition (Control, CH19, CH21, CH17, CH17+CH19)
- **Within-subject factor:** Time (immediate, 3h, 6h, 12h, 24h, 48h)
- **Post-hoc:** Tukey-adjusted pairwise comparisons
- **Non-parametric alternative:** Kruskal-Wallis if ANOVA assumptions violated
- **Significance threshold:** p < 0.05 (two-tailed)
- **Effect sizes:** Cohen's d, partial eta squared
- **Multiple comparisons:** Tukey HSD for conditions, Bonferroni for timepoints

This analysis is **planned and not run**: there is no optical-density data in the repository. The results on [Results so far](RESULTS.md) are descriptive.

### Success criteria

- p < 0.05 on primary outcome
- Moderate effect size (d >= 0.4)
- Transfer to at least one secondary outcome
- Subjective-only effects without quantitative confirmation = weak evidence

### Data exclusion

- Contamination, preparation failure, or recording failure only
- Outliers reported but not removed
- Missing observations not imputed

## Equipment

| Equipment | Specification |
|---|---|
| **Emitter system** | 6 nodes, 60W avg / 144W peak, clean sine wave |
| **Temperature sensors** | DHT11 digital (temp + humidity), placed next to each sample |
| **Light sensors** | Photoresistors + ADC |
| **Microscope** | Light microscope with strong LED illumination |
| **Data center** | Linux-based microprocessor, 1 TB storage, auto-logging |
| **Containers** | Petri dishes |
| **Staining supplies** | Methylene blue 0.1 mg/mL, sodium citrate dihydrate 2%, glass slides |

The emitter control software is a separate repository ([ASRP ecosystem](ECOSYSTEM.md)); this study logs only channel identifiers.
