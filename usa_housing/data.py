import pandas as pd

def get_data():
    """ Get initial DataFrame """
    df = pd.read_csv('usa_housing/data/kc_house_data.csv')
    return df


def clean_dataframe():
    """ Remove houses with no bedrooms and no bathrooms,
    also remove id, date and zipcode columns """
    df = get_data()
    df = df[df.bedrooms != 0]
    df = df[df.bathrooms !=0]
    df = df.drop(['id','date','zipcode'], axis=1)
    return df


if __name__ == '__main__':
    # Get data frame
    df = clean_dataframe()
