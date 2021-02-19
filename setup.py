from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='academic-ads-bibtex',
    version='0.2.3',
    packages=['academic_ads_bibtex'],
    scripts=['bin/academic_ads_bibtex'],
    url='https://github.com/astrochun/academic-ads-bibtex',
    license='GNU GPLv3',
    author='Chun Ly',
    author_email='astro.chun@gmail.com',
    description='Construct a proper BibTeX file to use with the Hugo Academic theme from ADS export',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={'': ['database/bibtex_journals.db']},
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
