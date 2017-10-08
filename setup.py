import os
import re

from pip.req import parse_requirements

from pygsmmodule import __version__

from setuptools import find_packages, setup


README_FILE = "README.md"
install_reqs = parse_requirements("requirements.txt", session=False)
requirements = [str(ir.req) for ir in install_reqs]
package_name = "pygsmmodule"
hyphen_package_name = package_name.replace("_", "-")


def read_file_content(file_name):
    with open(file_name) as f:
        return f.read()


def read_version():
    regexp = re.compile(r"^__version__\s*=\s*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__), package_name, "__init__.py")
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError("Cannot find version in {}".format(init_py))


if __name__ == "__main__":
    packages_to_remove = ["script", "tests"]
    packages = find_packages()

    for item in packages_to_remove:
        if item in packages:
            packages.remove(item)

    setup(
        name="pygsmmodule",
        packages=packages,
        version=__version__,
        description="GSM modem control libraty for SIM800/SIM900 modules",
        long_description=read_file_content(README_FILE),
        author="Bohdan Danishevsky",
        author_email="dbn@aminis.com.ua",
        url="https://github.com/JFF-Bohdan/{}".format(package_name),  # use the URL to the github repo
        keywords=["GSM", "sim module", "SIM-800", "SIM 800", " SIM-900", "SIM 900"],  # arbitrary keywords
        install_requires=requirements,
        classifiers=[],
        license="MIT",
        zip_safe=False
    )
