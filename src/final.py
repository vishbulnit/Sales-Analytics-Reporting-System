
from src.config import RAW_FILE,CLEAN_FILE,REPORT_FILE
from src.data_loader import CSVDataLoader
from src.data_cleaner import SalesDataCleaner
from src.analyzer import SalesAnalyser
from src.reporter import SalesReporter

def save_clean_data(df):
    """ save cleaned data to CSV """

    CLEAN_FILE.parent.mkdir(
        parents=True
        ,exist_ok=True
    )

    df.to_csv(
        CLEAN_FILE,
        index = False
    )

def main():

    # load data
    loader =  CSVDataLoader(RAW_FILE)
    raw_df = loader.load()
    print(f"Rawdata loaded with no. of rows {len(raw_df)}.")

    # clean data
    cleaner = SalesDataCleaner()
    clean_df = cleaner.clean(raw_df)
    print(f"Cleaned data with no. of rows {len(clean_df)}.")

    # save cleaned data
    save_clean_data(clean_df)
    print(f"Cleaned data is saved.")

    # analyze data
    analyser = SalesAnalyser(clean_df)

    # writting data to sales report
    reporter = SalesReporter(analyser)
    reporter.generate(REPORT_FILE)
    print(f"Sales summary report is generate.")
    

