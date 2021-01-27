Introduction
============

The `Hugo Academic admin tool <https://github.com/wowchemy/hugo-academic-cli>`_
allows for the ingestion of BibTeX records to add to the publication list.
One easy solution is to use the `NASA ADS <https://ui.adsabs.harvard.edu/>`_
to retrieve such records from a
`NASA ADS Library <https://ui.adsabs.harvard.edu/help/libraries/creating-libraries>`_.
However, such records often contain LaTeX ``\newcommand``. For example:

::

   @ARTICLE{2016ApJS..226....5L,
      author = {{Ly}, C. and {Malhotra}, S. and {Malkan}, M.~A. and {Rigby}, J.~R. and
           {Kashikawa}, N. and {de los Reyes}, M.~A. and {Rhoads}, J.~E.
           },
       title = "{The Metal Abundances across Cosmic Time (MACT) Survey. I. Optical Spectroscopy in the Subaru Deep Field}",
     journal = {\apjs},
   archivePrefix = "arXiv",
      eprint = {1602.01089},
    keywords = {galaxies: abundances, galaxies: distances and redshifts, galaxies: evolution, galaxies: ISM, galaxies: photometry, galaxies: star formation},
        year = 2016,
       month = sep,
      volume = 226,
         eid = {5},
       pages = {5},
         doi = {10.3847/0067-0049/226/1/5},
      adsurl = {https://ui.adsabs.harvard.edu/abs/2016ApJS..226....5L},
     adsnote = {Provided by the SAO/NASA Astrophysics Data System}
   }

Here, the journal name is simplified to ``\apjs``. This ends up propagating into
Hugo Academic sites. To fix this, this simple pure Python script will convert
such aliases into the full journal names. It uses a journal database to
conduct the replacement.
