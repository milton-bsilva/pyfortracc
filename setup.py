
import os
try:
    os.system("pip install --upgrade setuptools")
    os.system("python -m ensurepip --upgrade")
except:
    pass

from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open(os.path.join('pyfortracc', '_version.py')) as f:
    version_line = next(filter(lambda line: line.startswith('__version__'), f))
    __version__ = version_line.split('=')[-1]

setup(
    name="pyfortracc",
    version=__version__.strip().strip('"'),
    author="Helvecio B. L. Neto, Alan J. P. Calheiros",
    author_email="fortraccproject@gmail.com",
    description="A Python package for track and forecasting.",
    long_description=open("README.md").read(),
    long_description_content_type="text/x-rst",
    url="https://github.com/fortracc-project/fortracc",
    packages=find_packages(),
    install_requires=requirements,
    license="LICENSE",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: None",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Hydrology",
    ]
)