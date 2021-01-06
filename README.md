# academic-ads-bibtex

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/academic-ads-bibtex)
![PyPI](https://img.shields.io/pypi/v/academic-ads-bibtex?color=blue)
![License](https://img.shields.io/github/license/astrochun/academic-ads-bibtex?color=blue)

![PyPI - Downloads](https://img.shields.io/pypi/dm/academic-ads-bibtex?color=light%20green&label=PyPI-download&style=flat-square)
![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgithub.com%2Fastrochun%2Facademic-ads-bibtex)

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Installation Instructions](#installation-instructions)
- [Execution](#execution)
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


## Getting Started

These instructions will have the code running.

### Installation Instructions

#### Setting up a Python environment

I recommend creating a separate (virtual) environment to avoid any possible
conflicts with existing software that you used. Instructions are provided
for `conda` and `virtualenv`.

##### Instructions for `conda`

```bash
$ (sudo) conda create -n bibtex python=3.7
$ conda activate bibtex
```

##### Instructions for `virtualenv`
```bash
$ (sudo) conda install virtualenv  # if not installed
$ mkdir academic-ads-bibtex
$ cd academic-ads-bibtex
$ virtualenv venv
$ source venv/bin/activate
```

There are way two to get the code:
1. From [source](https://github.com/astrochun/academic-ads-bibtex)
2. From [PyPi](https://pypi.org/project/academic-ads-bibtex/)

Installation from source:
```bash
# For conda
$ git clone https://github.com/astrochun/academic-ads-bibtex.git
$ cd academic-ads-bibtex

# For virtualenv
$ git clone https://github.com/astrochun/academic-ads-bibtex.git .

# Install
$ (sudo) python setup.py install
```

Installation from PyPi:
```bash
$ (sudo) pip install academic-ads-bibtex
```

## Execution

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
   [bibtex_journals.db](bibtex_journals.db). This can be changed by specifying
   the `-d` or `--db_filename` command-line flag.
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
