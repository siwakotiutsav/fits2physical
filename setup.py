from setuptools import setup, find_packages

setup(
    name="f2p",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "astropy",
        "scipy"
    ],
    description="FITS 2D/3D physical size analyzer",
    author="Your Name",
    python_requires=">=3.8"
)
