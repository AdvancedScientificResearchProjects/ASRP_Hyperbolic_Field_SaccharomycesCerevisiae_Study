# ════════════════════════════════════════════════════════════════════
# STUDY: runs, datasets, tools, roles, ASRP documents, hypotheses, claims
# ════════════════════════════════════════════════════════════════════
# exec()'d inside build_blueprint.py: E() and C() are already defined.
# Paths in `source=` are relative to this repository unless they start with
# "crowdfunding:" (the ASRP_Crowdfunding_Research repository).

S = "hyperbolic-saccharomyces"
CAMP = "campaign-yeast-result-that-flipped"
R = "reports/2026-06-09_density-analysis/report_en.md"

# ── ASRP DOCUMENTS ───────────────────────────────────────────────────
E("pub-yeast-density-report", "Density report of 9 June 2026", "publication",
  label_ru="Отчёт о плотности от 9 июня 2026",
  description="'Yeast Cell-Density Response to Hyperbolic-Field Exposure: Triangulated Image Analysis', v2. In-repository report, not peer reviewed. Status line: 'Preliminary signal — not confirmatory'.",
  description_ru="«Yeast Cell-Density Response to Hyperbolic-Field Exposure: Triangulated Image Analysis», v2. Отчёт в репозитории, без рецензирования. Строка статуса: «предварительный сигнал, не подтверждение».",
  date="2026-06-09", source=R)
E("pub-yeast-protocol", "Experiment protocol", "publication",
  label_ru="Протокол эксперимента",
  description="Setup, channel mapping, schedule, registered viability stain. Recipes of the two liquids and the handling of the control dishes are not written down.",
  description_ru="Установка, смысл каналов, расписание, зарегистрированная окраска на жизнеспособность. Рецепты двух жидкостей и условия контрольных чашек не записаны.",
  source="reports/experiment_protocol_en.md")
E("pub-yeast-prereg-file", "In-repository preregistration file", "publication",
  label_ru="Файл пререгистрации в репозитории",
  description="OSF_PREREGISTRATION.md, first committed 2026-06-10, after the data and the report; contains an observed result. Not the frozen April registration text.",
  description_ru="OSF_PREREGISTRATION.md, впервые закоммичен 2026-06-10, после данных и отчёта; содержит полученный результат. Это не замороженный апрельский текст регистрации.",
  date="2026-06-10", source="guide/EVIDENCE.md:31")
E("pub-campaign-prereg-draft", "Pre-registration draft for the blinded repeat", "publication",
  label_ru="Черновик пререгистрации слепого повторения",
  description="Draft of 20 Nov 2026, not filed. Six runs, 144 dishes, counting chamber, outside counter, three fixed result sentences. Items marked for a statistician and the lab lead are open.",
  description_ru="Черновик от 20 ноября 2026, не подан. Шесть прогонов, 144 чашки, счётная камера, внешний счётчик, три заранее заданные фразы результата. Пункты для статистика и руководителя лаборатории открыты.",
  date="2026-11-20", source="crowdfunding:campaigns/yeast-replication-study/launch/preregistration-draft.md")

# ── RUNS ─────────────────────────────────────────────────────────────
E("ev-yeast-round-1", "Round 1 (set 001), April 2026", "event",
  label_ru="Раунд 1 (набор 001), апрель 2026",
  description="First exposure batch. Different imaging protocol: no magnification split, so no cell counts; occupancy only.",
  description_ru="Первая партия облучения. Другой протокол съёмки: без разделения по увеличению, поэтому подсчёта клеток нет; только заполненность кадра.",
  date="2026-04", source=R + ":113")
E("ev-yeast-round-2", "Round 2 (set 002), April 2026", "event",
  label_ru="Раунд 2 (набор 002), апрель 2026",
  description="Second exposure batch; 100× photos counted. One control dish in the nutrient liquid spilled and is excluded.",
  description_ru="Вторая партия облучения; фото на 100× посчитаны. Одна контрольная чашка с питательной жидкостью пролита и исключена.",
  date="2026-04", source="reports/experiment_protocol_en.md:106")
E("ev-yeast-round-3", "Round 3 (set 003), April 2026", "event",
  label_ru="Раунд 3 (набор 003), апрель 2026",
  description="Third exposure batch; 100× photos counted.",
  description_ru="Третья партия облучения; фото на 100× посчитаны.",
  date="2026-04", source=R + ":107")
E("ev-yeast-repeat-planned", "Planned blinded repeat (six runs, 144 dishes)", "event",
  label_ru="Плановое слепое повторение (шесть прогонов, 144 чашки)",
  description="Not started. A dry run without the emitter comes first; emitter off, setting 17 and setting 21 in two liquids; counts by an outside counter and by backers before the key is opened.",
  description_ru="Не начато. Сначала холостой прогон без излучателя; излучатель выключен, настройка 17 и настройка 21 в двух жидкостях; подсчёт внешним счётчиком и бэкерами до открытия ключа.",
  status="planned", source="crowdfunding:campaigns/yeast-replication-study/launch/preregistration-draft.md:41")

# ── DATASETS ─────────────────────────────────────────────────────────
E("ds-yeast-photos", "Photo set (972 eyepiece photos + 18 digital frames)", "dataset",
  label_ru="Набор фото (972 фото через окуляр + 18 цифровых кадров)",
  description="data/photos/: HEIC originals taken with a phone through the eyepiece. No scale bar. 198 files carry a date, 792 do not.",
  description_ru="data/photos/: оригиналы HEIC, снятые телефоном через окуляр. Масштабной линейки нет. Дата есть у 198 файлов, у 792 нет.",
  source="guide/EVIDENCE.md:36")
E("ds-yeast-journal-mapping", "Journal mapping (photo number to dish)", "dataset",
  label_ru="Соответствие журнала (номер фото → чашка)",
  description="data/photos/journal-mapping.csv: transcription of a handwritten three-page journal; the only link between a photo and its channel, liquid, round and magnification.",
  description_ru="data/photos/journal-mapping.csv: расшифровка рукописного журнала на трёх страницах; единственная связь фото с каналом, жидкостью, раундом и увеличением.",
  source=R + ":219")
E("ds-yeast-white-counts", "Cell counts, 398 photos at 100×", "dataset",
  label_ru="Подсчёт клеток, 398 фото на 100×",
  description="results/cv_analysis/white_counts.csv (and the JSON twin): automatic counts, rounds 2 and 3 only.",
  description_ru="results/cv_analysis/white_counts.csv (и JSON-копия): автоматический подсчёт, только раунды 2 и 3.",
  source=R + ":214")
E("ds-yeast-occupancy", "Occupancy scores, 972 photos", "dataset",
  label_ru="Оценки заполненности кадра, 972 фото",
  description="results/cv_analysis/occupancy_full.csv: share of each photo covered by cells; the only measure that exists for round 1.",
  description_ru="results/cv_analysis/occupancy_full.csv: доля кадра, занятая клетками; единственная мера, которая есть для раунда 1.",
  source=R + ":216")
E("ds-yeast-llm-scores", "Blind vision-model scores, 920 photos", "dataset",
  label_ru="Слепые оценки модели зрения, 920 фото",
  description="results/llm_full/llm_full.json: one density estimate per photo from a vision model that saw neutral file names only.",
  description_ru="results/llm_full/llm_full.json: одна оценка плотности на фото от модели зрения, видевшей только нейтральные имена файлов.",
  source=R + ":217")
E("ds-yeast-medium-split", "Recount split by liquid (20 Nov 2026)", "dataset",
  label_ru="Пересчёт с разделением по жидкости (20 ноября 2026)",
  description="Table made for the campaign from the public count file and the journal mapping: means by liquid, by round and by dish.",
  description_ru="Таблица, сделанная для кампании из публичного файла подсчёта и соответствия журнала: средние по жидкости, по раунду и по чашке.",
  date="2026-11-20", source="crowdfunding:campaigns/yeast-replication-study/research/medium-split-out/medium_split_table.md")

# ── TOOLS AND DEVICES ────────────────────────────────────────────────
E("tool-cellpose-cyto2", "Cellpose, model cyto2", "tooling-class",
  label_ru="Cellpose, модель cyto2",
  description="Open-source segmentation network used out of the box (no fine-tuning) to count cells at 100×.",
  description_ru="Открытая сеть сегментации, применена как есть (без дообучения) для подсчёта клеток на 100×.",
  source=R + ":44")
E("tool-yeast-occupancy", "Occupancy score (texture + Otsu + Canny)", "tooling-class",
  label_ru="Оценка заполненности (текстура + Оцу + Канни)",
  description="In-house script scripts/cv_analysis/occupancy.py; reads the same pixels as the cell counter.",
  description_ru="Собственный скрипт scripts/cv_analysis/occupancy.py; читает те же пиксели, что и счётчик клеток.",
  source=R + ":45")
E("tool-yeast-blind-llm", "Blind vision-model scoring", "tooling-class",
  label_ru="Слепая оценка моделью зрения",
  description="One pass of a multimodal model per photo, condition not disclosed (scripts/llm_analysis/).",
  description_ru="Один проход мультимодальной модели на фото, условие не раскрывается (scripts/llm_analysis/).",
  source=R + ":46")
E("dev-yeast-microscope-phone", "Light microscope with a phone at the eyepiece", "device",
  label_ru="Световой микроскоп с телефоном у окуляра",
  description="Endpoint photos in HEIC through the eyepiece; two objectives (the journal's 'white' and 'yellow'); no scale bar, no fixed focus rule.",
  description_ru="Конечные фото в HEIC через окуляр; два объектива («белый» и «жёлтый» в журнале); без масштабной линейки, без правила фокусировки.",
  source="reports/experiment_protocol_en.md:57")
E("dev-neubauer-chamber", "Counting chamber (improved Neubauer), planned", "device",
  label_ru="Счётная камера (улучшенная Нейбауэра), в плане",
  description="Planned for the repeat: squares of known volume, so that counts become cells per millilitre and every photo has a scale.",
  description_ru="В плане повторения: квадраты известного объёма, чтобы счёт стал клетками на миллилитр и у каждого фото был масштаб.",
  status="planned", source="crowdfunding:campaigns/yeast-replication-study/launch/preregistration-draft.md:79")

# ── ROLES (no names) ─────────────────────────────────────────────────
E("role-yeast-lab-lead", "Lab lead of the yeast work", "role",
  label_ru="Руководитель работ по дрожжам",
  description="Ran the April pilot and confirmed the label meanings on 9 June 2026.",
  description_ru="Провела апрельский пилот и подтвердила смысл меток 9 июня 2026.",
  source=R + ":21")
E("role-yeast-photographer", "Pilot photographer (knew the group)", "role",
  label_ru="Фотограф пилота (знал группу)",
  description="Took the photos group by group, knowing which dish was which.",
  description_ru="Снимал группу за группой, зная, какая чашка какая.",
  source="crowdfunding:campaigns/yeast-replication-study/launch/preregistration-draft.md:25")
E("role-key-holder", "Key holder outside ASRP (not yet named)", "role",
  label_ru="Хранитель ключа вне ASRP (пока не назван)",
  description="Planned: draws the random lists and opens the key once, after all counts are frozen.",
  description_ru="В плане: составляет случайные списки и открывает ключ один раз, после заморозки всех подсчётов.",
  status="open")
E("role-outside-counter", "Outside counter (not yet named)", "role",
  label_ru="Внешний счётчик (пока не назван)",
  description="Planned: makes the primary count without knowing the condition.",
  description_ru="В плане: делает основной подсчёт, не зная условия.",
  status="open")
E("role-statistician", "Statistician (not yet named)", "role",
  label_ru="Статистик (пока не назван)",
  description="Planned: approves the analysis, the margin and the number of runs before filing.",
  description_ru="В плане: утверждает анализ, границу и число прогонов до подачи.",
  status="open")
E("role-backer-scorers", "Backer-scorers", "role",
  label_ru="Бэкеры-счётчики",
  description="Planned: backers who count 24 coded photos each before the key is opened; they do not decide the primary result.",
  description_ru="В плане: бэкеры, которые считают по 24 закодированных фото до открытия ключа; основной результат они не определяют.",
  status="planned")

# ── HYPOTHESES ───────────────────────────────────────────────────────
E("hyp-yeast-ch17-more-cells", "Setting 17 raises yeast cell density", "hypothesis",
  label_ru="Настройка 17 повышает плотность клеток дрожжей",
  description="Not predicted beforehand (H7 said 'unknown'). Status: a lead from two rounds, in one liquid, in four dishes; not replicated.",
  description_ru="Заранее не предсказывалось (H7: «неизвестно»). Статус: зацепка из двух раундов, в одной жидкости, в четырёх чашках; не воспроизведено.",
  status="open")
E("hyp-yeast-ch21-fewer-cells", "Setting 21 lowers yeast cell density", "hypothesis",
  label_ru="Настройка 21 понижает плотность клеток дрожжей",
  description="Matches the protocol's 'deceleration' reading in rounds 2-3; reversed in round 1.",
  description_ru="Совпадает с трактовкой «замедление» в раундах 2–3; в раунде 1 обратная картина.",
  status="open")
E("hyp-yeast-ch19-faster-division", "Setting 19 speeds up division (smaller, thinner cells, same count)", "hypothesis",
  label_ru="Настройка 19 ускоряет деление (клетки мельче и тоньше, число то же)",
  description="The report's own verdict: not supported on this batch; untestable from single snapshots.",
  description_ru="Вердикт самого отчёта: на этой партии не подтверждается; по одиночным снимкам непроверяемо.",
  status="not supported", source=R + ":201")
E("hyp-yeast-handling-artefact", "The difference comes from handling and imaging, not from the emitter", "hypothesis",
  label_ru="Разница возникает из-за обращения с пробами и съёмки, а не из-за излучателя",
  description="Uneven filling, settling, where the drop was taken, sharper photos, a photographer who knew the group. None can be ruled out from the files.",
  description_ru="Неравномерное наполнение, оседание, место взятия капли, более резкие фото, фотограф, знавший группу. Ничто из этого по файлам исключить нельзя.",
  status="open", source="crowdfunding:campaigns/yeast-replication-study/story-and-film/story-v1.md:77")

# ── FACTS: the study's own numbers ───────────────────────────────────
E("f-yeast-headline-83", "Setting 17: 205 cells per photo against 112 (+83 %), both liquids pooled", "fact",
  label_ru="Настройка 17: 205 клеток на фото против 112 (+83 %), обе жидкости вместе",
  description="Mean automatic count per 100× photo, rounds 2-3: control 112 (82 photos), setting 17 205 (112 photos), setting 19 118, setting 21 88. Recomputed by the study's own tools from the count file; verifies the arithmetic and the join, not the imaging.",
  description_ru="Средний автоматический счёт на фото 100×, раунды 2–3: контроль 112 (82 фото), настройка 17 — 205 (112 фото), настройка 19 — 118, настройка 21 — 88. Пересчитано инструментами самого исследования из файла подсчёта; проверена арифметика и соединение таблиц, а не съёмка.",
  confidence="high", source="pub-yeast-density-report", where=R + ":79")
E("f-yeast-medium-split", "The excess exists only in the neutral liquid: 279 against 124; nutrient liquid 102 against 92", "fact",
  label_ru="Превышение есть только в нейтральной жидкости: 279 против 124; в питательной 102 против 92",
  description="Recount of 20 Nov 2026, mean cells per 100× photo: neutral 124.3 (control) and 279.3 (setting 17); nutrient 92.1 and 102.2. The +83 % is an average of 'more than double' and 'nothing'. The June report did not split by liquid.",
  description_ru="Пересчёт 20 ноября 2026, среднее клеток на фото 100×: нейтральная 124,3 (контроль) и 279,3 (настройка 17); питательная 92,1 и 102,2. +83 % — среднее между «больше чем вдвое» и «ничего». Июньский отчёт по жидкостям не делил.",
  confidence="high", source="ds-yeast-medium-split")
E("f-yeast-four-dishes", "The neutral-liquid result rests on four dishes against four", "fact",
  label_ru="Результат в нейтральной жидкости держится на четырёх чашках против четырёх",
  description="Dish means, setting 17: 286, 350, 237, 269; control: 66, 107, 182, 146. 31 dishes carry all the count evidence.",
  description_ru="Средние по чашкам, настройка 17: 286, 350, 237, 269; контроль: 66, 107, 182, 146. Все данные подсчёта держатся на 31 чашке.",
  confidence="high", source="ds-yeast-medium-split")
E("f-yeast-round1-flip", "Round 1 reverses the order: setting 21 highest (0.246 against 0.141)", "fact",
  label_ru="Раунд 1 переворачивает порядок: настройка 21 выше всех (0,246 против 0,141)",
  description="On occupancy, the only measure available in round 1, setting 21 is the densest and setting 17 is second. Round 1 used a different imaging protocol.",
  description_ru="По заполненности кадра, единственной мере в раунде 1, настройка 21 самая плотная, настройка 17 вторая. В раунде 1 был другой протокол съёмки.",
  confidence="high", source="pub-yeast-density-report", where=R + ":113")
E("f-yeast-sharpness", "Sharper photos give higher automatic counts, and the setting 17 photos were the sharpest", "fact",
  label_ru="Более резкие фото дают больший автоматический счёт, а фото настройки 17 были самыми резкими",
  description="Rank correlation between sharpness and count 0.68 over the 398 photos; mean sharpness of the setting 17 neutral photos 138 against 96. From the campaign's recount; not recomputed for this graph.",
  description_ru="Ранговая корреляция резкости и счёта 0,68 по 398 фото; средняя резкость фото настройки 17 в нейтральной жидкости 138 против 96. Из пересчёта кампании; для этого графа не пересчитывалось.",
  confidence="medium", source="pub-campaign-prereg-draft")
E("f-yeast-twin-dishes", "Twin dishes differ from each other by a factor of about 1.4", "fact",
  label_ru="Чашки-близнецы различаются между собой примерно в 1,4 раза",
  description="Same round, liquid and setting; SD of the log dish mean 0.31 over 15 pairs. From the campaign's recount; not recomputed for this graph.",
  description_ru="Тот же раунд, жидкость и настройка; СО логарифма среднего по чашке 0,31 по 15 парам. Из пересчёта кампании; для этого графа не пересчитывалось.",
  confidence="medium", source="pub-campaign-prereg-draft")
E("f-yeast-method-agreement", "Three scoring methods agree per photo (rho 0.81-0.89 at 100×)", "fact",
  label_ru="Три метода оценки согласуются по фото (ρ 0,81–0,89 на 100×)",
  description="As reported; not recomputed. The methods read the same photos, so agreement guards against an algorithm artefact, not against an imaging one.",
  description_ru="По отчёту; не пересчитывалось. Методы читают одни и те же фото, поэтому согласие защищает от артефакта алгоритма, но не съёмки.",
  confidence="medium", source="pub-yeast-density-report", where=R + ":138")
E("f-yeast-undercount-40", "'cyto2 misses about 40 % of cells in dense fields'", "fact",
  label_ru="«cyto2 пропускает около 40 % клеток в плотных полях»",
  description="Stated in the report without a hand-count reference: who counted, and on how many photos, is NOT FOUND in the repository.",
  description_ru="Заявлено в отчёте без ссылки на ручной подсчёт: кто считал и на скольких фото — в репозитории NOT FOUND.",
  confidence="low", source="pub-yeast-density-report", where=R + ":187")
E("f-yeast-prereg-after-data", "The plan naming cell density as the main outcome was written after the counts", "fact",
  label_ru="План, называющий плотность клеток главным исходом, написан после подсчётов",
  description="File first committed 2026-06-10; photos 2026-04-19 to 2026-04-22; report 2026-06-09. The April OSF registration is not publicly readable (API answers 401, checked 2026-11-20).",
  description_ru="Файл впервые закоммичен 2026-06-10; фото 2026-04-19 — 2026-04-22; отчёт 2026-06-09. Апрельская регистрация OSF публично не читается (API отвечает 401, проверено 2026-11-20).",
  confidence="high", source="pub-yeast-prereg-file", where="guide/EVIDENCE.md:31")
E("f-yeast-ch19-area", "Setting 19 cells are 7.6 % smaller in area, but so are the cells of every exposed setting", "fact",
  label_ru="Клетки настройки 19 на 7,6 % меньше по площади, но так же и у всех облучённых настроек",
  description="Setting 17 −12.7 %, setting 21 −6.1 %; cells not more elongated; budding score flat. As reported.",
  description_ru="Настройка 17 −12,7 %, настройка 21 −6,1 %; клетки не более вытянутые; оценка почкования ровная. По отчёту.",
  confidence="medium", source="pub-yeast-density-report", where=R + ":201")

# ── FACTS: what the ASRP text attributes to a source, and what the source says ──
E("f-asrp-plasma-precedent", "ASRP text: the plasma study showed setting 19 = fast clot, setting 21 = dense slow clot", "fact",
  label_ru="Текст ASRP: в исследовании плазмы настройка 19 = быстрый сгусток, настройка 21 = плотный медленный сгусток",
  description="Protocol channel table and the report's Motivation, citing osf.io/8q42f, DOI 10.17605/OSF.IO/GWA9E.",
  description_ru="Таблица каналов в протоколе и раздел «Мотивация» отчёта со ссылкой на osf.io/8q42f, DOI 10.17605/OSF.IO/GWA9E.",
  confidence="low", source="pub-yeast-protocol", where="reports/experiment_protocol_en.md:28")
E("f-osf-registration-no-channels", "The cited registration is a plan with 'Emitter A' and 'Emitter B'; no channel numbers, no clot results", "fact",
  label_ru="Указанная регистрация — план с «излучателем A» и «излучателем B»; номеров каналов и результатов по сгусткам нет",
  description="Registration text read through the public OSF API on 2026-11-20: registered 2026-01-25 as 'Registration prior to creation of data'; the strings CH19, CH21, channel, acceleration, deceleration do not occur. Project files and the plasma repository were not checked.",
  description_ru="Текст регистрации прочитан через публичный API OSF 2026-11-20: зарегистрирована 2026-01-25 как «регистрация до создания данных»; строк CH19, CH21, channel, acceleration, deceleration в ней нет. Файлы проекта и репозиторий плазмы не проверялись.",
  confidence="high", source="src-asrp2026chrono_osf")
E("f-asrp-decoupling", "ASRP text: division rate can be decoupled from biomass, so 'faster division, same count' is valid", "fact",
  label_ru="Текст ASRP: темп деления можно отвязать от биомассы, значит «быстрее деление при том же числе» допустимо",
  description="Report, Conclusion, citing Schmidt-Glenewinkel & Barkai 2014.",
  description_ru="Отчёт, раздел «Заключение», со ссылкой на Schmidt-Glenewinkel & Barkai 2014.",
  confidence="low", source="pub-yeast-density-report", where=R + ":203")
E("f-src-decoupling-arrest", "Source: decoupling was forced genetically and the cells lost size control and arrested", "fact",
  label_ru="Источник: развязка вызвана генетически, клетки теряли контроль размера и останавливались",
  description="'genetic manipulations that decouple cell division from cell size, leading to the loss of growth homeostasis, with cells becoming progressively smaller or progressively larger until arresting' (abstract, p. 1).",
  description_ru="«генетические манипуляции, развязывающие деление и размер клетки, ведут к потере гомеостаза роста: клетки становятся всё мельче или всё крупнее вплоть до остановки» (аннотация, с. 1).",
  confidence="high", source="src-schmidtglenewinkel2014")
E("f-src-kato-shrink", "Source: a yeast cell loses about 27 % of its area when it dies", "fact",
  label_ru="Источник: клетка дрожжей теряет около 27 % площади при гибели",
  description="27.2 % and 27.0 % in two laboratory strains, time-lapse of stationary-phase cells; fewer than 1 % of surviving cells shrank by more than 10 %.",
  description_ru="27,2 % и 27,0 % у двух лабораторных штаммов, покадровая съёмка клеток стационарной фазы; менее 1 % выживших клеток сжались более чем на 10 %.",
  confidence="high", source="src-kato2021")
E("f-asrp-cielab", "ASRP text: a CIELAB colour model gives R²=0.81 for turbidity 'on S. cerevisiae with iPhone'", "fact",
  label_ru="Текст ASRP: CIELAB-модель даёт R²=0,81 для мутности «на S. cerevisiae с iPhone»",
  description="Planned-pipeline table, no citation.",
  description_ru="Таблица планового конвейера, без ссылки.",
  confidence="low", source="hyperbolic-saccharomyces", where="guide/DATA.md:46")
E("f-src-cielab-flasks", "Source: R²=0.81 was for whole shake flasks calibrated against a spectrophotometer", "fact",
  label_ru="Источник: R²=0,81 получен для целых колб с калибровкой по спектрофотометру",
  description="18 cultivations, more than 340 paired measurements, leave-one-experiment-out validation; nothing about Petri dishes or microscope fields.",
  description_ru="18 культивирований, более 340 парных измерений, проверка с исключением одного опыта; о чашках Петри и полях микроскопа ничего.",
  confidence="high", source="src-august2019")
E("f-src-blind-bias", "Source: non-blind studies reported larger effects than their blind twins in 53 of 83 pairs", "fact",
  label_ru="Источник: неслепые исследования дали больший эффект, чем их слепые пары, в 53 из 83 пар",
  description="Effect size higher by 0.55 ± 0.25 (Hedges' g) in the non-blind study of each pair (p. 3). Evolutionary-biology studies.",
  description_ru="Размер эффекта выше на 0,55 ± 0,25 (g Хеджеса) у неслепого исследования в паре (с. 3). Исследования по эволюционной биологии.",
  confidence="high", source="src-holman2015")
E("f-src-pseudoreplication", "Source: repeated measurements of one unit do not add to the sample size", "fact",
  label_ru="Источник: повторные измерения одной единицы не увеличивают размер выборки",
  description="'Pseudoreplication artificially inflates the sample size, and thus the evidence for a scientific claim, resulting in false positives' (p. 1).",
  description_ru="«Псевдорепликация искусственно завышает размер выборки, а значит и доказательность утверждения, и ведёт к ложноположительным результатам» (с. 1).",
  confidence="high", source="src-lazic2018")
E("f-gos-null", "Precedent: a reported field effect on yeast division did not hold with concurrent controls", "fact",
  label_ru="Прецедент: заявленный эффект поля на деление дрожжей не подтвердился при одновременном контроле",
  description="Gos et al. 1997: 'no consistently significant differences' between exposed and unexposed cells, 'in contrast to previous studies'. Abstract only; a different frequency range and device from the ASRP emitter.",
  description_ru="Gos и др. 1997: «устойчиво значимых различий нет» между облучёнными и необлучёнными клетками, «в отличие от прежних работ». Только аннотация; диапазон частот и устройство иные, чем у излучателя ASRP.",
  confidence="medium", source="src-gos1997")

# ── CONNECTIONS ──────────────────────────────────────────────────────
for _ev in ("ev-yeast-round-1", "ev-yeast-round-2", "ev-yeast-round-3"):
    C(S, _ev, ctype="has-run")
    C("role-yeast-lab-lead", _ev, ctype="ran")
    C("role-yeast-photographer", _ev, ctype="photographed")
    C(_ev, "ds-yeast-photos", ctype="produced")
    C(_ev, "ds-yeast-occupancy", ctype="measured_in")
    C("hyperbolic-emitter-generator", _ev, ctype="used-in")
C("ev-yeast-round-2", "ds-yeast-white-counts", ctype="measured_in")
C("ev-yeast-round-3", "ds-yeast-white-counts", ctype="measured_in")
C("dev-yeast-microscope-phone", "ds-yeast-photos", ctype="produced")
C("ds-yeast-journal-mapping", "ds-yeast-photos", ctype="labels")
C("role-yeast-lab-lead", "ds-yeast-journal-mapping", ctype="confirmed")
C("tool-cellpose-cyto2", "ds-yeast-white-counts", ctype="produced")
C("tool-yeast-occupancy", "ds-yeast-occupancy", ctype="produced")
C("tool-yeast-blind-llm", "ds-yeast-llm-scores", ctype="produced")
C("ds-yeast-photos", "ds-yeast-llm-scores", ctype="scored-into")
C("ds-yeast-white-counts", "ds-yeast-medium-split", ctype="recounted-into")
C("ds-yeast-journal-mapping", "ds-yeast-medium-split", ctype="recounted-into")
C(S, "pub-yeast-density-report", ctype="published")
C(S, "pub-yeast-protocol", ctype="published")
C(S, "pub-yeast-prereg-file", ctype="published")
C("pub-yeast-prereg-file", "src-asrp2026yeast_osf", ctype="mirror-of-unreadable")
C(CAMP, "pub-campaign-prereg-draft", ctype="published")
C(CAMP, "ev-yeast-repeat-planned", ctype="funds")
C("ev-yeast-repeat-planned", S, ctype="replicates")
C("pub-campaign-prereg-draft", "ev-yeast-repeat-planned", ctype="plans")
C("dev-neubauer-chamber", "ev-yeast-repeat-planned", ctype="used-in")
for _r in ("role-key-holder", "role-outside-counter", "role-statistician", "role-backer-scorers"):
    C(_r, "ev-yeast-repeat-planned", ctype="takes-part-in")
C("tool-cellpose-cyto2", "src-stringer2021cellpose", ctype="described-in")
C("tool-cellpose-cyto2", "src-pachitariu2022cellpose2", ctype="described-in")
C("tool-yeast-occupancy", "src-otsu1979", ctype="uses-method-from")
C("tool-yeast-occupancy", "src-canny1986", ctype="uses-method-from")
C("dev-neubauer-chamber", "src-student1907", ctype="counting-error-in")

# facts: where they were measured
C("f-yeast-headline-83", "ds-yeast-white-counts", ctype="measured_in")
C("f-yeast-medium-split", "ds-yeast-medium-split", ctype="measured_in")
C("f-yeast-four-dishes", "ds-yeast-medium-split", ctype="measured_in")
C("f-yeast-round1-flip", "ds-yeast-occupancy", ctype="measured_in")
C("f-yeast-round1-flip", "ev-yeast-round-1", ctype="measured_in")
C("f-yeast-sharpness", "ds-yeast-white-counts", ctype="measured_in")
C("f-yeast-twin-dishes", "ds-yeast-medium-split", ctype="measured_in")
C("f-yeast-method-agreement", "ds-yeast-llm-scores", ctype="measured_in")
C("f-yeast-undercount-40", "tool-cellpose-cyto2", ctype="about")
C("f-yeast-ch19-area", "ds-yeast-white-counts", ctype="measured_in")
C("f-yeast-prereg-after-data", "pub-yeast-prereg-file", ctype="about")
for _f, _doc in (("f-yeast-headline-83", "pub-yeast-density-report"), ("f-yeast-round1-flip", "pub-yeast-density-report"),
                 ("f-yeast-method-agreement", "pub-yeast-density-report"), ("f-yeast-undercount-40", "pub-yeast-density-report"),
                 ("f-yeast-ch19-area", "pub-yeast-density-report"), ("f-asrp-decoupling", "pub-yeast-density-report"),
                 ("f-asrp-plasma-precedent", "pub-yeast-protocol"), ("f-yeast-sharpness", "pub-campaign-prereg-draft"),
                 ("f-yeast-twin-dishes", "pub-campaign-prereg-draft"), ("f-asrp-cielab", S)):
    C(_f, _doc, ctype="sourced-from")
C("f-osf-registration-no-channels", "src-asrp2026chrono_osf", ctype="sourced-from")
C("f-src-decoupling-arrest", "src-schmidtglenewinkel2014", ctype="sourced-from")
C("f-src-kato-shrink", "src-kato2021", ctype="sourced-from")
C("f-src-cielab-flasks", "src-august2019", ctype="sourced-from")
C("f-src-blind-bias", "src-holman2015", ctype="sourced-from")
C("f-src-pseudoreplication", "src-lazic2018", ctype="sourced-from")

# facts: what they support and contradict
C("f-yeast-headline-83", "hyp-yeast-ch17-more-cells", ctype="supports")
C("f-yeast-headline-83", "hyp-yeast-ch21-fewer-cells", ctype="supports")
C("f-yeast-method-agreement", "hyp-yeast-ch17-more-cells", ctype="supports")
C("f-yeast-medium-split", "f-yeast-headline-83", ctype="contradicts", note="the pooled figure hides that the excess is in one liquid only")
C("f-yeast-four-dishes", "hyp-yeast-ch17-more-cells", ctype="contradicts", note="weakens: four dishes against four")
C("f-yeast-round1-flip", "hyp-yeast-ch17-more-cells", ctype="contradicts")
C("f-yeast-round1-flip", "hyp-yeast-ch21-fewer-cells", ctype="contradicts")
C("f-yeast-sharpness", "hyp-yeast-handling-artefact", ctype="supports")
C("f-yeast-twin-dishes", "hyp-yeast-handling-artefact", ctype="supports")
C("f-src-blind-bias", "hyp-yeast-handling-artefact", ctype="supports")
C("f-src-pseudoreplication", "f-yeast-headline-83", ctype="contradicts", note="398 photos are not 398 independent observations")
C("f-yeast-undercount-40", "f-yeast-headline-83", ctype="contradicts", note="the counter's error is unmeasured")
C("f-yeast-prereg-after-data", "hyp-yeast-ch17-more-cells", ctype="contradicts", note="the outcome was chosen after the data")
C("f-yeast-ch19-area", "hyp-yeast-ch19-faster-division", ctype="contradicts")
C("f-asrp-decoupling", "hyp-yeast-ch19-faster-division", ctype="supports")
C("f-src-decoupling-arrest", "f-asrp-decoupling", ctype="contradicts")
C("f-src-kato-shrink", "hyp-yeast-ch19-faster-division", ctype="contradicts", note="smaller cells may be dying cells")
C("f-asrp-plasma-precedent", "channel-19-21-taxonomy", ctype="supports")
C("f-osf-registration-no-channels", "f-asrp-plasma-precedent", ctype="contradicts")
C("f-src-cielab-flasks", "f-asrp-cielab", ctype="contradicts")
C("f-gos-null", "ev-yeast-repeat-planned", ctype="precedent-for")
C("channel-17", "hyp-yeast-ch17-more-cells", ctype="subject-of")
C("channel-19-21-taxonomy", "hyp-yeast-ch21-fewer-cells", ctype="subject-of")
C("channel-19-21-taxonomy", "hyp-yeast-ch19-faster-division", ctype="subject-of")

# what the campaign uses
for _n in ("f-yeast-headline-83", "f-yeast-medium-split", "f-yeast-four-dishes", "f-yeast-round1-flip",
           "f-yeast-sharpness", "f-yeast-twin-dishes", "f-yeast-prereg-after-data",
           "hyp-yeast-handling-artefact", "ds-yeast-medium-split", "pub-yeast-density-report"):
    C(_n, CAMP, ctype="used_by_campaign")
