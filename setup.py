from distutils.core import setup

setup(
    name='okscraper-django',
    version='0.0.2',
    description='okscraper django integration',
    author='Ori Hoch',
    author_email='ori@uumpa.com',
    license='GPLv3',
    url='https://github.com/orihoch/okscraper-django',
    packages=['okscraper_django'],
    install_requires=['okscraper==0.0.2'],
    dependency_links=['git+ssh://git@github.com/OriHoch/okscraper.git@v0.0.2#egg=okscraper-0.0.2']
)
