import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, chi2_contingency, f_oneway
import seaborn as sns
import matplotlib.pyplot as plt

def compute_claim_frequency(df, group_col):
    """
    Compute claim frequency for different groups as proportion of policies with claims.
    """
    return df.groupby(group_col).apply(lambda x: (x['TotalClaims'] > 0).mean())

def compute_claim_severity(df, group_col):
    """
    Compute claim severity for different groups as average number of claims.
    """
    return df.groupby(group_col)['TotalClaims'].mean()

def compute_margin(df):
    """
    Compute margin as (TotalPremium - TotalClaims) and add it as a new column.
    """
    df = df.copy()
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df

def perform_t_test(group_a, group_b, metric_name):
    """
    Perform independent two-sample t-test between two groups.
    Warn if sample sizes are small (<30).
    """
    if len(group_a) < 30 or len(group_b) < 30:
        print(f"Warning: Sample size for t-test groups less than 30. Results may be unreliable.")
    stat, p_value = ttest_ind(group_a, group_b, equal_var=False)
    print(f"T-test for {metric_name}: t-stat = {stat:.4f}, p-value = {p_value:.4f}")
    return p_value
def perform_t_test_by_group(df, group_col, metric_col, group_a, group_b):
    """
    Perform a t-test between two groups based on a specified column.
    
    Parameters:
        df (pd.DataFrame): The dataset.
        group_col (str): The column name for grouping.
        metric_col (str): The column name for the metric being compared.
        group_a (str): The first group to compare.
        group_b (str): The second group to compare.
    
    Returns:
        float: The p-value from the t-test.
    """
    data_a = df[df[group_col] == group_a][metric_col].dropna()
    data_b = df[df[group_col] == group_b][metric_col].dropna()
    
    if len(data_a) < 30 or len(data_b) < 30:
        print(f"Warning: Sample size for one or both groups is less than 30. Results may be unreliable.")
    
    stat, p_value = ttest_ind(data_a, data_b, equal_var=False)
    print(f"T-test between {group_a} and {group_b} for {metric_col}:")
    print(f"t-stat = {stat:.4f}, p-value = {p_value:.4f}")
    
    return p_value

def perform_anova(*groups, metric_name="Metric"):
    """
    Perform one-way ANOVA test for multiple groups.
    Warn if any group has fewer than 30 samples.
    """
    if any(len(g) < 30 for g in groups):
        print("Warning: At least one group has fewer than 30 samples. ANOVA results may be unreliable.")
    stat, p_value = f_oneway(*groups)
    print(f"ANOVA for {metric_name}: F-stat = {stat:.4f}, p-value = {p_value:.4f}")
    return p_value

def perform_chi_squared_test(df, group_col, metric_col):
    """
    Perform a chi-squared test of independence between two categorical variables.
    """
    contingency_table = pd.crosstab(df[group_col], df[metric_col])
    chi2, p_value, _, _ = chi2_contingency(contingency_table)
    print(f"Chi-squared test between {group_col} and {metric_col}: chi2 = {chi2:.4f}, p-value = {p_value:.4f}")
    return p_value

def visualize_risk_by_group(df, group_col, metric_col, metric_name):
    """
    Visualize the average metric by group with standard deviation error bars.
    """
    sns.barplot(x=group_col, y=metric_col, data=df, estimator=np.mean, errorbar='sd')
    plt.title(f"{metric_name} by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel(metric_name)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
