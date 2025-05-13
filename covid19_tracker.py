# COVID-19 Global Data Tracker
# This script analyzes global COVID-19 trends, including cases, deaths, recoveries, and vaccinations.

import pandas as pd  # type: ignore # For data manipulation
import matplotlib.pyplot as plt  # type: ignore # For visualizations
import seaborn as sns  # type: ignore # For enhanced visualizations

# Step 1: Data Collection
# Download the dataset (owid-covid-data.csv) and save it in the 'data' folder.

# Step 2: Data Loading & Exploration
def load_and_explore_data(filepath):
    """
    Load the COVID-19 dataset and explore its structure.
    """
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully!")
        print("Columns in the dataset:", df.columns)
        print("Preview of the data:")
        print(df.head())
        print("Missing values in each column:")
        print(df.isnull().sum())
        return df
    except FileNotFoundError:
        print("The file was not found. Please check the filepath.")
        return None

# Step 3: Data Cleaning
def clean_data(df):
    """
    Clean the dataset by filtering countries, handling missing values, and converting date columns.
    """
    # Filter for specific countries (e.g., Kenya, USA, India)
    countries_of_interest = ['Kenya', 'United States', 'India']
    df = df[df['location'].isin(countries_of_interest)]

    # Drop rows with missing critical values
    df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])

    # Convert the date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Fill missing numeric values
    df = df.fillna(method='ffill')

    print("Data cleaned successfully!")
    return df

# Step 4: Exploratory Data Analysis (EDA)
def perform_eda(df):
    """
    Perform exploratory data analysis and generate visualizations.
    """
    # Plot total cases over time for selected countries
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_cases'], label=country)
    plt.title('Total COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.legend()
    plt.show()

    # Plot total deaths over time for selected countries
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_deaths'], label=country)
    plt.title('Total COVID-19 Deaths Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.legend()
    plt.show()

    # Compare daily new cases between countries
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['new_cases'], label=country)
    plt.title('Daily New COVID-19 Cases')
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.legend()
    plt.show()

# Step 5: Visualizing Vaccination Progress
def visualize_vaccination_progress(df):
    """
    Analyze and visualize vaccination rollouts.
    """
    # Plot cumulative vaccinations over time for selected countries
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
    plt.title('Cumulative Vaccinations Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.legend()
    plt.show()

    # Compare percentage of vaccinated population
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['people_vaccinated_per_hundred'], label=country)
    plt.title('Percentage of Vaccinated Population Over Time')
    plt.xlabel('Date')
    plt.ylabel('People Vaccinated per Hundred')
    plt.legend()
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Filepath to the dataset
    filepath = 'data/owid-covid-data.csv'

    # Step 2: Load and explore the data
    covid_data = load_and_explore_data(filepath)

    if covid_data is not None:
        # Step 3: Clean the data
        cleaned_data = clean_data(covid_data)

        # Step 4: Perform EDA
        perform_eda(cleaned_data)

        # Step 5: Visualize vaccination progress
        visualize_vaccination_progress(cleaned_data)