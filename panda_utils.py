from pandas import DataFrame


def deduplicate_columns(df: DataFrame) -> DataFrame:
    return df.loc[:,~df.columns.duplicated()].copy()


def deduplicate_indexes(df: DataFrame) -> DataFrame:
    return df.loc[~df.index.duplicated(),:].copy()