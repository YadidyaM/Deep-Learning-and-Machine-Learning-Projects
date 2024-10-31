# Titanic Survival Prediction

## Overview
This project aims to predict the survival of passengers aboard the Titanic using machine learning techniques. The sinking of the Titanic is one of the most infamous shipwrecks in history, and the dataset used for this project contains information about passengers on the Titanic, including features such as age, gender, passenger class, and whether they survived or not.

## Dataset
The dataset used in this project is sourced from the [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic) competition on Kaggle. It consists of two CSV files:

- `train.csv`: Contains information about a subset of passengers (891 to be exact) and their survival status (ground truth).
- `test.csv`: Contains similar information for the remaining passengers (418) but does not disclose the survival status.

You can download the dataset from [this link](https://www.kaggle.com/c/titanic/data). 

## Dependencies
- Python 3.x
- pandas
- numpy
- scikit-learn
- tensorflow
- matplotlib

Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Getting Started
Follow these steps to run the project:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/YadidyaM/Titanic---Machine-Learning-from-Disaster/
    ```

2. Navigate to the project directory:

    ```
    cd Titanic---Machine-Learning-from-Disaster
    ```

3. Download the dataset from the link provided above and place it in the `data` directory.

4. Run the Jupyter Notebook or Python scripts to preprocess the data, train the models, and make predictions.

## Model Performance
The trained model achieved a score of 0.7 in the Titanic competition on Kaggle. This score indicates that the model predicted Titanic survival correctly for 70% of people.

## Contents
- `data/`: Directory to store the dataset files.
- `notebooks/`: Jupyter Notebooks for data exploration, preprocessing, model training, and evaluation.
- `src/`: Python scripts for preprocessing, training, and predicting.
- `requirements.txt`: List of required Python packages.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
