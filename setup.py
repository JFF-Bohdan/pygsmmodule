from distutils.core import setup

if __name__ == "__main__":
    setup(
        name="pygsmmodule",
        packages=["pygsmmodule"],  # this must be the same as the name above
        version="0.1",
        description="GSM modules support library",
        author="Bohdan Danishevsky",
        author_email="dbn@aminis.com.ua",
        url="https://github.com/JFF-Bohdan/pygsmmodule",  # use the URL to the github repo
        download_url="",  # I"ll explain this in a second
        keywords=["GSM", "sim module", "SIM-800", "SIM 800", " SIM-900", "SIM 900"],  # arbitrary keywords
        classifiers=[],
    )
