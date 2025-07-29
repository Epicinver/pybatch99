from setuptools import setup, find_packages

setup(
    name="batch4py",
    version="1.0.3",
    description="Batch and Windows CMD syntax for Python.",
    author="Arran Hewitt",
    packages=find_packages(),  # Will auto-detect 'batch4py'
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
