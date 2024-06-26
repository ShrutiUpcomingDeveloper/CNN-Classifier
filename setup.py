import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"


REPO_NAME="cnn-classifier"
Author_name="shruti shravani"
SRC_REPO="CNN_Classifier"
AUTHOR_EMAIL="shrutichoudhary312@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    versions=__version__,
    author=Author_name,
    author_email=AUTHOR_EMAIL,
    description="this is my classificaion project",
    long_description = long_description,
    long_description_content ="text/markdown",
    url=f"https://github.com/{Author_name}/{REPO_NAME}",
    project_urls={"Bug Tracker":f"https://github.com/{Author_name}/{REPO_NAME}/issues",},

package_dir={"":"src"},
packages=setuptools.find_packages(where='src')
)