import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Recursive Signal Recomposer", layout="wide")
st.title("🔄 Recursive Signal Recomposer")

st.markdown("""
This simulation attempts to reconstruct symbolic coherence from fragmented input sequences.
Adjust symbolic noise and loop depth to explore self-repair in identity attractors.
""")

# Sidebar
st.sidebar.header("Controls")
seq_length = st.sidebar.slider("Fragment Length", 5, 50, 20)
noise_level = st.sidebar.slider("Symbolic Noise", 0.0, 1.0, 0.3)
loop_depth = st.sidebar.slider("Recursion Depth", 1, 10, 5)

# Generate input signal
np.random.seed(42)
base_signal = np.sin(np.linspace(0, 3*np.pi, seq_length))
noise = np.random.normal(0, noise_level, seq_length)
fragment = base_signal + noise

# Recursive reconstruction
reconstructed = fragment.copy()
for i in range(loop_depth):
    reconstructed = 0.8 * reconstructed + 0.2 * base_signal

df = pd.DataFrame({
    "Token": np.arange(seq_length),
    "Fragmented Input": fragment,
    "Reconstructed Signal": reconstructed
})

fig = px.line(df, x="Token", y=["Fragmented Input", "Reconstructed Signal"],
              title="Recursive Signal Recomposition",
              labels={"value": "Symbolic Amplitude", "Token": "Sequence Position"})

st.plotly_chart(fig, use_container_width=True)
