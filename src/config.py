
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"

RAW_FILE = DATA_DIR / "raw_sales.csv"
CLEAN_FILE = DATA_DIR / "cleaned_sales.csv"
REPORT_FILE = REPORT_DIR / "sales_report.txt"

REQUIRED_COLUMNS = [
    "order_id",
    "date",
    "customer",
    "product",
    "category",
    "quantity",
    "unit_price",
    "region",
]


