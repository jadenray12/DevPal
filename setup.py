from setuptools import setup, find_packages

setup(
    name="devpal",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "setuptools",
        "fastapi",
        "uvicorn",
        "requests",
        "pydantic",
        "requests",
        "langchain",
        "langchain-groq",
        "groq",
        "dotenv",
    ],
    entry_points={
        "console_scripts": [
            "devpal = cli.main:main"
        ]
    },
)
