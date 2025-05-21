import streamlit as st
from utils import load_data, create_boxplot, get_top_regions

# Set page configuration for a professional look
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

# Title and description
st.title("🌞 Solar Potential Dashboard")
st.markdown("Compare solar potential across Benin, Sierra Leone, and Togo with interactive visualizations.")

# Load data
with st.spinner("Loading data..."):
    try:
        data = load_data()
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()

# Sidebar for user inputs
st.sidebar.header("Visualization Settings")
countries = st.sidebar.multiselect(
    "Select Countries",
    options=['Benin', 'Sierra Leone', 'Togo'],
    default=['Benin', 'Sierra Leone', 'Togo']
)
metric = st.sidebar.selectbox(
    "Select Metric",
    options=['GHI', 'DNI', 'DHI'],
    index=0
)

# Main content
if not countries:
    st.warning("Please select at least one country to visualize.")
else:
    # Boxplot section
    st.subheader(f"Boxplot of {metric} by Country")
    fig = create_boxplot(data, metric, countries)
    st.pyplot(fig)

    # Top regions table
    st.subheader(f"Top Countries by Average {metric}")
    top_regions = get_top_regions(data, metric)
    st.dataframe(top_regions, use_container_width=True)

    # Data info
    filtered_data = data[data['Country'].isin(countries)]
    st.write(f"Showing data for {len(filtered_data)} records across {len(countries)} countries.")