
# 🎬 Kuku Microdrama Promo Extractor & Ranker
[![Streamlit App](https://img.shields.io/badge/Streamlit-Open_App-blue?logo=streamlit)](https://kuku-promo-finder-azwufwgoh5hwvsq8oxs2wp.streamlit.app/)
An AI-powered pipeline and interactive web dashboard designed to extract, analyze, and rank high-potential promotional clips (20–60 seconds) from microdrama screenplays.

Built for short-form storytelling platforms such as ReelShort and DramaBox, the system identifies compelling narrative moments, emotional hooks, and cliffhangers that can be used as standalone promotional content.

## 🚀 Key Features

### 1.Promo Clip Extraction
- Uses **Google Gemini 3.5 Flash-Lite** to analyze raw screenplay text.
- Identifies high-tension scenes, emotional turning points, dramatic reveals, and compelling cliffhangers.
- Extracts standalone promotional segments with strong audience-engagement potential.

### 2. Strict Duration & Continuity Enforcement
- Enforces a strict promotional clip duration of **20–60 seconds**.
- Programmatically validates extracted timestamps.
- Prevents excessively short clips and fragmented promotional sequences.
- Ensures extracted segments maintain narrative continuity.

### 3. Multi-Option Promo Generation
- Generates multiple promotional clip options for each episode.
- Identifies different promotional opportunities, including:
  - Mid-scene conflicts and dramatic twists.
  - Emotional confrontations and unexpected revelations.
  - Episode-ending cliffhangers.
- Provides greater flexibility for promotional content selection.

### 4. Automated Heuristic Ranking
- Evaluates extracted promotional clips using a heuristic scoring mechanism.
- Considers factors such as:
  - Narrative richness.
  - Hook impact.
  - Emotional intensity.
  - Audience retention potential.
- Generates a global leaderboard to rank promotional options across episodes.

### 5. Interactive Streamlit Dashboard

Provides a responsive dashboard with an intuitive interface and light/dark mode support.

**Dashboard Capabilities:**
- Global leaderboard displaying the highest-ranked promotional clips.
- Episode-wise browsing and segment-level rankings.
- Tab-based navigation across multiple promotional options per episode.
- Detailed display of hooks, cliffhangers, and extraction reasoning.
- Direct JSON download functionality for processed screenplay outputs.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| AI Model | Google Gemini 3.5 Flash-Lite |
| AI Integration | Google Generative AI (`google-generativeai`) |
| Web Framework | Streamlit |
| Data Format | JSON |
| Input Format | Plain Text (`.txt`) |

## 📁 Repository Structure

```text
Kuku-promo-finder/
│
├── Episodes/               # Raw screenplay text files
│
├── extractor.py            # AI-powered extraction and validation pipeline
│
├── raw_outputs/           # Generated JSON promo extraction results
│
├── app.py                  # Interactive Streamlit dashboard
│
├── requirements.txt        # Project dependencies
│
└── README.md               # Project documentation
```

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Manideep1928/Kuku-promo-finder.git

cd Kuku-promo-finder
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure the Gemini API Key

Obtain a Gemini API key and configure it as an environment variable.

**Windows (PowerShell):**

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**macOS / Linux:**

```bash
export GEMINI_API_KEY="your_api_key_here"
```

## 🏃 Usage

### Step 1: Add Screenplays

Place the raw screenplay `.txt` files inside the `Episodes/` directory.

### Step 2: Run the Extraction Pipeline

```bash
python extractor.py
```

The pipeline analyzes the screenplays, extracts multiple promotional options, validates their duration, and saves the results as JSON files inside `raw_outputs1/`.

### Step 3: Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser, allowing you to explore promotional clips, compare rankings, browse episodes, and download JSON outputs.

## 📊 Output JSON Schema

Each processed screenplay generates a JSON file containing the episode information and its extracted promotional options.

### Example Output

```json
{
  "episode_number": "Episode 1",
  "promo_options": [
    {
      "option_number": 1,
      "segments": [
        {
          "start_timestamp": "00:02:15",
          "end_timestamp": "00:02:55"
        }
      ],
      "hook": "Juliana discovers her fiancé at the altar with another woman.",
      "cliffhanger": "Juliana gasps in devastation as the dramatic score cuts to black.",
      "reasoning": "Quickly establishes the core betrayal and emotional stakes for new viewers."
    }
  ]
}
```

### Output Fields

| Field | Description |
|---|---|
| `episode_number` | Identifies the processed episode. |
| `promo_options` | Contains multiple promotional clip options. |
| `option_number` | Unique identifier for each promotional option. |
| `segments` | Contains the extracted clip's timestamp boundaries. |
| `start_timestamp` | Beginning timestamp of the promotional clip. |
| `end_timestamp` | Ending timestamp of the promotional clip. |
| `hook` | Describes the primary attention-grabbing moment. |
| `cliffhanger` | Describes the suspenseful ending or unresolved moment. |
| `reasoning` | Explains why the segment was selected as promotional content. |

## 🎯 Project Objective

The primary objective of Kuku Microdrama Promo Extractor & Ranker is to automate the identification and evaluation of high-potential promotional moments from long-form microdrama screenplays.

By combining AI-driven screenplay analysis, programmatic duration validation, heuristic ranking, and an interactive dashboard, the system streamlines promotional clip discovery and helps prioritize engaging content for short-form video marketing.

---

**Developed with Python, Google Gemini, and Streamlit.**
