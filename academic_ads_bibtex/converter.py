class Convert:
    """
    Main class to perform BibTeX conversion for Academic compatibility
    """

    def __init__(self, filename, db_filename, out_filename=None):

        self.filename = filename
        self.db_filename = db_filename

        if out_filename is None:
            self.out_filename = self.filename.replace('.bbl', '_revised.bbl')

        # Import BibTeX file and journal database
        self.bibtex_content = self.import_file()
        self.db_dict = self.import_database()

        # Update journal to full name
        self.bibtex_revised = self.replace()

    def import_file(self):
        with open(self.filename, 'r') as f:
            bibtex_content = f.read()
        f.close()
        return bibtex_content

    def import_database(self):
        with open(self.db_filename, 'r') as f:
            content = f.read()
        db_list = content.split("\n")
        db_dict = dict(item.split(',') for item in db_list)
        f.close()
        return db_dict

    def replace(self):
        bibtex_revised = str(self.bibtex_content)
        for key, value in self.db_dict.items():
            bibtex_revised = bibtex_revised.replace(f'\{key}', value)

        return bibtex_revised

    def write_file(self):
        print(f"Writing : {self.out_filename}")
        with open(self.out_filename, 'w') as f:
            f.writelines(self.bibtex_revised)
        f.close()
