# import csv
# from pathlib import 



# def read_csv(path: str | Path) -> list[dict[str, str]]:
#     with Path(path).open(newline="", encoding="utf-8") as source:
#         return list(csv.DictReader(source))



from pathlib import Path
import pandas as pd


class DataExtractor:
    """
    Extracts data from CSV and Excel files.

    Supported sources:
        CSV
        XLSX
        XLS

    Methods
    -------
    extract(path)
        Reads a file and returns a DataFrame.

    extract_directory(directory)
        Reads every supported file in a directory.
    """

    SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls"}

    def extract(self, path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(f"File does not exist: {path}")

        extension = path.suffix.lower()

        if extension == ".csv":
            return pd.read_csv(path)

        if extension in {".xlsx", ".xls"}:
            return pd.read_excel(path)

        raise ValueError(
            f"Unsupported file type: {extension}. "
            f"Supported: {self.SUPPORTED_EXTENSIONS}"
        )

    def extract_directory(self, directory):
        directory = Path(directory)

        datasets = {}

        for file in directory.iterdir():
            if file.suffix.lower() in self.SUPPORTED_EXTENSIONS:
                datasets[file.stem] = self.extract(file)

        return datasets
