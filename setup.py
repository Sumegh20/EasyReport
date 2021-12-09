from setuptools import setup
import setuptools

with open("README.md", "r") as rd:
    long_description = rd.read()

setup(
    name='PreProcessingNinja',
    version='0.0.1',
    description='A data preprocessing helper consists of your basic preprocessing needs',
    author='Bijoy Kumar Roy',
    url='https://github.com/Bijoy99roy/PreProcessingNinja',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['preprocessing', 'preprocessing ninja'],
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
        'seaborn'
    ]
)
