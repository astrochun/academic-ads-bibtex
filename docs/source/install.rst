Installation
============

There are two ways to get the code:
  1. From `PyPi`_
  2. From `source`_

But first, we recommend creating a separate (virtual) environment to
avoid any possible conflicts with existing software that you used.
Instructions are provided for ``conda`` and ``virtualenv``.


From PyPi
'''''''''

Using ``conda``:

.. code:: bash

   (base) $ (sudo) conda create -n bibtex python=3.7
   (base) $ conda activate bibtex
   (bibtex) $ (sudo) pip install academic-ads-bibtex


Using ``virtualenv``:

.. code:: bash

   (base) $ (sudo) conda install virtualenv  # if not installed
   (base) $ mkdir academic-ads-bibtex
   (base) $ cd academic-ads-bibtex
   (base) $ virtualenv venv
   (base) $ source venv/bin/activate
   (venv) $ pip install academic-ads-bibtex


From Source
'''''''''''

Using ``conda``:

.. code:: bash

   (base) $ (sudo) conda create -n bibtex python=3.7
   (base) $ conda activate bibtex
   (bibtex) $ git clone https://github.com/astrochun/academic-ads-bibtex.git
   (bibtex) $ cd academic-ads-bibtex
   (bibtex) $ (sudo) python setup.py install

Using ``virtualenv``:

.. code:: bash

   (base) $ (sudo) conda install virtualenv  # if not installed
   (base) $ git clone https://github.com/astrochun/academic-ads-bibtex.git
   (base) $ cd academic-ads-bibtex
   (base) $ virtualenv venv
   (base) $ source venv/bin/activate
   (venv) $ python setup.py install

.. _source: https://github.com/astrochun/academic-ads-bibtex
.. _PyPi: https://pypi.org/project/academic-ads-bibtex/
