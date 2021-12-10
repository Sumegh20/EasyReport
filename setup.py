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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_module=['easy_report'],
    package_dir={'': 'src'},
    install_requires=[
        'pandas==1.1.5',
        'seaborn==0.11.2',
        'scipy==1.5.4',
        'matplotlib==3.3.4',
        'missingno==0.5.0'
    ]
)
