import setuptools
from glob import glob

# Reading the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Reading the list of requirements from the requirements file
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

# Setting up the package
setuptools.setup(
    name="Sanatio",
    version="1.6.0",
    author="Deepak Raj",
    author_email="deepak008@live.com",
    description="Simple and easy to validate data in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeperfectplus/Sanatio",
    data_files=[('assets', glob('sanatio/assets/*'))],
    keywords=[
        "sanatio", "validation", "python", "data", "data-validation", 
        "data-validation-python", "data-validation-library", 
        "data-validation-python-library", "data-validation-python-package", 
        "data-validation-package", "data-validation-library-python"
    ],
    install_requires=requirements,
    packages=setuptools.find_packages(),
    project_urls={
        "Documentation": "https://sanatio.readthedocs.io/en/latest/",
        "Source": "https://github.com/codeperfectplus/Sanatio",
        "Tracker": "https://github.com/codeperfectplus/Sanatio/issues"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    python_requires=">=3.4",
    include_package_data=True,
)
