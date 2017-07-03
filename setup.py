from setuptools import setup, find_packages

setup(
    name="bitwrap-psql",
    version="0.2.0",
    author="Matthew York",
    author_email="myork@stackdump.com",
    description="a python api to for bitwrap-io to use PostgreSQL as an eventstore",
    license='MIT',
    keywords='PNML petri-net eventstore state-machine',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['bitwrap-machine', 'pg8000==1.10.6'],
    long_description="""
# Bitwrap-psql

This library provides a database abstraction for the bitwrap-io package.

""",
    url="http://getbitwrap.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Database :: Database Engines/Servers",
        "License :: OSI Approved :: MIT License"
    ],
)
