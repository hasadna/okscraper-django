from setuptools import setup, find_packages

setup(
    name='okscraper-django',
    version='0.0.5',
    description='okscraper django integration',
    author='Ori Hoch',
    author_email='ori@uumpa.com',
    license='GPLv3',
    url='https://github.com/orihoch/okscraper-django',
    packages=find_packages(exclude=["tests", "test.*", 'settings', 'manage']),
    install_requires=['okscraper==0.0.3'],
    dependency_links=['https://github.com/OriHoch/okscraper/archive/master.tar.gz#egg=okscraper-0.0.3']
)
