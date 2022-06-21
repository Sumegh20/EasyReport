from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as rd:
    long_description = rd.read()

setup(
    name='EasyReport',
    version='0.0.7',
    author='Sumegh Sen',
    author_email="sumegh20@gmail.com",
    description='Generate a quick EDA report of a pandas DataFrame',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Sumegh20/EasyReport',
    project_urls = {
        "Bug Tracker": "https://github.com/Sumegh20/EasyReport/issues",
    },
    keywords=['EDA', 'Exploratory Data Analysis', 'Easy Report', 'Dataset Report'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_dir={'': 'src'},
    packages = setuptools.find_packages(where='src'),
    install_requires=[
        'pandas==1.1.5',
        'seaborn==0.11.2',
        'scipy==1.5.4',
        'matplotlib==3.3.4',
        'missingno==0.5.0',
    ]
)
