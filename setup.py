from setuptools import setup, find_packages

setup(
    name='EEGsigPy',
    version='0.1',
    description='A Python library for EEG signal processing',
    author='Fardin Ghorbani',
    license='Apache-2.0 license',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
)