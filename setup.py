from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='candlestick',
    version='0.0.2',
    author='Jeffrey Phung',
    author_email='phung1043@yahoo.com',
    description='Candlestick Patterns',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ForexAndBeyond/candlestick-patterns',
    license='MIT',
    packages=['candlestick'],
    install_requires=['pandas','requests'],
)