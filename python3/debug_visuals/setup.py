from setuptools import setup, find_packages

long_description = None
with open("../../README.md") as file:
    long_description = file.read()

setup(
    name="debug_visuals",
    version="0.0.2",
    description="Visualization functions ready-to-use with VS Code Debug Visualizer",
    author="Fabian Tepe",
    author_email="fabiantepe1.2@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
)
