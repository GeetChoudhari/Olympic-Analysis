import pandas as pd


def preprocess(df, region_df):
    # ==================================================PreProcess Summer Olympics==============================================

    # first of all merge with region data
    df = df.merge(region_df, on='NOC', how='left')

    # filter or Summer olympics
    df = df[df['Season'] == "Summer"]

    # dropping duplicates
    df.drop_duplicates(inplace=True)

    # Olympics was not been recognised in 1906
    df = df.loc[df["Year"] != 1906]

    # used one_hot_encoding for Medals Row
    df = pd.concat([df, pd.get_dummies(df["Medal"])], axis=1)
    # df = df['region'].dropna()

    return df
