

from pathlib import Path

class SalesReporter:
    """ writting output to sales report """

    def __init__(self, analyzer):
        self.analyzer = analyzer

    def generate(self, output_path: Path):
        output_path.parent.mkdir(
            parents=True
            ,exist_ok= True
        )

        with open(output_path, "w", encoding="utf-8") as file:
            file.write("=" * 50 + "\n")
            file.write("SALES ANALYTICS REPORT" + "\n")
            file.write("=" * 50 + "\n")
            file.write("SUMMARY\n")
            file.write("-" * 50 + "\n")

            file.write(f"Total sales: {round(self.analyzer.total_sales(),2)}\n\n")

            file.write(f"Average sales: {round(self.analyzer.average_sales(),2)}\n\n")

            file.write(f"Total orders: {round(self.analyzer.total_order(),2)}\n\n")

            file.write(f"Total quantity: {round(self.analyzer.total_quantity(),2)}\n\n")

            file.write(f"Sales by region: \n {self.analyzer.sale_by_region()}\n\n")

            file.write(f"Sales by product: \n {self.analyzer.sale_by_product()}\n\n")

            file.write(f"Sales by category: \n {self.analyzer.sale_by_category()}\n\n")

            file.write(f"Sales by month: \n {self.analyzer.sale_by_month()}\n\n")

            file.write(f"Sales statistics: \n {self.analyzer.sales_statistics()}\n\n")

            file.write(f"Top product: \n {self.analyzer.top_product()}\n\n")

            file.write(f"Top region: \n {self.analyzer.top_region()}\n\n")

            file.write("=" * 50)







    
            


    

    


