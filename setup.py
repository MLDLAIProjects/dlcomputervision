import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

ORGANIZATION_NAME = "MLDLAIProjects"
REPO_NAME = "dlcomputervision"
AUTHOR_USER_NAME = "sahilv05"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "connect.sahil5@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for dl app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{ORGANIZATION_NAME}/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{ORGANIZATION_NAME}/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)