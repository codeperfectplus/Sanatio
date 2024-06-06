import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read().decode("utf-8")

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="Sanatio",
    version="1.1.0",
    author="Deepak Raj",
    author_email="deepak008@live.com",
    description="Simple and easy to validate data in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeperfectplus/Sanatio",
    data_files=[('assets', glob('sanatio/assets/*'))],
    keywords="sanatio, validation, python, data, data-validation, data-validation-python, data-validation-library, data-validation-python-library, data-validation-python-package, data-validation-package, data-validation-library-python",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    project_urls={"Documentation": "https://sanatio.readthedocs.io/en/latest/",
                  "Source": "https://github.com/codeperfectplus/Sanatio",
                  "Tracker": "https://github.com/codeperfectplus/Sanatio/issues"},
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Programming Language :: Python :: 3",
                 "License :: OSI Approved :: Apache Software License",
                 "Operating System :: OS Independent",
                 "Intended Audience :: Developers"],
    python_requires=">=3.4",
    include_package_data=True,
)
