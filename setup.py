from setuptools import setup, find_packages

##Read requirements.txt, ignore comments
try:
    REQUIRES = list()
    f = open("requirements.txt", "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[: line.find("#")].strip()
        if line:
            REQUIRES.append(line)
except:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name="drlportfolio",
    version="0.0.1",
    # include_package_data=True,
    author="bibo feng",
    author_email="bibofeng@gmail.com",
    description="DRL portfolio package from https://github.com/vermouth1992/drl-portfolio-management ",
    url="github.com/bibofeng/drl-portfolio-management.git",
    license="unlicense",
    package_dir={"": "src"},  # package directory,
    packages=find_packages(where="src"),
    package_data={'': ['../stock_trading.py']}, ## include non py files
    include_package_data=True,
    install_requires=REQUIRES
    + ["pyfolio @ git+https://github.com/bibofeng/pyfolio.git"],
    # install_requires=REQUIRES
    zip_safe=False,
)                                    