from setuptools import setup

setup(
    name="monzo",
    version="0.11.2",
    description="A python SDK for interacting with the Monzo API.",
    url="https://github.com/owenvoke/monzo-python",
    author="Owen Voke",
    author_email="development@voke.dev",
    license="MIT",
    packages=["monzo"],
    install_requires=["requests~=2.31", "requests-oauthlib~=1.3", "python-dotenv~=1.0"],
)
