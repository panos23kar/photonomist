from setuptools import setup, find_packages

setup(
    name='photonomist',
    version='1.0.0',
    description='Tidy your photos',
    author='Panagiotis Karydakis',
    author_email='photonomist.23@gmail.com',
    package_dir= {'': 'src'},
    packages=find_packages('photonomist'),
)