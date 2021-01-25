Examples
========

The primary script to execute is `academic_ads_bibtex`_.
The above installation will include this executable in your python
environment paths.

Execution requires only one argument, which is the full path to the BibTeX
file. It can be provided with the ``-f`` or ``--filename`` command-line flag.

.. code:: bash

    $ academic_ads_bibtex -f /full/path/to/my_pubs.bbl


By default:

1. The code uses the repository-based journal database,
   `bibtex_journals.db`_. This can be changed by specifying
   the ``-d`` or ``--db_filename`` command-line flag.
2. The revised BibTeX file will be based on the input ``filename`` with the
   prefix changed to include ``_revised``. For example, for the above case,
   the output file will be ``/full/path/to/my_pubs_revised.bbl``. This can be
   changed by specifying the ``-o`` or ``--out_filename`` command-line flag.

A log file is constructed: ``/full/path/to/academic_ads_bibtex.YYYY-MM-DD.log``

.. _academic_ads_bibtex: https://github.com/astrochun/academic-ads-bibtex/blob/main/bin/academic_ads_bibtex
.. _bibtex_journals.db: https://github.com/astrochun/academic-ads-bibtex/blob/main/academic_ads_bibtex/database/bibtex_journals.db