# setup.py
from setuptools import setup, find_packages

setup(
    name='your_library',
    version='1.0.0',
    packages=find_packages(),  # Automatically find packages in your_library/
    description='A simple example library',
    author='Aakash Yadav',
    install_requires=['requests>=2.21.0']
)

