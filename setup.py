from setuptools import setup

setup(
    name='pyl',
    version='0.0.1',
    author='Matthias Vogelgesang',
    author_email='matthias.vogelgesang@kit.edu',
    license='MIT',
    scripts=['bin/pyl-filter',
             'bin/pyl-build'],
    install_requires=['pandocfilters'],
)
