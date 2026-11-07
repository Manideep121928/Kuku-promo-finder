import os
import json
import time
import google.generativeai as genai

# 1. Paste your API key here
genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel(
    'gemini-3.5-flash-lite',
    generation_config={"response_mime_type": "application/json"}
)

PROMPT = """
You are an expert video editor for microdramas. Read the following screenplay and identify promotional clip options (you can provide one or multiple distinct 20 to 60-second promo clips if the episode has multiple strong highlights).
STRICT REQUIREMENT: Each promo option must be a continuous window whose total duration from its start timestamp to its end timestamp is between 20 seconds and 60 seconds.

For each promo option, provide:
1. Opens on a strong hook in the first 3 seconds (shocking line, reveal, slap).
2. Ends on a cliffhanger.
3. Makes sense on its own to a new viewer.

Return a JSON object containing an array of promos or a structure with multiple options matching this exact format:
{
  "episode_number": "Episode X",
  "promo_options": [
    {
      "option_number": 1,
      "segments": [{"start_timestamp": "00:00.00", "end_timestamp": "00:00.00"}],
      "hook": "Describe the 3-second hook",
      "cliffhanger": "Describe the unresolved ending",
      "reasoning": "One line on why this option works standalone"
    }
  ]
}

Screenplay:
"""

input_dir = "Episodes"
output_dir = "raw_outputs"
os.makedirs(output_dir, exist_ok=True)

for filename in sorted(os.listdir(input_dir)):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_dir, filename)
        out_file = os.path.join(output_dir, f"{filename.split('.')[0]}_promo.json")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            print(f"Processing multiple promos for {filename}...")
            response = model.generate_content(PROMPT + content)
            promo_data = json.loads(response.text)
            
            with open(out_file, 'w', encoding='utf-8') as out_f:
                json.dump(promo_data, out_f, indent=4)
            print(f"✅ Saved multiple promo options to {out_file}")
            
            time.sleep(12)
            
        except Exception as e:
            print(f"❌ Error on {filename}: {e}")
            time.sleep(12)