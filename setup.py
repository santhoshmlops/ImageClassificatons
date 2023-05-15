import setuptools

with open("README.md","r" ,encoding="utf-8")as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME ="ImageClassificatons"
SRC_REPO ="cnnClassifier"
AUTHOR_NAME = "santhoshmlops"
AUTHOR_EMAIL = "santhoshmlops@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Image Classification Using CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/santhoshmlops/ImageClassificatons",
    packages=setuptools.find_packages(where="src"),
    package_dir={"":"src"}
)
