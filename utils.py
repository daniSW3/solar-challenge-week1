import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    """Load and combine the cleaned datasets from Benin, Sierra Leone, and Togo."""
    try:
        benin = pd.read_csv('datas/benin-malanville.csv')
        sierra_leone = pd.read_csv('datas/sierraleone-bumbuna.csv')
        togo = pd.read_csv('datas/togo-dapaong_qc.csv')

        # Add Country column
        benin['Country'] = 'Benin'
        sierra_leone['Country'] = 'Sierra Leone'
        togo['Country'] = 'Togo'

        # Combine datasets
        data = pd.concat([benin, sierra_leone, togo], ignore_index=True)
        return data
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error loading data: {e}. Ensure CSV files are in the 'data/' folder.")

def create_boxplot(data, metric, countries):
    """Generate a boxplot for the selected metric and countries."""
    fig, ax = plt.subplots(figsize=(8, 5))
    filtered_data = data[data['Country'].isin(countries)]
    sns.boxplot(x='Country', y=metric, data=filtered_data, palette='Set2', ax=ax)
    plt.title(f'{metric} by Country')
    plt.xlabel('Country')
    plt.ylabel(f'{metric} (W/m²)')
    plt.tight_layout()
    return fig

def get_top_regions(data, metric, n=3):
    """Return a table of top regions (countries) ranked by the selected metric."""
    summary = data.groupby('Country')[metric].agg(['mean']).round(2)
    summary.columns = [f'Average_{metric}']
    summary = summary.sort_values(by=f'Average_{metric}', ascending=False).head(n)
    return summary