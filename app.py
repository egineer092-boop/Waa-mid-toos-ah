import streamlit as st
import random
import time

st.set_page_config(
    page_title="Nexus Engine",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Nexus Live Engine")
st.caption("Nidaamka casriga ah ee xisaabinta iyo socodka tooska ah.")

if "balance" not in st.session_state:
    st.session_state.balance = 120.50
if "signals" not in st.session_state:
    st.session_state.signals = 0

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Wadarta Guud (USD)", value=f"${st.session_state.balance:.2f}")

with col2:
    st.metric(label="Wareegyada La Baaray", value=st.session_state.signals)

st.divider()

col_start, col_reset = st.columns(2)

with col_start:
    run_engine = st.button("🚀 Bilow Mashiinka", use_container_width=True)

with col_reset:
    reset_engine = st.button("🔄 Dib u Bilaaw", use_container_width=True)

if reset_engine:
    st.session_state.balance = 120.50
    st.session_state.signals = 0
    st.rerun()

if run_engine or st.session_state.get("is_running", False):
    st.session_state.is_running = True
    log_container = st.empty()
    
    for _ in range(5):
        st.session_state.signals += 1
        gain = round(random.uniform(2.5, 15.0), 2)
        st.session_state.balance += gain
        
        with log_container.container():
            st.info(f"Wareegga {st.session_state.signals}: Waxaa la helay +${gain} (Nadiif ah)")
        
        time.sleep(1)
    
    st.success("Wareegii waa la dhameeyay si nabad ah!")
    st.session_state.is_running = False
    st.rerun()
