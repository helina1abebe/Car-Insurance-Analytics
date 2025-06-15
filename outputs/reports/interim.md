# 📝 Interim Report: Claim Frequency and Severity Analysis

## Dataset Overview
- **Analysis period:** 18 months  
- **Date variable used:** `TransactionMonth`  
- **Target variables:** `TotalClaims`, Claim frequency, and severity  

---

## Key Findings So Far
- 📊 **Monthly claim frequency trends**: [Insert brief insight after running analysis]  
- 📈 **Average claim severity**: Varies month to month with peaks around [Insert observations]  
- 🔎 Further analysis needed for **seasonality** and factors affecting claim amounts.  

---

## Interim Report Summary

### Portfolio Analysis Overview
This analysis provides insights into key metrics and trends for the insurance portfolio, focusing on:
- **Loss ratios**  
- **Outlier identification**  
- **Vehicle claim patterns**  

### Key Metrics
#### Overall Loss Ratio
- The portfolio's overall **loss ratio** stands at **100.24%**, indicating a break-even performance where total claims nearly equal total premiums.  

#### Loss Ratio Segmentation
- **By Vehicle Type**:  
  - Highest: Heavy Commercial (161.24%)  
  - Lowest: Light Commercial (23.21%) and Bus (0%).  

- **By Gender**:  
  - Highest: Not Specified (101.50%)  
  - Lowest: Unknown (61.45%).  

---

### Outlier and Distribution Analysis
- **Outliers**:  
  - `TotalClaims`: **2,788** data points flagged as outliers.  
  - `CustomValueEstimate`: **217,868** outliers detected, suggesting potential data issues or significant skew in asset valuation.  

- **Distributions**:  
  - Claims data is heavily **skewed**, with a large portion of policies showing **zero claims**.  
  - `CustomValueEstimate` demonstrates high variability, potentially affecting **loss severity calculations**.  

---

### Temporal Trends
- **Claim Frequency and Severity**:  
  - Frequency and severity metrics show clear **temporal trends**, suggesting possible seasonality or external market influences over the 18-month period.  
  - These patterns can be leveraged for **improved forecasting** and **pricing strategies**.  

---

### Vehicle Make/Model Claim Analysis
- **Highest Average Claim Amounts**:  
  - Top vehicles by make/model (e.g., Toyota Land Cruiser, Hyundai H-1) have average claim amounts exceeding **$4,000**, often linked to high-value vehicles.  

- **Lowest Average Claim Amounts**:  
  - Certain models (e.g., Volkswagen Transporter variants, Audi A5) report **zero claims**, likely due to specific underwriting strategies or low exposure.  

---

### Visualizations
Three key visualizations saved in `plots/` directory:
1. 📅 **Monthly Claim Frequency Over Time**  
2. 📈 **Monthly Claim Severity Over Time**  
3. ⚖️ **Loss Ratio by Gender and Vehicle Type**  

---

### Data Quality Observations
- 🚧 **Missing Data**:  
  - **550** missing entries for vehicle attributes (e.g., `VehicleType`, `Make`, `Model`).  
  - **640,000+** missing entries for vehicle conditions (`WrittenOff`, `Rebuilt`, `Converted`).  

These gaps highlight the need for **enhanced data collection and validation processes**.  

---

## 🔜 Next Steps
- 🔎 **Deeper multivariate analysis**: Correlations, bivariate plots  
- 🚨 **Outlier detection** and impact on premiums  
- 📊 Finalize visualizations and insights for the final report  

---

**Prepared by:** Helina Abebe  
**Date:** 2025-06-15
