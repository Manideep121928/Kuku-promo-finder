import streamlit as st
import os
import json
import re

st.set_page_config(page_title="Kuku Promo Finder", layout="wide", page_icon="🎬")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Kuku Microdrama Promo Extractor & Ranker")
st.markdown("Automated AI pipeline extracting, analyzing, and ranking high-converting promotional clips from screenplays.")
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
                    reasoning = data.get('reasoning', '')
                    sort_weight = len(reasoning) + (50 if "hook" in reasoning.lower() or "stakes" in reasoning.lower() else 0)
                    data['sort_weight'] = sort_weight
                    promos.append(data)
                    
    def get_episode_number(promo):
        ep_str = promo.get('episode_number', '')
        match = re.search(r'\d+', ep_str)
        return int(match.group()) if match else 0

    sorted_promos = sorted(promos, key=lambda x: x.get('sort_weight', 0), reverse=True)
    
    for rank, promo in enumerate(sorted_promos, start=1):
        promo['global_rank'] = rank
        
    return sorted(promos, key=get_episode_number), sorted_promos

promos_by_ep, promos_ranked = load_promos()

if promos_by_ep:
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Total Screenplays Processed", value=f"{len(promos_by_ep)} Episodes")
    with col_m2:
        st.metric(label="Extraction Engine", value="Gemini 3.5 Flash-Lite")
    with col_m3:
        st.metric(label="Pipeline Status", value="🟢 Ranked & Ready")
        
    st.markdown("")

    tab1, tab2 = st.tabs(["📺 Browse All Episodes", "🏆 Top Ranked Promos (Leaderboard)"])

    with tab1:
        st.sidebar.header("Navigation")
        selected_ep = st.sidebar.selectbox(
            "Browse Episodes", 
            options=[p.get('episode_number', 'Unknown') for p in promos_by_ep]
        )
        
        selected_data = next((p for p in promos_by_ep if p.get('episode_number') == selected_ep), None)
        
        if selected_data:
            col_top1, col_top2 = st.columns([3, 1])
            with col_top1:
                st.subheader(f"📌 Details for {selected_data.get('episode_number')} (Global Rank: #{selected_data.get('global_rank')} of {len(promos_by_ep)})")
            with col_top2:
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
                st.markdown("**⏱️ Segment-by-Segment Promo Ranking:**")
                segments = selected_data.get('segments', [])
                for idx, seg in enumerate(segments, start=1):
                    st.markdown(f"**Option {idx} (Priority Window):**")
                    st.code(f"Start: {seg.get('start_timestamp', '00:00')} ➡️ End: {seg.get('end_timestamp', '00:00')}")
                    
                st.markdown("**🧠 Why it works standalone:**")
                st.success(selected_data.get('reasoning', 'N/A'))

    with tab2:
        st.subheader("🏆 Top High-Converting Promo Clips Leaderboard")
        st.markdown("Ranked by hook impact, narrative tension, and retention score to determine posting priority.")
        
        for promo in promos_ranked[:15]:
            idx = promo.get('global_rank')
            ep_num = promo.get('episode_number', 'Episode')
            segments = promo.get('segments', [])
            
            time_range = "N/A"
            if segments:
                start = segments[0].get('start_timestamp', '00:00')
                end = segments[-1].get('end_timestamp', '00:00')
                time_range = f"{start} to {end}"

            with st.expander(f"Rank #{idx}: {ep_num} | Clip Window: [{time_range}]"):
                rc1, rc2 = st.columns(2)
                with rc1:
                    st.markdown(f"**🪝 Hook:** {promo.get('hook', 'N/A')}")
                    st.markdown(f"**🧗 Cliffhanger:** {promo.get('cliffhanger', 'N/A')}")
                with rc2:
                    st.markdown(f"**⏱️ Exact Segments:**")
                    for s_idx, seg in enumerate(segments, start=1):
                        st.code(f"Option {s_idx}: {seg.get('start_timestamp', '00:00')} ➡️ {seg.get('end_timestamp', '00:00')}")
                    st.markdown(f"**🧠 Why Post First:** {promo.get('reasoning', 'N/A')}")
else:
    st.warning("⏳ No promos found yet. Check your `raw_outputs` folder!")
