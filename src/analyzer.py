

import pandas as pd
import numpy as np

class SalesAnalyser:
    """ perform analysis on cleaned sales data """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def total_sales(self) -> float:
        return self.df['sales'].sum()

    def average_sales(self) -> float:
        return self.df['sales'].mean()
    
    def total_order(self) -> int:
        return self.df['order_id'].nunique()
    
    def total_quantity(self) -> int:
        return self.df['quantity'].sum()

    def sale_by_region(self) -> pd.DataFrame:

        output_df =  (
            self.df
            .groupby("region", as_index = False)['sales']
            .sum()
            .sort_values('sales',
                         ascending=False
                    )
            )
        return output_df
        
    def sale_by_product(self) -> pd.DataFrame:

        output_df =  (
            self.df
            .groupby("product", as_index = False)['sales']
            .sum()
            .sort_values('sales',
                         ascending=False
                    )
            )
        return output_df    

    def sale_by_category(self) -> pd.DataFrame:

        output_df = (
            self.df
            .groupby("category", as_index = False)['sales']
            .sum()
            .sort_values('sales',
                         ascending=False
                    )
            )

        return output_df    

    def sale_by_month(self) -> pd.DataFrame:

        output_df =  (
            self.df
            .groupby("month", as_index = False)['sales']
            .sum()
            )   
        
        return output_df 

    def sales_statistics(self) -> dict:

        val = self.df['sales'].to_numpy()

        output_dict =  {
            "minimum": np.min(val),
            "maximum": np.max(val),
            "sum":    np.sum(val)
        }

        return output_dict

    def top_product(self):
        top_item = self.sale_by_product()
        return top_item.iloc[0,0]

    def top_region(self):
        top_region = self.sale_by_region()
        return top_region.iloc[0,0]