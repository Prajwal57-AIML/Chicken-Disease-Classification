import setuptools  # setuptools is used to package and distribute our project


# Reading the README file to use as the long description of the package.
# This helps when the project is uploaded to PyPI or viewed on GitHub.
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# Version of the package.
# This can be updated whenever we make significant changes.
__version__ = "0.0.0"

# Basic project metadata
REPO_NAME = "Chicken-Disease-Classification"  # GitHub repository name
AUTHOR_USER_NAME = "Prajwal57-AIML"  # GitHub username
SRC_REPO = "cnnClassifier"  # Main source folder name (inside src/)
AUTHOR_EMAIL = "prajwalhgowda7@gmail.com"  # Contact email


# Setup configuration – this tells Python how to install and identify our package
setuptools.setup(
    name=SRC_REPO,  # Name of the package (import name)
    version=__version__,  # Current version of the project
    author=AUTHOR_USER_NAME,  # Author name
    author_email=AUTHOR_EMAIL,  # Author email
    description="End-to-End Deep Learning project for Chicken Disease Classification using CNN",  # Short description
    long_description=long_description,  # Detailed description from README
    long_description_content_type="text/markdown",  # README format
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Project URL
    project_urls={
        # Link for reporting issues
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Tells setuptools that packages are inside the 'src' folder
    packages=setuptools.find_packages(where="src")  # Automatically find all packages inside src
)
