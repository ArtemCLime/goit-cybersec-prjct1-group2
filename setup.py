from setuptools import setup, find_packages

setup(
    name='datadefendersbot',
    version='1.0',  
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rich",
        "pytest"
    ],
    entry_points={
        'console_scripts': [
            'datadefendersbot=source.main:main',  
        ],
    },
)