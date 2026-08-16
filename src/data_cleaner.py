

import pandas as pd
import numpy as np
from src.decorators import log_execution


class SalesDataCleaner:
    """ clean and prepare sales data for analysis """

    @log_execution
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        #remove duplicate order
        df = df.drop_duplicates(subset=["order_id"], keep= "first")

        # convert date
        df['date'] = pd.to_datetime(df['date'], errors="coerce")

        # convert numeric column
        df['quantity'] = pd.to_numeric(df['quantity'], errors="coerce")

        df['unit_price'] = pd.to_numeric(df['unit_price'], errors="coerce")

        # replace invalid values with NaN
        df.loc[df['quantity'] <= 0, 'quantity']  = np.nan
        df.loc[df['unit_price'] <= 0, 'unit_price']  = np.nan

        # fill missing numeric values with median
        df['quantity'] = df['quantity'].fillna(df['quantity'].median())

        df['unit_price'] = df['unit_price'].fillna(df['unit_price'].median()) 

        # remove rows where important values are still missing
        df = df.dropna(subset=['order_id','date','customer','product','region'])

        # create calculated column
        df['sales'] = df['quantity'] * df['unit_price']

        df["month"] = df["date"].dt.to_period("M").astype(str)

        return df.reset_index(drop=True)









