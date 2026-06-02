import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mg Implant Digital Twin",
    layout="wide"
)
st.markdown("""
<style>

/* Selected value */
div[data-baseweb="select"] span {
    font-size: 20px !important;
}

/* Dropdown container */
div[data-baseweb="select"] > div {
    min-height: 50px !important;
}

/* Dropdown options */
li {
    font-size: 20px !important;
    padding-top: 20px !important;
    padding-bottom: 20px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='font-size:55px; font-weight:bold;'>
🦴 Magnesium Implant Digital Twin
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<p style='font-size:22px;'>
Digital Twin Platform for Biodegradable Magnesium Implants
</p>
""", unsafe_allow_html=True)

# ADD HERE 👇

st.subheader("🧪 Select Coating Condition")

sample = st.selectbox(
    "",
    ["Pure Mg", "PMMA 5 Dips", "PMMA 10 Dips", "PMMA 15 Dips"]
)

# EXISTING CODE
if sample == "Pure Mg":
    hydrogen = "10 mL"
    contact = "61.2°"
    adhesion = "N/A"
elif sample == "PMMA 5 Dips":
    hydrogen = "0.1 mL"
    contact = "95.6°"
    adhesion = "5B"
elif sample == "PMMA 10 Dips":
    hydrogen = "0 mL"
    contact = "93.4°"
    adhesion = "5B"
elif sample == "PMMA 15 Dips":
    hydrogen = "0 mL"
    contact = "82.9°"
    adhesion = "4B"
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Hydrogen Evolution (mL)",
        hydrogen
    )
with col2:
    st.metric(
        "Contact Angle",
        contact
    )
with col3:
    st.metric(
        "Adhesion Strength",
        adhesion
    )
    
if sample == "Pure Mg":
     score = 30

elif sample == "PMMA 5 Dips":
     score = 85

elif sample == "PMMA 10 Dips":
     score = 100

elif sample == "PMMA 15 Dips":
     score = 90

if sample == "PMMA 10 Dips":
    recommendation = "✅ Recommended Coating"

elif sample == "PMMA 15 Dips":
    recommendation = "🟢 Excellent Corrosion Protection"

elif sample == "PMMA 5 Dips":
    recommendation = "🟡 Good Protection"

else:
    recommendation = "🔴 Not Recommended"
st.metric(
    "Overall Implant Performance Score",
    f"{score}/100",
    delta=f"{score-50}"
)

st.success(recommendation)
if sample == "PMMA 10 Dips":

    st.info("""
### 🤖 AI Insight

PMMA 10 Dips exhibited:

✔ Zero hydrogen evolution

✔ Excellent adhesion (5B)

✔ Most uniform coating morphology

✔ High hydrophobicity

✔ Optimal balance between corrosion protection and coating stability

**Recommended as the best coating condition for biodegradable AZ31B implants.**
""")

elif sample == "PMMA 15 Dips":

    st.info("""
### 🤖 AI Insight

PMMA 15 Dips completely suppressed hydrogen evolution.

However, FESEM and adhesion studies suggest possible interlayer stress and minor coating delamination due to excessive coating thickness.
""")

elif sample == "PMMA 5 Dips":

    st.info("""
### 🤖 AI Insight

PMMA 5 Dips significantly reduced hydrogen evolution and showed excellent hydrophobicity.

However, a small amount of hydrogen evolution (0.1 mL) was still observed, indicating incomplete corrosion suppression.
""")

else:

    st.info("""
### 🤖 AI Insight

Pure AZ31B showed rapid degradation and high hydrogen evolution (10 mL), making it unsuitable for long-term implant applications without surface modification.
""")
st.divider()

st.subheader("📈 Hydrogen Evolution Analysis")

corrosion_df = pd.read_csv(
    "data/corrosion_data.csv"
)
corrosion_df["Highlight"] = (
    corrosion_df["Sample"] == sample
)

fig = px.bar(
    corrosion_df,
    x="Sample",
    y="Hydrogen_Evolution_ml",
    text="Hydrogen_Evolution_ml",
    title="Hydrogen Evolution Comparison",
    color_discrete_sequence=["#00BFFF"],
    category_orders={
        "Sample": [
            "Pure Mg",
            "PMMA 5 Dips",
            "PMMA 10 Dips",
            "PMMA 15 Dips"
        ]
    }
)
fig.update_layout(showlegend=False)
st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

st.subheader("💧 Surface Wettability Analysis")
contact_df = pd.read_csv(
    "data/contact_angle.csv"
)
fig2 = px.bar(
    contact_df,
    x="Sample",
    y="Contact_Angle",
    text="Contact_Angle",
    title="Contact Angle Comparison",
    color_discrete_sequence=["#FFB84D"],

    category_orders={
        "Sample": [
            "Pure Mg",
            "PMMA 5 Dips",
            "PMMA 10 Dips",
            "PMMA 15 Dips"
        ]
    }
)
st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.subheader("🧲 Coating Adhesion Analysis")
adhesion_df = pd.read_csv(
    "data/adhesion_data.csv"
)
fig3 = px.bar(
    adhesion_df,
    x="Sample",
    y="Adhesion_Rating",
    text="Adhesion_Rating",
    title="Cross Hatch Adhesion Test",

    color_discrete_sequence=["#4CAF50"],

    category_orders={
        "Sample":[
            "PMMA 5 Dips",
            "PMMA 10 Dips",
            "PMMA 15 Dips"
        ]
    }
)
st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

st.subheader("🏆 Implant Performance Ranking")

score_df = pd.read_csv(
    "data/performance_score.csv"
)
score_df = score_df.sort_values(
    by="Score",
    ascending=False
).reset_index(drop=True)
score_df.index = score_df.index + 1

st.dataframe(
    score_df,
    use_container_width=True
)
st.divider()

st.subheader("🤖 Digital Twin Recommendation")

best_sample = score_df.iloc[0]["Sample"]
best_score = score_df.iloc[0]["Score"]

st.success(
    f"""
    Recommended Implant Coating: {best_sample}

    Performance Score: {best_score}/100

    Based on hydrogen evolution, wettability, and adhesion performance,
    this coating condition demonstrates the best overall implant suitability.
    """
)
st.divider()
st.subheader("🔬 FESEM Morphology Explorer")

# Select correct image
if sample == "Pure Mg":
    image_path = "images/FESEM/Pure Mg.png"

elif sample == "PMMA 5 Dips":
    image_path = "images/FESEM/pmma_5_dips_fesem.png"

elif sample == "PMMA 10 Dips":
    image_path = "images/FESEM/pmma_10_dips_fesem.png"

elif sample == "PMMA 15 Dips":
    image_path = "images/FESEM/pmma_15_dips_fesem.png"

else:
    image_path = None

# Display interpretation

col1, col2 = st.columns([2, 3])

with col1:

    st.image(
        image_path,
        caption=f"FESEM Surface Morphology - {sample}",
        width=500
    )

with col2:

    st.markdown("### 🔬 FESEM Observation")

    if sample == "Pure Mg":

        st.markdown("""
- Rough and heterogeneous surface morphology observed

- Presence of corrosion products and surface irregularities

- Higher surface reactivity due to absence of protective coating

- Increased susceptibility to localized corrosion and degradation

- Indicates poor corrosion resistance compared to PMMA-coated samples
""")

    elif sample == "PMMA 5 Dips":

        st.markdown("""
- Partial PMMA surface coverage observed

- Minor agglomerates visible

- Improved protection compared to bare Mg

- Some exposed regions may still allow corrosion initiation
""")

    elif sample == "PMMA 10 Dips":

        st.markdown("""
- Most homogeneous coating

- Smooth morphology

- Minimal defects

- Uniform PMMA coverage across the substrate

- Optimum coating condition for corrosion protection
""")

    elif sample == "PMMA 15 Dips":

        st.markdown("""
- Thick coating layer

- Crack-like features observed

- Possible internal stress development

- Excessive coating thickness may reduce coating stability
""")
        
st.divider()

st.subheader("🧪 FTIR Spectrum Explorer")
ftir_image = "images/FTIR/ftir_spectrum.png"
col1, col2 = st.columns([2, 3])
with col1:

    st.image(
        ftir_image,
        caption="FTIR Spectrum of PDA-Assisted PMMA Coating",
        width=500
    )
with col2:
    st.markdown("""
<div style='font-size:18px; line-height:0.8;'>

<h3>🧪 FTIR Interpretation</h3>

<b>Major Peaks Identified : </b>

<ul>
<li><b>2981 cm⁻¹</b> → C–H stretching vibration of PMMA</li>
<li><b>1595 cm⁻¹</b> → Aromatic ring vibration associated with PDA layer</li>
<li><b>1375 cm⁻¹</b> → CH₃ bending vibration of PMMA</li>
<li><b>1242 cm⁻¹</b> → C–O–C ester stretching vibration</li>
</ul>

<b>Key Findings : </b>

<ul>
<li>Characteristic PMMA functional groups are clearly observed.</li>
<li>PDA-assisted coating successfully deposited on magnesium substrate.</li>
<li>Presence of ester and methyl groups confirms PMMA coating integrity.</li>
<li>FTIR results support successful surface modification of AZ31B magnesium.</li>
</ul>

</div>
""", unsafe_allow_html=True)
st.markdown("### 📋 FTIR Peak Assignment")

ftir_table = pd.DataFrame({
    "Peak (cm⁻¹)": ["2981", "1595", "1375", "1242"],
    "Assignment": [
        "C-H Stretching",
        "Aromatic Ring Vibration (PDA)",
        "CH₃ Bending",
        "C-O-C Ester Stretching"
    ],
    "Significance": [
        "PMMA Backbone",
        "PDA Presence",
        "PMMA Functional Group",
        "Ester Bond Confirmation"
    ]
})


st.dataframe(
    ftir_table,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.divider()

st.subheader("⚛️ XRD Phase Analysis Explorer")
col1, col2 = st.columns([1, 2])
with col1:
    st.image(
        "images/XRD/xrd_analysis.png",
        caption="XRD Patterns of Pure and PMMA-Coated AZ31B Magnesium",
        width=400
    )
with col2:
 st.markdown("""
<h3>⚛️ XRD Interpretation</h3>

<div style='font-size:20px; line-height:1.8;'>

• Dominant α-Mg peaks observed around 32°–37°<br><br>

• Characteristic Mg₁₇Al₁₂ phase detected near 63° and 72°<br><br>

• No additional crystalline impurity peaks detected after coating<br><br>

• PMMA coating does not alter the bulk crystal structure of AZ31B magnesium<br><br>

• Similar diffraction patterns across all dip cycles indicate structural stability<br><br>

• Surface modification occurs without affecting substrate crystallinity

</div>
""", unsafe_allow_html=True)
st.markdown("### 📋 Phase Identification")

xrd_table = pd.DataFrame({
    "2θ Position (°)": ["32", "34", "36", "63", "72"],
    "Phase": [
        "α-Mg",
        "α-Mg",
        "α-Mg",
        "Mg₁₇Al₁₂",
        "Mg₁₇Al₁₂"
    ],
    "Significance": [
        "Magnesium Matrix",
        "Magnesium Matrix",
        "Magnesium Matrix",
        "Intermetallic Phase",
        "Intermetallic Phase"
    ]
})

st.dataframe(
    xrd_table,
    use_container_width=True,
    hide_index=True
)
st.success("""
### 🔬 XRD Conclusion

The XRD analysis confirms that PDA-assisted PMMA coating does not
alter the crystalline structure of AZ31B magnesium.

The characteristic α-Mg and Mg₁₇Al₁₂ phases remain preserved after
5, 10, and 15 dip cycles, indicating that the coating process
modifies only the surface while maintaining substrate integrity.
""")
st.info("""
### 📌 Characterization Summary

✔ FESEM confirms successful PMMA coating formation

✔ FTIR confirms PMMA and PDA functional groups

✔ XRD confirms substrate crystallinity remains unchanged

✔ PMMA 10 Dips exhibits the most homogeneous and stable coating

✔ Surface modification improves implant suitability without altering bulk structure
""")

st.divider()
st.subheader("🤖 AI Corrosion Prediction")
if sample == "Pure Mg":
    prediction = "Very High Corrosion Risk"
    color = "error"

elif sample == "PMMA 5 Dips":
    prediction = "Moderate Corrosion Risk"
    color = "warning"

elif sample == "PMMA 10 Dips":
    prediction = "Low Corrosion Risk"
    color = "success"

elif sample == "PMMA 15 Dips":
    prediction = "Low Corrosion Risk"
    color = "info"

if color == "error":
    st.error(f"Predicted Corrosion Behaviour: {prediction}")

elif color == "warning":
    st.warning(f"Predicted Corrosion Behaviour: {prediction}")

elif color == "success":
    st.success(f"Predicted Corrosion Behaviour: {prediction}")

else:
    st.info(f"Predicted Corrosion Behaviour: {prediction}")

st.subheader("🧠 AI Materials Insight")
if sample == "Pure Mg":

    st.error("""
    Pure magnesium exhibits severe corrosion susceptibility due to rapid
    hydrogen evolution and absence of a protective PMMA coating.

    FESEM analysis reveals heterogeneous morphology and corrosion products.

    This condition demonstrates the lowest implant suitability among all samples.
    """)

elif sample == "PMMA 5 Dips":

    st.warning("""
    PMMA 5 Dips significantly improves corrosion resistance compared to bare magnesium.

    Improved wettability and strong adhesion are observed.

    However, residual hydrogen evolution indicates incomplete corrosion suppression.
    """)

elif sample == "PMMA 10 Dips":

    st.success("""
    PMMA 10 Dips demonstrates the optimal balance between corrosion resistance,
    surface wettability, coating adhesion and structural integrity.

    Zero hydrogen evolution together with homogeneous FESEM morphology
    suggests excellent implant performance potential.
    """)

elif sample == "PMMA 15 Dips":

    st.info("""
    PMMA 15 Dips provides excellent corrosion protection.

    However, FESEM observations indicate crack-like features and possible
    internal coating stress due to excessive coating thickness.

    Performance remains high but slightly below PMMA 10 Dips.
    """)

st.divider()
st.subheader("📡 Implant Suitability Radar")
st.markdown(f"### Selected Sample: {sample}")
if sample == "Pure Mg":

    radar_values = [2, 3, 1, 2, 2]

elif sample == "PMMA 5 Dips":

    radar_values = [8, 10, 10, 8, 8]

elif sample == "PMMA 10 Dips":

    radar_values = [10, 9, 10, 10, 10]

elif sample == "PMMA 15 Dips":

    radar_values = [10, 7, 8, 7, 9]

categories = [
    "Corrosion Resistance",
    "Hydrophobicity",
    "Adhesion",
    "Surface Quality",
    "Overall Stability"
]
fig = go.Figure()

fig.add_trace(
    go.Scatterpolar(
        r=radar_values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(0,191,255,0.35)',
        line=dict(width=3),
        name=sample
    )
)

fig.update_layout(margin=dict(l=50, r=50, t=50, b=50),
        polar=dict(
        bgcolor="#0E1117",
        radialaxis=dict(
            visible=True,
            range=[0, 10],
            gridcolor="gray",
            linecolor="gray"
     ),
        angularaxis=dict(
            gridcolor="gray",
            linecolor="gray"
        )
    ),

    paper_bgcolor="#0E1117",
    font=dict(color="white"),

    showlegend=False,
    height=500,
    width=550

)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.plotly_chart(fig)
st.divider()
st.subheader("📄 Digital Twin Summary Report")
st.markdown(f"**Selected Sample:** {sample}")
st.markdown("---")
report_text = f"""
MAGNESIUM IMPLANT DIGITAL TWIN REPORT

Selected Sample: {sample}

Hydrogen Evolution: {hydrogen}
Contact Angle: {contact}
Adhesion Strength: {adhesion}

Predicted Corrosion Behaviour:
{prediction}

Overall Recommendation:
{sample}

Performance Score:
{score}/100

Corrosion Behaviour:
{prediction}

Generated using Magnesium Implant Digital Twin Platform.
"""
st.subheader("📊 Overall Implant Status")
if sample == "Pure Mg":
    st.error("""### Recommendation

Not suitable for long-term biodegradable implant application due to rapid corrosion, high hydrogen evolution, poor surface stability, and absence of a protective coating.
""")

elif sample == "PMMA 5 Dips":
    st.info("""### Recommendation

Suitable for short-term corrosion protection and demonstrates improved wettability and adhesion compared to bare magnesium. However, measurable hydrogen evolution is still observed, indicating incomplete corrosion suppression.
""")

elif sample == "PMMA 10 Dips":
    st.success("""### Recommendation

Highly recommended for biodegradable implant applications. This coating condition provides the best balance of corrosion resistance, surface wettability, coating adhesion, and structural integrity, with negligible hydrogen evolution and uniform surface morphology.
""")

elif sample == "PMMA 15 Dips":
    st.warning("""### Recommendation

Provides excellent corrosion protection and effectively suppresses hydrogen evolution. However, FESEM analysis indicates increased coating thickness and crack-like features that may reduce long-term coating stability compared to the optimized 10-dip condition.
""")
if sample == "PMMA 10 Dips":
    st.balloons()
st.download_button(
    label="📥 Download Implant Report",
    data=report_text,
    file_name=f"{sample}_report.txt",
    mime="text/plain"
)
st.info(
    "Generate a personalized implant assessment report based on corrosion, wettability, adhesion and characterization results."
)
st.caption(
    "Digital Twin developed from experimental corrosion, wettability, adhesion, FESEM, FTIR and XRD characterization data of PDA-assisted PMMA coated AZ31B magnesium implants."
)