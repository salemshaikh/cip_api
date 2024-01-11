from setuptools import setup, find_packages

setup(
    name='cip',
    version='0.1',
    packages=find_packages(),
    description='Python package for API',
    author='SalemShaikh',
    author_email='salem.shaikh@cipla.com',
    url='https://github.com/salemshaikh/cip_api',
    install_requires=[
        "plotly==5.17.0",
        "matplotlib==3.8.1",
    ]
)
