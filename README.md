# Loan Default Prediction

This project aims to predict whether a loan will default, as well as estimate the monetary loss incurred if it does. By leveraging machine learning algorithms, this model helps financial institutions make informed decisions regarding loan approvals and manage financial risks.

![Loan Prediction](path_to_image/loan_prediction_image.png)

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Models](#models)
6. [Evaluation](#evaluation)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

Loan default prediction is a critical task for financial institutions to mitigate financial risks. This project aims to predict both whether a loan will default and the severity of the loss using a dataset of applicant features. By utilizing various machine learning techniques, the project bridges traditional banking approaches with asset management perspectives, optimizing risk assessment.

---

## Dataset

The dataset includes the following features:

| **Variable**         | **Description**                                   |
|----------------------|---------------------------------------------------|
| Loan_ID              | Unique Loan ID                                    |
| Gender               | Male/ Female                                      |
| Married              | Applicant married (Y/N)                           |
| Dependents           | Number of dependents                              |
| Education            | Applicant Education (Graduate/Under Graduate)     |
| Self_Employed        | Self employed (Y/N)                               |
| ApplicantIncome      | Applicant income                                  |
| CoapplicantIncome    | Coapplicant income                                |
| LoanAmount           | Loan amount in thousands                          |
| Loan_Amount_Term     | Term of loan in months                            |
| Credit_History       | Credit history meets guidelines                   |
| Property_Area        | Urban/ Semi Urban/ Rural                          |
| Loan_Status          | Loan approved (Y/N)                               |
| Loss                 | Monetary loss incurred if the loan defaults       |

You can find the dataset [here](path_to_dataset).

---

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/loan-default-prediction.git
    ```

2. Navigate to the project directory:
    ```bash
    cd loan-default-prediction
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have Jupyter Notebook installed to run the notebook files:
    ```bash
    pip install notebook
    ```

---

## Usage

1. **Preprocess the Dataset:** Use the preprocessing cells in the Jupyter Notebook to clean and prepare the data.
2. **Train the Model:** Utilize the cells in the Jupyter Notebook to train various machine learning models on the dataset.
3. **Make Predictions:** Follow the instructions in the notebook to make predictions on the test dataset.

**To run the Jupyter Notebook:**
1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
2. Open the relevant notebook file and follow the instructions within.

---

## Models

This project employs various machine learning models to predict loan default and estimate loss, including:
- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

Each model is implemented and evaluated within the Jupyter Notebook to determine its effectiveness in predicting loan defaults and estimating financial loss.

---

## Evaluation

Model performance is evaluated using the Mean Absolute Error (MAE) of the loss predictions. MAE measures the average magnitude of errors in the predictions, with a lower MAE indicating better accuracy.

---

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:
1. Fork the repository on GitHub.
2. Create a new branch for your feature or fix.
3. Commit your changes and push them to your forked repository.
4. Open a pull request on the original repository with a description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For further information or questions, please contact [your email] or open an issue on the repository.
