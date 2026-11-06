import streamlit as st
import os
import json
import re

st.set_page_config(page_title="Kuku Promo Finder", layout="wide", page_icon="🎬")

# Custom CSS for a sleek professional dashboard feel
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Kuku Microdrama Promo Extractor")
st.markdown("Automated AI pipeline extracting high-converting hooks, timestamps, and cliffhangers from screenplays.")
st.divider()

output_dir = "raw_outputs" 

@st.cache_data
def load_promos():
    promos = []
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            if file.endswith(".json"):
                with open(os.path.join(output_dir, file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    promos.append(data)
                    
    def get_episode_number(promo):
        ep_str = promo.get('episode_number', '')
        match = re.search(r'\d+', ep_str)
        return int(match.group()) if match else 0

    return sorted(promos, key=get_episode_number)

promos = load_promos()

if promos:
    # Top metrics summary
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Total Screenplays Processed", value=f"{len(promos)} Episodes")
    with col_m2:
        st.metric(label="Extraction Engine", value="Gemini 3.5 Flash-Lite")
    with col_m3:
        st.metric(label="Pipeline Status", value="🟢 Ready for Review")
        
    st.markdown("")

    st.sidebar.header("Navigation")
    st.sidebar.markdown(f"📁 **Dataset:** `{len(promos)}/50 Loaded`")
    
    selected_ep = st.sidebar.selectbox(
        "Browse Episodes", 
        options=[p.get('episode_number', 'Unknown') for p in promos]
    )
    
    selected_data = next((p for p in promos if p.get('episode_number') == selected_ep), None)
    
    if selected_data:
        col_top1, col_top2 = st.columns([3, 1])
        with col_top1:
            st.subheader(f"📌 Details for {selected_data.get('episode_number')}")
        with col_top2:
            # Direct JSON download button for evaluation
            json_str = json.dumps(selected_data, indent=4)
            st.download_button(
                label="📥 Download JSON",
                data=json_str,
                file_name=f"{selected_data.get('episode_number','ep').lower().replace(' ', '_')}_promo.json",
                mime="application/json"
            )
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🪝 The Hook (First 3 seconds):**")
            st.info(selected_data.get('hook', 'N/A'))
            
            st.markdown("**🧗 The Cliffhanger:**")
            st.warning(selected_data.get('cliffhanger', 'N/A'))
        
        with col2:
            st.markdown("**⏱️ Suggested Timestamps:**")
            segments = selected_data.get('segments', [])
            for seg in segments:
                st.code(f"Start: {seg.get('start_timestamp', '00:00')} ➡️ End: {seg.get('end_timestamp', '00:00')}")
                
            st.markdown("**🧠 Why it works standalone:**")
            st.success(selected_data.get('reasoning', 'N/A'))
else:
    st.warning("⏳ No promos found yet. Make sure your JSON files are inside the `raw_outputs` folder!")
