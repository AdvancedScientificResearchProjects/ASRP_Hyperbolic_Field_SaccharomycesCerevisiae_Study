**[English](NAVIGATION.md) | Русский**

[← Исследование влияния гиперболических полей на Saccharomyces cerevisiae](../README.ru.md) · [Указатель страниц](README.ru.md)

<div align="center">

# Навигация и структура

</div>

## Где что лежит

Это репозиторий исследования, а не программный проект: большая часть объёма — фотографии. Начните с вашего вопроса.

| Если нужно | Куда идти |
|---|---|
| что исследование спрашивает и где оно сейчас | [Исследование](STUDY.ru.md), затем [Доказательства](EVIDENCE.ru.md) |
| зарегистрированные гипотезы, дизайн и статистика | [Гипотезы и дизайн](DESIGN.ru.md); протокол: [`reports/experiment_protocol_ru.md`](../reports/experiment_protocol_ru.md) |
| единственный проанализированный пакет и его границы | [Результаты пока](RESULTS.ru.md); полный отчёт: [`report_ru.md`](../reports/2026-06-09_density-analysis/report_ru.md) |
| как фото соотносятся с каналами | [Данные и методы](DATA.ru.md); [`journal-mapping.csv`](../data/photos/journal-mapping.csv), [`journal-note.txt`](../data/photos/journal-note.txt) |
| числа за отчётом | [`results/cv_analysis/`](../results/cv_analysis/white_counts.csv), [`results/llm_full/`](../results/llm_full/llm_full.json) |
| код анализа | [`scripts/cv_analysis/`](../scripts/cv_analysis/occupancy.py), [`scripts/llm_analysis/`](../scripts/llm_analysis/run_single.py) |
| регистрация и патентная заявка | [Экосистема, регистрация и патент](ECOSYSTEM.ru.md); [`OSF_PREREGISTRATION.md`](../OSF_PREREGISTRATION.md) |
| термины: псевдорепликация, занятость, конечная точка | [Глоссарий](GLOSSARY.ru.md) |
| что пока не сходится | [Открытые вопросы](OPEN.ru.md) |
| хаб данных прежнего README | [`data/README.md`](../data/README.md) (частично устарел) |
| прежние англоязычный и русскоязычный README | [`en/README.md`](../en/README.md), [`ru/README.md`](../ru/README.md) |
| прежний README без изменений | [`archive/README_2026-11-19_pre-showcase.md`](../archive/README_2026-11-19_pre-showcase.md) |

## Для чего каждая папка

- `data/` — наблюдения: фотографии и их сопоставление по журналу. Аналитические корзины `control-NN` и `sample-chXX` — пустые заглушки в ожидании атрибуции.
- `results/` — выход скриптов: счёты, занятость, морфометрия и оценка LLM. Всё в `reports/` выведено из него.
- `scripts/` — компьютерное зрение cyto2 и занятости и скрипты оценки LLM. Инструментов из планового стека здесь нет.
- `reports/` — протокол и один отчёт.
- `tools/` и `tests/` относятся к этой витрине: факты, диаграммы, выдержки, проверка без потерь против архивного README.

## Дерево папок

Дерево ниже порождается `tools/build_facts.py` из файлов, известных git, и вычисленных фактов: несуществующий путь или недостающая запись верхнего уровня останавливают сборку.

<!-- tree -->
```
ASRP_Hyperbolic_Field_SaccharomycesCerevisiae_Study/
├── README.md                         # главная страница (английская)
├── README.ru.md                      # главная страница (русская)
├── guide/                            # страницы-детали X.md + X.ru.md; assets/ = сгенерированные SVG
├── archive/                          # прежний README, сохранён байт в байт
├── tools/                            # инструменты витрины: факты, визуалы, выдержки, проверка без потерь
├── tests/                            # регрессионный гейт витрины
├── OSF_PREREGISTRATION.md            # копия предрегистрации в репозитории (спорна, см. Открытые вопросы)
├── en/README.md                      # англоязычное зеркало прежнего README
├── ru/README.md                      # русскоязычное зеркало прежнего README
├── data/                             # сырые наблюдательные данные: 990 снимков, сопоставление по журналу, заглушки
│   ├── README.md                     # хаб данных (частично устарел)
│   ├── photos/                       # плоский набор фото: манифест, сопоставление, original/ (HEIC, PNG), jpg/ (972 превью)
│   ├── equipment/                    # фото установки
│   ├── microscopy/                   # фото микроскопии и окрашивания
│   └── control-01/                   # пустые корзины 7: control-NN, sample-chXX
├── results/                          # результаты анализа
│   ├── cv_analysis/                  # счёт cyto2, морфометрия, занятость (CSV + JSON)
│   ├── llm_blind/                    # 2 пилотных слепых прогона + ключ
│   └── llm_full/                     # итоговая оценка LLM, 920 полей
├── reports/                          # протокол (EN, RU) и отчёт по плотности
│   ├── experiment_protocol_en.md     # протокол эксперимента
│   └── 2026-06-09_density-analysis/  # отчёт v2 EN + RU, 5 графиков, скрипт графиков
├── scripts/                          # 8 файлов Python: cv_analysis/, llm_analysis/
├── charts/                           # 4 отрисованные схемы прежнего README
│   └── mermaid/                      # root_1 — root_3, retry_1 (PNG)
└── protocols/                        # пустая заглушка
```
<!-- /tree -->

## Ссылки на изображения прежнего README

Прежний README встраивал свои графики абсолютными ссылками. Они открываются, только когда репозиторий публичный; здесь страницы используют относительные пути к тем же файлам. Ссылки для справки:

- `https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_SaccharomycesCerevisiae_Study/main/charts/mermaid/root_1.png`
- `https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_SaccharomycesCerevisiae_Study/main/charts/mermaid/root_2.png`
- `https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_SaccharomycesCerevisiae_Study/main/charts/mermaid/root_3.png`
- `https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_SaccharomycesCerevisiae_Study/main/charts/mermaid/retry_1.png`
- `https://raw.githubusercontent.com/AdvancedScientificResearchProjects/Hyperbolic_Field_SaccharomycesCerevisiae_Study/main/reports/2026-06-09_density-analysis/charts/chart_counts_100x.png`

## Как собираются страницы

Числа на этих страницах считает `tools/facts.py`, а `tools/build_facts.py` вписывает их (невидимые маркеры). Диаграммы строит `tools/build_visuals.py`. Выдержки на главной подтягиваются из страниц-деталей скриптом `tools/build_readme_excerpts.py`, поэтому предложение на главной и страница-деталь не расходятся. `python3 -m unittest discover -s tests` пересобирает всё и падает при любом расхождении или потере относительно архивного README (`python3 tools/verify_no_loss.py`).
