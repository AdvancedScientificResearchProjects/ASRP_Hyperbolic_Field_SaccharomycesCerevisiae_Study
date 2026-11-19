**[English](FIGURES.md) | Русский**

[← Исследование Hyperbolic Field на дрожжах](../README.ru.md) · [Указатель руководства](README.ru.md)

<div align="center">

# Рисунки: всё, что есть в репозитории

</div>

Каждый рисунок репозитория достижим отсюда. Таблицы без миниатюр: рисунок, что он показывает, откуда он. Схемы-перерисовки заменили старые mermaid-PNG на страницах, а исходные файлы остаются на месте и указаны в первой таблице.

## Перерисованные схемы (исходный PNG остаётся)

| Рисунок | Что показывает | Исходная схема |
|---|---|---|
| [Группы воздействия и контроль](assets/diagrams/design-groups.ru.svg) | четыре группы воздействия и контроль, по 5-10 образцов, к измерениям и результатам | [`charts/mermaid/root_1.png`](../charts/mermaid/root_1.png) |
| [Планируемый стек анализа](assets/diagrams/planned-pipeline.ru.svg) | камера телефона, Cellpose3, разветвление по типу снимка, ветви YeastSAM или OpenCV, AMiGA, LME + ANOVA | [`charts/mermaid/root_2.png`](../charts/mermaid/root_2.png) |
| [План вех](assets/diagrams/plan-milestones.ru.svg) | восемь вех от 28 марта до подготовки публикации, 3-4 кв. 2026 | [`charts/mermaid/root_3.png`](../charts/mermaid/root_3.png) |
| [Связь с патентом](assets/diagrams/patent-connection.ru.svg) | заявка KZ 2025/1095.1 к технологии излучателей и к четырём исследованиям (заявка, не выданный патент) | [`charts/mermaid/retry_1.png`](../charts/mermaid/retry_1.png) |

## Схемы руководства

| Рисунок | Что показывает | Страница |
|---|---|---|
| [Карта программы](assets/diagrams/programme-map.ru.svg) | зарегистрированная программа против одной проанализированной серии | [Исследование](STUDY.ru.md) |
| [Хронология](assets/diagrams/timeline.ru.svg) | дорожка плана против того, что записано в истории git и файлах | [Исследование](STUDY.ru.md) |
| [Поток анализа](assets/diagrams/analysis-flow.ru.svg) | журнал, сопоставление, снимки, три метода, один отчёт | [Данные и методы](DATA.ru.md) |
| [Результаты по плотности](assets/diagrams/density-results.ru.svg) | счёт клеток по каналам, циклы 2-3 и разворот цикла 1 | [Результаты](RESULTS.ru.md) |
| [Заявлено и показано](assets/diagrams/claimed-vs-shown.ru.svg) | что говорит прежний README против того, что показывают данные и код | [Доказательства](EVIDENCE.ru.md) |
| [Экосистема](assets/diagrams/ecosystem-flow.ru.svg) | от чего зависит исследование и что только перечислено | [Экосистема](ECOSYSTEM.ru.md) |
| [Баннер](assets/banner/hero-banner.ru.svg) | сгенерированная иллюстрация, не скриншот | [README](../README.ru.md) |

## Графики отчёта о плотности

| Рисунок | Что показывает | Источник |
|---|---|---|
| [Счёт клеток по каналам, 100x](../reports/2026-06-09_density-analysis/charts/chart_counts_100x.png) | среднее число клеток на поле: контроль, CH17, CH19, CH21 (cyto2) | [report](../reports/2026-06-09_density-analysis/report_ru.md) |
| [Эффект поля к контролю](../reports/2026-06-09_density-analysis/charts/chart_relative_effect.png) | изменение счёта клеток к контролю в процентах, 100x | [report](../reports/2026-06-09_density-analysis/report_ru.md) |
| [Занятость по каналам и увеличению](../reports/2026-06-09_density-analysis/charts/chart_occupancy_by_magnification.png) | занятость текстуры (proxy плотности) при 10x и 100x, 787 полей с известным увеличением | [report](../reports/2026-06-09_density-analysis/report_ru.md) |
| [Счёт клеток по циклам](../reports/2026-06-09_density-analysis/charts/chart_counts_by_cycle.png) | тот же счёт по циклам; видно, что цикл 1 расходится | [report](../reports/2026-06-09_density-analysis/report_ru.md) |
| [Согласие CV и LLM](../reports/2026-06-09_density-analysis/charts/chart_cv_vs_llm.png) | поле за полем: счёт cyto2 против слепой оценки LLM, ρ Спирмена | [report](../reports/2026-06-09_density-analysis/report_ru.md) |

## Фотографии и рабочие снимки

| Папка или файл | Что там | Страница |
|---|---|---|
| [`data/equipment/`](../data/equipment/) | 3 фотографии: пакетик дрожжей (лицо и оборот) и рукописный эскиз раскладки датчиков (чашка с образцом, DHT11, АЦП) | [Данные и методы](DATA.ru.md) |
| [`data/microscopy/`](../data/microscopy/) | 3 фотографии: вид через окуляр концентрата дрожжей и два снимка подписанного трёхпольного предметного стекла (живые, с этанолом, с этанолом и красителем) | [Данные и методы](DATA.ru.md) |
| [`data/microscopy/staining/`](../data/microscopy/staining/) | 3 снимка экрана телефона с окрашенными дрожжами под микроскопом | [Данные и методы](DATA.ru.md) |
| [`results/SEMANTICS_objectives_photo.jpg`](../results/SEMANTICS_objectives_photo.jpg) | скриншот страницы магазина: объективы, окуляры и держатель телефона для микроскопа | [Данные и методы](DATA.ru.md) |
| [`data/photos/`](../data/photos/) | сырые данные, не рисунки: 972 + 18 снимков образцов (990 файлов) анализируемого эксперимента, соотнесённых с каналами через journal-mapping.csv | [Данные и методы](DATA.ru.md) |

Снимки оборудования и микроскопа — необработанные снимки телефона и скриншоты; файлы с именем человека в названии здесь не перечислены по именам (частные лица), открывайте папку целиком.
