from setuptools import setup
import setuptools

with open("README.md", "r") as rd:
    long_description = rd.read()

setup(
    name='EasyReport',
    version='0.0.1',
    description='Generate a quick EDA report of a pandas DataFrame',
    author='Sumegh Sen',
    url='https://github.com/Sumegh20/EasyReport',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['EDA', 'Exploratory Data Analysis', 'Easy Report', 'Dataset Report'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['easy_report'],
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'seaborn',
        'scipy',
        'matplotlib',
        'missingno'
    ]
)
