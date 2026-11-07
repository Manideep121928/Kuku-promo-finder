and?# 🎬 Kuku Microdrama Promo Extractor & Ranker
An automated AI pipeline and interactive web dashboard built to extract, analyze, and rank high-converting, standalone promotional clips (20–60 seconds) from microdrama screenplays. Designed for fast-paced content platforms like ReelShort and DramaBox.

🚀 Key Features
Intelligent Clip Extraction: Utilizes Gemini 3.5 Flash-Lite to analyze raw screenplay text and identify high-tension promotional windows.

Strict Duration & Continuity Enforcement: Programmatically validates and enforces clip windows to be strictly 20 to 60 seconds long, preventing excessively short cuts or fragmented clips.

Multi-Option Support: Extracts multiple viable promo options per episode (e.g., mid-scene conflict twists and ending cliffhangers) to maximize marketing flexibility.

Automated Heuristic Ranking: Calculates a global leaderboard ranking based on narrative richness, hook impact, and retention potential.

Adaptive Streamlit Dashboard: Provides a clean, responsive UI supporting both light and dark modes, featuring:

Global and segment-level ranking displays.

Tabbed navigation across multiple promo options per episode.

Direct JSON download capabilities for each processed screenplay.

🛠️ Tech Stack
AI Model: Google Gemini (gemini-3.5-flash-lite) via google-generativeai

Web Framework: Streamlit

Language: Python

📁 Repository Structure
Plaintext
├── Episodes/              # Folder containing raw input screenplay .txt files
├── raw_outputs1/          # Generated JSON outputs containing multi-option promos & timestamps
├── extractor.py           # Automated AI extraction script with duration validation
├── app.py                 # Interactive Streamlit dashboard application
└── requirements.txt       # Project dependencies
⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/Manideep1928/Kuku-promo-finder.git
cd Kuku-promo-finder
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Set Up Your API Key
Set your Gemini API key as an environment variable or configure it directly in your script:

Bash
# On Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"

# On macOS/Linux
export GEMINI_API_KEY="your_api_key_here"
🏃 Usage
Step 1: Run the Extractor Pipeline
Place your raw screenplay text files inside the Episodes/ directory, then run the extraction script to process and validate the 20–60 second promo clips into raw_outputs1/:

Bash
python extractor.py
Step 2: Launch the Streamlit Dashboard
Run the Streamlit application locally to explore the interactive leaderboard and episode browser:

Bash
streamlit run app.py
📊 JSON Data Schema
Each processed JSON file in raw_outputs1/ adheres to the following structure:

JSON
{
  "episode_number": "Episode 1",
  "promo_options": [
    {
      "option_number": 1,
      "segments": [
      {
          "start_timestamp": " ",
          "end_timestamp": " "
        }
      ],
      "hook": "Juliana discovers her fiancé at the altar with another woman.",
      "cliffhanger": "Juliana gasps in devastation as the dramatic score cuts to black.",
      "reasoning": "Quickly establishes the core betrayal and emotional stakes for new viewers."
    }
  ]
}
