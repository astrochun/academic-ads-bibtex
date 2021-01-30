from typing import Union
from pathlib import Path

from .logger import log_stdout
import pkg_resources


class Convert:
    """
    Main class to perform BibTeX conversion for Academic compatibility

    :param filename: BibTeX file
    :param db_filename: Journal database file
    :param out_filename: Modified BibTeX file
    :param log: LogClass or logger object

    :ivar str bibtex_content: BiBTeX content (from ``import_file`` method)
    :ivar dict db_dict: Journal database dict (from ``import_database`` method)
    :ivar str bibtex_revised: BibTeX content (from ``replace`` method)
    """

    def __init__(self, filename: Union[str, Path],
                 db_filename: Union[str, Path],
                 out_filename: Union[str, Path], log=None):

        if log is None:
            log = log_stdout()

        self.log = log
        self.filename = filename
        self.db_filename = db_filename
        self.out_filename = out_filename

        # Import BibTeX file and journal database
        self.bibtex_content = self.import_file()
        self.db_dict = self.import_database()

        # Update journal to full name
        self.bibtex_revised = self.replace()

    def import_file(self) -> str:
        """Import BibTeX file"""
        self.log.info(f"Reading: {self.filename}")
        with open(self.filename, 'r') as f:
            bibtex_content = f.read()
        f.close()
        return bibtex_content

    def import_database(self) -> dict:
        """Import journal database file"""
        if isinstance(self.db_filename, str):
            self.log.info(f"Reading: {self.db_filename}")
            with open(self.db_filename, 'r') as f:
                content = f.read()
            f.close()
        else:
            if self.db_filename is None:
                self.log.info("Importing database from source")
                stream = pkg_resources.resource_stream(__name__, 'database/bibtex_journals.db')
                content = stream.read().decode("utf-8")
            else:
                self.log.warning("Neither a filename or None was provided db_filename")
                raise ValueError(
                    "import_database: Neither a filename or None was provided db_filename")
        db_list = content.split("\n")
        db_dict = dict(item.split(',') for item in db_list)

        return db_dict

    def replace(self) -> str:
        """Replace journal abbreviations"""
        bibtex_revised = str(self.bibtex_content)
        for key, value in self.db_dict.items():
            in_str = '{' + f'\{key}' + '}'
            out_str = '{' + f'{value}' + '}'
            bibtex_revised = bibtex_revised.replace(in_str, out_str)

        return bibtex_revised

    def write_file(self):
        """Write revised BibTeX file"""
        self.log.info(f"Writing : {self.out_filename}")
        with open(self.out_filename, 'w') as f:
            f.writelines(self.bibtex_revised)
        f.close()
