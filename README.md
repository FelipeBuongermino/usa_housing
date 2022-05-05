# house-sales-in-king-country-usa

[House Sales in King County, USA](https://www.kaggle.com/harlfoxem/housesalesprediction) is a dataset provided by [harlfoxem](https://www.kaggle.com/harlfoxem) which contains house sales prices for King County sold between may 2014 and may 2015. 

## Table of contents

- [Getting Started](#getting-started)
- [Models Performances](#models-performances)

## Getting started

The [notebook](./notebooks/USA_housing_analysis.ipynb) focus on how to find the best features using Filter Methods, Wrapper Methods and Embedded Methods. Depois disso, foram feitas diversas evaluações com diversos modelos de regressão (Linear Regression, Polynomial Regression, KNN Regression, Ridge Regression, Lasso Regression, Elastic Net Regression, Random Forest, Decision Tree, XGBoost, AdaBoost and Gradient Boosting).

Também foi feito um arquivo [model.py](./usa_housing/model.py) em forma de função com o modelo que obteve as melhores métricas. 

Para iniciar o modelo pelo console do python, basta digitar ```make run_model```, informando assim as métricas do modelo escolhido para previsao o preço de uma casa em King County.

## Models performances

**MAE error and R2 square metrics for differents Machine Learning Regression models**

![scores](./docs/imgs/scores.png)

To see more, check the [notebook](./notebooks/USA_housing_analysis.ipynb).

