# 🚗 **Car Insurance Analytics Report**

## 🎯 **Objective**
This report analyzes and identifies significant trends and risk factors in car insurance data. Key metrics include claim frequency, claim severity, and margins, assessed across demographic, geographic, and vehicle-related variables. Statistical tests were conducted to validate or reject key hypotheses.

---

## 📊 **1. Summary of Findings**

### 🗺️ **1.1 Provincial Risk Analysis**
- **Claim Frequency:**  
  - Gauteng has the highest claim frequency (0.0034).  
  - Northern Cape has the lowest (0.0013).  
- **Claim Severity:**  
  - KwaZulu-Natal exhibits the highest average claim severity (84.36).  
  - Northern Cape shows the lowest (14.03).  
- **T-Test Results:**  
  - Comparison between Gauteng and Western Cape:  
    - T-stat = 1.8645, p-value = 0.0623 (statistically insignificant).  
- **ANOVA Results:**  
  - Across all provinces:  
    - F-stat = 5.8672, p-value < 0.0001 (statistically significant).  
- **Z-Test Results:**  
  - Z-stat = 7.5148, p-value < 0.0001 (statistically significant).  

### 📍 **1.2 Postal Code Risk Analysis**
- **Margin Differences:**  
  - T-stat = -0.4371, p-value = 0.6630 (statistically insignificant).  
  - Margins vary widely across postal codes, with a high of 131.76 and a low of -145.73.

### 👥 **1.3 Gender-Based Risk Analysis**
- **Claim Frequency:**  
  - Female: 0.0021  
  - Male: 0.0022  
  - Not Specified: 0.0028  
  - Unknown: 0.0015  
- **Claim Severity:**  
  - Female: 37.05  
  - Male: 32.80  
  - Not Specified: 66.67  
  - Unknown: 53.11  
- **Statistical Tests:**  
  - **T-test for Total Claims:**  
    - T-stat = 4.2577, p-value < 0.0001 (statistically significant).  
  - **Chi-Squared Test:**  
    - Chi2 = 13.0669, p-value = 0.0045 (statistically significant).  

---

## 💡 **2. Key Insights and Interpretations**

### 🌍 **2.1 Regional Risk**
- Gauteng’s high claim frequency and significant ANOVA differences suggest targeted interventions are needed.  
- KwaZulu-Natal’s high claim severity indicates possible costlier claims, warranting premium adjustments.

### 👫 **2.2 Gender Differences**
- Statistically significant differences in claim severity and frequency between genders highlight the need for tailored communication and policies.

### 🗺️ **2.3 Postal Code Margins**
- Insignificant statistical results for margins suggest uniform pricing strategies might be acceptable, but further segmentation could reveal nuances.

---

## ✅ **3. Recommendations**

1. **Provincial Premium Adjustments**  
   - Increase premiums in Gauteng to account for higher risk.  
   - Investigate and address costlier claims in KwaZulu-Natal.  

2. **Gender-Specific Strategies**  
   - Develop gender-targeted risk reduction campaigns.  
   - Review claim severity patterns to ensure fairness in underwriting.  

3. **Localized Marketing and Risk Mitigation**  
   - Focus efforts in high-claim-frequency areas (e.g., Gauteng, KwaZulu-Natal).  
   - Address postal codes with extreme margins to improve profitability.  

4. **Further Research**  
   - Dive deeper into high-variance regions and customer segments.  
   - Examine outliers in postal code margins and claim severity for hidden trends.

---

## 📚 **4. Statistical Appendix**

### 📈 **4.1 Test Results**

| Test        | Metric                  | Statistic | p-value  | Conclusion        |
| ----------- | ----------------------- | --------- | -------- | ----------------- |
| Z-Test      | Claim Frequency (Prov.) | 7.5148    | < 0.0001 | Reject H₀         |
| T-Test      | Total Claims (G-WC)     | 1.8645    | 0.0623   | Fail to Reject H₀ |
| ANOVA       | Total Claims (Prov.)    | 5.8672    | < 0.0001 | Reject H₀         |
| T-Test      | Margin (Postal Code)    | -0.4371   | 0.6630   | Fail to Reject H₀ |
| Chi-Squared | Gender vs. HasClaim     | 13.0669   | 0.0045   | Reject H₀         |

### 🌍 **4.2 Claim Frequency and Severity**

| Province      | Frequency | Severity |
| ------------- | --------- | -------- |
| Eastern Cape  | 0.0016    | 44.72    |
| Free State    | 0.0014    | 43.82    |
| Gauteng       | 0.0034    | 74.67    |
| KwaZulu-Natal | 0.0028    | 84.36    |
| Limpopo       | 0.0027    | 40.93    |
| Mpumalanga    | 0.0024    | 38.80    |
| North West    | 0.0024    | 41.32    |
| Northern Cape | 0.0013    | 14.03    |
| Western Cape  | 0.0022    | 60.87    |

### 👥 **4.3 Gender Metrics**

| Gender        | Frequency | Severity |
| ------------- | --------- | -------- |
| Female        | 0.0021    | 37.05    |
| Male          | 0.0022    | 32.80    |
| Not Specified | 0.0028    | 66.67    |
| Unknown       | 0.0015    | 53.11    |

---

## 🎉 **5. Conclusion**
This analysis highlights significant regional and demographic risk patterns. Implementing these recommendations will enhance risk-based pricing, improve profitability, and support customer segmentation strategies.

