import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__="0.0.0"

REPO_NAME = "ChestCancerClassification"
AUTHOUT_USER_NAME = "mxiid"
SRC_REPO = "ccc"
AUTHOR_EMAIL = "abdulmuid300@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOUT_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Chest Cancer Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOUT_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOUT_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)