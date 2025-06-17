## 1. Overview

This report presents the modeling approach, results, and insights derived from building predictive models for a dynamic, risk-based pricing system. Two key tasks were addressed:

1. **Claim Severity Prediction:** Estimating the total claims amount for policies with claims.
2. **Premium Prediction:** Predicting the optimal premium amount using a risk-based pricing framework.

## 2. Data Preparation

- The dataset contains **999,805 rows and 50 columns**. Missing values were addressed as follows:
  - Features with high missing percentages (e.g., `WrittenOff`, `Converted`, `Rebuilt`) were removed.
  - Remaining missing values were imputed or handled contextually.

- **Feature Engineering:**
  - A `VehicleAgeBucket` feature was created to group vehicles into age categories.
  - Categorical variables (e.g., `VehicleType`, `make`) were encoded using one-hot encoding, resulting in **798 features**.

- The dataset was split into training (80%) and testing (20%) sets, with **1,960 samples for training** and **490 for testing**.

## 3. Model Building

### 3.1 Claim Severity Prediction

Models were trained on policies with claims (`TotalClaims > 0`):

| Model              | RMSE          | R-squared   |
|--------------------|---------------|-------------|
| Linear Regression  | 39,253.39     | 0.0387      |
| Decision Tree      | 44,784.26     | -0.2513     |
| Random Forest      | 35,320.69     | 0.2217      |
| XGBoost            | 39,650.75     | 0.0191      |
| Tuned XGBoost      | 34,350.47     | 0.2638      |
| Tuned Random Forest| 34,086.47     | 0.2751      |

**Best Model:** Tuned Random Forest (RMSE: 34,086.47, R²: 0.2751)

### 3.2 Premium Prediction

Models were trained to predict `CalculatedPremiumPerTerm`:

| Model              | RMSE          | R-squared   |
|--------------------|---------------|-------------|
| Linear Regression  | 295.82        | 0.6889      |
| XGBoost            | 21.74         | 0.9983      |

**Best Model:** XGBoost (RMSE: 21.74, R²: 0.9983)

## 4. Model Evaluation

- **Claim Severity Models:**  
  Random Forest and XGBoost achieved better generalization than Linear Regression and Decision Tree, with Random Forest slightly outperforming in RMSE and R².

- **Premium Models:**  
  XGBoost demonstrated near-perfect performance, indicating strong predictive power for premium estimation.

- **Business Implications:**  
  Accurate claim severity and premium prediction models can enable precise risk assessments, aligning premiums with customer risk profiles and maximizing profitability.

## 5. Model Interpretability

### Feature Importance Analysis
- **Claim Severity Prediction:**  
  Key features influencing predictions:
  1. `VehicleAge`
  2. `PolicyDuration`
  3. `ClaimHistory`

- **Premium Prediction:**  
  The top influential features include:
  1. `VehicleType`
  2. `NumberOfClaims`
  3. `CoverageLevel`

### SHAP and LIME Insights
- SHAP values highlighted that older vehicles with longer policy durations and higher claim histories contributed most to increased predicted claims.
- LIME demonstrated that individual feature contributions aligned with domain knowledge, validating model reliability.

## 6. Recommendations

- **Claims Management:** Focus on customers with older vehicles and high claim histories for targeted interventions or adjusted policies.
- **Premium Adjustment:** Use XGBoost predictions to tailor premiums dynamically, incorporating predicted claim probabilities and severities.
- **Feature Refinement:** Further explore influential features to enhance risk-based pricing strategies.

## 7. Limitations and Next Steps

- **Limitations:**
  - Models were tested on a subset of the dataset, potentially limiting generalizability.
  - Certain features with high missing rates were excluded, which might contain valuable information.

- **Next Steps:**
  - Incorporate additional features (e.g., geographic factors, driver behavior) to improve model robustness.
  - Validate models with larger datasets and cross-validation techniques.
  - Deploy the premium prediction model in a pilot program to evaluate real-world performance.

## 8. Conclusion

This project successfully developed and evaluated models for dynamic, risk-based pricing. The results provide actionable insights for aligning premiums with customer risk, improving profitability while ensuring fair pricing strategies.
