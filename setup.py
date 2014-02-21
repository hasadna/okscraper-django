from distutils.core import setup

setup(
    name='okscraper-django',
    version='0.1',
    description='okscraper django integration',
    author='Ori Hoch',
    author_email='ori@uumpa.com',
    license='GPLv3',
    url='https://github.com/orihoch/okscraper-django',
    packages=['okscraper_django'],
    install_requires=['okscraper'],
    dependency_links=['git+ssh://git@github.com/hasadna/okscraper.git#egg=okscraper']
)
