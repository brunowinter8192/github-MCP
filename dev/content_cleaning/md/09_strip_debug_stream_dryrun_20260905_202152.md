MinerU__1646.md:49-53 [loguru_narration]
2025-01-31 02:33:20.834 | INFO     | magic_pdf.data.dataset:__init__:156 - lang: None
2025-01-31 02:33:23.298 | INFO     | magic_pdf.libs.pdf_check:detect_invalid_chars:57 - cid_count: 22, text_len: 20142, cid_chars_radio: 0.0011018731844135029
2025-01-31 02:33:23.311 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:78 - DocAnalysis init, this may take some times, layout_model: doclayout_yolo, apply_formula: True, apply_ocr: False, apply_table: True, table_model: rapid_table, lang: None
2025-01-31 02:33:23.311 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:99 - using device: cuda
2025-01-31 02:33:23.311 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:103 - using models_dir: /home/hongbo-miao/.cache/huggingface/hub/models--opendatalab--PDF-Extract-Kit-1.0/snapshots/60416a2cabad3f7b7284b43ce37a99864484fba2/models

MinerU__1646.md:63-75 [loguru_narration]
2025-01-31 02:33:42.576 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:181 - DocAnalysis init done!
2025-01-31 02:33:42.576 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:custom_model_init:141 - model init cost: 19.269118070602417
2025-01-31 02:33:42.576 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:doc_analyze:193 - gpu_memory: 8 GB, batch_ratio: 2
2025-01-31 02:41:13.741 | INFO     | magic_pdf.model.batch_analyze:__call__:74 - layout time: 421.29, image num: 2081
2025-01-31 02:48:23.183 | INFO     | magic_pdf.model.batch_analyze:__call__:85 - mfd time: 429.44, image num: 2081
2025-01-31 03:00:44.704 | INFO     | magic_pdf.model.batch_analyze:__call__:100 - mfr time: 741.52, image num: 14969
2025-01-31 03:00:47.317 | INFO     | magic_pdf.model.sub_modules.model_utils:clean_vram:50 - gc time: 2.6
2025-01-31 03:28:02.538 | INFO     | magic_pdf.model.batch_analyze:__call__:195 - det time: 271.24, image num: 30459
2025-01-31 03:28:02.538 | INFO     | magic_pdf.model.batch_analyze:__call__:197 - table time: 1354.89, image num: 3684
2025-01-31 03:28:25.932 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:doc_analyze:247 - gc time: 0.31
2025-01-31 03:28:25.932 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:doc_analyze:251 - doc analyze time: 3283.36, speed: 0.63 pages/second
2025-01-31 03:36:57.721 | INFO     | magic_pdf.data.dataset:__init__:156 - lang: None
2025-01-31 03:37:01.083 | INFO     | magic_pdf.libs.pdf_check:detect_invalid_chars:57 - cid_count: 12, text_len: 13590, cid_chars_radio: 0.0008892841262783459

MinerU__1646.md:116-121 [loguru_narration]
2025-02-18 16:23:20.103 | INFO     | __mp_main__:parse_pdf:164 - Load file completed, transferring to MinerU Dataset.
2025-02-18 16:23:20.123 | INFO     | magic_pdf.data.dataset:__init__:156 - lang: None
2025-02-18 16:23:20.123 | INFO     | __mp_main__:parse_pdf:166 - Transfer to Dataset completed, ready for the PARSING process.
2025-02-18 16:23:25.150 | INFO     | magic_pdf.libs.pdf_check:detect_invalid_chars:57 - cid_count: 0, text_len: 10, cid_chars_radio: 0.0
2025-02-18 16:23:25.151 | WARNING  | magic_pdf.filter.pdf_classify_by_type:classify:334 - pdf is not classified by area and text_len, by_image_area: False, by_text: False, by_avg_words: False, by_img_num: True, by_text_layout: False, by_img_narrow_strips: True, by_invalid_chars: True
2025-02-18 16:23:25.152 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:doc_analyze:193 - gpu_memory: 10 GB, batch_ratio: 4

MinerU__2237.md:12-15 [loguru_narration]
2025-04-15 15:55:57.005 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:82 - using device: cuda
2025-04-15 15:55:57.005 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:86 - using models_dir: /root/.cache/modelscope/hub/models/opendatalab/PDF-Extract-Kit-1___0/models
2025-04-15 15:56:01.718 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:164 - DocAnalysis init done!
2025-04-15 15:56:01.718 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:custom_model_init:116 - model init cost: 4.714559078216553

MinerU__260.md:39-43 [loguru_narration]
2024-07-31 20:22:42.076 | WARNING  | magic_pdf.cli.magicpdf:get_model_json:310 - not found json demo.json existed
2024-07-31 20:22:42.077 | INFO     | magic_pdf.cli.magicpdf:do_parse:91 - local output dir is /Users/yfeng/tmp_output/magic-pdf/demo/auto
2024-07-31 20:22:43.100 | INFO     | magic_pdf.libs.pdf_check:detect_invalid_chars:57 - cid_count: 1, text_len: 30267, cid_chars_radio: 3.304801877127466e-05
2024-07-31 20:23:35.813 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:92 - DocAnalysis init, this may take some times. apply_layout: True, apply_formula: True, apply_ocr: False
2024-07-31 20:23:35.813 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:100 - using device: mps

MinerU__2832.md:15-17 [loguru_narration]
2025-06-30 07:01:49.476 | WARNING  | mineru.backend.vlm.predictor:<module>:35 - sglang is not installed. If you are not using sglang, you can ignore this warning.
2025-06-30 07:05:12.987 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze:124 - Batch 1/2: 100 pages/160 pages
2025-06-30 07:05:13.020 | INFO     | mineru.backend.pipeline.model_init:__init__:137 - DocAnalysis init, this may take some times......

MinerU__2832.md:35-37 [loguru_narration]
2025-06-30 07:34:33.724 | WARNING  | mineru.backend.vlm.predictor:<module>:35 - sglang is not installed. If you are not using sglang, you can ignore this warning.
2025-06-30 07:37:27.161 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze:124 - Batch 1/2: 100 pages/138 pages
2025-06-30 07:37:27.206 | INFO     | mineru.backend.pipeline.model_init:__init__:137 - DocAnalysis init, this may take some times......

MinerU__322.md:52-55 [loguru_narration]
2024-08-05 14:10:24.153 | WARNING  | magic_pdf.cli.magicpdf:get_model_json:312 - not found json "pdf_path".json existed
2024-08-05 14:10:24.154 | WARNING  | magic_pdf.libs.config_reader:get_local_dir:64 - 'temp-output-dir' not found in magic-pdf.json, use '/tmp' as default
2024-08-05 14:10:24.378 | INFO     | magic_pdf.libs.pdf_check:detect_invalid_chars:57 - cid_count: 0, text_len: 2, cid_chars_radio: 0.0
2024-08-05 14:10:24.378 | WARNING  | magic_pdf.filter.pdf_classify_by_type:classify:334 - pdf is not classified by area and text_len, by_image_area: False, by_text: False, by_avg_words: False, by_img_num: True, by_text_layout: False, by_img_narrow_strips: True, by_invalid_chars: True

MinerU__322.md:57-59 [loguru_narration]
2024-08-05 14:10:32.531 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:99 - DocAnalysis init, this may take some times. apply_layout: True, apply_formula: True, apply_ocr: True
2024-08-05 14:10:32.532 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:107 - using device: cpu
2024-08-05 14:10:32.532 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:109 - using models_dir: E:\PDF-Extract-Kit\models

MinerU__322.md:448-450 [loguru_narration]
2024-08-05 14:11:00.031 | INFO     | magic_pdf.model.pdf_extract_kit:__init__:132 - DocAnalysis init done!
2024-08-05 14:11:00.032 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:custom_model_init:92 - model init cost: 35.65274977684021
2024-08-05 14:11:35.095 | INFO     | magic_pdf.model.pdf_extract_kit:__call__:143 - layout detection cost: 34.73

MinerU__322.md:454-456 [loguru_narration]
2024-08-05 14:11:42.570 | INFO     | magic_pdf.model.pdf_extract_kit:__call__:173 - formula nums: 0, mfr time: 0.0
2024-08-05 14:11:50.457 | INFO     | magic_pdf.model.pdf_extract_kit:__call__:250 - ocr cost: 7.89
2024-08-05 14:12:24.253 | INFO     | magic_pdf.model.pdf_extract_kit:__call__:143 - layout detection cost: 33.79

MinerU__322.md:460-468 [loguru_narration]
2024-08-05 14:12:29.161 | INFO     | magic_pdf.model.pdf_extract_kit:__call__:173 - formula nums: 0, mfr time: 0.0
2024-08-05 14:12:30.193 | INFO     | magic_pdf.model.pdf_extract_kit:__call__:250 - ocr cost: 1.03
2024-08-05 14:12:30.194 | INFO     | magic_pdf.model.doc_analyze_by_custom_model:doc_analyze:118 - doc analyze cost: 89.82563972473145
2024-08-05 14:12:30.260 | INFO     | magic_pdf.pdf_parse_union_core:pdf_parse_union:221 - page_id: 0, last_page_cost_time: 0.0
2024-08-05 14:12:30.480 | INFO     | magic_pdf.pdf_parse_union_core:pdf_parse_union:221 - page_id: 1, last_page_cost_time: 0.22
2024-08-05 14:12:30.802 | INFO     | magic_pdf.para.para_split_v2:__connect_middle_align_text:682 - 1.0
2024-08-05 14:12:30.848 | INFO     | magic_pdf.pipe.UNIPipe:pipe_mk_markdown:48 - uni_pipe mk mm_markdown finished
2024-08-05 14:12:30.865 | INFO     | magic_pdf.pipe.UNIPipe:pipe_mk_uni_format:43 - uni_pipe mk content list finished
2024-08-05 14:12:30.867 | INFO     | magic_pdf.cli.magicpdf:do_parse:165 - local output dir is '/tmp\magic-pdf\单个文件名\auto', you can found the result in it.`

MinerU__322.md:494-496 [loguru_narration]
2025-12-24 10:22:56.385 | WARNING  | mineru.utils.pdf_page_id:get_end_page_id:8 - end_page_id is out of range, use images length
2025-12-24 10:23:02.096 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze:128 - Batch 1/1: 93 pages/93 pages
2025-12-24 10:23:02.098 | INFO     | mineru.backend.pipeline.pipeline_analyze:batch_image_analyze:186 - GPU Memory: 8 GB, Batch Ratio: 4. You can set MINERU_VIRTUAL_VRAM_SIZE environment variable to adjust GPU memory allocation.

MinerU__4516.md:47-50 [loguru_narration]
2026-02-08 08:56:14.004 | INFO     | mineru.backend.vlm.vlm_analyze:get_model:218 - get vllm-engine predictor cost: 25.82s
2026-02-08 08:56:14.005 | DEBUG    | mineru.utils.pdf_image_tools:load_images_from_pdf:116 - PDF to images using 4 processes, page ranges: [(0, 1), (2, 3), (4, 5), (6, 9)]
2026-02-08 08:56:14.241 | DEBUG    | mineru.backend.hybrid.hybrid_analyze:doc_analyze:405 - load images cost: 0.24, speed: 41.667 images/s
2026-02-08 08:56:14.241 | INFO     | mineru.backend.hybrid.hybrid_analyze:get_batch_ratio:365 - hybrid batch ratio (auto, vram=24GB): 8

MinerU__4516.md:145-148 [loguru_narration]
2026-02-08 08:54:12.763 | INFO     | mineru.backend.vlm.vlm_analyze:get_model:218 - get vllm-engine predictor cost: 20.64s
2026-02-08 08:54:12.763 | DEBUG    | mineru.utils.pdf_image_tools:load_images_from_pdf:116 - PDF to images using 4 processes, page ranges: [(0, 1), (2, 3), (4, 5), (6, 9)]
2026-02-08 08:54:12.993 | DEBUG    | mineru.backend.hybrid.hybrid_analyze:doc_analyze:405 - load images cost: 0.23, speed: 43.478 images/s
2026-02-08 08:54:12.994 | INFO     | mineru.backend.hybrid.hybrid_analyze:get_batch_ratio:365 - hybrid batch ratio (auto, vram=24GB): 8

MinerU__4699.md:16-19 [loguru_narration]
2026-03-31 15:40:29.701 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:182 - Pipeline processing-window multi-file run. doc_count=1, total_pages=2, window_size=64, total_batches=1
2026-03-31 15:40:35.737 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:234 - Pipeline processing window batch 1/1: 2/2 pages, batch_pages=2, doc_slices=doc0:1-2
2026-03-31 15:40:35.739 | INFO     | mineru.backend.pipeline.pipeline_analyze:batch_image_analyze:327 - GPU Memory: 1 GB, Batch Ratio: 1. 
2026-03-31 15:40:35.739 | INFO     | mineru.backend.pipeline.model_init:__init__:206 - DocAnalysis init, this may take some times......

MinerU__4728.md:74-77 [loguru_narration]
2026-04-03 15:13:02.603 | INFO     | mineru.backend.vlm.vlm_analyze:get_model:238 - get vllm-async-engine predictor cost: 31.0s
2026-04-03 15:13:02.686 | INFO     | mineru.backend.hybrid.hybrid_analyze:aio_doc_analyze:702 - Hybrid processing-window run. page_count=25, window_size=64, total_windows=1
2026-04-03 15:13:02.686 | INFO     | mineru.backend.hybrid.hybrid_analyze:get_batch_ratio:511 - hybrid batch ratio (auto, vram=47GB): 16
2026-04-03 15:13:06.573 | INFO     | mineru.backend.hybrid.hybrid_analyze:aio_doc_analyze:724 - Hybrid processing window 1/1: pages 1-25/25 (25 pages)

MinerU__4882.md:117-125 [loguru_narration]
2026-04-29 22:34:00.065 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:183 - Pipeline processing-window multi-file run. doc_count=1, total_pages=13, window_size=64, total_batches=1
2026-04-29 22:34:00.065 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:183 - Pipeline processing-window multi-file run. doc_count=1, total_pages=6, window_size=64, total_batches=1
2026-04-29 22:34:03.245 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:235 - Pipeline processing window batch 1/1: 6/6 pages, batch_pages=6, doc_slices=doc0:1-6
2026-04-29 22:34:03.333 | INFO     | mineru.backend.pipeline.pipeline_analyze:batch_image_analyze:328 - GPU Memory: 8 GB, Batch Ratio: 4.
2026-04-29 22:34:03.333 | INFO     | mineru.backend.pipeline.model_init:__init__:207 - DocAnalysis init, this may take some times......
2026-04-29 22:34:03.548 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:235 - Pipeline processing window batch 1/1: 13/13 pages, batch_pages=13, doc_slices=doc0:1-13
2026-04-29 22:34:07.483 | INFO     | mineru.backend.pipeline.model_init:__init__:260 - DocAnalysis init done!
2026-04-29 22:34:07.483 | INFO     | mineru.backend.pipeline.pipeline_analyze:custom_model_init:83 - model init cost: 4.1497015953063965
2026-04-29 22:34:07.483 | INFO     | mineru.backend.pipeline.pipeline_analyze:batch_image_analyze:328 - GPU Memory: 8 GB, Batch Ratio: 4.

MinerU__4882.md:146-148 [loguru_narration]
2026-04-29 22:34:38.459 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:183 - Pipeline processing-window multi-file run. doc_count=1, total_pages=13, window_size=64, total_batches=1
2026-04-29 22:34:39.062 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:235 - Pipeline processing window batch 1/1: 13/13 pages, batch_pages=13, doc_slices=doc0:1-13
2026-04-29 22:34:39.062 | INFO     | mineru.backend.pipeline.pipeline_analyze:batch_image_analyze:328 - GPU Memory: 8 GB, Batch Ratio: 4.

MinerU__4884.md:59-64 [loguru_narration]
2026-04-29 18:25:27.696 | INFO     | mineru.cli.client:run_planned_task:771 - Submitting batch 1/1 | 1 document, 1 page in this batch | 1 page total | task#1 [book1]
2026-04-29 18:25:28.677 | DEBUG    | mineru.utils.pdf_page_id:get_end_page_id:8 - end_page_id is out of range, use images length
2026-04-29 18:25:33.154 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:183 - Pipeline processing-window multi-file run. doc_count=1, total_pages=1, window_size=64, total_batches=1
2026-04-29 18:25:33.154 | DEBUG    | mineru.utils.pdf_image_tools:_load_images_from_pdf_bytes_range:220 - PDF image rendering uses 1 processes for pages 1-1: [(0, 0)]
2026-04-29 18:25:33.154 | DEBUG    | mineru.utils.pdf_image_tools:_create_pdf_render_executor:139 - PDF image rendering switches multiprocessing start method from fork to spawn
2026-04-29 18:25:33.155 | DEBUG    | mineru.utils.pdf_image_tools:_get_pdf_render_executor:157 - Created persistent PDF render executor with max_workers=4

MinerU__5045.md:429-432 [loguru_narration]
2026-05-30 14:22:16.306 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:183 - Pipeline processing-window multi-file run. doc_count=1, total_pages=10, window_size=64, total_batches=1
2026-05-30 14:22:16.306 | DEBUG    | mineru.utils.pdf_image_tools:_load_images_from_pdf_bytes_range:224 - PDF image rendering uses 1 processes for pages 1-10: [(0, 9)]
2026-05-30 14:22:16.722 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:235 - Pipeline processing window batch 1/1: 10/10 pages, batch_pages=10, doc_slices=doc0:1-10
2026-05-30 14:22:16.722 | INFO     | mineru.backend.pipeline.pipeline_analyze:batch_image_analyze:328 - GPU Memory: 24 GB, Batch Ratio: 8. 

MinerU__5045.md:748-751 [loguru_narration]
2026-05-30 15:57:09.397 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:183 - Pipeline processing-window multi-file run. doc_count=1, total_pages=2, window_size=64, total_batches=1
2026-05-30 15:57:10.817 | INFO     | mineru.backend.pipeline.pipeline_analyze:doc_analyze_streaming:235 - Pipeline processing window batch 1/1: 2/2 pages, batch_pages=2, doc_slices=doc0:1-2
2026-05-30 15:57:10.885 | INFO     | mineru.backend.pipeline.pipeline_analyze:batch_image_analyze:328 - GPU Memory: 24 GB, Batch Ratio: 8. 
2026-05-30 15:57:10.885 | INFO     | mineru.backend.pipeline.model_init:__init__:214 - DocAnalysis init, this may take some times......

ghostty__10379.md:166-336 [ghostty_debug]
info(config): default shell src=passwd value=/bin/bash
info(config): default working directory src=passwd value=/home/mjbommar
warning(gtk_ghostty_application): setting GDK_DEBUG=opengl
warning(gtk_ghostty_application): setting GDK_DISABLE=gles-api,vulkan
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.fontconfig serial: 0
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-microphone
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-camera
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy old-files-age
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.privacy remember-recent-files: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-sound-output
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy send-software-usage-stats
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy report-technical-problems
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remove-old-trash-files
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remove-old-temp-files
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy privacy-screen
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy usb-protection
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy usb-protection-level
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remember-app-usage
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy show-full-name-in-top-bar
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy hide-identity
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.privacy recent-files-max-age: -1
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y.interface show-status-shapes: false
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y.interface high-contrast: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.a11y always-show-universal-access-status
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y always-show-text-caret: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolkit-accessibility
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-color-palette
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface can-change-accels
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface document-font-name
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface enable-animations: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-weekday
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface icon-theme: 'Yaru-sage'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-im-preedit-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface scaling-factor
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menus-have-tearoff
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-size: 24
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-seconds
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-im-module: ''
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-timeout-initial
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface accent-color
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-theme: 'Yaru-sage'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-color-scheme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-date
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink-time: 1200
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-icons-size
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-antialiasing: 'rgba'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface enable-hot-corners
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface monospace-font-name
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-timeout-repeat
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface overlay-scrolling: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink-timeout: 10
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-key-theme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-detachable
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-rendering: 'automatic'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-theme: 'Yaru'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface avatar-directories
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-im-status-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menubar-detachable
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface text-scaling-factor: 1.0
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface show-battery-percentage
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-format
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menubar-accel
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-enable-primary-paste: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface color-scheme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface locate-pointer
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-rgba-order: 'rgb'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-hinting: 'slight'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-name: 'Berkeley Mono Variable ZY761Y88 Thin 10 @wght=100'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound theme-name: 'Yaru'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound event-sounds: false
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound input-feedback-sounds: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.sound allow-volume-above-100-percent
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse left-handed
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.peripherals.mouse double-click: 400
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse natural-scroll
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse middle-click-emulation
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse speed
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse accel-profile
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.peripherals.mouse drag-threshold: 8
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources mru-sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources show-all-sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources current
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources xkb-options
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources xkb-model
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources per-window
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.calendar show-weekdate
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences theme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences focus-new-windows
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences disable-workarounds
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences num-workspaces
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences titlebar-uses-system-font
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences raise-on-click
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences titlebar-font
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences resize-with-right-button
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences auto-raise
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-right-click-titlebar: 'menu'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences mouse-button-modifier
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-double-click-titlebar: 'toggle-maximize'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences workspace-names
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences visual-bell-type
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-middle-click-titlebar: 'lower'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences focus-mode
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences button-layout: ':minimize,maximize,close'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences auto-raise-delay
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences audible-bell
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences visual-bell
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings overrides
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings disabled-gtk-modules
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings enabled-gtk-modules
debug(glib): DEBUG: GLib-GIO: _g_io_module_get_default: Found default implementation gvfs (GDaemonVfs) for ‘gio-vfs’
debug(glib): DEBUG: GLib-GIO: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
debug(glib): DEBUG: dconf: watch_fast: "/org/gnome/desktop/interface/" (establishing: 0, active: 0)
debug(glib): DEBUG: dconf: watch_established: "/org/gnome/desktop/interface/" (establishing: 1)
debug(glib): DEBUG: Adwaita: Using style /org/gnome/Adwaita/styles/defaults-light-yaru-sage.css
debug(winproto_wayland): found global wl_compositor
debug(winproto_wayland): found global wl_eglstream_display
debug(winproto_wayland): found global wl_drm
debug(winproto_wayland): found global wl_shm
debug(winproto_wayland): found global wl_output
debug(winproto_wayland): found global wl_output
debug(winproto_wayland): found global zxdg_output_manager_v1
debug(winproto_wayland): found global wl_data_device_manager
debug(winproto_wayland): found global xdg_toplevel_drag_manager_v1
debug(winproto_wayland): found global zwp_primary_selection_device_manager_v1
debug(winproto_wayland): found global wl_subcompositor
debug(winproto_wayland): found global xdg_wm_base
debug(winproto_wayland): found global gtk_shell1
debug(winproto_wayland): found global wp_viewporter
debug(winproto_wayland): found global wp_fractional_scale_manager_v1
debug(winproto_wayland): found global zwp_pointer_gestures_v1
debug(winproto_wayland): found global zwp_tablet_manager_v2
debug(winproto_wayland): found global wl_seat
debug(winproto_wayland): found global zwp_relative_pointer_manager_v1
debug(winproto_wayland): found global zwp_pointer_constraints_v1
debug(winproto_wayland): found global zxdg_exporter_v2
debug(winproto_wayland): found global zxdg_importer_v2
debug(winproto_wayland): found global zxdg_exporter_v1
debug(winproto_wayland): found global zxdg_importer_v1
debug(winproto_wayland): found global zwp_linux_dmabuf_v1
debug(winproto_wayland): found global wp_single_pixel_buffer_manager_v1
debug(winproto_wayland): found global zwp_keyboard_shortcuts_inhibit_manager_v1
debug(winproto_wayland): found global zwp_text_input_manager_v3
debug(winproto_wayland): found global wp_presentation
debug(winproto_wayland): found global xdg_activation_v1
debug(winproto_wayland): matched wayland.client.xdg.ActivationV1
debug(winproto_wayland): found global zwp_idle_inhibit_manager_v1
debug(winproto_wayland): found global wp_linux_drm_syncobj_manager_v1
debug(winproto_wayland): found global xdg_wm_dialog_v1
debug(winproto_wayland): found global wp_color_manager_v1
debug(winproto_wayland): found global xdg_system_bell_v1
debug(winproto_wayland): found global wp_drm_lease_device_v1
debug(winproto_wayland): found global wp_drm_lease_device_v1
debug(winproto_wayland): found global wp_commit_timing_manager_v1
debug(winproto_wayland): found global wp_fifo_manager_v1
debug(winproto_wayland): found global wp_cursor_shape_manager_v1
debug(gtk_ghostty_application): windowing protocol=wayland
debug(gtk_ghostty_application): creating GTK application id=com.mitchellh.ghostty-debug single-instance=true
debug(gtk_ghostty_application): runtime CSS is 911 bytes
debug(gtk_ghostty_application): startup
debug(glib): DEBUG: Gtk: Not using session manager
debug(glib): DEBUG: Adwaita: Using style /org/gnome/Adwaita/styles/defaults-dark-yaru-sage.css
debug(gtk_ghostty_application): style manager changed scheme=.dark
debug(gtk_ghostty_application): runtime CSS is 911 bytes
info(gtk_systemd_cgroup): transient scope created cgroup=/user.slice/user-1000.slice/user@1000.service/app.slice/app-ghostty-transient-34003.scope
info(gtk_ghostty_application): cgroup isolation enabled base=/user.slice/user-1000.slice/user@1000.service/app.slice/app-ghostty-transient-34003.scope
debug(gtk_ghostty_application): activate
debug(gtk_ghostty_application): entering runloop
debug(app): mailbox message=new_window

ghostty__10379.md:429-435 [ghostty_debug]
debug(glib): DEBUG: Gtk: snapshot symbolic icon using mask
debug(glib): DEBUG: Gtk: snapshot symbolic icon using mask
debug(glib): DEBUG: Gtk: snapshot symbolic icon using mask
debug(glib): DEBUG: Gtk: snapshot symbolic icon using mask
debug(glib): DEBUG: Gtk: snapshot symbolic icon using mask
debug(glib): DEBUG: Gtk: snapshot symbolic icon using mask
debug(glib): DEBUG: Gtk: snapshot symbolic icon using mask

ghostty__10379.md:445-509 [ghostty_debug]
debug(gtk_ghostty_surface): gl resize width=800 height=513 scale=1 window_scale=1
info(opengl): loaded OpenGL 4.6
debug(surface): xscale=1 yscale=1 xdpi=96 ydpi=96
debug(font_shared_grid_set): initializing new grid for font config
info(font_shared_grid_set): font regular: Berkeley Mono Variable ZY761Y88 Regular
info(font_shared_grid_set): font bold: Berkeley Mono Variable ZY761Y88 Bold
info(font_shared_grid_set): font italic: Berkeley Mono Variable ZY761Y88 Oblique
info(font_shared_grid_set): font bold_italic: Berkeley Mono Variable ZY761Y88 Bold Oblique
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=Berkeley Mono Variable ZY761Y88
debug(font_face): variation axis: name=Weight id=wght min=100 max=900 def=400
debug(font_face): variation axis: name=Width id=wdth min=60 max=100 def=100
debug(font_face): variation axis: name=Slant id=slnt min=-16 max=0 def=0
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(opengl): shader created id=1
debug(opengl): shader created id=2
debug(opengl): program created id=14
debug(opengl): program linked id=14
debug(opengl): shader destroyed id=2
debug(opengl): shader destroyed id=1
debug(opengl): shader created id=15
debug(opengl): shader created id=16
debug(opengl): program created id=17
debug(opengl): program linked id=17
debug(opengl): shader destroyed id=16
debug(opengl): shader destroyed id=15
debug(opengl): shader created id=18
debug(opengl): shader created id=19
debug(opengl): program created id=20
debug(opengl): program linked id=20
debug(opengl): shader destroyed id=19
debug(opengl): shader destroyed id=18
debug(opengl): shader created id=21
debug(opengl): shader created id=22
debug(opengl): program created id=23
debug(opengl): program linked id=23
debug(opengl): shader destroyed id=22
debug(opengl): shader destroyed id=21
debug(opengl): shader created id=24
debug(opengl): shader created id=25
debug(opengl): program created id=26
debug(opengl): program linked id=26
debug(opengl): shader destroyed id=25
debug(opengl): shader destroyed id=24
info(io_exec): found Ghostty resources dir: /home/mjbommar/src/ghostty/zig-out/share/ghostty
debug(io_exec): appending ghostty bin to path dir=/home/mjbommar/src/ghostty/zig-out/bin
info(io_exec): shell integration automatically injected shell=.bash
warning(gtk_ghostty_application): unimplemented action=.cell_size
debug(renderer_thread): starting renderer thread
debug(io_exec): starting command command=`/bin/sh`, `-c`, `/bin/bash --posix`
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 3 (bound to GL_ARRAY_BUFFER_ARB, usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 6 (bound to GL_ARRAY_BUFFER_ARB, usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
info(io_exec): started subcommand path=/bin/sh pid=34039
info(io_exec): subcommand cgroup=/user.slice/user-1000.slice/user@1000.service/app.slice/app-ghostty-transient-34003.scope/surfaces/1C3E8A70.scope
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 3 (bound to GL_UNIFORM_BUFFER (1), and GL_UNIFORM_BUFFER_EXT, usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 3 (bound to GL_UNIFORM_BUFFER (1), and GL_UNIFORM_BUFFER_EXT, usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 5 (bound to GL_SHADER_STORAGE_BUFFER, and GL_SHADER_STORAGE_BUFFER (1), usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 5 (bound to GL_SHADER_STORAGE_BUFFER, and GL_SHADER_STORAGE_BUFFER (1), usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 5 (bound to GL_SHADER_STORAGE_BUFFER, and GL_SHADER_STORAGE_BUFFER (1), usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.

ghostty__10379.md:518-521 [ghostty_debug]
debug(io_thread): starting IO thread
debug(io_thread): mailbox message=resize
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface

ghostty__10379.md:523-605 [ghostty_debug]
debug(gtk_ghostty_surface): gl resize width=1008 height=729 scale=1 window_scale=1
debug(io_thread): mailbox message=resize
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 5 (bound to GL_ARRAY_BUFFER_ARB, GL_SHADER_STORAGE_BUFFER, and GL_SHADER_STORAGE_BUFFER (1), usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 5 (bound to GL_SHADER_STORAGE_BUFFER, and GL_SHADER_STORAGE_BUFFER (1), usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 5 (bound to GL_SHADER_STORAGE_BUFFER, and GL_SHADER_STORAGE_BUFFER (1), usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(app): mailbox message=surface_message
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .resize = .{ .screen = .{ .width = 1008, .height = 729 }, .cell = .{ .width = 8, .height = 19 }, .padding = .{ .top = 22, .bottom = 22, .right = 24, .left = 24 } } }
debug(generic_renderer): screen size size=.{ .screen = .{ .width = 1008, .height = 729 }, .cell = .{ .width = 8, .height = 19 }, .padding = .{ .top = 22, .bottom = 22, .right = 24, .left = 24 } }
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=surface_message
debug(renderer_thread): mailbox message=.{ .reset_cursor_blink = void }
debug(io_handler): terminal pwd: /home/mjbommar
debug(app): mailbox message=surface_message
debug(app): mailbox message=surface_message
debug(surface): changing title "/home/mjbommar"
debug(app): mailbox message=surface_message
debug(surface): changing title "~"
debug(font_face): variation axes font=Berkeley Mono Variable ZY761Y88
debug(font_face): variation axis: name=Weight id=wght min=100 max=900 def=400
debug(font_face): variation axis: name=Width id=wdth min=60 max=100 def=100
debug(font_face): variation axis: name=Slant id=slnt min=-16 max=0 def=0
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(opengl): [131185] (OpenGL API: Other) Buffer detailed info: Buffer object 4 (bound to GL_ARRAY_BUFFER_ARB, usage hint is GL_DYNAMIC_DRAW) will use VIDEO memory as the source for buffer object operations.
debug(io_exec): termios change mode=.{ .canonical = false, .echo = false }
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(renderer_thread): mailbox message=.{ .reset_cursor_blink = void }
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(renderer_thread): mailbox message=.{ .reset_cursor_blink = void }
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(renderer_thread): mailbox message=.{ .reset_cursor_blink = void }
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=write_small
debug(app): mailbox message=redraw_surface

ghostty__10406.md:128-298 [ghostty_debug]
debug(config): config has 'keybind = vimscroll/', table cleared
info(config): config-default-files unset, discarding configuration from default files
warning(gtk_ghostty_application): setting GDK_DEBUG=opengl
warning(gtk_ghostty_application): setting GDK_DISABLE=gles-api,vulkan
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.fontconfig serial: 0
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-microphone
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-camera
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy old-files-age
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.privacy remember-recent-files: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-sound-output
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy send-software-usage-stats
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy report-technical-problems
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remove-old-trash-files
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remove-old-temp-files
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy privacy-screen
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy usb-protection
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy usb-protection-level
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remember-app-usage
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy show-full-name-in-top-bar
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy hide-identity
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.privacy recent-files-max-age: -1
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y.interface show-status-shapes: false
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y.interface high-contrast: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.a11y always-show-universal-access-status
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y always-show-text-caret: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolkit-accessibility
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-color-palette
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface can-change-accels
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface document-font-name
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface enable-animations: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-weekday
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface icon-theme: 'Adwaita'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-im-preedit-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface scaling-factor
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menus-have-tearoff
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-size: 24
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-seconds
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-im-module: ''
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-timeout-initial
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface accent-color
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-theme: 'Adwaita'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-color-scheme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-date
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink-time: 1200
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-icons-size
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-antialiasing: 'rgba'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface enable-hot-corners
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface monospace-font-name
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-timeout-repeat
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface overlay-scrolling: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink-timeout: 10
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-key-theme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-detachable
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-rendering: 'automatic'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-theme: 'Adwaita'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface avatar-directories
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-im-status-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menubar-detachable
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface text-scaling-factor: 1.0
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface show-battery-percentage
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-format
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menubar-accel
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-enable-primary-paste: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface color-scheme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface locate-pointer
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-rgba-order: 'rgb'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-hinting: 'full'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-name: 'Adwaita Sans 11'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound theme-name: '__custom'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound event-sounds: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound input-feedback-sounds: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.sound allow-volume-above-100-percent
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse left-handed
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.peripherals.mouse double-click: 400
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse natural-scroll
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse middle-click-emulation
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse speed
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse accel-profile
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.peripherals.mouse drag-threshold: 8
debug(glib): DEBUG: Gdk: Using portal setting for org.freedesktop.appearance contrast: 0
debug(glib): DEBUG: Gdk: Using portal setting for org.freedesktop.appearance color-scheme: 1
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.freedesktop.appearance accent-color
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources mru-sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources show-all-sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources current
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources xkb-options
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources xkb-model
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources per-window
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.calendar show-weekdate
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences theme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences focus-new-windows
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences disable-workarounds
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences num-workspaces
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences titlebar-uses-system-font
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences raise-on-click
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences titlebar-font
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences resize-with-right-button
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences auto-raise
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-right-click-titlebar: 'menu'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences mouse-button-modifier
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-double-click-titlebar: 'toggle-maximize'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences workspace-names
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences visual-bell-type
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-middle-click-titlebar: 'none'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences focus-mode
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences button-layout: 'appmenu:minimize,maximize,close'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences auto-raise-delay
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences audible-bell
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences visual-bell
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings overrides
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings disabled-gtk-modules
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings enabled-gtk-modules
debug(glib): DEBUG: GLib-GIO: _g_io_module_get_default: Found default implementation gvfs (GDaemonVfs) for ‘gio-vfs’
debug(glib): DEBUG: GLib-GIO: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
debug(glib): DEBUG: dconf: watch_fast: "/org/gnome/desktop/interface/" (establishing: 0, active: 0)
debug(glib): DEBUG: dconf: watch_established: "/org/gnome/desktop/interface/" (establishing: 1)
debug(winproto_wayland): found global wl_compositor
debug(winproto_wayland): found global wl_shm
debug(winproto_wayland): found global wl_output
debug(winproto_wayland): found global wl_output
debug(winproto_wayland): found global zxdg_output_manager_v1
debug(winproto_wayland): found global wl_data_device_manager
debug(winproto_wayland): found global xdg_toplevel_drag_manager_v1
debug(winproto_wayland): found global zwp_primary_selection_device_manager_v1
debug(winproto_wayland): found global wl_subcompositor
debug(winproto_wayland): found global xdg_wm_base
debug(winproto_wayland): found global gtk_shell1
debug(winproto_wayland): found global wp_viewporter
debug(winproto_wayland): found global wp_fractional_scale_manager_v1
debug(winproto_wayland): found global zwp_pointer_gestures_v1
debug(winproto_wayland): found global zwp_tablet_manager_v2
debug(winproto_wayland): found global wp_pointer_warp_v1
debug(winproto_wayland): found global wl_seat
debug(winproto_wayland): found global zwp_relative_pointer_manager_v1
debug(winproto_wayland): found global zwp_pointer_constraints_v1
debug(winproto_wayland): found global zxdg_exporter_v2
debug(winproto_wayland): found global zxdg_importer_v2
debug(winproto_wayland): found global zxdg_exporter_v1
debug(winproto_wayland): found global zxdg_importer_v1
debug(winproto_wayland): found global zwp_linux_dmabuf_v1
debug(winproto_wayland): found global wp_single_pixel_buffer_manager_v1
debug(winproto_wayland): found global zwp_keyboard_shortcuts_inhibit_manager_v1
debug(winproto_wayland): found global zwp_text_input_manager_v3
debug(winproto_wayland): found global wp_presentation
debug(winproto_wayland): found global xdg_activation_v1
debug(winproto_wayland): matched wayland.client.xdg.ActivationV1
debug(winproto_wayland): found global zwp_idle_inhibit_manager_v1
debug(winproto_wayland): found global wp_linux_drm_syncobj_manager_v1
debug(winproto_wayland): found global xdg_wm_dialog_v1
debug(winproto_wayland): found global wp_color_manager_v1
debug(winproto_wayland): found global xdg_system_bell_v1
debug(winproto_wayland): found global xdg_toplevel_tag_manager_v1
debug(winproto_wayland): found global wp_drm_lease_device_v1
debug(winproto_wayland): found global wp_commit_timing_manager_v1
debug(winproto_wayland): found global wp_fifo_manager_v1
debug(winproto_wayland): found global wp_cursor_shape_manager_v1
debug(winproto_wayland): found global wp_color_representation_manager_v1
debug(winproto_wayland): found global wl_fixes
debug(gtk_ghostty_application): windowing protocol=wayland
debug(gtk_ghostty_application): creating GTK application id=com.mitchellh.ghostty-debug single-instance=false
debug(gtk_ghostty_application): runtime CSS is 1019 bytes
debug(gtk_ghostty_application): startup
debug(gtk_ghostty_application): style manager changed scheme=.dark
debug(gtk_ghostty_application): runtime CSS is 1019 bytes
info(gtk_ghostty_application): cgroup isolation disabled via config=.single-instance
debug(gtk_ghostty_application): activate
debug(gtk_ghostty_application): entering runloop
debug(app): mailbox message=new_window

ghostty__10406.md:365-371 [ghostty_debug]
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node

ghostty__10406.md:383-446 [ghostty_debug]
debug(gtk_ghostty_surface): gl resize width=800 height=512 scale=1 window_scale=1
info(opengl): loaded OpenGL 4.6
debug(surface): xscale=1 yscale=1 xdpi=96 ydpi=96
debug(font_shared_grid_set): initializing new grid for font config
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(opengl): shader created id=1
debug(opengl): shader created id=2
debug(opengl): program created id=16
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 56 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): program linked id=16
debug(opengl): shader destroyed id=2
debug(opengl): shader destroyed id=1
debug(opengl): shader created id=17
debug(opengl): shader created id=18
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 260 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): program created id=19
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 56 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): program linked id=19
debug(opengl): shader destroyed id=18
debug(opengl): shader destroyed id=17
debug(opengl): shader created id=20
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 736 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): shader created id=21
debug(opengl): program created id=22
debug(opengl): program linked id=22
debug(opengl): shader destroyed id=21
debug(opengl): shader destroyed id=20
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 64 VGPRS: 32 Code Size: 1412 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 3 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): shader created id=23
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 928 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): shader created id=24
debug(opengl): program created id=25
debug(opengl): program linked id=25
debug(opengl): shader destroyed id=24
debug(opengl): shader destroyed id=23
debug(opengl): shader created id=26
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 48 VGPRS: 12 Code Size: 356 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 1 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 296 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): shader created id=27
debug(opengl): program created id=28
debug(opengl): program linked id=28
debug(opengl): shader destroyed id=27
debug(opengl): shader destroyed id=26
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 836 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 3 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 48 VGPRS: 24 Code Size: 684 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
info(io_exec): found Ghostty resources dir: /home/jeff/dev/ghostty/zig-out/share/ghostty
debug(io_exec): appending ghostty bin to path dir=/home/jeff/dev/ghostty/zig-out/bin
info(io_exec): shell integration automatically injected shell=.fish
warning(gtk_ghostty_application): unimplemented action=.cell_size
debug(renderer_thread): starting renderer thread
debug(io_exec): starting command command=`/bin/sh`, `-c`, `fish`
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 60 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 132 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 1 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
info(io_exec): started subcommand path=/bin/sh pid=786525
info(io_exec): subcommand cgroup=-
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 60 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 32 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (CS, W64)

ghostty__10406.md:457-502 [ghostty_debug]
debug(io_thread): starting IO thread
debug(io_thread): mailbox message=resize
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .resize = .{ .screen = .{ .width = 800, .height = 512 }, .cell = .{ .width = 10, .height = 21 }, .padding = .{ .top = 2, .bottom = 2, .right = 2, .left = 2 } } }
debug(generic_renderer): screen size size=.{ .screen = .{ .width = 800, .height = 512 }, .cell = .{ .width = 10, .height = 21 }, .padding = .{ .top = 2, .bottom = 2, .right = 2, .left = 2 } }
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 36 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (CS, W64)
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=surface_message
debug(renderer_thread): mailbox message=.{ .reset_cursor_blink = void }
debug(io_handler): querying kitty keyboard mode
debug(io_handler): reporting XTVERSION: ghostty 1.3.0-my-stuff+7e6d8a2d8
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_stable
debug(io_thread): mailbox message=write_stable
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 64 VGPRS: 32 Code Size: 1416 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 3 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(io_handler): terminal pwd: /home/jeff/dev/ghostty
debug(app): mailbox message=surface_message
debug(app): mailbox message=surface_message
debug(surface): changing title "/home/jeff/dev/ghostty"
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=surface_message
debug(io_handler): terminal pwd: /home/jeff/dev/ghostty
debug(app): mailbox message=surface_message
debug(app): mailbox message=surface_message
debug(surface): changing title "/home/jeff/dev/ghostty"
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=surface_message
debug(surface): changing title "👻 🐟 jeff@home04 — ~/d/ghostty — fish"
debug(io_handler): setting kitty keyboard mode: set .{ .disambiguate = true, .report_events = false, .report_alternates = true, .report_all = false, .report_associated = false }
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_stable
debug(app): mailbox message=redraw_surface
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 4 Code Size: 52 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (CS, W64)
debug(app): mailbox message=redraw_surface
debug(io_exec): termios change mode=.{ .canonical = false, .echo = false }
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface

ghostty__10406.md:514-540 [ghostty_debug]
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .focus = false }
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(renderer_thread): mailbox message=.{ .focus = true }
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=inspector
debug(renderer_thread): mailbox message=.{ .inspector = true }

ghostty__10406.md:564-574 [ghostty_debug]
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(app): mailbox message=redraw_inspector
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .focus = false }
debug(app): mailbox message=redraw_inspector
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_inspector
debug(app): mailbox message=redraw_surface

ghostty__10406.md:577-594 [ghostty_debug]
debug(io_thread): mailbox message=inspector
debug(renderer_thread): mailbox message=.{ .inspector = false }
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .focus = true }
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=inspector
debug(renderer_thread): mailbox message=.{ .inspector = true }

ghostty__10406.md:756-926 [ghostty_debug]
debug(config): config has 'keybind = vimscroll/', table cleared
info(config): config-default-files unset, discarding configuration from default files
warning(gtk_ghostty_application): setting GDK_DEBUG=opengl
warning(gtk_ghostty_application): setting GDK_DISABLE=gles-api,vulkan
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.fontconfig serial: 0
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-microphone
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-camera
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy old-files-age
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.privacy remember-recent-files: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy disable-sound-output
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy send-software-usage-stats
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy report-technical-problems
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remove-old-trash-files
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remove-old-temp-files
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy privacy-screen
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy usb-protection
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy usb-protection-level
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy remember-app-usage
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy show-full-name-in-top-bar
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.privacy hide-identity
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.privacy recent-files-max-age: -1
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y.interface show-status-shapes: false
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y.interface high-contrast: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.a11y always-show-universal-access-status
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.a11y always-show-text-caret: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolkit-accessibility
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-color-palette
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface can-change-accels
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface document-font-name
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface enable-animations: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-weekday
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface icon-theme: 'Adwaita'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-im-preedit-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface scaling-factor
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menus-have-tearoff
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-size: 24
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-seconds
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-im-module: ''
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-timeout-initial
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface accent-color
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-theme: 'Adwaita'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-color-scheme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-show-date
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink-time: 1200
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-icons-size
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-antialiasing: 'rgba'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface enable-hot-corners
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface monospace-font-name
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-timeout-repeat
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface overlay-scrolling: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-blink-timeout: 10
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-key-theme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface toolbar-detachable
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-rendering: 'automatic'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface cursor-theme: 'Adwaita'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface avatar-directories
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface gtk-im-status-style
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menubar-detachable
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface text-scaling-factor: 1.0
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface show-battery-percentage
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface clock-format
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface menubar-accel
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface gtk-enable-primary-paste: true
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface color-scheme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.interface locate-pointer
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-rgba-order: 'rgb'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-hinting: 'full'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.interface font-name: 'Adwaita Sans 11'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound theme-name: '__custom'
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound event-sounds: true
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.sound input-feedback-sounds: false
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.sound allow-volume-above-100-percent
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse left-handed
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.peripherals.mouse double-click: 400
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse natural-scroll
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse middle-click-emulation
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse speed
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.peripherals.mouse accel-profile
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.peripherals.mouse drag-threshold: 8
debug(glib): DEBUG: Gdk: Using portal setting for org.freedesktop.appearance contrast: 0
debug(glib): DEBUG: Gdk: Using portal setting for org.freedesktop.appearance color-scheme: 1
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.freedesktop.appearance accent-color
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources mru-sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources show-all-sources
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources current
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources xkb-options
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources xkb-model
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.input-sources per-window
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.calendar show-weekdate
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences theme
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences focus-new-windows
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences disable-workarounds
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences num-workspaces
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences titlebar-uses-system-font
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences raise-on-click
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences titlebar-font
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences resize-with-right-button
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences auto-raise
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-right-click-titlebar: 'menu'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences mouse-button-modifier
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-double-click-titlebar: 'toggle-maximize'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences workspace-names
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences visual-bell-type
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences action-middle-click-titlebar: 'none'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences focus-mode
debug(glib): DEBUG: Gdk: Using portal setting for org.gnome.desktop.wm.preferences button-layout: 'appmenu:minimize,maximize,close'
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences auto-raise-delay
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences audible-bell
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.desktop.wm.preferences visual-bell
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings overrides
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings disabled-gtk-modules
debug(glib): DEBUG: Gdk: Ignoring portal setting for org.gnome.settings-daemon.plugins.xsettings enabled-gtk-modules
debug(glib): DEBUG: GLib-GIO: _g_io_module_get_default: Found default implementation gvfs (GDaemonVfs) for ‘gio-vfs’
debug(glib): DEBUG: GLib-GIO: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
debug(glib): DEBUG: dconf: watch_fast: "/org/gnome/desktop/interface/" (establishing: 0, active: 0)
debug(glib): DEBUG: dconf: watch_established: "/org/gnome/desktop/interface/" (establishing: 1)
debug(winproto_wayland): found global wl_compositor
debug(winproto_wayland): found global wl_shm
debug(winproto_wayland): found global wl_output
debug(winproto_wayland): found global wl_output
debug(winproto_wayland): found global zxdg_output_manager_v1
debug(winproto_wayland): found global wl_data_device_manager
debug(winproto_wayland): found global xdg_toplevel_drag_manager_v1
debug(winproto_wayland): found global zwp_primary_selection_device_manager_v1
debug(winproto_wayland): found global wl_subcompositor
debug(winproto_wayland): found global xdg_wm_base
debug(winproto_wayland): found global gtk_shell1
debug(winproto_wayland): found global wp_viewporter
debug(winproto_wayland): found global wp_fractional_scale_manager_v1
debug(winproto_wayland): found global zwp_pointer_gestures_v1
debug(winproto_wayland): found global zwp_tablet_manager_v2
debug(winproto_wayland): found global wp_pointer_warp_v1
debug(winproto_wayland): found global wl_seat
debug(winproto_wayland): found global zwp_relative_pointer_manager_v1
debug(winproto_wayland): found global zwp_pointer_constraints_v1
debug(winproto_wayland): found global zxdg_exporter_v2
debug(winproto_wayland): found global zxdg_importer_v2
debug(winproto_wayland): found global zxdg_exporter_v1
debug(winproto_wayland): found global zxdg_importer_v1
debug(winproto_wayland): found global zwp_linux_dmabuf_v1
debug(winproto_wayland): found global wp_single_pixel_buffer_manager_v1
debug(winproto_wayland): found global zwp_keyboard_shortcuts_inhibit_manager_v1
debug(winproto_wayland): found global zwp_text_input_manager_v3
debug(winproto_wayland): found global wp_presentation
debug(winproto_wayland): found global xdg_activation_v1
debug(winproto_wayland): matched wayland.client.xdg.ActivationV1
debug(winproto_wayland): found global zwp_idle_inhibit_manager_v1
debug(winproto_wayland): found global wp_linux_drm_syncobj_manager_v1
debug(winproto_wayland): found global xdg_wm_dialog_v1
debug(winproto_wayland): found global wp_color_manager_v1
debug(winproto_wayland): found global xdg_system_bell_v1
debug(winproto_wayland): found global xdg_toplevel_tag_manager_v1
debug(winproto_wayland): found global wp_drm_lease_device_v1
debug(winproto_wayland): found global wp_commit_timing_manager_v1
debug(winproto_wayland): found global wp_fifo_manager_v1
debug(winproto_wayland): found global wp_cursor_shape_manager_v1
debug(winproto_wayland): found global wp_color_representation_manager_v1
debug(winproto_wayland): found global wl_fixes
debug(gtk_ghostty_application): windowing protocol=wayland
debug(gtk_ghostty_application): creating GTK application id=com.mitchellh.ghostty-debug single-instance=false
debug(gtk_ghostty_application): runtime CSS is 1019 bytes
debug(gtk_ghostty_application): startup
debug(gtk_ghostty_application): style manager changed scheme=.dark
debug(gtk_ghostty_application): runtime CSS is 1019 bytes
info(gtk_ghostty_application): cgroup isolation disabled via config=.single-instance
debug(gtk_ghostty_application): activate
debug(gtk_ghostty_application): entering runloop
debug(app): mailbox message=new_window

ghostty__10406.md:993-999 [ghostty_debug]
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node

ghostty__10406.md:1011-1074 [ghostty_debug]
debug(gtk_ghostty_surface): gl resize width=800 height=512 scale=1 window_scale=1
info(opengl): loaded OpenGL 4.6
debug(surface): xscale=1 yscale=1 xdpi=96 ydpi=96
debug(font_shared_grid_set): initializing new grid for font config
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(font_face): variation axes font=JetBrains Mono
debug(font_face): variation axis: name=Weight id=wght min=100 max=800 def=400
debug(opengl): shader created id=1
debug(opengl): shader created id=2
debug(opengl): program created id=16
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 56 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): program linked id=16
debug(opengl): shader destroyed id=2
debug(opengl): shader destroyed id=1
debug(opengl): shader created id=17
debug(opengl): shader created id=18
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 260 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): program created id=19
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 56 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): program linked id=19
debug(opengl): shader destroyed id=18
debug(opengl): shader destroyed id=17
debug(opengl): shader created id=20
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 736 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): shader created id=21
debug(opengl): program created id=22
debug(opengl): program linked id=22
debug(opengl): shader destroyed id=21
debug(opengl): shader destroyed id=20
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 64 VGPRS: 32 Code Size: 1412 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 3 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): shader created id=23
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 928 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): shader created id=24
debug(opengl): program created id=25
debug(opengl): program linked id=25
debug(opengl): shader destroyed id=24
debug(opengl): shader destroyed id=23
debug(opengl): shader created id=26
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 48 VGPRS: 12 Code Size: 356 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 1 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 296 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): shader created id=27
debug(opengl): program created id=28
debug(opengl): program linked id=28
debug(opengl): shader destroyed id=27
debug(opengl): shader destroyed id=26
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 16 Code Size: 836 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 3 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 48 VGPRS: 24 Code Size: 684 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
info(io_exec): found Ghostty resources dir: /home/jeff/dev/ghostty/zig-out/share/ghostty
debug(io_exec): appending ghostty bin to path dir=/home/jeff/dev/ghostty/zig-out/bin
info(io_exec): shell integration automatically injected shell=.fish
warning(gtk_ghostty_application): unimplemented action=.cell_size
debug(renderer_thread): starting renderer thread
debug(io_exec): starting command command=`/bin/sh`, `-c`, `fish`
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 60 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 132 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 1 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
info(io_exec): started subcommand path=/bin/sh pid=786525
info(io_exec): subcommand cgroup=-
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 16 Code Size: 60 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 1 InlineUniforms: 0 DivergentLoop: 0 (PS, W64)
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 32 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (CS, W64)

ghostty__10406.md:1085-1130 [ghostty_debug]
debug(io_thread): starting IO thread
debug(io_thread): mailbox message=resize
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .resize = .{ .screen = .{ .width = 800, .height = 512 }, .cell = .{ .width = 10, .height = 21 }, .padding = .{ .top = 2, .bottom = 2, .right = 2, .left = 2 } } }
debug(generic_renderer): screen size size=.{ .screen = .{ .width = 800, .height = 512 }, .cell = .{ .width = 10, .height = 21 }, .padding = .{ .top = 2, .bottom = 2, .right = 2, .left = 2 } }
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 16 VGPRS: 4 Code Size: 36 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (CS, W64)
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=surface_message
debug(renderer_thread): mailbox message=.{ .reset_cursor_blink = void }
debug(io_handler): querying kitty keyboard mode
debug(io_handler): reporting XTVERSION: ghostty 1.3.0-my-stuff+7e6d8a2d8
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_stable
debug(io_thread): mailbox message=write_stable
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 64 VGPRS: 32 Code Size: 1416 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 3 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (VS, W64)
debug(io_handler): terminal pwd: /home/jeff/dev/ghostty
debug(app): mailbox message=surface_message
debug(app): mailbox message=surface_message
debug(surface): changing title "/home/jeff/dev/ghostty"
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=surface_message
debug(io_handler): terminal pwd: /home/jeff/dev/ghostty
debug(app): mailbox message=surface_message
debug(app): mailbox message=surface_message
debug(surface): changing title "/home/jeff/dev/ghostty"
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=surface_message
debug(surface): changing title "👻 🐟 jeff@home04 — ~/d/ghostty — fish"
debug(io_handler): setting kitty keyboard mode: set .{ .disambiguate = true, .report_events = false, .report_alternates = true, .report_all = false, .report_associated = false }
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_small
debug(io_thread): mailbox message=write_stable
debug(app): mailbox message=redraw_surface
debug(opengl): [1] (Shader Compiler: Other) Shader Stats: SGPRS: 32 VGPRS: 4 Code Size: 52 LDS: 0 Scratch: 0 Max Waves: 8 Spilled SGPRs: 0 Spilled VGPRs: 0 PrivMem VGPRs: 0 LSOutputs: 0 HSOutputs: 0 HSPatchOuts: 0 ESOutputs: 0 GSOutputs: 0 VSOutputs: 0 PSOutputs: 0 InlineUniforms: 0 DivergentLoop: 0 (CS, W64)
debug(app): mailbox message=redraw_surface
debug(io_exec): termios change mode=.{ .canonical = false, .echo = false }
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface

ghostty__10406.md:1142-1168 [ghostty_debug]
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .focus = false }
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(renderer_thread): mailbox message=.{ .focus = true }
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=inspector
debug(renderer_thread): mailbox message=.{ .inspector = true }

ghostty__10406.md:1192-1202 [ghostty_debug]
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(glib): DEBUG: Gtk: snapshot symbolic icon as recolored node
debug(app): mailbox message=redraw_inspector
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .focus = false }
debug(app): mailbox message=redraw_inspector
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_inspector
debug(app): mailbox message=redraw_surface

ghostty__10406.md:1205-1222 [ghostty_debug]
debug(io_thread): mailbox message=inspector
debug(renderer_thread): mailbox message=.{ .inspector = false }
debug(app): mailbox message=redraw_surface
debug(renderer_thread): mailbox message=.{ .focus = true }
debug(io_thread): mailbox message=focused
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(app): mailbox message=redraw_surface
debug(io_thread): mailbox message=inspector
debug(renderer_thread): mailbox message=.{ .inspector = true }

ghostty__10432.md:535-539 [ghostty_debug]
info(font_codepoint_resolver): found codepoint 0x2315 in fallback face=DejaVu Sans Mono
info(page_list): adjusting page capacity=.{ .cols = 83, .rows = 556, .styles = 128, .hyperlink_bytes = 384, .grapheme_bytes = 8192, .string_bytes = 2048 }
info(font_codepoint_resolver): found codepoint 0x23BF in fallback face=Noto Sans Mono CJK JP
info(page_list): adjusting page capacity=.{ .cols = 83, .rows = 556, .styles = 128, .hyperlink_bytes = 768, .grapheme_bytes = 8192, .string_bytes = 2048 }
info(font_codepoint_resolver): found codepoint 0x23F5 in fallback face=FreeMono

ghostty__10432.md:670-672 [ghostty_debug]
info(os_locale): setlocale from env result=LC_CTYPE=en_US.UTF-8;LC_NUMERIC=en_US.UTF-8;LC_TIME=en_US.UTF-8;LC_COLLATE=C;LC_MONETARY=en_US.UTF-8;LC_MESSAGES=en_US.UTF-8;LC_PAPER=en_US.UTF-8;LC_NAME=en_US.UTF-8;LC_ADDRESS=en_US.UTF-8;LC_TELEPHONE=en_US.UTF-8;LC_MEASUREMENT=en_US.UTF-8;LC_IDENTIFICATION=en_US.UTF-8
info(gtk): GTK version build=4.20.1 runtime=4.20.1
info(gtk): libadwaita version build=1.8.0 runtime=1.8.0

ghostty__10432.md:674-682 [ghostty_debug]
info(config): default shell source=env value=/bin/bash
warning(gtk_ghostty_application): setting GDK_DEBUG=
warning(gtk_ghostty_application): setting GDK_DISABLE=gles-api,vulkan
info(opengl): loaded OpenGL 4.6
info(io_exec): found Ghostty resources dir: /home/jon/src/github.com/ghostty-org/ghostty/zig-out/share/ghostty
warning(io_exec): shell could not be detected, no automatic shell integration will be injected
warning(gtk_ghostty_application): unimplemented action=.cell_size
info(io_exec): started subcommand path=python3 pid=206321
warning(glib): WARNING: Gtk: Trying to snapshot GtkRevealer 0x3b10ba30 without a current allocation

ghostty__10432.md:746-748 [ghostty_debug]
info(os_locale): setlocale from env result=LC_CTYPE=en_US.UTF-8;LC_NUMERIC=en_US.UTF-8;LC_TIME=en_US.UTF-8;LC_COLLATE=C;LC_MONETARY=en_US.UTF-8;LC_MESSAGES=en_US.UTF-8;LC_PAPER=en_US.UTF-8;LC_NAME=en_US.UTF-8;LC_ADDRESS=en_US.UTF-8;LC_TELEPHONE=en_US.UTF-8;LC_MEASUREMENT=en_US.UTF-8;LC_IDENTIFICATION=en_US.UTF-8
info(gtk): GTK version build=4.20.1 runtime=4.20.1
info(gtk): libadwaita version build=1.8.0 runtime=1.8.0

ghostty__10432.md:751-764 [ghostty_debug]
warning(config): both config files `/home/jon/.config/ghostty/config` and `/home/jon/.config/ghostty/config.ghostty` exist.
warning(config): loading them both in that order
info(config): default shell source=env value=/bin/bash
warning(gtk_ghostty_application): setting GDK_DEBUG=
warning(gtk_ghostty_application): setting GDK_DISABLE=gles-api,vulkan
info(opengl): loaded OpenGL 4.6
info(io_exec): found Ghostty resources dir: /home/jon/src/github.com/ghostty-org/ghostty/zig-out/share/ghostty
warning(io_exec): shell could not be detected, no automatic shell integration will be injected
warning(gtk_ghostty_application): unimplemented action=.cell_size
info(io_exec): started subcommand path=python3 pid=209512
warning(glib): WARNING: Gtk: Trying to snapshot GtkRevealer 0x15dde920 without a current allocation
info(font_codepoint_resolver): found codepoint 0x23BF in fallback face=Noto Sans Mono CJK JP
info(io_exec): pty fd closed, read thread exiting
info(surface): surface closed addr=17863990

ghostty__10957.md:32-38 [ghostty_debug]
info(opengl): loaded OpenGL 4.6
info(opengl): loaded OpenGL 4.6
info(io_exec): found Ghostty resources dir: /usr/share/ghostty
info(io_exec): shell integration automatically injected shell=termio.shell_integration.Shell.bash
warning(gtk_ghostty_application): unimplemented action=apprt.action.Action.Key.cell_size
info(io_exec): started subcommand path=/bin/bash pid=7872
info(io_exec): subcommand cgroup=-

ghostty__10957.md:78-80 [ghostty_debug]
info(os_locale): setlocale from env result=en_US.UTF-8
info(gtk): GTK version build=4.18.6 runtime=4.18.6
info(gtk): libadwaita version build=1.7.6 runtime=1.7.6

ghostty__10957.md:82-85 [ghostty_debug]
info(config): default shell src=passwd value=/bin/bash
info(config): default working directory src=passwd value=/home/arag00rn
warning(gtk_ghostty_application): setting GDK_DEBUG=
warning(gtk_ghostty_application): setting GDK_DISABLE=gles-api,vulkan

ghostty__12410.md:67-69 [ghostty_debug]
warning(gtk_ghostty_application): setting GDK_DEBUG=
warning(gtk_ghostty_application): setting GDK_DISABLE=gles-api,vulkan
warning(glib): WARNING: IBUS: ghostty has no capability of surrounding-text feature

ghostty__4632.md:217-219 [ghostty_debug]
info(config): default shell source=env value=/run/current-system/sw/bin/bash
warning(gtk): setting GDK_DEBUG=gl-no-fractional
warning(gtk): setting GDK_DISABLE=gles-api,vulkan

ghostty__4632.md:221-231 [ghostty_debug]
info(gtk): libadwaita version build=1.7.3 runtime=1.7.3
info(grid): loaded OpenGL 4.6
info(io_exec): found Ghostty resources dir: /nix/store/hsp07ywi2gv6dlh7dr105rsjs28skpdz-ghostty-1.1.3/share/ghostty
info(io_exec): shell integration automatically injected shell=termio.shell_integration.Shell.bash
warning(gtk): unimplemented action=apprt.action.Action.Key.cell_size
info(io_exec): started subcommand path=/bin/sh pid=9258
info(io_exec): subcommand cgroup=-
info(grid): reallocating GPU buffer old=0 new=20
info(io_exec): pty fd closed, read thread exiting
info(grid): reallocating GPU buffer old=20 new=38
info(surface): surface closed addr=557af64a3980

ghostty__7987.md:130-132 [ghostty_debug]
info(os_locale): setlocale from env result=LC_CTYPE=en_US.UTF-8;LC_NUMERIC=fr_FR.UTF-8;LC_TIME=fr_FR.UTF-8;LC_COLLATE=en_US.UTF-8;LC_MONETARY=fr_FR.UTF-8;LC_MESSAGES=en_US.UTF-8;LC_PAPER=fr_FR.UTF-8;LC_NAME=en_US.UTF-8;LC_ADDRESS=fr_FR.UTF-8;LC_TELEPHONE=fr_FR.UTF-8;LC_MEASUREMENT=fr_FR.UTF-8;LC_IDENTIFICATION=en_US.UTF-8
info(gtk): GTK version build=4.18.6 runtime=4.18.6
info(gtk): libadwaita version build=1.7.6 runtime=1.7.6

ghostty__7987.md:134-151 [ghostty_debug]
info(config): default shell source=env value=/bin/fish
warning(gtk): setting GDK_DEBUG=
warning(gtk): setting GDK_DISABLE=gles-api,vulkan
info(opengl): loaded OpenGL 4.6
info(font_shared_grid_set): font regular: CaskaydiaMono NFP Bold
info(font_shared_grid_set): font bold: CaskaydiaMono NFP Bold
info(font_shared_grid_set): font italic: CaskaydiaMono NFP Italic
info(font_shared_grid_set): font bold_italic: CaskaydiaMono NFP Bold Italic
info(io_exec): found Ghostty resources dir: /usr/share/ghostty
info(io_exec): shell integration automatically injected shell=termio.shell_integration.Shell.fish
warning(gtk): unimplemented action=apprt.action.Action.Key.cell_size
info(io_exec): started subcommand path=/bin/sh pid=309693
info(io_exec): subcommand cgroup=-
warning(io_handler): unimplemented or unknown SGR attribute: terminal.sgr.Attribute__struct_275010{ .full = { 38 }, .partial = { 38 } }
warning(stream): unimplemented OSC callback: terminal.osc.Command{ .end_of_command = terminal.osc.Command__struct_251301{ .exit_code = null } }
warning(stream): unimplemented OSC command: end_of_command
info(osc): unknown semantic prompts option: special_key
info(osc): unknown semantic prompts option: special_key

playwright__13027.md:82-84 [playwright_pw]
  pw:api <= browserContext.newPage succeeded +1ms
  pw:api => page.goto started +2ms
  pw:api navigating to "https://develop.shopcanal.com/", waiting until "load" +2ms

playwright__13027.md:92-95 [playwright_pw]
pw:api => browserType.launch started +0ms
  pw:browser <launching> /ms-playwright/firefox-1319/firefox/firefox -no-remote -headless -profile /tmp/playwright_firefoxdev_profile-UL9sig -juggler-pipe -silent +0ms
  pw:browser <launched> pid=289 +4ms
  pw:browser [pid=289][err] *** You are running in headless mode. +26ms

playwright__13156.md:122-416 [playwright_pw]
pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'BrowserType',
  pw:channel:event     initializer: {
  pw:channel:event       executablePath: '/Users/christophelombart/Library/Caches/ms-playwright/chromium-978106/chrome-mac/Chromium.app/Contents/MacOS/Chromium',
  pw:channel:event       name: 'chromium'
  pw:channel:event     },
  pw:channel:event     guid: 'browser-type@c4820a91ce7b48c09d099d124bde4390'
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'BrowserType',
  pw:channel:event     initializer: {
  pw:channel:event       executablePath: '/Users/christophelombart/Library/Caches/ms-playwright/firefox-1319/firefox/Nightly.app/Contents/MacOS/firefox',
  pw:channel:event       name: 'firefox'
  pw:channel:event     },
  pw:channel:event     guid: 'browser-type@bf7cb740065d592995e044b6738111ce'
  pw:channel:event   }
  pw:channel:event } +2ms
  pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'BrowserType',
  pw:channel:event     initializer: {
  pw:channel:event       executablePath: '/Users/christophelombart/Library/Caches/ms-playwright/webkit-1616/pw_run.sh',
  pw:channel:event       name: 'webkit'
  pw:channel:event     },
  pw:channel:event     guid: 'browser-type@52d09ae87ad845ec9bdcbc9d097e95c2'
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Android',
  pw:channel:event     initializer: {},
  pw:channel:event     guid: 'android@7fbbc49104ef0789f400547c21443345'
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Electron',
  pw:channel:event     initializer: {},
  pw:channel:event     guid: 'electron@31d51ccc49ed2e8397363b4f6289a486'
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'LocalUtils',
  pw:channel:event     initializer: {},
  pw:channel:event     guid: 'localUtils@ab8f59b59189b6296041ef09a0b84aa9'
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Selectors',
  pw:channel:event     initializer: {},
  pw:channel:event     guid: 'selectors@3212cda3e9bd42fbde3e6c9ee1810764'
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: '',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Playwright',
  pw:channel:event     initializer: {
  pw:channel:event       chromium: [Object],
  pw:channel:event       firefox: [Object],
  pw:channel:event       webkit: [Object],
  pw:channel:event       android: [Object],
  pw:channel:event       electron: [Object],
  pw:channel:event       utils: [Object],
  pw:channel:event       deviceDescriptors: [Array],
  pw:channel:event       selectors: [Object],
  pw:channel:event       preLaunchedBrowser: undefined,
  pw:channel:event       socksSupport: undefined
  pw:channel:event     },
  pw:channel:event     guid: 'Playwright'
  pw:channel:event   }
  pw:channel:event } +1ms
  pw:api => browserType.launch started +0ms
  pw:channel:command {
  pw:channel:command   id: 1,
  pw:channel:command   guid: 'browser-type@c4820a91ce7b48c09d099d124bde4390',
  pw:channel:command   method: 'launch',
  pw:channel:command   params: { ignoreAllDefaultArgs: false, headless: false }
  pw:channel:command } +0ms
  pw:browser <launching> /Users/christophelombart/Library/Caches/ms-playwright/chromium-978106/chrome-mac/Chromium.app/Contents/MacOS/Chromium --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --enable-use-zoom-for-dsf=false --no-sandbox --user-data-dir=/var/folders/kd/307tf1f930dg6b1hpn74c77h0000gn/T/playwright_chromiumdev_profile-U5Hlpz --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=30982 +4ms
  pw:protocol SEND ► {"id":1,"method":"Browser.getVersion"} +0ms
  pw:browser [pid=30982][err] objc[30993]: Class WebSwapCGLLayer is implemented in both /System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib (0x24c4d31a8) and /Users/christophelombart/Library/Caches/ms-playwright/chromium-978106/chrome-mac/Chromium.app/Contents/Frameworks/Chromium Framework.framework/Versions/101.0.4929.0/Libraries/libGLESv2.dylib (0x1098a9550). One of the two will be used. Which one is undefined. +546ms
  pw:protocol ◀ RECV {"id":1,"result":{"protocolVersion":"1.3","product":"Chrome/101.0.4929.0","revision":"@110dd5afedc7ef6846418b5df65fcc2c456184e0","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4929.0 Safari/537.36","jsVersion":"10.1.69"}} +548ms
  pw:protocol SEND ► {"id":2,"method":"Target.setAutoAttach","params":{"autoAttach":true,"waitForDebuggerOnStart":true,"flatten":true}} +1ms
  pw:protocol ◀ RECV {"id":2,"result":{}} +1ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-type@c4820a91ce7b48c09d099d124bde4390',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Browser',
  pw:channel:event     initializer: { version: '101.0.4929.0', name: 'chromium' },
  pw:channel:event     guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab'
  pw:channel:event   }
  pw:channel:event } +562ms
  pw:channel:response {
  pw:channel:response   id: 1,
  pw:channel:response   result: { browser: { guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab' } }
  pw:channel:response } +0ms
  pw:api <= browserType.launch succeeded +561ms
  pw:api => browser.newPage started +1ms
  pw:channel:command {
  pw:channel:command   id: 2,
  pw:channel:command   guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab',
  pw:channel:command   method: 'newContext',
  pw:channel:command   params: { noDefaultViewport: false }
  pw:channel:command } +562ms
  pw:protocol SEND ► {"id":3,"method":"Target.createBrowserContext","params":{"disposeOnDetach":true}} +3ms
  pw:protocol ◀ RECV {"id":3,"result":{"browserContextId":"25A5F54FA26E46F079170C5F39F67A1A"}} +2ms
  pw:protocol SEND ► {"id":4,"method":"Browser.setDownloadBehavior","params":{"behavior":"allowAndName","browserContextId":"25A5F54FA26E46F079170C5F39F67A1A","downloadPath":"/var/folders/kd/307tf1f930dg6b1hpn74c77h0000gn/T/playwright-artifacts-2OfoAP","eventsEnabled":true}} +1ms
  pw:protocol ◀ RECV {"id":4,"result":{}} +0ms
  pw:channel:event {
  pw:channel:event   guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Tracing',
  pw:channel:event     initializer: {},
  pw:channel:event     guid: 'Tracing@cd29d7b91a894ba43315afe666d6615e'
  pw:channel:event   }
  pw:channel:event } +7ms
  pw:channel:event {
  pw:channel:event   guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'APIRequestContext',
  pw:channel:event     initializer: { tracing: [Object] },
  pw:channel:event     guid: 'fetchRequest@4d9eed5ee01a0168888fc90c71d8829d'
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'BrowserContext',
  pw:channel:event     initializer: {
  pw:channel:event       isChromium: true,
  pw:channel:event       APIRequestContext: [Object],
  pw:channel:event       tracing: [Object]
  pw:channel:event     },
  pw:channel:event     guid: 'browser-context@102a6e6334eca2f7608830a922204f74'
  pw:channel:event   }
  pw:channel:event } +1ms
  pw:channel:response {
  pw:channel:response   id: 2,
  pw:channel:response   result: {
  pw:channel:response     context: { guid: 'browser-context@102a6e6334eca2f7608830a922204f74' }
  pw:channel:response   }
  pw:channel:response } +7ms
  pw:api <= browser.newPage succeeded +6ms
  pw:api => browser.newPage started +0ms
  pw:channel:command {
  pw:channel:command   id: 3,
  pw:channel:command   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:command   method: 'newPage',
  pw:channel:command   params: undefined
  pw:channel:command } +6ms
  pw:protocol SEND ► {"id":5,"method":"Target.createTarget","params":{"url":"about:blank","browserContextId":"25A5F54FA26E46F079170C5F39F67A1A"}} +3ms
  pw:protocol ◀ RECV {"method":"Target.attachedToTarget","params":{"sessionId":"B948B16D59A9CD517144E2F07B179082","targetInfo":{"targetId":"C52202D4B739564FFB365DA92230C91E","type":"page","title":"","url":"about:blank","attached":true,"canAccessOpener":false,"browserContextId":"25A5F54FA26E46F079170C5F39F67A1A"},"waitingForDebugger":true}} +83ms
  pw:protocol SEND ► {"id":6,"method":"Browser.getWindowForTarget","sessionId":"B948B16D59A9CD517144E2F07B179082"} +1ms
  pw:protocol ◀ RECV {"id":5,"result":{"targetId":"C52202D4B739564FFB365DA92230C91E"}} +9ms
  pw:protocol ◀ RECV {"id":6,"result":{"windowId":1,"bounds":{"left":22,"top":60,"width":1200,"height":1035,"windowState":"normal"}},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +249ms
  pw:protocol SEND ► {"id":7,"method":"Page.enable","sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":8,"method":"Page.getFrameTree","sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":9,"method":"Log.enable","params":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":10,"method":"Page.setLifecycleEventsEnabled","params":{"enabled":true},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":11,"method":"Runtime.enable","params":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +1ms
  pw:protocol SEND ► {"id":12,"method":"Page.addScriptToEvaluateOnNewDocument","params":{"source":"","worldName":"__playwright_utility_world__"},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":13,"method":"Network.enable","sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":14,"method":"Target.setAutoAttach","params":{"autoAttach":true,"waitForDebuggerOnStart":true,"flatten":true},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":15,"method":"Emulation.setFocusEmulationEnabled","params":{"enabled":true},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":16,"method":"Emulation.setDeviceMetricsOverride","params":{"mobile":false,"width":1280,"height":720,"screenWidth":1280,"screenHeight":720,"deviceScaleFactor":1,"screenOrientation":{"angle":90,"type":"landscapePrimary"}},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":17,"method":"Browser.setWindowBounds","params":{"windowId":1,"bounds":{"width":1282,"height":800}},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":18,"method":"Emulation.setEmulatedMedia","params":{"media":"","features":[{"name":"prefers-color-scheme","value":"light"},{"name":"prefers-reduced-motion","value":"no-preference"},{"name":"forced-colors","value":"none"}]},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":19,"method":"Runtime.runIfWaitingForDebugger","sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":17,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +3ms
  pw:protocol ◀ RECV {"id":7,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +80ms
  pw:protocol ◀ RECV {"id":8,"result":{"frameTree":{"frame":{"id":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","url":"about:blank","domainAndRegistry":"","securityOrigin":"://","mimeType":"text/html","adFrameStatus":{"adFrameType":"none"},"secureContextType":"InsecureScheme","crossOriginIsolatedContextType":"NotIsolated","gatedAPIFeatures":[]}}},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol SEND ► {"id":20,"method":"Page.createIsolatedWorld","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","grantUniveralAccess":true,"worldName":"__playwright_utility_world__"},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +1ms
  pw:protocol ◀ RECV {"id":9,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Page.lifecycleEvent","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","name":"commit","timestamp":36708.670551},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Page.lifecycleEvent","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","name":"DOMContentLoaded","timestamp":36708.67063},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Page.lifecycleEvent","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","name":"load","timestamp":36708.673207},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Page.lifecycleEvent","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","name":"networkAlmostIdle","timestamp":36708.675533},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Page.lifecycleEvent","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","name":"networkIdle","timestamp":36708.675533},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":10,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Runtime.executionContextCreated","params":{"context":{"id":1,"origin":"://","name":"","uniqueId":"-5341451335804414185.4468257835436916133","auxData":{"isDefault":true,"type":"default","frameId":"C52202D4B739564FFB365DA92230C91E"}}},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":11,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":12,"result":{"identifier":"1"},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +1ms
  pw:protocol ◀ RECV {"id":13,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":14,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":15,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Page.frameResized","params":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":16,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":18,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"id":19,"result":{},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Frame',
  pw:channel:event     initializer: {
  pw:channel:event       url: 'about:blank',
  pw:channel:event       name: '',
  pw:channel:event       parentFrame: undefined,
  pw:channel:event       loadStates: [Array]
  pw:channel:event     },
  pw:channel:event     guid: 'frame@6bb1251e6f8360f6eb719f8a7a111d1d'
  pw:channel:event   }
  pw:channel:event } +429ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Page',
  pw:channel:event     initializer: {
  pw:channel:event       mainFrame: [Object],
  pw:channel:event       viewportSize: [Object],
  pw:channel:event       isClosed: false,
  pw:channel:event       opener: undefined
  pw:channel:event     },
  pw:channel:event     guid: 'page@7700523f5e709a3c7dca2337e9e26e1d'
  pw:channel:event   }
  pw:channel:event } +1ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:event   method: 'page',
  pw:channel:event   params: { page: { guid: 'page@7700523f5e709a3c7dca2337e9e26e1d' } }
  pw:channel:event } +0ms
  pw:channel:response {
  pw:channel:response   id: 3,
  pw:channel:response   result: { page: { guid: 'page@7700523f5e709a3c7dca2337e9e26e1d' } }
  pw:channel:response } +430ms
  pw:api <= browser.newPage succeeded +430ms
  pw:api => page.goto started +0ms
  pw:channel:command {
  pw:channel:command   id: 4,
  pw:channel:command   guid: 'frame@6bb1251e6f8360f6eb719f8a7a111d1d',
  pw:channel:command   method: 'goto',
  pw:channel:command   params: { url: 'https://www.belfius.be/', waitUntil: 'load' }
  pw:channel:command } +430ms
  pw:api navigating to "https://www.belfius.be/", waiting until "load" +1ms
  pw:protocol SEND ► {"id":21,"method":"Page.navigate","params":{"url":"https://www.belfius.be/","frameId":"C52202D4B739564FFB365DA92230C91E"},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +3ms
  pw:protocol ◀ RECV {"method":"Network.requestWillBeSent","params":{"requestId":"2DF7B7877093D0570894EE7BD22C6431","loaderId":"2DF7B7877093D0570894EE7BD22C6431","documentURL":"https://www.belfius.be/","request":{"url":"https://www.belfius.be/","method":"GET","headers":{"Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4929.0 Safari/537.36","sec-ch-ua":"\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"101\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"macOS\""},"mixedContentType":"none","initialPriority":"VeryHigh","referrerPolicy":"strict-origin-when-cross-origin","isSameSite":true},"timestamp":36708.75017,"wallTime":1648659056.847938,"initiator":{"type":"other"},"redirectHasExtraInfo":false,"type":"Document","frameId":"C52202D4B739564FFB365DA92230C91E","hasUserGesture":false},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +34ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:event   method: '__create__',
  pw:channel:event   params: {
  pw:channel:event     type: 'Request',
  pw:channel:event     initializer: {
  pw:channel:event       frame: [Object],
  pw:channel:event       url: 'https://www.belfius.be/',
  pw:channel:event       resourceType: 'document',
  pw:channel:event       method: 'GET',
  pw:channel:event       postData: undefined,
  pw:channel:event       headers: [Array],
  pw:channel:event       isNavigationRequest: true,
  pw:channel:event       redirectedFrom: undefined
  pw:channel:event     },
  pw:channel:event     guid: 'request@68358544e4bd980870041006768ac73d'
  pw:channel:event   }
  pw:channel:event } +37ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:event   method: 'request',
  pw:channel:event   params: {
  pw:channel:event     request: { guid: 'request@68358544e4bd980870041006768ac73d' },
  pw:channel:event     page: { guid: 'page@7700523f5e709a3c7dca2337e9e26e1d' }
  pw:channel:event   }
  pw:channel:event } +0ms
  pw:protocol ◀ RECV {"method":"Runtime.executionContextCreated","params":{"context":{"id":2,"origin":"","name":"__playwright_utility_world__","uniqueId":"8661107130363845658.5094228730823388992","auxData":{"isDefault":false,"type":"isolated","frameId":"C52202D4B739564FFB365DA92230C91E"}}},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +1ms
  pw:protocol ◀ RECV {"id":20,"result":{"executionContextId":2},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +0ms
  pw:protocol ◀ RECV {"method":"Page.lifecycleEvent","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","name":"networkAlmostIdle","timestamp":36708.675533},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +932ms
  pw:protocol ◀ RECV {"method":"Page.lifecycleEvent","params":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"197E41D002EB53228B64B64AB822DA51","name":"networkIdle","timestamp":36708.675533},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +1ms
  pw:channel:response {
  pw:channel:response   id: 4,

playwright__13156.md:419-422 [playwright_pw]
  pw:channel:response       message: 'Timeout 30000ms exceeded.\n' +
  pw:channel:response         '=========================== logs ===========================\n' +
  pw:channel:response         'navigating to "https://www.belfius.be/", waiting until "load"\n' +
  pw:channel:response         '============================================================',

playwright__13156.md:424-430 [playwright_pw]
  pw:channel:response         '=========================== logs ===========================\n' +
  pw:channel:response         'navigating to "https://www.belfius.be/", waiting until "load"\n' +
  pw:channel:response         '============================================================\n' +
  pw:channel:response         '    at ProgressController.run (/Users/christophelombart/Dev/script-comparateur/node_modules/playwright-core/lib/server/progress.js:96:26)\n' +
  pw:channel:response         '    at Frame.goto (/Users/christophelombart/Dev/script-comparateur/node_modules/playwright-core/lib/server/frames.js:620:23)\n' +
  pw:channel:response         '    at FrameDispatcher.goto (/Users/christophelombart/Dev/script-comparateur/node_modules/playwright-core/lib/dispatchers/frameDispatcher.js:80:77)\n' +
  pw:channel:response         '    at DispatcherConnection.dispatch (/Users/christophelombart/Dev/script-comparateur/node_modules/playwright-core/lib/dispatchers/dispatcher.js:352:46)',

playwright__13156.md:432-434 [playwright_pw]
  pw:channel:response     }
  pw:channel:response   }
  pw:channel:response } +30s

playwright__13156.md:443-453 [playwright_pw]
  pw:api => browser.close started +4ms
  pw:channel:command {
  pw:channel:command   id: 5,
  pw:channel:command   guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab',
  pw:channel:command   method: 'close',
  pw:channel:command   params: undefined
  pw:channel:command } +30s
  pw:browser [pid=30982] <gracefully close start> +30s
  pw:protocol ◀ RECV {"id":-9999,"result":{}} +29s
  pw:protocol ◀ RECV {"method":"Inspector.detached","params":{"reason":"Render process gone."},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +3ms
  pw:protocol ◀ RECV {"id":21,"result":{"frameId":"C52202D4B739564FFB365DA92230C91E","loaderId":"2DF7B7877093D0570894EE7BD22C6431"},"sessionId":"B948B16D59A9CD517144E2F07B179082"} +9ms

playwright__13156.md:455-460 [playwright_pw]
  pw:channel:event {
  pw:channel:event   guid: 'frame@6bb1251e6f8360f6eb719f8a7a111d1d',
  pw:channel:event   method: 'navigated',
  pw:channel:event   params: {
  pw:channel:event     url: 'about:blank',
  pw:channel:event     name: '',

playwright__13156.md:462-466 [playwright_pw]
  pw:channel:event     newDocument: { request: [Object] }
  pw:channel:event   }
  pw:channel:event } +30s
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',

playwright__13156.md:468-521 [playwright_pw]
  pw:channel:event   params: {
  pw:channel:event     request: { guid: 'request@68358544e4bd980870041006768ac73d' },
  pw:channel:event     failureText: 'net::ERR_ABORTED',
  pw:channel:event     responseEndTiming: -1,
  pw:channel:event     page: { guid: 'page@7700523f5e709a3c7dca2337e9e26e1d' }
  pw:channel:event   }
  pw:channel:event } +1ms
  pw:protocol ◀ RECV {"method":"Target.detachedFromTarget","params":{"sessionId":"B948B16D59A9CD517144E2F07B179082","targetId":"C52202D4B739564FFB365DA92230C91E"}} +1ms
  pw:channel:event {
  pw:channel:event   guid: 'page@7700523f5e709a3c7dca2337e9e26e1d',
  pw:channel:event   method: 'close',
  pw:channel:event   params: undefined
  pw:channel:event } +1ms
  pw:channel:event {
  pw:channel:event   guid: 'page@7700523f5e709a3c7dca2337e9e26e1d',
  pw:channel:event   method: '__dispose__',
  pw:channel:event   params: {}
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: 'Tracing@cd29d7b91a894ba43315afe666d6615e',
  pw:channel:event   method: '__dispose__',
  pw:channel:event   params: {}
  pw:channel:event } +16ms
  pw:channel:event {
  pw:channel:event   guid: 'fetchRequest@4d9eed5ee01a0168888fc90c71d8829d',
  pw:channel:event   method: '__dispose__',
  pw:channel:event   params: {}
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:event   method: 'close',
  pw:channel:event   params: undefined
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: 'browser-context@102a6e6334eca2f7608830a922204f74',
  pw:channel:event   method: '__dispose__',
  pw:channel:event   params: {}
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab',
  pw:channel:event   method: 'close',
  pw:channel:event   params: undefined
  pw:channel:event } +0ms
  pw:channel:event {
  pw:channel:event   guid: 'browser@c086f7c8be1485bf593945e5fdb2d7ab',
  pw:channel:event   method: '__dispose__',
  pw:channel:event   params: {}
  pw:channel:event } +1ms
  pw:browser [pid=30982] <process did exit: exitCode=0, signal=null> +130ms
  pw:browser [pid=30982] starting temporary directories cleanup +1ms
  pw:browser [pid=30982] finished temporary directories cleanup +17ms
  pw:browser [pid=30982] <gracefully close end> +0ms
  pw:channel:response { id: 5 } +157ms
  pw:api <= browser.close succeeded +149ms

playwright__13230.md:295-298 [playwright_pw]
    pw:api => browserType.launch started +0ms
    pw:browser <launching> /ms-playwright/firefox-1319/firefox/firefox -no-remote -headless -profile **/tmp/playwright_firefoxdev_profile-s4JBOc -juggler-pipe** -silent +0ms
    pw:browser <launched> pid=14769 +4ms
    pw:browser [pid=14769][err] *** You are running in headless mode. +187ms

playwright__13230.md:477-479 [playwright_pw]
  pw:browser <launching> /ms-playwright/firefox-1319/firefox/firefox -no-remote -headless -profile /tmp/playwright_firefoxdev_profile-S66zjg -juggler-pipe -silent +0ms
  pw:browser <launched> pid=570 +2ms
  pw:browser [pid=570][err] *** You are running in headless mode. +14ms

playwright__13230.md:494-497 [playwright_pw]
  pw:browser [pid=570] <kill> +30s
  pw:browser [pid=570] <will force kill> +0ms
  pw:browser [pid=570] starting temporary directories cleanup +0ms
  pw:browser [pid=570] finished temporary directories cleanup +2ms

playwright__13230.md:499-501 [playwright_pw]
  pw:browser <launching> /ms-playwright/firefox-1319/firefox/firefox -no-remote -headless -profile /tmp/playwright_firefoxdev_profile-QmzsDn -juggler-pipe -silent +0ms
  pw:browser <launched> pid=797 +3ms
  pw:browser [pid=797][err] *** You are running in headless mode. +13ms

playwright__13230.md:516-519 [playwright_pw]
  pw:browser [pid=797] <kill> +30s
  pw:browser [pid=797] <will force kill> +0ms
  pw:browser [pid=797] starting temporary directories cleanup +1ms
  pw:browser [pid=797] finished temporary directories cleanup +1ms

playwright__13230.md:521-523 [playwright_pw]
  pw:browser <launching> /ms-playwright/firefox-1319/firefox/firefox -no-remote -headless -profile /tmp/playwright_firefoxdev_profile-A6wtbK -juggler-pipe -silent +0ms
  pw:browser <launched> pid=1026 +5ms
  pw:browser [pid=1026][err] *** You are running in headless mode. +25ms

playwright__13230.md:538-541 [playwright_pw]
  pw:browser [pid=1026] <kill> +30s
  pw:browser [pid=1026] <will force kill> +0ms
  pw:browser [pid=1026] starting temporary directories cleanup +0ms
  pw:browser [pid=1026] finished temporary directories cleanup +2ms

playwright__13230.md:543-545 [playwright_pw]
  pw:browser <launching> /ms-playwright/firefox-1319/firefox/firefox -no-remote -headless -profile /tmp/playwright_firefoxdev_profile-ElYN82 -juggler-pipe -silent +0ms
  pw:browser <launched> pid=1255 +3ms
  pw:browser [pid=1255][err] *** You are running in headless mode. +15ms

playwright__13230.md:560-563 [playwright_pw]
  pw:browser [pid=1255] <kill> +30s
  pw:browser [pid=1255] <will force kill> +0ms
  pw:browser [pid=1255] starting temporary directories cleanup +0ms
  pw:browser [pid=1255] finished temporary directories cleanup +1ms

playwright__13230.md:565-567 [playwright_pw]
  pw:browser <launching> /ms-playwright/firefox-1319/firefox/firefox -no-remote -headless -profile /tmp/playwright_firefoxdev_profile-9EWIcd -juggler-pipe -silent +0ms
  pw:browser <launched> pid=1482 +3ms
  pw:browser [pid=1482][err] *** You are running in headless mode. +16ms

playwright__14689.md:98-105 [playwright_pw]
  pw:browser <launching> /Applications/Microsoft Edge Beta.app/Contents/MacOS/Microsoft Edge Beta --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --enable-use-zoom-for-dsf=false --no-sandbox --user-data-dir=/var/folders/ws/2s8ybxq53x36k0cgzltxztl80000gn/T/playwright_chromiumdev_profile-Ee4996 --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=847 +7ms
  pw:browser [pid=847][err] objc[855]: Class WebSwapCGLLayer is implemented in both /System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib (0x7ffa55136318) and /Applications/Microsoft Edge Beta.app/Contents/Frameworks/Microsoft Edge Framework.framework/Versions/103.0.1264.17/Libraries/libGLESv2.dylib (0x10d0abd18). One of the two will be used. Which one is undefined. +793ms
  pw:browser [pid=847] <gracefully close start> +3s
  pw:browser [pid=847] <process did exit: exitCode=0, signal=null> +300ms
  pw:browser [pid=847] starting temporary directories cleanup +1ms
  pw:browser [pid=847] finished temporary directories cleanup +47ms
  pw:browser [pid=847] <gracefully close end> +0ms

playwright__15870.md:116-118 [playwright_pw]
  pw:browser <launching> /Users/maksimyakubovskiy/Library/Caches/ms-playwright/chromium-1015/chrome-mac/Chromium.app/Contents/MacOS/Chromium --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --enable-use-zoom-for-dsf=false --no-sandbox --disable-extensions-except=/Users/maksimyakubovskiy/Documents/<path_to_extension> --load-extension=/Users/maksimyakubovskiy/Documents/<path_to_extension> --disable-gpu --user-data-dir=/tmp/test-user-data-22 --remote-debugging-pipe about:blank +0ms
  pw:browser <launching> /Users/maksimyakubovskiy/Library/Caches/ms-playwright/chromium-1015/chrome-mac/Chromium.app/Contents/MacOS/Chromium --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --enable-use-zoom-for-dsf=false --no-sandbox --disable-extensions-except=/Users/maksimyakubovskiy/Documents/<path_to_extension> --load-extension=/Users/maksimyakubovskiy/Documents/<path_to_extension> --disable-gpu --user-data-dir=/tmp/test-user-data-22 --remote-debugging-pipe about:blank +0ms
  pw:browser <launched> pid=66264 +5ms

playwright__15870.md:125-137 [playwright_pw]
  pw:browser [pid=66264][out] Opening in existing browser session. +473ms
  pw:browser [pid=66264] <process did exit: exitCode=0, signal=null> +34ms
  pw:browser [pid=66264] starting temporary directories cleanup +0ms
  pw:browser [pid=66264] <gracefully close start> +7ms
  pw:browser [pid=66264] <kill> +0ms
  pw:browser [pid=66264] <skipped force kill spawnedProcess.killed=false processClosed=true> +1ms
  pw:browser [pid=66264] finished temporary directories cleanup +11ms
  pw:browser [pid=66264] <gracefully close end> +0ms
  pw:browser [pid=66263] <gracefully close start> +24s
  pw:browser [pid=66263] <process did exit: exitCode=0, signal=null> +316ms
  pw:browser [pid=66263] starting temporary directories cleanup +0ms
  pw:browser [pid=66263] finished temporary directories cleanup +3ms
  pw:browser [pid=66263] <gracefully close end> +0ms

playwright__16168.md:32-38 [playwright_pw]
  pw:browser [pid=20347][err] [0802/204658.982967:WARNING:bluez_dbus_manager.cc(247)] Floss manager not present, cannot set Floss enable/disable. +11ms
  pw:browser [pid=20347][err] [0802/204658.992137:WARNING:sandbox_linux.cc(376)] InitializeSandbox() called with multiple threads in process gpu-process. +9ms
  pw:browser [pid=20347] <gracefully close start> +51ms
  pw:browser [pid=20347] <process did exit: exitCode=0, signal=null> +29ms
  pw:browser [pid=20347] starting temporary directories cleanup +1ms
  pw:browser [pid=20347] finished temporary directories cleanup +2ms
  pw:browser [pid=20347] <gracefully close end> +0ms

playwright__16168.md:72-76 [playwright_pw]
  pw:browser [pid=20498] <gracefully close start> +27s
  pw:browser [pid=20498] <process did exit: exitCode=0, signal=null> +25ms
  pw:browser [pid=20498] starting temporary directories cleanup +2ms
  pw:browser [pid=20498] finished temporary directories cleanup +7ms
  pw:browser [pid=20498] <gracefully close end> +1ms

playwright__18552.md:34-36 [playwright_pw]
  pw:browser <launching> /Users/jeaton/Library/Caches/ms-playwright/chromium-1029/chrome-mac/Chromium.app/Contents/MacOS/Chromium --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --enable-use-zoom-for-dsf=false --headless --hide-scrollbars --mute-audio --blink-settings=primaryHoverType=2,availableHoverTypes=2,primaryPointerType=4,availablePointerTypes=4 --no-sandbox --user-data-dir=/var/folders/qc/h9qm30hx48gfflk9qzx1wygm0000gn/T/playwright_chromiumdev_profile-NM482j --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=34517 +4ms
  pw:browser [pid=34517][err] objc[34518]: Class WebSwapCGLLayer is implemented in both /System/Library/Frameworks/WebKit.framework/Versions/A/Frameworks/WebCore.framework/Versions/A/Frameworks/libANGLE-shared.dylib (0x24f071b50) and /Users/jeaton/Library/Caches/ms-playwright/chromium-1029/chrome-mac/Chromium.app/Contents/Frameworks/Chromium Framework.framework/Versions/107.0.5304.29/Libraries/libGLESv2.dylib (0x10b314230). One of the two will be used. Which one is undefined. +205ms

playwright__18552.md:39-43 [playwright_pw]
  pw:browser [pid=34517] <gracefully close start> +69ms
  pw:browser [pid=34517] <process did exit: exitCode=0, signal=null> +15ms
  pw:browser [pid=34517] starting temporary directories cleanup +0ms
  pw:browser [pid=34517] finished temporary directories cleanup +1ms
  pw:browser [pid=34517] <gracefully close end> +0ms

playwright__18552.md:48-62 [playwright_pw]
  pw:browser [pid=34534][err] 2022-11-03 15:29:04.858 com.apple.WebKit.WebContent.Development[34542:3796920] ApplePersistence=NO +114ms
  pw:browser [pid=34534][err] 2022-11-03 15:29:12.221 com.apple.WebKit.WebContent.Development[34547:3797011] ApplePersistence=NO +7s
  pw:browser [pid=34534][err] 2022-11-03 15:29:15.251 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x12386e710> - changing property contentsScale in transform-only layer, will have no effect +3s
  pw:browser [pid=34534][err] 2022-11-03 15:29:15.251 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x12386e710> - changing property rasterizationScale in transform-only layer, will have no effect +1ms
  pw:browser [pid=34534][err] 2022-11-03 15:29:17.994 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x122fb3e30> - changing property contentsScale in transform-only layer, will have no effect +3s
  pw:browser [pid=34534][err] 2022-11-03 15:29:17.994 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x122fb3e30> - changing property rasterizationScale in transform-only layer, will have no effect +0ms
  pw:browser [pid=34534][err] 2022-11-03 15:29:19.848 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x17fb1a9e0> - changing property contentsScale in transform-only layer, will have no effect +2s
  pw:browser [pid=34534][err] 2022-11-03 15:29:19.848 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x17fb1a9e0> - changing property rasterizationScale in transform-only layer, will have no effect +1ms
  pw:browser [pid=34534][err] 2022-11-03 15:29:20.110 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x104d11cc0> - changing property contentsScale in transform-only layer, will have no effect +262ms
  pw:browser [pid=34534][err] 2022-11-03 15:29:20.111 com.apple.WebKit.WebContent.Development[34547:3797007] <CATransformLayer: 0x104d11cc0> - changing property rasterizationScale in transform-only layer, will have no effect +0ms
  pw:browser [pid=34534] <gracefully close start> +15s
  pw:browser [pid=34534] <process did exit: exitCode=0, signal=null> +13ms
  pw:browser [pid=34534] starting temporary directories cleanup +0ms
  pw:browser [pid=34534] finished temporary directories cleanup +16ms
  pw:browser [pid=34534] <gracefully close end> +0ms

playwright__26497.md:123-129 [playwright_pw]
  pw:browser [pid=270] <gracefully close start> +16ms
  pw:browser [pid=270] <kill> +1ms
  pw:browser [pid=270] <will force kill> +0ms
  pw:browser [pid=270] <process did exit: exitCode=1, signal=null> +0ms
  pw:browser [pid=270] starting temporary directories cleanup +1ms
  pw:browser [pid=270] finished temporary directories cleanup +1ms
  pw:browser [pid=270] <gracefully close end> +0ms

playwright__27363.md:112-114 [playwright_pw]
  pw:browser [pid=40116][err]  +10s
  pw:browser [pid=40116][err]  +0ms
  pw:browser [pid=40116][err] # +0ms

playwright__27363.md:117-119 [playwright_pw]
  pw:browser [pid=40116][err] # +0ms
  pw:browser [pid=40116][err] # +0ms
  pw:browser [pid=40116][err] # +0ms

playwright__27363.md:124-165 [playwright_pw]
  pw:browser [pid=40116][err] 4   Chromium Framework                  0x000000011610fad8 v8_inspector::InjectedScript::ProtocolPromiseHandler::catchCallback(v8::FunctionCallbackInfo<v8::Value> const&) + 0 +0ms
  pw:browser [pid=40116][err] 5   ???                                 0x0000000147e4f6b4 0x0 + 5501154996 +0ms
  pw:browser [pid=40116][err] 6   ???                                 0x0000000147f44bd8 0x0 + 5502159832 +0ms
  pw:browser [pid=40116][err] 7   ???                                 0x0000000147e759ac 0x0 + 5501311404 +0ms
  pw:browser [pid=40116][err] 8   ???                                 0x0000000147e4af98 0x0 + 5501136792 +0ms
  pw:browser [pid=40116][err] 9   Chromium Framework                  0x0000000115a241f8 v8::internal::(anonymous namespace)::Invoke(v8::internal::Isolate*, v8::internal::(anonymous namespace)::InvokeParams const&) + 1788 +0ms
  pw:browser [pid=40116][err] 10  Chromium Framework                  0x0000000115a24aac v8::internal::(anonymous namespace)::InvokeWithTryCatch(v8::internal::Isolate*, v8::internal::(anonymous namespace)::InvokeParams const&) + 88 +0ms
  pw:browser [pid=40116][err] 11  Chromium Framework                  0x0000000115a24c78 v8::internal::Execution::TryRunMicrotasks(v8::internal::Isolate*, v8::internal::MicrotaskQueue*) + 64 +0ms
  pw:browser [pid=40116][err] 12  Chromium Framework                  0x0000000115a4cf60 v8::internal::MicrotaskQueue::RunMicrotasks(v8::internal::Isolate*) + 320 +0ms
  pw:browser [pid=40116][err] 13  Chromium Framework                  0x0000000115a4cdd0 v8::internal::MicrotaskQueue::PerformCheckpointInternal(v8::Isolate*) + 76 +0ms
  pw:browser [pid=40116][err] 14  Chromium Framework                  0x0000000115918a54 v8::MicrotasksScope::~MicrotasksScope() + 116 +0ms
  pw:browser [pid=40116][err] 15  Chromium Framework                  0x000000011614ad10 v8_inspector::(anonymous namespace)::innerCallFunctionOn(v8_inspector::V8InspectorSessionImpl*, v8_inspector::InjectedScript::Scope&, v8::Local<v8::Value>, v8_inspector::String16 const&, v8_crdtp::detail::PtrMaybe<std::__Cr::vector<std::__Cr::unique_ptr<v8_inspector::protocol::Runtime::CallArgument, std::__Cr::default_delete<v8_inspector::protocol::Runtime::CallArgument>>, std::__Cr::allocator<std::__Cr::unique_ptr<v8_inspector::protocol::Runtime::CallArgument, std::__Cr::default_delete<v8_inspector::protocol::Runtime::CallArgument>>>>>, bool, std::__Cr::unique_ptr<v8_inspector::WrapOptions, std::__Cr::default_delete<v8_inspector::WrapOptions>>, bool, bool, v8_inspector::String16 const&, bool, std::__Cr::unique_ptr<v8_inspector::protocol::Runtime::Backend::CallFunctionOnCallback, std::__Cr::default_delete<v8_inspector::protocol::Runtime::Backend::CallFunctionOnCallback>>) + 852 +0ms
  pw:browser [pid=40116][err] 16  Chromium Framework                  0x000000011614a704 v8_inspector::V8RuntimeAgentImpl::callFunctionOn(v8_inspector::String16 const&, v8_crdtp::detail::ValueMaybe<v8_inspector::String16>, v8_crdtp::detail::PtrMaybe<std::__Cr::vector<std::__Cr::unique_ptr<v8_inspector::protocol::Runtime::CallArgument, std::__Cr::default_delete<v8_inspector::protocol::Runtime::CallArgument>>, std::__Cr::allocator<std::__Cr::unique_ptr<v8_inspector::protocol::Runtime::CallArgument, std::__Cr::default_delete<v8_inspector::protocol::Runtime::CallArgument>>>>>, v8_crdtp::detail::ValueMaybe<bool>, v8_crdtp::detail::ValueMaybe<bool>, v8_crdtp::detail::ValueMaybe<bool>, v8_crdtp::detail::ValueMaybe<bool>, v8_crdtp::detail::ValueMaybe<bool>, v8_crdtp::detail::ValueMaybe<int>, v8_crdtp::detail::ValueMaybe<v8_inspector::String16>, v8_crdtp::detail::ValueMaybe<bool>, v8_crdtp::detail::ValueMaybe<v8_inspector::String16>, v8_crdtp::detail::ValueMaybe<bool>, v8_crdtp::detail::PtrMaybe<v8_inspector::protocol::Runtime::SerializationOptions>, std::__Cr::unique_ptr<v8_inspector::protocol::Runtime::Backend::CallFunctionOnCallback, std::__Cr::default_delete<v8_inspector::protocol::Runtime::Backend::CallFunctionOnCallback>>) + 1464 +1ms
  pw:browser [pid=40116][err] 17  Chromium Framework                  0x0000000116102324 v8_inspector::protocol::Runtime::DomainDispatcherImpl::callFunctionOn(v8_crdtp::Dispatchable const&) + 640 +0ms
  pw:browser [pid=40116][err] 18  Chromium Framework                  0x0000000116162164 v8_crdtp::UberDispatcher::DispatchResult::Run() + 56 +0ms
  pw:browser [pid=40116][err] 19  Chromium Framework                  0x0000000116143d00 v8_inspector::V8InspectorSessionImpl::dispatchProtocolMessage(v8_inspector::StringView) + 468 +0ms
  pw:browser [pid=40116][err] 20  Chromium Framework                  0x000000011b9a3cc4 blink::DevToolsSession::DispatchProtocolCommandImpl(int, WTF::String const&, base::span<unsigned char const, 18446744073709551615ul>) + 268 +0ms
  pw:browser [pid=40116][err] 21  Chromium Framework                  0x00000001177820f4 blink::mojom::blink::DevToolsSessionStubDispatch::Accept(blink::mojom::blink::DevToolsSession*, mojo::Message*) + 200 +0ms
  pw:browser [pid=40116][err] 22  Chromium Framework                  0x0000000118c8d550 mojo::InterfaceEndpointClient::HandleValidatedMessage(mojo::Message*) + 692 +0ms
  pw:browser [pid=40116][err] 23  Chromium Framework                  0x0000000118c91e90 mojo::MessageDispatcher::Accept(mojo::Message*) + 260 +0ms
  pw:browser [pid=40116][err] 24  Chromium Framework                  0x0000000118c8e854 mojo::InterfaceEndpointClient::HandleIncomingMessage(mojo::Message*) + 72 +0ms
  pw:browser [pid=40116][err] 25  Chromium Framework                  0x00000001190118d4 IPC::(anonymous namespace)::ChannelAssociatedGroupController::AcceptOnEndpointThread(mojo::Message) + 264 +0ms
  pw:browser [pid=40116][err] 26  Chromium Framework                  0x0000000118c90368 base::internal::Invoker<base::internal::BindState<void (mojo::(anonymous namespace)::ThreadSafeInterfaceEndpointClientProxy::*)(mojo::Message), scoped_refptr<mojo::(anonymous namespace)::ThreadSafeInterfaceEndpointClientProxy>, mojo::Message>, void ()>::RunOnce(base::internal::BindStateBase*) + 64 +0ms
  pw:browser [pid=40116][err] 27  Chromium Framework                  0x000000011864ca6c base::TaskAnnotator::RunTaskImpl(base::PendingTask&) + 304 +0ms
  pw:browser [pid=40116][err] 28  Chromium Framework                  0x0000000118662238 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::DoWorkImpl(base::LazyNow*) + 804 +0ms
  pw:browser [pid=40116][err] 29  Chromium Framework                  0x0000000118661dd4 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::DoWork() + 100 +0ms
  pw:browser [pid=40116][err] 30  Chromium Framework                  0x0000000118609db4 base::MessagePumpDefault::Run(base::MessagePump::Delegate*) + 120 +0ms
  pw:browser [pid=40116][err] 31  Chromium Framework                  0x0000000118662ad4 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::Run(bool, base::TimeDelta) + 332 +0ms
  pw:browser [pid=40116][err] 32  Chromium Framework                  0x000000011862fcd0 base::RunLoop::Run(base::Location const&) + 484 +0ms
  pw:browser [pid=40116][err] 33  Chromium Framework                  0x000000011ddfbe38 content::RendererMain(content::MainFunctionParams) + 1312 +0ms
  pw:browser [pid=40116][err] 34  Chromium Framework                  0x0000000117aeaee4 content::RunOtherNamedProcessTypeMain(std::__Cr::basic_string<char, std::__Cr::char_traits<char>, std::__Cr::allocator<char>> const&, content::MainFunctionParams, content::ContentMainDelegate*) + 596 +0ms
  pw:browser [pid=40116][err] 35  Chromium Framework                  0x0000000117aebbd8 content::ContentMainRunnerImpl::Run() + 688 +0ms
  pw:browser [pid=40116][err] 36  Chromium Framework                  0x0000000117aea134 content::RunContentProcess(content::ContentMainParams, content::ContentMainRunner*) + 836 +0ms
  pw:browser [pid=40116][err] 37  Chromium Framework                  0x0000000117aea5d0 content::ContentMain(content::ContentMainParams) + 128 +0ms
  pw:browser [pid=40116][err] 38  Chromium Framework                  0x0000000114845010 ChromeMain + 472 +0ms
  pw:browser [pid=40116][err] 39  Chromium Helper (Renderer)          0x00000001027a4a6c main + 364 +0ms
  pw:browser [pid=40116][err] 40  dyld                                0x00000001872f1058 start + 2224 +0ms
  pw:browser [pid=40116] <gracefully close start> +6s
  pw:browser [pid=40116] <process did exit: exitCode=0, signal=null> +54ms
  pw:browser [pid=40116] starting temporary directories cleanup +0ms
  pw:browser [pid=40116] finished temporary directories cleanup +54ms
  pw:browser [pid=40116] <gracefully close end> +0ms

playwright__27997.md:60-64 [playwright_pw]
  pw:browser [pid=7244][err]    ChromeMain [0x00007FF8F07B5002+147298] +0ms                                                                                                                                                          
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F52CEBE2+16303314] +0ms                                                                                                                                                
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44D545A+1649994] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44D6300+1653744] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44EEDD1+1754817] +0ms                                                                                                                                                 

playwright__27997.md:67-92 [playwright_pw]
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8FA8D090C+81530540] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8FA93886C+81956364] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F4991F56+6617158] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F6D0916E+18847502] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F5C61412+1382834] +0ms                                                                                                                                                
  pw:browser [pid=7244][err]    ChromeMain [0x00007FF8F1114499+9974777] +0ms                                                                                                                                                         
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F4D81379+10742889] +0ms                                                                                                                                                
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F4D811E0+10742480] +0ms                                                                                                                                                
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7697FD7+28870007] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F76979AF+28868431] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7623AE3+28393603] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7625CD5+28402293] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7627CE1+28410497] +1ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F6F28B44+21074148] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    ChromeMain [0x00007FF8F08A4E29+1129865] +0ms                                                                                                                                                         
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F46F058B+3858043] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F47F37F1+4919521] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F47F39CA+4919994] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F47F3A95+4920197] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44894B8+1338792] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F547849F+115487] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F5477DBD+113725] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F5489125+184229] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F5478F64+118244] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44A71AB+1460891] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F522017F+15587951] +0ms                                                                                                                                                

playwright__27997.md:97-104 [playwright_pw]
  pw:browser [pid=7244][err]    ChromeMain [0x00007FF8F0791390+752] +0ms                                                                                                                                                             
  pw:browser [pid=7244][err]    GetPakFileHashes [0x00007FF6C0C9293E+6462] +0ms                                                                                                                                                      
  pw:browser [pid=7244][err]    GetPakFileHashes [0x00007FF6C0C91A6F+2671] +0ms                                                                                                                                                      
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF6C0DF82B2+898034] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    BaseThreadInitThunk [0x00007FF9F7AD257D+29] +0ms                                                                                                                                                     
  pw:browser [pid=7244][err]    RtlUserThreadStart [0x00007FF9F950AA78+40] +0ms                                                                                                                                                      
  pw:browser [pid=7244][err] Task trace: +0ms                                                                                                                                                                                        
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F47F38ED+4919773] +0ms                                                                                                                                                 

playwright__27997.md:106-161 [playwright_pw]
  pw:browser [pid=7244][err]   "DelayLoad-ModuleName" = "USER32.dll" +0ms                                                                                                                                                            
  pw:browser [pid=7244][err]   "discardable-memory-free" = "11108352" +0ms                                                                                                                                                           
  pw:browser [pid=7244][err]   "discardable-memory-allocated" = "11390976" +0ms                                                                                                                                                      
  pw:browser [pid=7244][err]   "gpu-generation-intel" = "12" +0ms                                                                                                                                                                    
  pw:browser [pid=7244][err]   "gpu-vsver" = "5.0" +0ms                                                                                                                                                                              
  pw:browser [pid=7244][err]   "gpu-psver" = "5.0" +0ms                                                                                                                                                                              
  pw:browser [pid=7244][err]   "gpu-driver" = "31.0.101.4255" +0ms                                                                                                                                                                   
  pw:browser [pid=7244][err]   "gpu-rev" = "1" +0ms                                                                                                                                                                                  
  pw:browser [pid=7244][err]   "gpu-subid" = "0x22cb17aa" +0ms                                                                                                                                                                       
  pw:browser [pid=7244][err]   "gpu_count" = "2" +0ms                                                                                                                                                                                
  pw:browser [pid=7244][err]   "gpu-devid" = "0x9a49" +0ms                                                                                                                                                                           
  pw:browser [pid=7244][err]   "gpu-venid" = "0x8086" +1ms                                                                                                                                                                           
  pw:browser [pid=7244][err]   "view-count" = "1" +0ms                                                                                                                                                                               
  pw:browser [pid=7244][err]   "loaded-origin-0" = "https://app.cymulate.com" +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]   "web-frame-count" = "6" +0ms                                                                                                                                                                          
  pw:browser [pid=7244][err]   "renderer_foreground" = "true" +0ms                                                                                                                                                                   
  pw:browser [pid=7244][err]   "v8_ro_space_firstpage_address" = "0x30a00000000" +0ms                                                                                                                                                
  pw:browser [pid=7244][err]   "v8_isolate_address" = "0xd980080c000" +0ms                                                                                                                                                           
  pw:browser [pid=7244][err]   "variations" = "5e3a236d-59e286d0," +0ms                                                                                                                                                              
  pw:browser [pid=7244][err]   "num-experiments" = "1" +0ms                                                                                                                                                                          
  pw:browser [pid=7244][err]   "reentry_guard_tls_slot" = "unused" +0ms                                                                                                                                                              
  pw:browser [pid=7244][err]   "switch-19" = "--field-trial-handle=1952,i,14116009138538885456,145930369958662" +0ms                                                                                                                 
  pw:browser [pid=7244][err]   "switch-18" = "--mojo-platform-channel-handle=3756" +0ms                                                                                                                                              
  pw:browser [pid=7244][err]   "switch-17" = "--launch-time-ticks=1077482433883" +0ms                                                                                                                                                
  pw:browser [pid=7244][err]   "switch-16" = "--time-ticks-at-unix-epoch=-1698295991113988" +0ms                                                                                                                                     
  pw:browser [pid=7244][err]   "switch-15" = "--renderer-client-id=5" +0ms                                                                                                                                                           
  pw:browser [pid=7244][err]   "switch-14" = "--enable-main-frame-before-activation" +0ms                                                                                                                                            
  pw:browser [pid=7244][err]   "switch-13" = "--num-raster-threads=4" +0ms                                                                                                                                                           
  pw:browser [pid=7244][err]   "switch-12" = "--device-scale-factor=1" +0ms                                                                                                                                                          
  pw:browser [pid=7244][err]   "switch-11" = "--lang=en-US" +0ms                                                                                                                                                                     
  pw:browser [pid=7244][err]   "switch-10" = "--disable-databases" +0ms                                                                                                                                                              
  pw:browser [pid=7244][err]   "switch-9" = "--allow-pre-commit-input" +0ms                                                                                                                                                          
  pw:browser [pid=7244][err]   "switch-8" = "--remote-debugging-pipe" +0ms                                                                                                                                                           
  pw:browser [pid=7244][err]   "switch-7" = "--force-color-profile=srgb" +0ms                                                                                                                                                        
  pw:browser [pid=7244][err]   "switch-6" = "--file-url-path-alias=/gen=C:\Users\MichaelBehnam\AppData\Local\" +0ms                                                                                                                  
  pw:browser [pid=7244][err]   "switch-5" = "--enable-automation" +0ms                                                                                                                                                               
  pw:browser [pid=7244][err]   "switch-4" = "--disable-breakpad" +0ms                                                                                                                                                                
  pw:browser [pid=7244][err]   "switch-3" = "--disable-background-timer-throttling" +0ms                                                                                                                                             
  pw:browser [pid=7244][err]   "switch-2" = "--disable-back-forward-cache" +0ms                                                                                                                                                      
  pw:browser [pid=7244][err]   "switch-1" = "--user-data-dir=C:\Users\MICHAE~1\AppData\Local\Temp\playwright_" +0ms                                                                                                                  
  pw:browser [pid=7244][err]   "num-switches" = "23" +0ms                                                                                                                                                                            
  pw:browser [pid=7244][err]   "commandline-disabled-feature-12" = "Translate" +0ms                                                                                                                                                  
  pw:browser [pid=7244][err]   "commandline-disabled-feature-11" = "MediaRouter" +0ms                                                                                                                                                
  pw:browser [pid=7244][err]   "commandline-disabled-feature-10" = "LazyFrameLoading" +0ms                                                                                                                                           
  pw:browser [pid=7244][err]   "commandline-disabled-feature-9" = "ImprovedCookieControls" +0ms                                                                                                                                      
  pw:browser [pid=7244][err]   "commandline-disabled-feature-8" = "HttpsUpgrades" +0ms                                                                                                                                               
  pw:browser [pid=7244][err]   "commandline-disabled-feature-7" = "GlobalMediaControls" +0ms                                                                                                                                         
  pw:browser [pid=7244][err]   "commandline-disabled-feature-6" = "DialMediaRouteProvider" +0ms                                                                                                                                      
  pw:browser [pid=7244][err]   "commandline-disabled-feature-5" = "DestroyProfileOnBrowserClose" +0ms                                                                                                                                
  pw:browser [pid=7244][err]   "commandline-disabled-feature-4" = "CertificateTransparencyComponentUpdater" +0ms                                                                                                                     
  pw:browser [pid=7244][err]   "commandline-disabled-feature-3" = "AvoidUnnecessaryBeforeUnloadCheckSync" +0ms                                                                                                                       
  pw:browser [pid=7244][err]   "commandline-disabled-feature-2" = "AutoExpandDetailsElement" +0ms                                                                                                                                    
  pw:browser [pid=7244][err]   "commandline-disabled-feature-1" = "AcceptCHFrame" +0ms                                                                                                                                               
  pw:browser [pid=7244][err]   "commandline-enabled-feature-2" = "NetworkServiceInProcess" +1ms                                                                                                                                      
  pw:browser [pid=7244][err]   "commandline-enabled-feature-1" = "NetworkService" +0ms                                                                                                                                               
  pw:browser [pid=7244][err]  +0ms                                                                                                                                                                                                   

playwright__27997.md:163-165 [playwright_pw]
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44D5D16+1652230] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44D6300+1653744] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44EEDD1+1754817] +0ms                                                                                                                                                 

playwright__27997.md:168-193 [playwright_pw]
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8FA8D090C+81530540] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8FA93886C+81956364] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F4991F56+6617158] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F6D0916E+18847502] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F5C61412+1382834] +0ms                                                                                                                                                
  pw:browser [pid=7244][err]    ChromeMain [0x00007FF8F1114499+9974777] +0ms                                                                                                                                                         
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F4D81379+10742889] +0ms                                                                                                                                                
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F4D811E0+10742480] +0ms                                                                                                                                                
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7697FD7+28870007] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F76979AF+28868431] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7623AE3+28393603] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7625CD5+28402293] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F7627CE1+28410497] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    sqlite3_dbdata_init [0x00007FF8F6F28B44+21074148] +0ms                                                                                                                                               
  pw:browser [pid=7244][err]    ChromeMain [0x00007FF8F08A4E29+1129865] +0ms                                                                                                                                                         
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F46F058B+3858043] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F47F37F1+4919521] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F47F39CA+4919994] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F47F3A95+4920197] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44894B8+1338792] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F547849F+115487] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F5477DBD+113725] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F5489125+184229] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF8F5478F64+118244] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F44A71AB+1460891] +0ms                                                                                                                                                 
  pw:browser [pid=7244][err]    IsSandboxedProcess [0x00007FF8F522017F+15587951] +0ms                                                                                                                                                

playwright__27997.md:198-208 [playwright_pw]
  pw:browser [pid=7244][err]    ChromeMain [0x00007FF8F0791390+752] +0ms                                                                                                                                                             
  pw:browser [pid=7244][err]    GetPakFileHashes [0x00007FF6C0C9293E+6462] +0ms                                                                                                                                                      
  pw:browser [pid=7244][err]    GetPakFileHashes [0x00007FF6C0C91A6F+2671] +0ms                                                                                                                                                      
  pw:browser [pid=7244][err]    GetHandleVerifier [0x00007FF6C0DF82B2+898034] +0ms                                                                                                                                                   
  pw:browser [pid=7244][err]    BaseThreadInitThunk [0x00007FF9F7AD257D+29] +0ms                                                                                                                                                     
  pw:browser [pid=7244][err]    RtlUserThreadStart [0x00007FF9F950AA78+40] +0ms                                                                                                                                                      
  pw:browser [pid=7244] <gracefully close start> +3s
  pw:browser [pid=7244] <process did exit: exitCode=0, signal=null> +108ms
  pw:browser [pid=7244] starting temporary directories cleanup +0ms                                                                                                                                                                  
  pw:browser [pid=7244] finished temporary directories cleanup +38ms
  pw:browser [pid=7244] <gracefully close end> +0ms                                                                                                                                                                                  

playwright__30660.md:139-143 [playwright_pw]
  pw:browser [pid=3148] <gracefully close start> +2s
  pw:browser [pid=3148] <process did exit: exitCode=0, signal=null> +339ms
  pw:browser [pid=3148] starting temporary directories cleanup +1ms
  pw:browser [pid=3148] finished temporary directories cleanup +17ms
  pw:browser [pid=3148] <gracefully close end>

playwright__30660.md:149-153 [playwright_pw]
  pw:browser <launching> C:\Users\xxxx\AppData\Local\ms-playwright\firefox-1447\firefox\firefox.exe -no-remote -wait-for-browser -foreground -profile C:\Users\xxxx\AppData\Local\Temp\playwright_firefoxdev_profile-5EqNMJ -juggler-pipe -silent +0ms
  pw:browser <launched> pid=12764 +12ms
  pw:browser [pid=12764][err] JavaScript warning: resource://services-settings/Utils.sys.mjs, line 114: unreachable code after return statement +163ms
  pw:browser [pid=12764][out] console.warn: services.settings: Ignoring preference override of remote settings server +2ms
  pw:browser [pid=12764][out] console.warn: services.settings: Allow by setting MOZ_REMOTE_SETTINGS_DEVTOOLS=1 in the environment +0ms

playwright__30660.md:169-171 [playwright_pw]
  pw:browser [pid=12764][out]   Stack: +0ms
  pw:browser [pid=12764][out]     getEngineConfiguration@resource://gre/modules/SearchEngineSelectorOld.sys.mjs:118:24 +0ms
  pw:browser [pid=12764][out]  +0ms

playwright__30660.md:175-179 [playwright_pw]
  pw:browser [pid=12764] <gracefully close start> +461ms
  pw:browser [pid=12764] <process did exit: exitCode=0, signal=null> +730ms
  pw:browser [pid=12764] starting temporary directories cleanup +0ms
  pw:browser [pid=12764] finished temporary directories cleanup +20ms
  pw:browser [pid=12764] <gracefully close end>

playwright__31050.md:127-134 [playwright_pw]
 pw:api => selectors.setTestIdAttribute started +0ms
  pw:api => browserType.launch started +5ms
  pw:api <= selectors.setTestIdAttribute succeeded +8ms
  pw:api <= browserType.launch succeeded +285ms
  pw:api => browser.newContext started +2ms
  pw:api <= browser.newContext succeeded +7ms
  pw:api => browserContext.newPage started +3ms
  pw:api <= browserContext.newPage succeeded +97ms

playwright__31050.md:136-141 [playwright_pw]
  pw:api => page.goto started +2ms
  pw:api navigating to "https://www.fedex.com/en-us/home.html", waiting until "load" +2ms
  pw:api => page.screenshot started +30s
  pw:api taking page screenshot +2ms
  pw:api waiting for fonts to load... +1ms
  pw:api fonts loaded +0ms

playwright__31050.md:248-253 [playwright_pw]
pw:browser <launched> pid=29779 +7ms
  pw:browser [pid=29779] <gracefully close start> +35s
  pw:browser [pid=29779] <process did exit: exitCode=0, signal=null> +10s
  pw:browser [pid=29779] starting temporary directories cleanup +0ms
  pw:browser [pid=29779] finished temporary directories cleanup +13ms
  pw:browser [pid=29779] <gracefully close end> +1ms

playwright__31050.md:278-283 [playwright_pw]
pw:browser <launched> pid=71980 +6ms
  pw:browser [pid=71980] <gracefully close start> +35s
  pw:browser [pid=71980] <process did exit: exitCode=0, signal=null> +10s
  pw:browser [pid=71980] starting temporary directories cleanup +1ms
  pw:browser [pid=71980] finished temporary directories cleanup +14ms
  pw:browser [pid=71980] <gracefully close end> +0ms

playwright__31950.md:153-230 [playwright_pw]
  pw:browser [pid=13764][err]  [0x00011c559a58] +1ms
  pw:browser [pid=13764][err]  [0x00011c54dac8] +0ms
  pw:browser [pid=13764][err]  [0x00011c5599a8] +0ms
  pw:browser [pid=13764][err]  [0x000197217584] +0ms
  pw:browser [pid=13764][err]  [0x0001a1d6a4ec] +0ms
  pw:browser [pid=13764][err]  [0x0001a1d62844] +0ms
  pw:browser [pid=13764][err]  [0x0001a1d6260c] +0ms
  pw:browser [pid=13764][err]  [0x0001a1d5ffac] +0ms
  pw:browser [pid=13764][err]  [0x0001a1d5f880] +0ms
  pw:browser [pid=13764][err]  [0x0001a1d5f79c] +0ms
  pw:browser [pid=13764][err]  [0x0001a1d5f640] +0ms
  pw:browser [pid=13764][err]  [0x00019ac12f6c] +0ms
  pw:browser [pid=13764][err]  [0x00019ac12dec] +0ms
  pw:browser [pid=13764][err]  [0x00019ad2a63c] +0ms
  pw:browser [pid=13764][err]  [0x00019ad29f0c] +0ms
  pw:browser [pid=13764][err]  [0x00011d65d93c] +0ms
  pw:browser [pid=13764][err]  [0x00011b30fac4] +0ms
  pw:browser [pid=13764][err]  [0x00011bfb86e0] +0ms
  pw:browser [pid=13764][err]  [0x0001180318ac] +0ms
  pw:browser [pid=13764][err]  [0x00011a732244] +0ms
  pw:browser [pid=13764][err]  [0x00011a729950] +1ms
  pw:browser [pid=13764][err]  [0x00011a6c8024] +0ms
  pw:browser [pid=13764][err]  [0x00011a937a68] +0ms
  pw:browser [pid=13764][err]  [0x00011a92ca68] +0ms
  pw:browser [pid=13764][err]  [0x0001215a4798] +1ms
  pw:browser [pid=13764][err]  [0x0001215a3e80] +0ms
  pw:browser [pid=13764][err]  [0x00011f15b4d4] +0ms
  pw:browser [pid=13764][err]  [0x00011f1650b8] +0ms
  pw:browser [pid=13764][err]  [0x000119a402b4] +0ms
  pw:browser [pid=13764][err]  [0x00011f0f90d0] +0ms
  pw:browser [pid=13764][err]  [0x00011f0f71b8] +0ms
  pw:browser [pid=13764][err]  [0x00011a3b0790] +0ms
  pw:browser [pid=13764][err]  [0x00011a3b02b0] +0ms
  pw:browser [pid=13764][err]  [0x00011a391f28] +0ms
  pw:browser [pid=13764][err]  [0x00011a3ac3b8] +0ms
  pw:browser [pid=13764][err]  [0x00011c5018d0] +0ms
  pw:browser [pid=13764][err]  [0x00011c519954] +0ms
  pw:browser [pid=13764][err]  [0x00011c519500] +0ms
  pw:browser [pid=13764][err]  [0x00011c5646d4] +0ms
  pw:browser [pid=13764][err]  [0x00011c55feb4] +0ms
  pw:browser [pid=13764][err]  [0x00011c563ec0] +0ms
  pw:browser [pid=13764][err]  [0x0001972c64d8] +0ms
  pw:browser [pid=13764][err]  [0x0001972c646c] +0ms
  pw:browser [pid=13764][err]  [0x0001972c61dc] +0ms
  pw:browser [pid=13764][err]  [0x0001972c4dc8] +0ms
  pw:browser [pid=13764][err]  [0x0001972c4434] +0ms
  pw:browser [pid=13764][err]  [0x0001a1a6819c] +0ms
  pw:browser [pid=13764][err]  [0x0001a1a67fd8] +0ms
  pw:browser [pid=13764][err]  [0x0001a1a67d30] +0ms
  pw:browser [pid=13764][err]  [0x00019ab23d68] +0ms
  pw:browser [pid=13764][err]  [0x00019b319808] +0ms
  pw:browser [pid=13764][err]  [0x00011bf96848] +0ms
  pw:browser [pid=13764][err]  [0x00011c55feb4] +0ms
  pw:browser [pid=13764][err]  [0x00011bf96790] +0ms
  pw:browser [pid=13764][err]  [0x00019ab1709c] +0ms
  pw:browser [pid=13764][err]  [0x00011c564dd0] +0ms
  pw:browser [pid=13764][err]  [0x00011c563864] +0ms
  pw:browser [pid=13764][err]  [0x00011c519fc8] +0ms
  pw:browser [pid=13764][err]  [0x00011c4e7610] +0ms
  pw:browser [pid=13764][err]  [0x00011a3131e0] +0ms
  pw:browser [pid=13764][err]  [0x00011a3149dc] +0ms
  pw:browser [pid=13764][err]  [0x00011a310ae8] +0ms
  pw:browser [pid=13764][err]  [0x00011b9f33a0] +0ms
  pw:browser [pid=13764][err]  [0x00011b9f4668] +0ms
  pw:browser [pid=13764][err]  [0x00011b9f426c] +0ms
  pw:browser [pid=13764][err]  [0x00011b9f2928] +0ms
  pw:browser [pid=13764][err]  [0x00011b9f2d30] +0ms
  pw:browser [pid=13764][err]  [0x000117ee5430] +0ms
  pw:browser [pid=13764][err]  [0x000104328988] +1ms
  pw:browser [pid=13764][err]  [0x000196e5e0e0] +0ms
  pw:browser [pid=13764][err] [end of stack trace] +0ms
  pw:browser [pid=13764][err] [0801/131909.772439:WARNING:process_memory_mac.cc(94)] mach_vm_read(0x1047b0000, 0x8000): (os/kern) invalid address (1) +101ms
  pw:browser [pid=13764][err] [0801/131909.772972:WARNING:process_memory_mac.cc(94)] mach_vm_read(0x1047b0000, 0x8000): (os/kern) invalid address (1) +1ms
  pw:browser [pid=13764][err] [0801/131909.773190:WARNING:process_memory_mac.cc(94)] mach_vm_read(0x1047b0000, 0x8000): (os/kern) invalid address (1) +0ms
  pw:browser [pid=13764][err] [0801/131909.773482:WARNING:process_memory_mac.cc(94)] mach_vm_read(0x1047b0000, 0x8000): (os/kern) invalid address (1) +0ms
  pw:browser [pid=13764][err] [0801/131909.773712:WARNING:process_memory_mac.cc(94)] mach_vm_read(0x1047b0000, 0x8000): (os/kern) invalid address (1) +0ms
  pw:browser [pid=13764][err] [0801/131909.773914:WARNING:process_memory_mac.cc(94)] mach_vm_read(0x1047b0000, 0x8000): (os/kern) invalid address (1) +0ms
  pw:browser [pid=13764][err] [0801/131909.774113:WARNING:process_memory_mac.cc(94)] mach_vm_read(0x1047b0000, 0x8000): (os/kern) invalid address (1) +1ms

playwright__33515.md:493-496 [playwright_pw]
  pw:browser <launching> /root/.cache/ms-playwright/chromium-1140/chrome-linux/chrome --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate,HttpsUpgrades,PaintHolding,ThirdPartyStoragePartitioning,LensOverlay,PlzDedicatedWorker --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --headless=old --hide-scrollbars --mute-audio --blink-settings=primaryHoverType=2,availableHoverTypes=2,primaryPointerType=4,availablePointerTypes=4 --no-sandbox --user-data-dir=/tmp/playwright_chromiumdev_profile-rQMfD2 --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=3768 +17ms
  pw:browser [pid=3768][err] Old Headless mode will be removed from the Chrome binary soon. Please use the new Headless mode (https://developer.chrome.com/docs/chromium/new-headless) or the chrome-headless-shell which is a standalone implementation of the old Headless mode (https://developer.chrome.com/blog/chrome-headless-shell). +227ms
  pw:browser [pid=3768][err]  +0ms

playwright__33515.md:498-503 [playwright_pw]
  pw:browser [pid=3768][err] #0 0x55555e750152 base::debug::CollectStackTrace() +0ms
  pw:browser [pid=3768][err] #1 0x55555e73d90e base::debug::StackTrace::StackTrace() +1ms
  pw:browser [pid=3768][err] #2 0x55555e6943ea logging::LogMessage::Flush() +1ms
  pw:browser [pid=3768][err] #3 0x55555e6942cd logging::LogMessage::~LogMessage() +0ms
  pw:browser [pid=3768][err] #4 0x55555e67d820 logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +2ms
  pw:browser [pid=3768][err] #5 0x55555e67d87e logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +0ms

playwright__33515.md:505-516 [playwright_pw]
  pw:browser [pid=3768][err] #7 0x55555db2eb27 content::ZygoteMain() +2ms
  pw:browser [pid=3768][err] #8 0x55555db27b9e content::RunZygote() +1ms
  pw:browser [pid=3768][err] #9 0x55555db28892 content::RunOtherNamedProcessTypeMain() +1ms
  pw:browser [pid=3768][err] #10 0x55555db2990f content::ContentMainRunnerImpl::Run() +1ms
  pw:browser [pid=3768][err] #11 0x55555db27467 content::RunContentProcess() +0ms
  pw:browser [pid=3768][err] #12 0x55555db27697 content::ContentMain() +1ms
  pw:browser [pid=3768][err] #13 0x55555e16672c headless::HeadlessShellMain() +0ms
  pw:browser [pid=3768][err] #14 0x5555596d84d9 ChromeMain +1ms
  pw:browser [pid=3768][err] #15 0x2aaaac02b24a (/usr/lib/x86_64-linux-gnu/libc.so.6+0x27249) +0ms
  pw:browser [pid=3768][err] #16 0x2aaaac02b305 __libc_start_main +0ms
  pw:browser [pid=3768][err] #17 0x5555596d802a _start +1ms
  pw:browser [pid=3768][err]  +0ms

playwright__33515.md:519-524 [playwright_pw]
  pw:browser [pid=3768][err] #0 0x55555e750152 base::debug::CollectStackTrace() +0ms
  pw:browser [pid=3768][err] #1 0x55555e73d90e base::debug::StackTrace::StackTrace() +1ms
  pw:browser [pid=3768][err] #2 0x55555e6943ea logging::LogMessage::Flush() +0ms
  pw:browser [pid=3768][err] #3 0x55555e6942cd logging::LogMessage::~LogMessage() +0ms
  pw:browser [pid=3768][err] #4 0x55555e67d820 logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +1ms
  pw:browser [pid=3768][err] #5 0x55555e67d87e logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +0ms

playwright__33515.md:526-537 [playwright_pw]
  pw:browser [pid=3768][err] #7 0x55555db2eb27 content::ZygoteMain() +0ms
  pw:browser [pid=3768][err] #8 0x55555db27b9e content::RunZygote() +0ms
  pw:browser [pid=3768][err] #9 0x55555db28892 content::RunOtherNamedProcessTypeMain() +0ms
  pw:browser [pid=3768][err] #10 0x55555db2990f content::ContentMainRunnerImpl::Run() +0ms
  pw:browser [pid=3768][err] #11 0x55555db27467 content::RunContentProcess() +0ms
  pw:browser [pid=3768][err] #12 0x55555db27697 content::ContentMain() +0ms
  pw:browser [pid=3768][err] #13 0x55555e16672c headless::HeadlessShellMain() +1ms
  pw:browser [pid=3768][err] #14 0x5555596d84d9 ChromeMain +0ms
  pw:browser [pid=3768][err] #15 0x2aaaac02b24a (/usr/lib/x86_64-linux-gnu/libc.so.6+0x27249) +0ms
  pw:browser [pid=3768][err] #16 0x2aaaac02b305 __libc_start_main +0ms
  pw:browser [pid=3768][err] #17 0x5555596d802a _start +0ms
  pw:browser [pid=3768][err]  +0ms

playwright__33515.md:562-564 [playwright_pw]
  pw:browser [pid=3768][err] #0 0x55555e750152 base::debug::CollectStackTrace() +0ms
  pw:browser [pid=3768][err] #1 0x55555e73d90e base::debug::StackTrace::StackTrace() +0ms
  pw:browser [pid=3768][err] #2 0x55555e6943ea logging::LogMessage::Flush() +0ms

playwright__33515.md:566-569 [playwright_pw]
  pw:browser [pid=3768][err] #4 0x55555c266a17 content::(anonymous namespace)::IntentionallyCrashBrowserForUnusableGpuProcess() +0ms
  pw:browser [pid=3768][err] #5 0x55555c2636a1 content::GpuDataManagerImplPrivate::FallBackToNextGpuMode() +0ms
  pw:browser [pid=3768][err] #6 0x55555c26230b content::GpuDataManagerImpl::FallBackToNextGpuMode() +0ms
  pw:browser [pid=3768][err] #7 0x55555c26e569 content::GpuProcessHost::RecordProcessCrash() +0ms

playwright__33515.md:572-601 [playwright_pw]
  pw:browser [pid=3768][err] #10 0x55555c0ab270 content::internal::ChildProcessLauncherHelper::PostLaunchOnClientThread() +1ms
  pw:browser [pid=3768][err] #11 0x55555c0ab596 base::internal::Invoker<>::RunOnce() +0ms
  pw:browser [pid=3768][err] #12 0x55555e6e4f2f base::TaskAnnotator::RunTaskImpl() +0ms
  pw:browser [pid=3768][err] #13 0x55555e700969 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::DoWorkImpl() +0ms
  pw:browser [pid=3768][err] #14 0x55555e7003db base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::DoWork() +0ms
  pw:browser [pid=3768][err] #15 0x55555e700dc5 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::DoWork() +1ms
  pw:browser [pid=3768][err] #16 0x55555e76494c base::MessagePumpGlib::Run() +0ms
  pw:browser [pid=3768][err] #17 0x55555e701160 base::sequence_manager::internal::ThreadControllerWithMessagePumpImpl::Run() +0ms
  pw:browser [pid=3768][err] #18 0x55555e6c4de1 base::RunLoop::Run() +0ms
  pw:browser [pid=3768][err] #19 0x55555c050e1a content::BrowserMainLoop::RunMainMessageLoop() +0ms
  pw:browser [pid=3768][err] #20 0x55555c052ac2 content::BrowserMainRunnerImpl::Run() +0ms
  pw:browser [pid=3768][err] #21 0x555564e527df headless::HeadlessContentMainDelegate::RunProcess() +0ms
  pw:browser [pid=3768][err] #22 0x55555db2851b content::RunBrowserProcessMain() +0ms
  pw:browser [pid=3768][err] #23 0x55555db29d79 content::ContentMainRunnerImpl::RunBrowser() +0ms
  pw:browser [pid=3768][err] #24 0x55555db29933 content::ContentMainRunnerImpl::Run() +0ms
  pw:browser [pid=3768][err] #25 0x55555db27467 content::RunContentProcess() +0ms
  pw:browser [pid=3768][err] #26 0x55555db27697 content::ContentMain() +1ms
  pw:browser [pid=3768][err] #27 0x55555e166618 headless::HeadlessShellMain() +0ms
  pw:browser [pid=3768][err] #28 0x5555596d84d9 ChromeMain +0ms
  pw:browser [pid=3768][err] #29 0x2aaaac02b24a (/usr/lib/x86_64-linux-gnu/libc.so.6+0x27249) +0ms
  pw:browser [pid=3768][err] #30 0x2aaaac02b305 __libc_start_main +0ms
  pw:browser [pid=3768][err] #31 0x5555596d802a _start +0ms
  pw:browser [pid=3768][err] Task trace: +0ms
  pw:browser [pid=3768][err] #0 0x55555c0ab08f content::internal::ChildProcessLauncherHelper::PostLaunchOnLauncherThread() +0ms
  pw:browser [pid=3768][err] #1 0x55555c0aa2d8 content::internal::ChildProcessLauncherHelper::StartLaunchOnClientThread() +0ms
  pw:browser [pid=3768][err] #2 0x55555ea6fb78 mojo::SimpleWatcher::Context::Notify() +1ms
  pw:browser [pid=3768][err] #3 0x55555ea6fb78 mojo::SimpleWatcher::Context::Notify() +0ms
  pw:browser [pid=3768][err] #4 0x55555ea6fb78 mojo::SimpleWatcher::Context::Notify() +0ms
  pw:browser [pid=3768][err] Task trace buffer limit hit, update PendingTask::kTaskBacktraceLength to increase. +0ms
  pw:browser [pid=3768][err]  +0ms

playwright__33515.md:606-612 [playwright_pw]
  pw:browser <launching> /root/.cache/ms-playwright/chromium-1140/chrome-linux/chrome --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate,HttpsUpgrades,PaintHolding,ThirdPartyStoragePartitioning,LensOverlay,PlzDedicatedWorker --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --headless=old --hide-scrollbars --mute-audio --blink-settings=primaryHoverType=2,availableHoverTypes=2,primaryPointerType=4,availablePointerTypes=4 --no-sandbox --user-data-dir=/tmp/playwright_chromiumdev_profile-958UOc --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=3820 +16ms
  pw:browser <launching> /opt/google/chrome/chrome --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate,HttpsUpgrades,PaintHolding,ThirdPartyStoragePartitioning,LensOverlay,PlzDedicatedWorker --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --headless=old --hide-scrollbars --mute-audio --blink-settings=primaryHoverType=2,availableHoverTypes=2,primaryPointerType=4,availablePointerTypes=4 --no-sandbox --user-data-dir=/tmp/playwright_chromiumdev_profile-BBL79h --remote-debugging-pipe --no-startup-window +18ms
  pw:browser <launched> pid=3823 +11ms
  pw:browser [pid=3823][err] [1213/144935.235430:WARNING:chrome_main_linux.cc(80)] Read channel stable from /opt/google/chrome/CHROME_VERSION_EXTRA +49ms
  pw:browser [pid=3823][err] Old Headless mode will be removed from the Chrome binary soon. Please use the new Headless mode (https://developer.chrome.com/docs/chromium/new-headless) or the chrome-headless-shell which is a standalone implementation of the old Headless mode (https://developer.chrome.com/blog/chrome-headless-shell). +2ms
  pw:browser [pid=3823][err]  +0ms

playwright__33515.md:645-650 [playwright_pw]
  pw:browser [pid=3820][err] #0 0x55555e750152 base::debug::CollectStackTrace() +1ms
  pw:browser [pid=3820][err] #1 0x55555e73d90e base::debug::StackTrace::StackTrace() +1ms
  pw:browser [pid=3820][err] #2 0x55555e6943ea logging::LogMessage::Flush() +0ms
  pw:browser [pid=3820][err] #3 0x55555e6942cd logging::LogMessage::~LogMessage() +0ms
  pw:browser [pid=3820][err] #4 0x55555e67d820 logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +0ms
  pw:browser [pid=3820][err] #5 0x55555e67d87e logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +0ms

playwright__33515.md:652-663 [playwright_pw]
  pw:browser [pid=3820][err] #7 0x55555db2eb27 content::ZygoteMain() +0ms
  pw:browser [pid=3820][err] #8 0x55555db27b9e content::RunZygote() +0ms
  pw:browser [pid=3820][err] #9 0x55555db28892 content::RunOtherNamedProcessTypeMain() +1ms
  pw:browser [pid=3820][err] #10 0x55555db2990f content::ContentMainRunnerImpl::Run() +0ms
  pw:browser [pid=3820][err] #11 0x55555db27467 content::RunContentProcess() +0ms
  pw:browser [pid=3820][err] #12 0x55555db27697 content::ContentMain() +0ms
  pw:browser [pid=3820][err] #13 0x55555e16672c headless::HeadlessShellMain() +0ms
  pw:browser [pid=3820][err] #14 0x5555596d84d9 ChromeMain +0ms
  pw:browser [pid=3820][err] #15 0x2aaaac02b24a (/usr/lib/x86_64-linux-gnu/libc.so.6+0x27249) +1ms
  pw:browser [pid=3820][err] #16 0x2aaaac02b305 __libc_start_main +0ms
  pw:browser [pid=3820][err] #17 0x5555596d802a _start +0ms
  pw:browser [pid=3820][err]  +0ms

playwright__33515.md:666-671 [playwright_pw]
  pw:browser [pid=3820][err] #0 0x55555e750152 base::debug::CollectStackTrace() +0ms
  pw:browser [pid=3820][err] #1 0x55555e73d90e base::debug::StackTrace::StackTrace() +0ms
  pw:browser [pid=3820][err] #2 0x55555e6943ea logging::LogMessage::Flush() +0ms
  pw:browser [pid=3820][err] #3 0x55555e6942cd logging::LogMessage::~LogMessage() +1ms
  pw:browser [pid=3820][err] #4 0x55555e67d820 logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +0ms
  pw:browser [pid=3820][err] #5 0x55555e67d87e logging::(anonymous namespace)::CheckLogMessage::~CheckLogMessage() +0ms

playwright__33515.md:673-684 [playwright_pw]
  pw:browser [pid=3820][err] #7 0x55555db2eb27 content::ZygoteMain() +0ms
  pw:browser [pid=3820][err] #8 0x55555db27b9e content::RunZygote() +0ms
  pw:browser [pid=3820][err] #9 0x55555db28892 content::RunOtherNamedProcessTypeMain() +0ms
  pw:browser [pid=3820][err] #10 0x55555db2990f content::ContentMainRunnerImpl::Run() +0ms
  pw:browser [pid=3820][err] #11 0x55555db27467 content::RunContentProcess() +0ms
  pw:browser [pid=3820][err] #12 0x55555db27697 content::ContentMain() +0ms
  pw:browser [pid=3820][err] #13 0x55555e16672c headless::HeadlessShellMain() +1ms
  pw:browser [pid=3820][err] #14 0x5555596d84d9 ChromeMain +0ms
  pw:browser [pid=3820][err] #15 0x2aaaac02b24a (/usr/lib/x86_64-linux-gnu/libc.so.6+0x27249) +0ms
  pw:browser [pid=3820][err] #16 0x2aaaac02b305 __libc_start_main +0ms
  pw:browser [pid=3820][err] #17 0x5555596d802a _start +0ms
  pw:browser [pid=3820][err]  +0ms

playwright__33515.md:703-706 [playwright_pw]
  pw:browser [pid=3820] <process did exit: exitCode=0, signal=null> +80ms
  pw:browser [pid=3820] starting temporary directories cleanup +2ms
  pw:browser [pid=3820] finished temporary directories cleanup +8ms
  pw:browser [pid=3820] <gracefully close end> +1ms

playwright__34879.md:99-104 [playwright_pw]
 pw:browser <launching> C:\Users\Bunmi\AppData\Local\ms-playwright\chromium_headless_shell-1155\chrome-win\headless_shell.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate,HttpsUpgrades,PaintHolding,ThirdPartyStoragePartitioning,LensOverlay,PlzDedicatedWorker --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --headless --hide-scrollbars --mute-audio --blink-settings=primaryHoverType=2,availableHoverTypes=2,primaryPointerType=4,availablePointerTypes=4 --no-sandbox --disable-gpu --user-data-dir=C:\Users\Bunmi\AppData\Local\Temp\playwright_chromiumdev_profile-LboV7n --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=17680 +64ms
  pw:protocol SEND ► {"id":1,"method":"Browser.getVersion"} +0ms
  pw:browser [pid=17680] <gracefully close start> +55s
  pw:browser [pid=17680] <kill> +85ms
  pw:browser [pid=17680] <will force kill> +115ms

playwright__34879.md:106-110 [playwright_pw]
  pw:browser  +2s
  pw:browser [pid=17680] <process did exit: exitCode=0, signal=null> +18ms
  pw:browser [pid=17680] starting temporary directories cleanup +8ms
  pw:browser [pid=17680] finished temporary directories cleanup +39ms
  pw:browser [pid=17680] <gracefully close end> +21ms

playwright__35369.md:70-72 [playwright_pw]
  pw:api => selectors.setTestIdAttribute started +0ms
  pw:api => browserType.connect started +16ms
  pw:api <= selectors.setTestIdAttribute succeeded +21ms

playwright__36292.md:41-45 [playwright_pw]
  pw:browser <launching> C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=AcceptCHFrame,AutoExpandDetailsElement,AvoidUnnecessaryBeforeUnloadCheckSync,CertificateTransparencyComponentUpdater,DeferRendererTasksAfterInput,DestroyProfileOnBrowserClose,DialMediaRouteProvider,ExtensionManifestV2Disabled,GlobalMediaControls,HttpsUpgrades,ImprovedCookieControls,LazyFrameLoading,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --no-sandbox --remote-debugging-io-pipes=3,4 --user-data-dir=Temp\playwright_chromiumdev_profile-aXHo4Y --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=13144 +10ms
  pw:browser [pid=13144] <gracefully close start> +22ms
  pw:browser [pid=13144] <kill> +0ms
  pw:browser [pid=13144] <will force kill> +0ms

playwright__36292.md:47-51 [playwright_pw]
  pw:browser  +114ms
  pw:browser [pid=13144] <process did exit: exitCode=0, signal=null> +1ms
  pw:browser [pid=13144] starting temporary directories cleanup +0ms
  pw:browser [pid=13144] finished temporary directories cleanup +558ms
  pw:browser [pid=13144] <gracefully close end> +0ms

playwright__36714.md:96-101 [playwright_pw]
 pw:browser <launching> C:\Program Files\Google\Chrome\Application\chrome.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate,HttpsUpgrades,PaintHolding,PlzDedicatedWorker --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --no-sandbox --app=data:text/html, --window-size=1280,800 --test-type= --user-data-dir=C:\Users\<redacted>\AppData\Local\Temp\playwright_chromiumdev_profile-xMB9td --remote-debugging-pipe about:blank +0ms
  pw:browser <launched> pid=2444 +100ms
  pw:protocol SEND ► {"id":1,"method":"Browser.getVersion"} +0ms
  pw:browser [pid=2444] <gracefully close start> +257ms
  pw:browser [pid=2444] <kill> +1ms
  pw:browser [pid=2444] <will force kill> +0ms

playwright__36714.md:103-107 [playwright_pw]
  pw:browser  +1s
  pw:browser [pid=2444] <process did exit: exitCode=0, signal=null> +0ms
  pw:browser [pid=2444] starting temporary directories cleanup +1ms
  pw:browser [pid=2444] finished temporary directories cleanup +5ms
  pw:browser [pid=2444] <gracefully close end> +0ms

playwright__36716.md:64-70 [playwright_pw]
  pw:browser <launching> C:\Users\DELL\AppData\Local\ms-playwright\chromium-1181\chrome-win\chrome.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=AcceptCHFrame,AutoExpandDetailsElement,AvoidUnnecessaryBeforeUnloadCheckSync,CertificateTransparencyComponentUpdater,DestroyProfileOnBrowserClose,DialMediaRouteProvider,ExtensionManifestV2Disabled,GlobalMediaControls,HttpsUpgrades,ImprovedCookieControls,LazyFrameLoading,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --edge-skip-compat-layer-relaunch --enable-automation --no-sandbox --user-data-dir=C:\Users\DELL\AppData\Local\Temp\playwright_chromiumdev_profile-8t0jAx --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=17696 +7ms
  pw:browser <launching> C:\Users\DELL\AppData\Local\ms-playwright\chromium-1181\chrome-win\chrome.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=AcceptCHFrame,AutoExpandDetailsElement,AvoidUnnecessaryBeforeUnloadCheckSync,CertificateTransparencyComponentUpdater,DestroyProfileOnBrowserClose,DialMediaRouteProvider,ExtensionManifestV2Disabled,GlobalMediaControls,HttpsUpgrades,ImprovedCookieControls,LazyFrameLoading,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --edge-skip-compat-layer-relaunch --no-sandbox --app=data:text/html, --window-size=600,600 --window-position=1020,10 --test-type= --user-data-dir=C:\Users\DELL\AppData\Local\Temp\playwright_chromiumdev_profile-lQhaph --remote-debugging-pipe about:blank +195ms
  pw:browser <launched> pid=16056 +6ms
  pw:browser [pid=16056] <gracefully close start> +157ms
  pw:browser [pid=16056] <kill> +1ms
  pw:browser [pid=16056] <will force kill> +0ms

playwright__36716.md:72-86 [playwright_pw]
  pw:browser  +251ms
  pw:browser [pid=16056] <process did exit: exitCode=0, signal=null> +2ms
  pw:browser [pid=16056] starting temporary directories cleanup +1ms
  pw:browser [pid=16056] finished temporary directories cleanup +4ms
  pw:browser [pid=16056] <gracefully close end> +1ms
  pw:browser [pid=17696] <kill> +2ms
  pw:browser [pid=17696] <will force kill> +0ms
  pw:browser [pid=17696] taskkill stdout: SUCCESS: The process with PID 1344 (child process of PID 17696) has been terminated.
  pw:browser SUCCESS: The process with PID 20792 (child process of PID 17696) has been terminated.
  pw:browser SUCCESS: The process with PID 12340 (child process of PID 17696) has been terminated.
  pw:browser SUCCESS: The process with PID 8532 (child process of PID 17696) has been terminated.
  pw:browser SUCCESS: The process with PID 17696 (child process of PID 17136) has been terminated.
  pw:browser  +243ms
  pw:browser [pid=17696] starting temporary directories cleanup +0ms
  pw:browser [pid=17696] finished temporary directories cleanup +371ms

playwright__37032.md:74-95 [playwright_pw]
  pw:api => apiRequest.newContext started +0ms
  pw:api <= apiRequest.newContext succeeded +36ms
  pw:api => apiRequestContext.get started +2ms
  pw:api → GET https://httpbin.dev/zstd +5ms
  pw:api   user-agent: Playwright/1.55.0-next (arm64; macOS 15.6) node/22.15 +0ms
  pw:api   accept: */* +0ms
  pw:api   accept-encoding: gzip,deflate,br +0ms
  pw:api ← 200 OK +697ms
  pw:api   access-control-allow-credentials: true +1ms
  pw:api   access-control-allow-origin: * +0ms
  pw:api   alt-svc: h3=":443"; ma=2592000 +0ms
  pw:api   content-encoding: zstd +0ms
  pw:api   content-length: 231 +0ms
  pw:api   content-security-policy: frame-ancestors 'self' *.httpbin.dev; font-src 'self' *.httpbin.dev; default-src 'self' *.httpbin.dev; img-src 'self' *.httpbin.dev https://cdn.scrapfly.io; media-src 'self' *.httpbin.dev; object-src 'self' *.httpbin.dev https://web-scraping.dev; script-src 'self' 'unsafe-inline' 'unsafe-eval' *.httpbin.dev; style-src 'self' 'unsafe-inline' *.httpbin.dev https://unpkg.com; frame-src 'self' *.httpbin.dev https://web-scraping.dev; worker-src 'self' *.httpbin.dev; connect-src 'self' *.httpbin.dev +0ms
  pw:api   content-type: application/json; encoding=utf-8 +0ms
  pw:api   date: Thu, 14 Aug 2025 08:31:09 GMT +0ms
  pw:api   permissions-policy: fullscreen=(self), autoplay=*, geolocation=(), camera=() +0ms
  pw:api   referrer-policy: strict-origin-when-cross-origin +0ms
  pw:api   strict-transport-security: max-age=31536000; includeSubDomains; preload +0ms
  pw:api   x-content-type-options: nosniff +0ms
  pw:api   x-xss-protection: 1; mode=block +0ms
  pw:api <= apiRequestContext.get succeeded +3ms

playwright__37199.md:157-161 [playwright_pw]
  pw:browser [pid=22864] <gracefully close start> +547ms
  pw:browser [pid=22864] <kill> +1ms
  pw:browser [pid=22864] <will force kill> +0ms
  pw:browser [pid=22864] taskkill stderr:     :    μ    "22864"  (  ) ã           ϴ .
  pw:browser  +293ms

playwright__37199.md:163-165 [playwright_pw]
  pw:browser [pid=22864] starting temporary directories cleanup +1ms
  pw:browser [pid=22864] finished temporary directories cleanup +10ms
  pw:browser [pid=22864] <gracefully close end> +0ms

playwright__37199.md:171-191 [playwright_pw]
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\chromium-1187\\chrome-win\\chrome.exe","name":"chromium"},"guid":"browser-type@8c20030ac8cd52cbd478161e4cb959ba"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\firefox-1490\\firefox\\firefox.exe","name":"firefox"},"guid":"browser-type@3dfc659290bc396a1b6e970d81d0d35d"}} +1ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\webkit-2203\\Playwright.exe","name":"webkit"},"guid":"browser-type@184176c871c2f76f78c5173ee6e0616e"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\chromium-1187\\chrome-win\\chrome.exe","name":"_bidiChromium"},"guid":"browser-type@92ebb3ffc5ee7950d5b9bdf807a1da7d"}} +1ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"","name":"_bidiFirefox"},"guid":"browser-type@b157b90823a1d901ec0f71b332285b3a"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"Android","initializer":{},"guid":"android@d328731391a310fcd47099fa09084ba8"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"Electron","initializer":{},"guid":"electron@06d499a739730b943982c9be93ad5c1b"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"LocalUtils","initializer":{"deviceDescriptors":[{"name":"BlackX PlayBook","descriptor":{"userAgent":"Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/26.0 Safari/536.2+","viewport":{"width":600,"height":1024},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"BlackX PlayBook landscape","descriptor":{"userAgent":"Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/26.0 Safari/536.2+","viewport":{"width":1024,"height":600},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"BlackX Z30","descriptor":{"userAgent":"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/26.0 Mobile Safari/537.10+","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"BlackX Z30 landscape","descriptor":{"userAgent":"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/26.0 Mobile Safari/537.10+","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note 3","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note 3 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note II","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note II landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy S III","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy S III landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy S5","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S5 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S8","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":740},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S8 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":740,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S9+","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":320,"height":658},"deviceScaleFactor":4.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S9+ landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":658,"height":320},"deviceScaleFactor":4.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S24","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-S921U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":480,"height":1040},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S24 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-S921U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":1040,"height":480},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy A55","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-A556B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":480,"height":1040},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy A55 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-A556B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":1040,"height":480},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":712,"height":1138},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1138,"height":712},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S9","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-X710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":640,"height":1024},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S9 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-X710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1024,"height":640},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"iPad (gen 5)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":768,"height":1024},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 5) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1024,"height":768},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 6)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":768,"height":1024},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 6) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1024,"height":768},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 7)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":810,"height":1080},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 7) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1080,"height":810},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 11)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/604.1","viewport":{"width":656,"height":944},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 11) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/604.1","viewport":{"width":944,"height":656},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Mini","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":768,"height":1024},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Mini landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1024,"height":768},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Pro 11","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":834,"height":1194},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Pro 11 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1194,"height":834},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":414,"height":736},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":736,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":414,"height":736},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":736,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":414,"height":736},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":736,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/14E304 Safari/602.1","viewport":{"width":320,"height":568},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/14E304 Safari/602.1","viewport":{"width":568,"height":320},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE (3rd gen)","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/602.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE (3rd gen) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/602.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone X","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone X landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":812,"height":375},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone XR","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":414,"height":896},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone XR landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":896,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":414,"height":715},"screen":{"width":414,"height":896},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":800,"height":364},"screen":{"width":414,"height":896},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":375,"height":635},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":724,"height":325},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":414,"height":715},"screen":{"width":414,"height":896},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":808,"height":364},"screen":{"width":414,"height":896},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":340},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":340},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":428,"height":746},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":832,"height":378},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Mini","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":375,"height":629},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Mini landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":712,"height":325},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":342},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":342},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":428,"height":746},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":832,"height":380},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Mini","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":375,"height":629},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Mini landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":712,"height":327},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":340},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":428,"height":746},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":832,"height":378},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":393,"height":660},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":734,"height":343},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":430,"height":740},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":814,"height":380},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":393,"height":659},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":734,"height":343},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":430,"height":739},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":814,"height":380},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":393,"height":659},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":734,"height":343},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":430,"height":739},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":814,"height":380},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Kindle Fire HDX","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true","viewport":{"width":800,"height":1280},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Kindle Fire HDX landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true","viewport":{"width":1280,"height":800},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"LG Optimus L70","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":384,"height":640},"deviceScaleFactor":1.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"LG Optimus L70 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":384},"deviceScaleFactor":1.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 550","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 550 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 950","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":360,"height":640},"deviceScaleFactor":4,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 950 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":640,"height":360},"deviceScaleFactor":4,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 10","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":800,"height":1280},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 10 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1280,"height":800},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":384,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":384},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5X","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":732},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5X landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":732,"height":412},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":732},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":732,"height":412},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6P","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":732},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6P landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":732,"height":412},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 7","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":600,"height":960},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 7 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":960,"height":600},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nokia Lumia 520","descriptor":{"userAgent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)","viewport":{"width":320,"height":533},"deviceScaleFactor":1.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nokia Lumia 520 landscape","descriptor":{"userAgent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)","viewport":{"width":533,"height":320},"deviceScaleFactor":1.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nokia N9","descriptor":{"userAgent":"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13","viewport":{"width":480,"height":854},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Nokia N9 landscape","descriptor":{"userAgent":"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13","viewport":{"width":854,"height":480},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Pixel 2","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":411,"height":731},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 2 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":731,"height":411},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 2 XL","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":411,"height":823},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 2 XL landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":823,"height":411},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 3","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":393,"height":786},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 3 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":786,"height":393},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":353,"height":745},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":745,"height":353},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4a (5G)","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":765},"screen":{"width":412,"height":892},"deviceScaleFactor":2.63,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4a (5G) landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":840,"height":312},"screen":{"width":412,"height":892},"deviceScaleFactor":2.63,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 5","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":393,"height":727},"screen":{"width":393,"height":851},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 5 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":802,"height":293},"screen":{"width":851,"height":393},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 7","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":839},"screen":{"width":412,"height":915},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 7 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":863,"height":360},"screen":{"width":915,"height":412},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Moto G4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Moto G4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Desktop Chrome HiDPI","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Edge HiDPI","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36 Edg/140.0.7339.16","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Firefox HiDPI","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"firefox"}},{"name":"Desktop Safari","descriptor":{"userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"webkit"}},{"name":"Desktop Chrome","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1280,"height":720},"screen":{"width":1920,"height":1080},"deviceScaleFactor":1,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Edge","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36 Edg/140.0.7339.16","viewport":{"width":1280,"height":720},"screen":{"width":1920,"height":1080},"deviceScaleFactor":1,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Firefox","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0","viewport":{"width":1280,"height":720},"screen":{"width":1920,"height":1080},"deviceScaleFactor":1,"isMobile":false,"hasTouch":false,"defaultBrowserType":"firefox"}}]},"guid":"localUtils"}} +2ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"Playwright","initializer":{"chromium":{"guid":"browser-type@8c20030ac8cd52cbd478161e4cb959ba"},"firefox":{"guid":"browser-type@3dfc659290bc396a1b6e970d81d0d35d"},"webkit":{"guid":"browser-type@184176c871c2f76f78c5173ee6e0616e"},"_bidiChromium":{"guid":"browser-type@92ebb3ffc5ee7950d5b9bdf807a1da7d"},"_bidiFirefox":{"guid":"browser-type@b157b90823a1d901ec0f71b332285b3a"},"android":{"guid":"android@d328731391a310fcd47099fa09084ba8"},"electron":{"guid":"electron@06d499a739730b943982c9be93ad5c1b"},"utils":{"guid":"localUtils"}},"guid":"Playwright"}} +6ms
  pw:test:task "apply rebaselines" started +0ms
  pw:test:task "apply rebaselines" finished +0ms
  pw:test:task "clear output" started +0ms
  pw:test:task "clear output" finished +0ms
  pw:test:task "plugin setup" started +0ms
  pw:test:task "plugin setup" finished +0ms
  pw:test:task "load tests" started +0ms
  pw:test:task "load tests" finished +0ms
  pw:test:task "create phases" started +0ms
  pw:test:task created phase #1 with chromium projects, 1 testGroups +0ms
  pw:test:task "create phases" finished +0ms
  pw:test:task "report begin" started +0ms

playwright__37199.md:195-215 [playwright_pw]
  pw:test:task "report begin" finished +0ms
  pw:test:task "plugin begin" started +0ms
  pw:test:task "plugin begin" finished +0ms
  pw:test:task "test suite" started +0ms
  pw:test:protocol ◀ RECV {"method":"ready"} +0ms
  pw:test:protocol SEND ►  +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\chromium-1187\\chrome-win\\chrome.exe","name":"chromium"},"guid":"browser-type@975ab3188b08ab00d59e6556665525f5"}} +0ms

  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\firefox-1490\\firefox\\firefox.exe","name":"firefox"},"guid":"browser-type@005c63fe0c53397bfddba06497c7a342"}} +1ms                
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\webkit-2203\\Playwright.exe","name":"webkit"},"guid":"browser-type@c740259c6316e8098662f3817fd16ded"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"C:\\Users\\X\\AppData\\Local\\ms-playwright\\chromium-1187\\chrome-win\\chrome.exe","name":"_bidiChromium"},"guid":"browser-type@6156f43b86ad0507063ccd5d4839a591"}} +0ms       
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"BrowserType","initializer":{"executablePath":"","name":"_bidiFirefox"},"guid":"browser-type@765fe37e589796fd148831747b480f13"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"Android","initializer":{},"guid":"android@41692742972e59c1963ed6381bc19102"}} +0ms
  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"Electron","initializer":{},"guid":"electron@ccdc39582126cea0216fa6c66a94912f"}} +1ms

  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"LocalUtils","initializer":{"deviceDescriptors":[{"name":"BlackX PlayBook","descriptor":{"userAgent":"Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/26.0 Safari/536.2+","viewport":{"width":600,"height":1024},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"BlackX PlayBook landscape","descriptor":{"userAgent":"Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/26.0 Safari/536.2+","viewport":{"width":1024,"height":600},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"BlackX Z30","descriptor":{"userAgent":"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/26.0 Mobile Safari/537.10+","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"BlackX Z30 landscape","descriptor":{"userAgent":"Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/26.0 Mobile Safari/537.10+","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note 3","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note 3 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note II","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy Note II landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy S III","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy S III landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/26.0 Mobile Safari/534.30","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Galaxy S5","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S5 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S8","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":740},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S8 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":740,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S9+","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":320,"height":658},"deviceScaleFactor":4.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S9+ landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":658,"height":320},"deviceScaleFactor":4.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S24","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-S921U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":480,"height":1040},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy S24 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-S921U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":1040,"height":480},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy A55","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-A556B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":480,"height":1040},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy A55 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-A556B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":1040,"height":480},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":712,"height":1138},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1138,"height":712},"deviceScaleFactor":2.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S9","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-X710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":640,"height":1024},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Galaxy Tab S9 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; SM-X710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1024,"height":640},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"iPad (gen 5)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":768,"height":1024},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 5) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1024,"height":768},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 6)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":768,"height":1024},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 6) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1024,"height":768},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 7)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":810,"height":1080},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 7) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1080,"height":810},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 11)","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/604.1","viewport":{"width":656,"height":944},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad (gen 11) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/604.1","viewport":{"width":944,"height":656},"deviceScaleFactor":2.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Mini","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":768,"height":1024},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Mini landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1024,"height":768},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Pro 11","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":834,"height":1194},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPad Pro 11 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":1194,"height":834},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":414,"height":736},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 6 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":736,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":414,"height":736},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 7 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":736,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":414,"height":736},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 8 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":736,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/14E304 Safari/602.1","viewport":{"width":320,"height":568},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/14E304 Safari/602.1","viewport":{"width":568,"height":320},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE (3rd gen)","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/602.1","viewport":{"width":375,"height":667},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone SE (3rd gen) landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/26.0 Mobile/19E241 Safari/602.1","viewport":{"width":667,"height":375},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone X","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone X landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/26.0 Mobile/15A372 Safari/604.1","viewport":{"width":812,"height":375},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone XR","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":414,"height":896},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone XR landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":896,"height":414},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":414,"height":715},"screen":{"width":414,"height":896},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":800,"height":364},"screen":{"width":414,"height":896},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":375,"height":635},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":724,"height":325},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":414,"height":715},"screen":{"width":414,"height":896},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 11 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":808,"height":364},"screen":{"width":414,"height":896},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":340},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":340},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":428,"height":746},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":832,"height":378},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Mini","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":375,"height":629},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 12 Mini landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":712,"height":325},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":342},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":342},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":428,"height":746},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":832,"height":380},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Mini","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":375,"height":629},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 13 Mini landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":712,"height":327},"screen":{"width":375,"height":812},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":390,"height":664},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":750,"height":340},"screen":{"width":390,"height":844},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":428,"height":746},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":832,"height":378},"screen":{"width":428,"height":926},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":393,"height":660},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":734,"height":343},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":430,"height":740},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 14 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":814,"height":380},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":393,"height":659},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":734,"height":343},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Plus","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":430,"height":739},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Plus landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":814,"height":380},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":393,"height":659},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":734,"height":343},"screen":{"width":393,"height":852},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro Max","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":430,"height":739},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"iPhone 15 Pro Max landscape","descriptor":{"userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1","viewport":{"width":814,"height":380},"screen":{"width":430,"height":932},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Kindle Fire HDX","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true","viewport":{"width":800,"height":1280},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Kindle Fire HDX landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true","viewport":{"width":1280,"height":800},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"LG Optimus L70","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":384,"height":640},"deviceScaleFactor":1.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"LG Optimus L70 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":384},"deviceScaleFactor":1.25,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 550","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":360,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 550 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":640,"height":360},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 950","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":360,"height":640},"deviceScaleFactor":4,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Microsoft Lumia 950 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36 Edge/14.14263","viewport":{"width":640,"height":360},"deviceScaleFactor":4,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 10","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":800,"height":1280},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 10 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1280,"height":800},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":384,"height":640},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":384},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5X","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":732},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 5X landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":732,"height":412},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":732},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":732,"height":412},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6P","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":732},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 6P landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":732,"height":412},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 7","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":600,"height":960},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nexus 7 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":960,"height":600},"deviceScaleFactor":2,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nokia Lumia 520","descriptor":{"userAgent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)","viewport":{"width":320,"height":533},"deviceScaleFactor":1.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nokia Lumia 520 landscape","descriptor":{"userAgent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)","viewport":{"width":533,"height":320},"deviceScaleFactor":1.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Nokia N9","descriptor":{"userAgent":"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13","viewport":{"width":480,"height":854},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Nokia N9 landscape","descriptor":{"userAgent":"Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13","viewport":{"width":854,"height":480},"deviceScaleFactor":1,"isMobile":true,"hasTouch":true,"defaultBrowserType":"webkit"}},{"name":"Pixel 2","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":411,"height":731},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 2 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":731,"height":411},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 2 XL","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":411,"height":823},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 2 XL landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":823,"height":411},"deviceScaleFactor":3.5,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 3","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":393,"height":786},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 3 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":786,"height":393},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":353,"height":745},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":745,"height":353},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4a (5G)","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":765},"screen":{"width":412,"height":892},"deviceScaleFactor":2.63,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 4a (5G) landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 4a (5G)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":840,"height":312},"screen":{"width":412,"height":892},"deviceScaleFactor":2.63,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 5","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":393,"height":727},"screen":{"width":393,"height":851},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 5 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":802,"height":293},"screen":{"width":851,"height":393},"deviceScaleFactor":2.75,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 7","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":412,"height":839},"screen":{"width":412,"height":915},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Pixel 7 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":863,"height":360},"screen":{"width":915,"height":412},"deviceScaleFactor":2.625,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Moto G4","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":360,"height":640},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Moto G4 landscape","descriptor":{"userAgent":"Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Mobile Safari/537.36","viewport":{"width":640,"height":360},"deviceScaleFactor":3,"isMobile":true,"hasTouch":true,"defaultBrowserType":"chromium"}},{"name":"Desktop Chrome HiDPI","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Edge HiDPI","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36 Edg/140.0.7339.16","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Firefox HiDPI","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"firefox"}},{"name":"Desktop Safari","descriptor":{"userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15","viewport":{"width":1280,"height":720},"screen":{"width":1792,"height":1120},"deviceScaleFactor":2,"isMobile":false,"hasTouch":false,"defaultBrowserType":"webkit"}},{"name":"Desktop Chrome","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36","viewport":{"width":1280,"height":720},"screen":{"width":1920,"height":1080},"deviceScaleFactor":1,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Edge","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.7339.16 Safari/537.36 Edg/140.0.7339.16","viewport":{"width":1280,"height":720},"screen":{"width":1920,"height":1080},"deviceScaleFactor":1,"isMobile":false,"hasTouch":false,"defaultBrowserType":"chromium"}},{"name":"Desktop Firefox","descriptor":{"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0","viewport":{"width":1280,"height":720},"screen":{"width":1920,"height":1080},"deviceScaleFactor":1,"isMobile":false,"hasTouch":false,"defaultBrowserType":"firefox"}}]},"guid":"localUtils"}} +1ms

  pw:channel <EVENT {"guid":"","method":"__create__","params":{"type":"Playwright","initializer":{"chromium":{"guid":"browser-type@975ab3188b08ab00d59e6556665525f5"},"firefox":{"guid":"browser-type@005c63fe0c53397bfddba06497c7a342"},"webkit":{"guid":"browser-type@c740259c6316e8098662f3817fd16ded"},"_bidiChromium":{"guid":"browser-type@6156f43b86ad0507063ccd5d4839a591"},"_bidiFirefox":{"guid":"browser-type@765fe37e589796fd148831747b480f13"},"android":{"guid":"android@41692742972e59c1963ed6381bc19102"},"electron":{"guid":"electron@ccdc39582126cea0216fa6c66a94912f"},"utils":{"guid":"localUtils"}},"guid":"Playwright"}} +2ms


  pw:test test started "has title" +0ms                                                                                                                                                                                                                                                                  

playwright__37199.md:219-262 [playwright_pw]
  pw:test started test +1ms

  pw:test finished test +1ms                                                                                                                                                                                                                                                                             

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepBegin","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"hook@1","title":"Before Hooks","category":"hook","wallTime":1756355461908}}} +0ms
  pw:test started setup "playwright" +3ms                                                                                                                                                                                                                                                                

  pw:test finished setup "playwright" +1ms                                                                                                                                                                                                                                                               

  pw:test started setup "channel" +1ms                                                                                                                                                                                                                                                                   

  pw:test finished setup "channel" +0ms                                                                                                                                                                                                                                                                  

  pw:test started setup "_browserOptions" +0ms                                                                                                                                                                                                                                                           

  pw:test finished setup "_browserOptions" +0ms                                                                                                                                                                                                                                                          

  pw:test started setup "acceptDownloads" +0ms                                                                                                                                                                                                                                                           

  pw:test finished setup "acceptDownloads" +1ms                                                                                                                                                                                                                                                          

  pw:test started setup "bypassCSP" +0ms                                                                                                                                                                                                                                                                 

  pw:test finished setup "bypassCSP" +0ms                                                                                                                                                                                                                                                                

  pw:test started setup "clientCertificates" +0ms                                                                                                                                                                                                                                                        

  pw:test finished setup "clientCertificates" +0ms                                                                                                                                                                                                                                                       

  pw:test started setup "colorScheme" +0ms                                                                                                                                                                                                                                                               

  pw:test finished setup "colorScheme" +0ms                                                                                                                                                                                                                                                              

  pw:test started setup "extraHTTPHeaders" +1ms                                                                                                                                                                                                                                                          

  pw:test finished setup "extraHTTPHeaders" +0ms                                                                                                                                                                                                                                                         

  pw:test started setup "geolocation" +0ms                                                                                                                                                                                                                                                               

  pw:test finished setup "geolocation" +0ms                                                                                                                                                                                                                                                              

  pw:test started setup "httpCredentials" +1ms                                                                                                                                                                                                                                                           

  pw:test finished setup "httpCredentials" +0ms                                                                                                                                                                                                                                                          

playwright__37199.md:268-344 [playwright_pw]
  pw:test started setup "javaScriptEnabled" +0ms                                                                                                                                                                                                                                                         

  pw:test finished setup "javaScriptEnabled" +0ms                                                                                                                                                                                                                                                        

  pw:test started setup "locale" +0ms                                                                                                                                                                                                                                                                    

  pw:test finished setup "locale" +0ms                                                                                                                                                                                                                                                                   

  pw:test started setup "offline" +1ms                                                                                                                                                                                                                                                                   

  pw:test finished setup "offline" +0ms                                                                                                                                                                                                                                                                  

  pw:test started setup "permissions" +0ms                                                                                                                                                                                                                                                               

  pw:test finished setup "permissions" +0ms                                                                                                                                                                                                                                                              

  pw:test started setup "proxy" +0ms                                                                                                                                                                                                                                                                     

  pw:test finished setup "proxy" +0ms                                                                                                                                                                                                                                                                    

  pw:test started setup "storageState" +0ms                                                                                                                                                                                                                                                              

  pw:test finished setup "storageState" +0ms                                                                                                                                                                                                                                                             

  pw:test started setup "timezoneId" +1ms                                                                                                                                                                                                                                                                

  pw:test finished setup "timezoneId" +0ms                                                                                                                                                                                                                                                               

  pw:test started setup "baseURL" +0ms                                                                                                                                                                                                                                                                   

  pw:test finished setup "baseURL" +0ms                                                                                                                                                                                                                                                                  

  pw:test started setup "serviceWorkers" +0ms                                                                                                                                                                                                                                                            

  pw:test finished setup "serviceWorkers" +0ms                                                                                                                                                                                                                                                           

  pw:test started setup "_combinedContextOptions" +1ms                                                                                                                                                                                                                                                   

  pw:test finished setup "_combinedContextOptions" +0ms                                                                                                                                                                                                                                                  

  pw:test started setup "context configuration" +0ms                                                                                                                                                                                                                                                     

  pw:test finished setup "context configuration" +0ms                                                                                                                                                                                                                                                    

  pw:test started setup "trace recording" +0ms                                                                                                                                                                                                                                                           

  pw:test finished setup "trace recording" +1ms                                                                                                                                                                                                                                                          

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepEnd","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"hook@1","wallTime":1756355461918,"annotations":[]}}} +0ms
  pw:test started test +0ms                                                                                                                                                                                                                                                                              

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepBegin","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"pw:api@25","title":"Launch browser","category":"pw:api","wallTime":1756355461921,"location":{"file":"C:\\Users\\X\\REPO\\E2E\\bizpp-web\\tests\\test.spec.js","line":17,"column":47}}}} +0ms
  pw:api => browserType.launch started +0ms                                                                                                                                                                                                                                                              

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0mSEND> {\"id\":1,\"guid\":\"browser-type@975ab3188b08ab00d59e6556665525f5\",\"method\":\"launch\",\"params\":{\"ignoreAllDefaultArgs\":false,\"handleSIGINT\":fals  pw:channel SEND> {"id":1,"guid":"browser-type@975ab3188b08ab00d59e6556665525f5","method":"launch","params":{"ignoreAllDefaultArgs":false,"handleSIGINT":false,"timeout":180000,"headless":false,"tracesDir":"C:\\Users\\X\\REPO\\E2E\\bizpp-web\\test-results\\.playwright-artifacts-0\\traces"}} +241ms

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[30;1mpw:browser \u001b[0m<launching> C:\\Users\\X\\AppData\\Local\\ms-playwright\\chromium-1187\\chrome-win\\chrome.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=AcceptCHFrame,AvoidUnnecessaryBeforeUnloadCheckSync,DestroyProfileOnBrowserClose,DialMediaRouteProvider,GlobalMediaControls,HttpsUpgrades,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate,AutoDeElevate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --edge-skip-compat-layer-relaunch --enable-automation --no-sandbox --user-data-dir=C:\\Users\\X\\AppData\\Local\\Temp\\playwright_chromiumdev_profile-jBmjyh --remote-debugging-pipe --no-startup-window \u001b[30m+0ms\u001b[0m  pw:browser <launching> C:\Users\X\AppData\Local\ms-playwright\chromium-1187\chrome-win\chrome.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=AcceptCHFrame,AvoidUnnecessaryBeforeUnloadCheckSync,DestroyProfileOnBrowserClose,DialMediaRouteProvider,GlobalMediaControls,HttpsUpgrades,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate,AutoDeElevate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --edge-skip-compat-layer-relaunch --enable-automation --no-sandbox --user-data-dir=C:\Users\X\AppData\Local\Temp\playwright_chromiumdev_profile-jBmjyh --remote-debugging-pipe --no-startup-window +0ms

  pw:browser <launched> pid=21520 +20ms                                                                                                                                                                                                                                                                  

  pw:protocol SEND ► {"id":1,"method":"Browser.getVersion"} +0ms                                                                                                                                                                                                                                         

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;34;1mpw:protocol \u001b[0m◀ RECV {\"id\":1,\"result\":{\"protocolVersion\":\"1.3\",\"product\":\"Chrome/140.0.7339.16\",\"revision\":\"@b50d93d6db089ce82ddf985f059aa524051fcb2a\",\"userA  pw:protocol ◀ RECV {"id":1,"result":{"protocolVersion":"1.3","product":"Chrome/140.0.7339.16","revision":"@b50d93d6db089ce82ddf985f059aa524051fcb2a","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36","jsVersion":"14.0.365.1"}} +474ms

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;34;1mpw:protocol \u001b[0mSEND ► {\"id\":2,\"method\":\"Target.setAutoAttach\",\"params\":{\"autoAttach\":true,\"waitForDebuggerOnStart\":true,\"flatten\":true}} \u001b[38;5;34m+0ms\u001  pw:protocol SEND ► {"id":2,"method":"Target.setAutoAttach","params":{"autoAttach":true,"waitForDebuggerOnStart":true,"flatten":true}} +0ms                                                                                                                                                             

  pw:protocol ◀ RECV {"id":2,"result":{}} +9ms                                                                                                                                                                                                                                                           

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0m<EVENT {\"guid\":\"browser-type@975ab3188b08ab00d59e6556665525f5\",\"method\":\"__create__\",\"params\":{\"type\":\"Browser\",\"initializer\":{\"version\":\"140.  pw:channel <EVENT {"guid":"browser-type@975ab3188b08ab00d59e6556665525f5","method":"__create__","params":{"type":"Browser","initializer":{"version":"140.0.7339.16","name":"chromium"},"guid":"browser@e90ab2087a19810f39b884927351dfd8"}} +510ms                                                      

  pw:channel <RECV {"id":1,"result":{"browser":{"guid":"browser@e90ab2087a19810f39b884927351dfd8"}}} +1ms                                                                                                                                                                                                

  pw:api <= browserType.launch succeeded +512ms                                                                                                                                                                                                                                                          

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepEnd","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"pw:api@25","wallTime":1756355462433,"annotations":[]}}} +0ms
  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepBegin","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"pw:api@26","title":"Create page","category":"pw:api","wallTime":1756355462435,"location":{"file":"C:\\Users\\X\\REPO\\E2E\\bizpp-web\\tests\\test.spec.js","line":18,"column":32}}}} +0ms
  pw:api => browser.newPage started +2ms                                                                                                                                                                                                                                                                 

playwright__37199.md:349-361 [playwright_pw]
  pw:protocol SEND ► {"id":3,"method":"Target.createBrowserContext","params":{"disposeOnDetach":true}} +5ms                                                                                                                                                                                              

  pw:protocol ◀ RECV {"id":3,"result":{"browserContextId":"56EC7CCFC369170AE7A4A99E40D98FA5"}} +5ms                                                                                                                                                                                                      

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;34;1mpw:protocol \u001b[0mSEND ► {\"id\":4,\"method\":\"Browser.setDownloadBehavior\",\"params\":{\"behavior\":\"allowAndName\",\"browserContextId\":\"56EC7CCFC369170AE7A4A99E40D98FA5\",  pw:protocol SEND ► {"id":4,"method":"Browser.setDownloadBehavior","params":{"behavior":"allowAndName","browserContextId":"56EC7CCFC369170AE7A4A99E40D98FA5","downloadPath":"C:\\Users\\X\\AppData\\Local\\Temp\\playwright-artifacts-jdxoXt","eventsEnabled":true}} +2ms                           

  pw:protocol ◀ RECV {"id":4,"result":{}} +1ms                                                                                                                                                                                                                                                           

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0m<EVENT {\"guid\":\"browser@e90ab2087a19810f39b884927351dfd8\",\"method\":\"__create__\",\"params\":{\"type\":\"Tracing\",\"initializer\":{},\"guid\":\"tracing@78  pw:channel <EVENT {"guid":"browser@e90ab2087a19810f39b884927351dfd8","method":"__create__","params":{"type":"Tracing","initializer":{},"guid":"tracing@7801b1bdb1d47357f92aa57602f56e0f"}} +10ms                                                                                                       

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0m<EVENT {\"guid\":\"browser@e90ab2087a19810f39b884927351dfd8\",\"method\":\"__create__\",\"params\":{\"type\":\"APIRequestContext\",\"initializer\":{\"tracing\":{  pw:channel <EVENT {"guid":"browser@e90ab2087a19810f39b884927351dfd8","method":"__create__","params":{"type":"APIRequestContext","initializer":{"tracing":{"guid":"tracing@7801b1bdb1d47357f92aa57602f56e0f"}},"guid":"request-context@32a903002b936c4f18fb2b983b7053e2"}} +0ms                         

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0m<EVENT {\"guid\":\"request-context@32a903002b936c4f18fb2b983b7053e2\",\"method\":\"__adopt__\",\"params\":{\"guid\":\"tracing@7801b1bdb1d47357f92aa57602f56e0f\"}  pw:channel <EVENT {"guid":"request-context@32a903002b936c4f18fb2b983b7053e2","method":"__adopt__","params":{"guid":"tracing@7801b1bdb1d47357f92aa57602f56e0f"}} +1ms                                                                                                                                   

playwright__37199.md:365-383 [playwright_pw]
  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0m<EVENT {\"guid\":\"browser-context@4d6bf156d83ad3bcee0c9a1d78133774\",\"method\":\"__adopt__\",\"params\":{\"guid\":\"request-context@32a903002b936c4f18fb2b983b7  pw:channel <EVENT {"guid":"browser-context@4d6bf156d83ad3bcee0c9a1d78133774","method":"__adopt__","params":{"guid":"request-context@32a903002b936c4f18fb2b983b7053e2"}} +0ms                                                                                                                           

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0m<EVENT {\"guid\":\"browser-context@4d6bf156d83ad3bcee0c9a1d78133774\",\"method\":\"__adopt__\",\"params\":{\"guid\":\"tracing@7801b1bdb1d47357f92aa57602f56e0f\"}  pw:channel <EVENT {"guid":"browser-context@4d6bf156d83ad3bcee0c9a1d78133774","method":"__adopt__","params":{"guid":"tracing@7801b1bdb1d47357f92aa57602f56e0f"}} +0ms                                                                                                                                   

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;33;1mpw:channel \u001b[0m<EVENT {\"guid\":\"browser@e90ab2087a19810f39b884927351dfd8\",\"method\":\"context\",\"params\":{\"context\":{\"guid\":\"browser-context@4d6bf156d83ad3bcee0c9a1d  pw:channel <EVENT {"guid":"browser@e90ab2087a19810f39b884927351dfd8","method":"context","params":{"context":{"guid":"browser-context@4d6bf156d83ad3bcee0c9a1d78133774"}}} +0ms                                                                                                                         

  pw:channel <RECV {"id":2,"result":{"context":{"guid":"browser-context@4d6bf156d83ad3bcee0c9a1d78133774"}}} +0ms                                                                                                                                                                                        

  pw:channel SEND> {"id":3,"guid":"browser-context@4d6bf156d83ad3bcee0c9a1d78133774","method":"newPage"} +1ms                                                                                                                                                                                            

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stdErr","params":{"text":"  \u001b[38;5;34;1mpw:protocol \u001b[0mSEND ► {\"id\":5,\"method\":\"Target.createTarget\",\"params\":{\"url\":\"about:blank\",\"browserContextId\":\"56EC7CCFC369170AE7A4A99E40D98FA5\"}} \u001b[38;5;  pw:protocol SEND ► {"id":5,"method":"Target.createTarget","params":{"url":"about:blank","browserContextId":"56EC7CCFC369170AE7A4A99E40D98FA5"}} +4ms                                                                                                                                                   

  pw:channel <EVENT {"guid":"browser-context@4d6bf156d83ad3bcee0c9a1d78133774","method":"close"} +46ms                                                                                                                                                                                                   

  pw:channel <EVENT {"guid":"browser-context@4d6bf156d83ad3bcee0c9a1d78133774","method":"__dispose__","params":{}} +1ms                                                                                                                                                                                  

  pw:channel <EVENT {"guid":"browser@e90ab2087a19810f39b884927351dfd8","method":"close"} +0ms                                                                                                                                                                                                            

  pw:channel <EVENT {"guid":"browser@e90ab2087a19810f39b884927351dfd8","method":"__dispose__","params":{}} +0ms                                                                                                                                                                                          

playwright__37199.md:390-467 [playwright_pw]
  pw:test finished test +576ms                                                                                                                                                                                                                                                                           

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepBegin","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"hook@27","title":"After Hooks","category":"hook","wallTime":1756355462494}}} +0ms
  pw:test started test +1ms                                                                                                                                                                                                                                                                              

  pw:test finished test +0ms                                                                                                                                                                                                                                                                             

  pw:test started teardown "trace recording" +0ms                                                                                                                                                                                                                                                        

  pw:test finished teardown "trace recording" +0ms                                                                                                                                                                                                                                                       

  pw:test started teardown "context configuration" +0ms                                                                                                                                                                                                                                                  

  pw:test finished teardown "context configuration" +0ms                                                                                                                                                                                                                                                 

  pw:test started teardown "testIdAttribute" +1ms                                                                                                                                                                                                                                                        

  pw:test finished teardown "testIdAttribute" +0ms                                                                                                                                                                                                                                                       

  pw:test started teardown "navigationTimeout" +0ms                                                                                                                                                                                                                                                      

  pw:test finished teardown "navigationTimeout" +0ms                                                                                                                                                                                                                                                     

  pw:test started teardown "actionTimeout" +0ms                                                                                                                                                                                                                                                          

  pw:test finished teardown "actionTimeout" +0ms                                                                                                                                                                                                                                                         

  pw:test started teardown "_combinedContextOptions" +0ms                                                                                                                                                                                                                                                

  pw:test finished teardown "_combinedContextOptions" +0ms                                                                                                                                                                                                                                               

  pw:test started teardown "serviceWorkers" +0ms                                                                                                                                                                                                                                                         

  pw:test finished teardown "serviceWorkers" +0ms                                                                                                                                                                                                                                                        

  pw:test started teardown "baseURL" +0ms                                                                                                                                                                                                                                                                

  pw:test finished teardown "baseURL" +0ms

  pw:test started teardown "userAgent" +1ms                                                                                                                                                                                                                                                              

  pw:test finished teardown "userAgent" +0ms                                                                                                                                                                                                                                                             

  pw:test started teardown "timezoneId" +0ms                                                                                                                                                                                                                                                             

  pw:test finished teardown "timezoneId" +0ms                                                                                                                                                                                                                                                            

  pw:test started teardown "viewport" +0ms                                                                                                                                                                                                                                                               

  pw:test finished teardown "viewport" +0ms                                                                                                                                                                                                                                                              

  pw:test started teardown "storageState" +0ms                                                                                                                                                                                                                                                           

  pw:test finished teardown "storageState" +0ms                                                                                                                                                                                                                                                          

  pw:test started teardown "proxy" +0ms                                                                                                                                                                                                                                                                  

  pw:test finished teardown "proxy" +0ms                                                                                                                                                                                                                                                                 

  pw:test started teardown "permissions" +0ms                                                                                                                                                                                                                                                            

  pw:test finished teardown "permissions" +0ms                                                                                                                                                                                                                                                           

  pw:test started teardown "offline" +0ms                                                                                                                                                                                                                                                                

  pw:test finished teardown "offline" +0ms                                                                                                                                                                                                                                                               

  pw:test started teardown "locale" +1ms                                                                                                                                                                                                                                                                 

  pw:test finished teardown "locale" +0ms                                                                                                                                                                                                                                                                

  pw:test started teardown "javaScriptEnabled" +0ms                                                                                                                                                                                                                                                      

  pw:test finished teardown "javaScriptEnabled" +0ms                                                                                                                                                                                                                                                     

  pw:test started teardown "isMobile" +0ms                                                                                                                                                                                                                                                               

  pw:test finished teardown "isMobile" +0ms                                                                                                                                                                                                                                                              

playwright__37199.md:473-542 [playwright_pw]
  pw:test started teardown "httpCredentials" +0ms                                                                                                                                                                                                                                                        

  pw:test finished teardown "httpCredentials" +0ms                                                                                                                                                                                                                                                       

  pw:test started teardown "geolocation" +0ms                                                                                                                                                                                                                                                            

  pw:test finished teardown "geolocation" +0ms                                                                                                                                                                                                                                                           

  pw:test started teardown "hasTouch" +0ms                                                                                                                                                                                                                                                               

  pw:test finished teardown "hasTouch" +0ms                                                                                                                                                                                                                                                              

  pw:test started teardown "extraHTTPHeaders" +0ms                                                                                                                                                                                                                                                       

  pw:test finished teardown "extraHTTPHeaders" +1ms                                                                                                                                                                                                                                                      

  pw:test started teardown "deviceScaleFactor" +0ms                                                                                                                                                                                                                                                      

  pw:test finished teardown "deviceScaleFactor" +0ms                                                                                                                                                                                                                                                     

  pw:test started teardown "colorScheme" +0ms                                                                                                                                                                                                                                                            

  pw:test finished teardown "colorScheme" +0ms                                                                                                                                                                                                                                                           

  pw:test started teardown "clientCertificates" +0ms                                                                                                                                                                                                                                                     

  pw:test finished teardown "clientCertificates" +0ms                                                                                                                                                                                                                                                    

  pw:test started teardown "bypassCSP" +0ms                                                                                                                                                                                                                                                              

  pw:test finished teardown "bypassCSP" +0ms                                                                                                                                                                                                                                                             

  pw:test started teardown "acceptDownloads" +0ms                                                                                                                                                                                                                                                        

  pw:test finished teardown "acceptDownloads" +0ms                                                                                                                                                                                                                                                       

  pw:test started teardown "contextOptions" +0ms                                                                                                                                                                                                                                                         

  pw:test finished teardown "contextOptions" +0ms                                                                                                                                                                                                                                                        

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepEnd","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"hook@27","wallTime":1756355462499,"annotations":[]}}} +0ms
  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepBegin","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"hook@57","title":"Worker Cleanup","category":"hook","wallTime":1756355462500}}} +0ms
  pw:test started teardown "screenshot" +1ms                                                                                                                                                                                                                                                             

  pw:test finished teardown "screenshot" +0ms                                                                                                                                                                                                                                                            

  pw:test started teardown "_browserOptions" +0ms                                                                                                                                                                                                                                                        

  pw:test finished teardown "_browserOptions" +0ms                                                                                                                                                                                                                                                       

  pw:test started teardown "channel" +0ms                                                                                                                                                                                                                                                                

  pw:test finished teardown "channel" +0ms                                                                                                                                                                                                                                                               

  pw:test started teardown "launchOptions" +0ms                                                                                                                                                                                                                                                          

  pw:test finished teardown "launchOptions" +0ms                                                                                                                                                                                                                                                         

  pw:test started teardown "headless" +1ms                                                                                                                                                                                                                                                               

  pw:test finished teardown "headless" +0ms                                                                                                                                                                                                                                                              

  pw:test started teardown "playwright" +0ms                                                                                                                                                                                                                                                             

  pw:test finished teardown "playwright" +0ms                                                                                                                                                                                                                                                            

  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"method":"stepEnd","params":{"testId":"31be70adcd52654ff551-57548ebc9bbec6bb12dd","stepId":"hook@57","wallTime":1756355462501,"annotations":[]}}} +0ms
  pw:test started test +0ms                                                                                                                                                                                                                                                                              

  pw:test finished test +0ms                                                                                                                                                                                                                                                                             

playwright__37199.md:565-581 [playwright_pw]
  pw:test:protocol SEND ► {"method":"__stop__"} +0ms
  pw:test:protocol ◀ RECV {"method":"__dispatch__","params":{"id":1}} +0ms
  pw:test:protocol ◀ RECV {"method":"__env_produced__","params":[["TEST_PARALLEL_INDEX","0"],["TEST_WORKER_INDEX","0"]]} +0ms
  pw:test started teardown +36ms                                                                                                                                                                                                                                                                         

  pw:test finished teardown +0ms                                                                                                                                                                                                                                                                         

  pw:test started teardown +0ms                                                                                                                                                                                                                                                                          

  pw:browser [pid=21520] <gracefully close start> +591ms                                                                                                                                                                                                                                                 

  pw:browser [pid=21520] <kill> +0ms                                                                                                                                                                                                                                                                     

  pw:browser [pid=21520] <will force kill> +0ms                                                                                                                                                                                                                                                          

  pw:browser [pid=21520] taskkill stderr:     :    μ    "21520"  (  ) ã           ϴ .                                                                                                                                                                                                                    
  pw:browser  +317ms

playwright__37199.md:585-608 [playwright_pw]
  pw:browser [pid=21520] starting temporary directories cleanup +0ms                                                                                                                                                                                                                                     

  pw:browser [pid=21520] finished temporary directories cleanup +9ms                                                                                                                                                                                                                                     

  pw:browser [pid=21520] <gracefully close end> +0ms                                                                                                                                                                                                                                                     

  pw:test finished teardown +16s                                                                                                                                                                                                                                                                         

  pw:test:task "test suite" finished +0ms
  pw:test:task "teardown for test suite" started +0ms
  pw:test:task "teardown for test suite" finished +0ms
  pw:test:task "teardown for plugin begin" started +0ms
  pw:test:task "teardown for plugin begin" finished +0ms
  pw:test:task "teardown for report begin" started +0ms
  pw:test:task "teardown for report begin" finished +0ms
  pw:test:task "teardown for create phases" started +0ms
  pw:test:task "teardown for create phases" finished +0ms
  pw:test:task "teardown for load tests" started +0ms
  pw:test:task "teardown for load tests" finished +0ms
  pw:test:task "teardown for plugin setup" started +0ms
  pw:test:task "teardown for plugin setup" finished +0ms
  pw:test:task "teardown for clear output" started +0ms
  pw:test:task "teardown for clear output" finished +0ms
  pw:test:task "teardown for apply rebaselines" started +0ms

playwright__41347.md:266-269 [playwright_pw]
  pw:browser [pid=31828][err] JavaScript warning: resource://services-settings/Utils.sys.mjs, line 119: unreachable code after return statement +285ms
  pw:browser [pid=3276] <gracefully close start> +2s
  pw:browser [pid=31828][out]  +2s
  pw:browser [pid=31828][out] Juggler listening to the pipe +1ms

playwright__41347.md:273-283 [playwright_pw]
  pw:browser [pid=29396][err] JavaScript warning: resource://services-settings/Utils.sys.mjs, line 119: unreachable code after return statement +2s
  pw:browser [pid=3276] <process did exit: exitCode=0, signal=null> +789ms
  pw:browser [pid=3276] starting temporary directories cleanup +0ms
  pw:browser [pid=3276] finished temporary directories cleanup +21ms
  pw:browser [pid=3276] <gracefully close end> +0ms
  pw:browser [pid=28384] <process did exit: exitCode=0, signal=null> +535ms
  pw:browser [pid=28384] starting temporary directories cleanup +0ms
  pw:browser [pid=28384] finished temporary directories cleanup +20ms
  pw:browser [pid=28384] <gracefully close end> +0ms
  pw:browser [pid=29396][out]  +530ms
  pw:browser [pid=29396][out] Juggler listening to the pipe +1ms

playwright__41347.md:289-300 [playwright_pw]
  pw:browser <launching> C:\Users\XXX\AppData\Local\ms-playwright\webkit-2311\Playwright.exe --inspector-pipe --disable-accelerated-compositing --no-startup-window +0ms
  pw:browser <launched> pid=14584 +15ms
  pw:browser [pid=28160] <gracefully close start> +1s
  pw:browser [pid=28160] <process did exit: exitCode=0, signal=null> +31ms
  pw:browser [pid=28160] starting temporary directories cleanup +1ms
  pw:browser [pid=28160] finished temporary directories cleanup +2ms
  pw:browser [pid=28160] <gracefully close end> +0ms
  pw:browser [pid=14584] <gracefully close start> +2s
  pw:browser [pid=14584] <process did exit: exitCode=0, signal=null> +42ms
  pw:browser [pid=14584] starting temporary directories cleanup +0ms
  pw:browser [pid=14584] finished temporary directories cleanup +1ms
  pw:browser [pid=14584] <gracefully close end> +0ms

playwright__41347.md:310-313 [playwright_pw]
  pw:browser [pid=31828] <process did exit: exitCode=0, signal=null> +59ms
  pw:browser [pid=31828] starting temporary directories cleanup +1ms
  pw:browser [pid=31828] finished temporary directories cleanup +8ms
  pw:browser [pid=31828] <gracefully close end> +0ms

playwright__41347.md:347-350 [playwright_pw]
  pw:browser [pid=29396] <process did exit: exitCode=0, signal=null> +63ms
  pw:browser [pid=29396] starting temporary directories cleanup +1ms
  pw:browser [pid=29396] finished temporary directories cleanup +7ms
  pw:browser [pid=29396] <gracefully close end> +0ms

playwright__41438.md:163-169 [playwright_pw]
  pw:browser <launching> C:\Program Files\Google\Chrome\Application\chrome.exe --disable-field-trial-config --disable-background-networking --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-component-update --no-default-browser-check --disable-default-apps --disable-dev-shm-usage --disable-edgeupdater --disable-extensions --disable-features=AvoidUnnecessaryBeforeUnloadCheckSync,BoundaryEventDispatchTracksNodeRemoval,DestroyProfileOnBrowserClose,DialMediaRouteProvider,GlobalMediaControls,HttpsUpgrades,LensOverlay,MediaRouter,PaintHolding,ThirdPartyStoragePartitioning,Translate,AutoDeElevate,RenderDocument,OptimizationHints,msForceBrowserSignIn,msEdgeUpdateLaunchServicesPreferredVersion --enable-features=CDPScreenshotNewSurface --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --force-color-profile=srgb --metrics-recording-only --no-first-run --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --disable-search-engine-choice-screen --unsafely-disable-devtools-self-xss-warnings --edge-skip-compat-layer-relaunch --disable-infobars --disable-search-engine-choice-screen --disable-sync --enable-unsafe-swiftshader --no-sandbox --user-data-dir=C:\Users\PRAVEE~1\AppData\Local\Temp\playwright_chromiumdev_profile-WZToBR --remote-debugging-pipe --no-startup-window +0ms
  pw:browser <launched> pid=18924 +11ms
  pw:browser [pid=18924] <gracefully close start> +9s
  pw:browser [pid=18924] <process did exit: exitCode=0, signal=null> +137ms
  pw:browser [pid=18924] starting temporary directories cleanup +0ms
  pw:browser [pid=18924] finished temporary directories cleanup +20ms
  pw:browser [pid=18924] <gracefully close end> +0ms
