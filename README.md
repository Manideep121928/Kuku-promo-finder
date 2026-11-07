# 🎬 Kuku Microdrama Promo Extractor & Ranker

An automated AI pipeline and interactive web dashboard built to extract, analyze, and rank high-converting, standalone promotional clips (20–60 seconds) from microdrama screenplays. Designed for fast-paced content platforms like ReelShort and DramaBox.

## 🚀 Key Features

* **Clip Extraction**: Utilizes Gemini 3.5 Flash-Lite to analyze raw screenplay text and identify high-tension promotional windows.
* **Strict Duration & Continuity Enforcement**: Programmatically validates and enforces clip windows to be strictly 20 to 60 seconds long, preventing excessively short cuts or fragmented clips.
* **Multi-Option Support**: Extracts multiple viable promo options per episode (e.g., mid-scene conflict twists and ending cliffhangers) to maximize marketing flexibility.
* **Automated Heuristic Ranking**: Calculates a global leaderboard ranking based on narrative richness, hook impact, and retention potential.
* **Adaptive Streamlit Dashboard**: Provides a clean, responsive UI supporting both light and dark modes, featuring:
  * Global and segment-level ranking displays.
  * Tabbed navigation across multiple promo options per episode.
  * Direct JSON download capabilities for each processed screenplay.

## 🛠️ Tech Stack

* **AI Model**: Google Gemini (`gemini-3.5-flash-lite`) via `google-generativeai`
* **Web Framework**: Streamlit
* **Language**: Python

## 📁 Repository Structure

```text
├── Episodes/              # Folder containing raw input screenplay .txt files
├── raw_outputs1/          # Generated JSON outputs containing multi-option promos & timestamps
├── extractor.py           # Automated AI extraction script with duration validation
├── app.py                 # Interactive Streamlit dashboard application
└── requirements.txt       # Project dependencies
