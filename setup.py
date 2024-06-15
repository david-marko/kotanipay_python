from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "KotaniPay Unofficial Python Packaga"
LONG_DESCRIPTION = "API Access to the KotaniPay system"

setup(
    name="kotanipay",
    version=VERSION,
    author="David Marko",
    author_email="markodave46@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # url='https://github.com/KotaniPay/kotanipay-python',
    install_requires=[
        "requests",
        "pydantic",
        "pydantic[email]"
    ],
    keywords=["python", "kotanipay", "mpesa", "crypto"],
    classifiers=[],
)
