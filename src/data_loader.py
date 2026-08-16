
import pandas as pd
from src.config import REQUIRED_COLUMNS
from pathlib import Path
from src.exceptions import FileLoadError, DataValidationError
from src.decorators import log_execution


class CSVDataLoader():

    """ responsible for loading and validating csv files """

    def __init__(self, file_path: Path):
        self.file_path = file_path

    @log_execution
    def load(self) -> pd.DataFrame:

        try:
            df = pd.read_csv(self.file_path)

        except FileNotFoundError as exc:
            raise FileLoadError (
                f"file not found {self.file_path}"
            ) from exc

        except pd.errors.ParserError as exc:                    
            raise FileLoadError (
                f"Unable to parse CSV: {self.file_path}"
            ) from exc
        
        self._Validate_columns(df)
                
        return df  


    def _Validate_columns(self, df: pd.DataFrame) -> None:

        missings = set(REQUIRED_COLUMNS) - set(df.columns)  

        if missings:
            raise DataValidationError(
                f"missing columns: {sorted(missings)}"
                )  

