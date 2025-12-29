import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

st.set_page_config(page_title="ජ්‍යාමිතික හැඩතල මවන්නා", layout="wide")

st.title("📐 ජ්‍යාමිතික හැඩතල නිර්මාණය")
st.write("අගයන් ලබා දී අදාළ ජ්‍යාමිතික හැඩතල නිරීක්ෂණය කරන්න.")

tab1, tab2, tab3 = st.tabs(["වෘත්ත චාපය", "ඉලිප්සය", "සෘජුකෝණී ත්‍රිකෝණය"])

# --- 1. වෘත්ත චාපය (Circular Arc) ---
with tab1:
    st.header("වෘත්ත චාපයක් ඇඳීම")
    angle_deg = st.number_input("චාපයේ කෝණය (අංශක වලින්):", min_value=1, max_value=360, value=90)
    
    fig1, ax1 = plt.subplots()
    # චාපය නිර්මාණය
    arc = patches.Arc((0.5, 0.5), 0.8, 0.8, angle=0, theta1=0, theta2=angle_deg, color='blue', linewidth=2)
    ax1.add_patch(arc)
    ax1.set_aspect('equal')
    ax1.axis('off')
    st.pyplot(fig1)
    st.caption(f"අංශක {angle_deg} ක චාපය")

# --- 2. ඉලිප්සය (Ellipse) ---
with tab2:
    st.header("ඉලිප්සයක් ඇඳීම")
    col_a, col_b = st.columns(2)
    with col_a:
        radius_x = st.slider("තිරස් අරය (X radius):", 0.1, 1.0, 0.8)
    with col_b:
        radius_y = st.slider("සිරස් අරය (Y radius):", 0.1, 1.0, 0.4)
    
    fig2, ax2 = plt.subplots()
    ellipse = patches.Ellipse((0.5, 0.5), radius_x, radius_y, color='green', alpha=0.6)
    ax2.add_patch(ellipse)
    ax2.set_aspect('equal')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    st.pyplot(fig2)

# --- 3. සෘජුකෝණී ත්‍රිකෝණය (Right-Angled Triangle) ---
with tab3:
    st.header("සෘජුකෝණී ත්‍රිකෝණය")
    small_angle = st.number_input("සිරස් කෝණයේ අගය (අංශක):", min_value=1, max_value=89, value=30)
    
    # ත්‍රිකෝණයේ ඛණ්ඩාංක ගණනය කිරීම (Trigonometry පාවිච්චි කර)
    angle_rad = np.radians(small_angle)
    base = 1.0
    height = base * np.tan(angle_rad)
    
    fig3, ax3 = plt.subplots()
    points = np.array([[0, 0], [base, 0], [0, height]])
    triangle = patches.Polygon(points, closed=True, color='orange', alpha=0.7)
    ax3.add_patch(triangle)
    
    ax3.set_xlim(-0.1, 1.2)
    ax3.set_ylim(-0.1, height + 0.2)
    ax3.set_aspect('equal')
    st.pyplot(fig3)
    st.info(f"කෝණය: {small_angle}° | පාදය: {base} | උස: {height:.2f}")

st.divider()
st.caption("Math Visualization App - Created with Streamlit & Matplotlib")
