import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="",
    version="0.0.1",
    author="Deepak Raj",
    author_email="deepak008@live.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    url="https://github.com/Py-Contributors/validator.py",
    keywords="audiobook",
    packages=setuptools.find_packages(),
    project_urls={"Documentation": "https://pycontributors.readthedocs.io/projects/morse/en/latest/",
                  "Source": "https://github.com/Py-Contributors/validator.py",
                  "Tracker": "https://github.com/Py-Contributors/validator.py/issues"},
    classifiers=["Development Status :: 2 - Pre-Alpha",
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Intended Audience :: Developers"],
    python_requires=">=3.4",
    # entry_points={
    #     "console_scripts": ["morse = morse.cli:main"],
    # },
)
