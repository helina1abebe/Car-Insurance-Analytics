import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_claim_distribution_by_age(df):
    """
    Plot the distribution of claims across age groups.
    """
    if 'Age' in df.columns:
        sns.histplot(df['Age'], bins=20, kde=True)
        plt.title("Distribution of Claims by Age")
        plt.xlabel("Age")
        plt.ylabel("Number of Claims")
        plt.show()

def plot_vehicle_type_distribution(df):
    """
    Plot the distribution of claims by vehicle type.
    """
    if 'VehicleType' in df.columns:
        vehicle_counts = df['VehicleType'].value_counts()
        vehicle_counts.plot(kind='bar', color='skyblue')
        plt.title("Distribution of Claims by Vehicle Type")
        plt.xlabel("Vehicle Type")
        plt.ylabel("Number of Claims")
        plt.show()

def plot_claims_over_time(df):
    """
    Plot the number of claims over time.
    """
    if 'ClaimDate' in df.columns:
        df['YearMonth'] = df['ClaimDate'].dt.to_period('M')
        claim_counts = df.groupby('YearMonth').size()
        claim_counts.plot(kind='line', marker='o', figsize=(10, 6))
        plt.title("Number of Claims Over Time")
        plt.xlabel("Year-Month")
        plt.ylabel("Number of Claims")
        plt.show()

if __name__ == "__main__":
    # Example usage
    cleaned_data_path = "data/processed/cleaned_insurance_claims.csv"

    data = pd.read_csv(cleaned_data_path, parse_dates=['ClaimDate'])
    plot_claim_distribution_by_age(data)
    plot_vehicle_type_distribution(data)
    plot_claims_over_time(data)
