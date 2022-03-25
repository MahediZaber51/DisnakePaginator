import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DisnakePaginator",
    version="0.0.1",
    author="Mahedi Zaman Zaber",
    author_email="mahedizaber51@gmail.com",
    description="A package containing easy paginators for disnake",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MahediZaber51/DisnakePaginator",
    keywords = ["discord", "disnake", "paginator"],
    install_requires = [
        "disnake",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/MahediZaber51/DisnakePaginator/issues",
    },
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    package_dir={"": "DisnakePaginator"},
    packages=setuptools.find_packages(where="DisnakePaginator"),
    python_requires=">=3.6",
)
