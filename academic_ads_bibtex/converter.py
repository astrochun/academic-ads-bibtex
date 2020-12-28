from .logger import log_stdout


class Convert:
    """
    Main class to perform BibTeX conversion for Academic compatibility

    :param filename: str or pathlib.Path object
    :param db_filename: str or pathlib.Path object
    :param out_filename: str or pathlib.Path object

    Attributes
    ----------
    bibtex_content: str (from import_file)
    db_dict: dict of journal database (from import_database)
    bibtex_revised: str (from replace)

    Methods
    -------
    import_file()
      Import BibTeX file

    import_database()
      Import journal database file

    replace()
      Replace journal abbreviations

    write_file()
      Write revised BibTeX file
    """

    def __init__(self, filename, db_filename, out_filename, log=None):

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

    def import_file(self):
        """Import BibTeX file"""
        self.log.info(f"Reading: {self.filename}")
        with open(self.filename, 'r') as f:
            bibtex_content = f.read()
        f.close()
        return bibtex_content

    def import_database(self):
        """Import journal database file"""
        self.log.info(f"Reading: {self.db_filename}")
        with open(self.db_filename, 'r') as f:
            content = f.read()
        db_list = content.split("\n")
        db_dict = dict(item.split(',') for item in db_list)
        f.close()
        return db_dict

    def replace(self):
        """Replace journal abbreviations"""
        bibtex_revised = str(self.bibtex_content)
        for key, value in self.db_dict.items():
            bibtex_revised = bibtex_revised.replace(f'\{key}', value)

        return bibtex_revised

    def write_file(self):
        """Write revised BibTeX file"""
        self.log.info(f"Writing : {self.out_filename}")
        with open(self.out_filename, 'w') as f:
            f.writelines(self.bibtex_revised)
        f.close()
