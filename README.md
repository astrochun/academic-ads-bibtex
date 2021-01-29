# academic-ads-bibtex

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/academic-ads-bibtex)
![PyPI](https://img.shields.io/pypi/v/academic-ads-bibtex?color=blue)
![License](https://img.shields.io/github/license/astrochun/academic-ads-bibtex?color=blue)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/astrochun/academic-ads-bibtex/Sphinx%20Docs%20Check?label=sphinx%20docs&color=blue)](https://github.com/astrochun/academic-ads-bibtex/actions?query=workflow%3A%22Sphinx+Docs+Check%22)

![PyPI - Downloads](https://img.shields.io/pypi/dm/academic-ads-bibtex?color=light%20green&label=PyPI-download&style=flat-square)
![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgithub.com%2Fastrochun%2Facademic-ads-bibtex)

API documentation is available at: [ReadTheDocs](https://academic-ads-bibtex.readthedocs.io)

- [Overview](#overview)
- [Installation](#installation)
    - [From PyPi](#from-pypi)
    - [From source](#from-source)
- [Examples](#examples)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)

## Overview

The [Hugo Academic admin tool](https://github.com/wowchemy/hugo-academic-cli)
allows for the ingestion of BibTeX records to add to the publication list.
One easy solution is to use the NASA ADS to retrieve such records from a
NASA ADS Library. However, such records often contain LaTeX `\newcommand`.
For example:

```
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
```

Here, the journal name is simplified to "\apjs". This ends up propagating into
Hugo Academic sites. To fix this, this simple pure Python script will convert
such aliases into the full journal names. It uses a journal database to
conduct the replacement.


## Installation

There are two ways to get the code:
1. From [PyPi](https://pypi.org/project/academic-ads-bibtex/)
2. From [source](https://github.com/astrochun/academic-ads-bibtex)

But first, we recommend creating a separate (virtual) environment to avoid any
possible conflicts with existing software that you used. Instructions are
provided for `conda` and `virtualenv`.

### From PyPi:

Using `conda`:

```bash
(base) $ (sudo) conda create -n bibtex python=3.7
(base) $ conda activate bibtex
(bibtex) $ (sudo) pip install academic-ads-bibtex
```

Using `virtualenv`:

```bash
(base) $ (sudo) conda install virtualenv  # if not installed
(base) $ mkdir academic-ads-bibtex
(base) $ cd academic-ads-bibtex
(base) $ virtualenv venv
(base) $ source venv/bin/activate
(venv) $ pip install academic-ads-bibtex
```

### From source:

Using `conda`:

```bash
(base) $ (sudo) conda create -n bibtex python=3.7
(base) $ conda activate bibtex
(bibtex) $ git clone https://github.com/astrochun/academic-ads-bibtex.git
(bibtex) $ cd academic-ads-bibtex
(bibtex) $ (sudo) python setup.py install
```

Using `virtualenv`:

```bash
(base) $ (sudo) conda install virtualenv  # if not installed
(base) $ git clone https://github.com/astrochun/academic-ads-bibtex.git
(base) $ cd academic-ads-bibtex
(base) $ virtualenv venv
(base) $ source venv/bin/activate
(venv) $ python setup.py install
```

## Examples

The primary script to execute is [`academic_ads_bibtex`](bin/academic_ads_bibtex).
The above installation will include this executable in your python
environment paths.

Execution requires only one argument, which is the full path to the BibTeX
file. It can be provided with the `-f` or `--filename` command-line flags.

```
$ academic_ads_bibtex -f /full/path/to/my_pubs.bbl
```

By default:

1. The code uses the repository-based journal database,
   [bibtex_journals.db](academic_ads_bibtex/database/bibtex_journals.db).
   This can be changed by specifying the `-d` or `--db_filename` command-line
   flag.
2. The revised BibTeX file will be based on the input `filename` with the
   prefix changed to include `_revised`. For example, for the above case,
   the output file will be `/full/path/to/my_pubs_revised.bbl`. This can be
   changed by specifying the `-o` or `--out_filename` command-line flag.

A log file is constructed: `/full/path/to/academic_ads_bibtex.YYYY-MM-DD.log`


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [releases on this repository](https://github.com/astrochun/academic-ads-bibtex/releases).


## Authors

* Chun Ly, Ph.D. ([@astrochun](http://www.github.com/astrochun))


## License

This project is licensed under the [GNU GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).
See the [LICENSE](LICENSE) file for details.
