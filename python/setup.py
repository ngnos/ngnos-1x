import os
from setuptools import setup

def packages(directory):
    return [
        _[0].replace('/','.')
        for _ in os.walk(directory)
        if os.path.isfile(os.path.join(_[0], '__init__.py'))
    ]

setup(
    name = "ngnos",
    version = "1.3.0",
    author = "ngNOS maintainers and contributors",
    author_email = "maintainers@ngnos.com",
    description = ("ngNOS configuration libraries."),
    license = "LGPLv2+",
    keywords = "ngnos",
    url = "http://www.ngnos.com",
    packages = packages('ngnos'),
    long_description="ngNOS configuration libraries",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ],
    entry_points={
        "console_scripts": [
            "config-mgmt = ngnos.config_mgmt:run",
        ],
    },
)
