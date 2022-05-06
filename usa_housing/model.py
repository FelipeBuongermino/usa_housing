import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from usa_housing.data import clean_dataframe
from usa_housing.data import get_data


def model(df):
    """ Gradient Boosting Regressor Model """
    X_gb = df.drop(columns=['price'], axis=1)
    y_gb = df['price']

    X_train, X_test, y_train, y_test = train_test_split(X_gb, y_gb, test_size=0.30, random_state=42)

    model = GradientBoostingRegressor(n_estimators=500)

    gb = model.fit(X_train,y_train)
    y_pred = gb.predict(X_train)
    y_pred_test = gb.predict(X_test)

    r2_train = r2_score(y_train,y_pred)
    mae_train = mean_absolute_error(y_train,y_pred)
    r2_test = r2_score(y_test,y_pred_test)
    mae_test = mean_absolute_error(y_test,y_pred_test)

    return r2_train,mae_train,r2_test,mae_test


if __name__ == '__main__':
    # Get data frame
    df = clean_dataframe()
    # Train Model
    final = model(df)
    print('Model: Gradient Boosting Regressor')
    print(f'R^2 Train = {round(final[0],3)}, R^2 Test = {round(final[2],3)}, MAE Train = {round(final[1],2)} and MAE Test = {round(final[3],2)}')
