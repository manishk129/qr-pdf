from setuptools import setup, find_packages

setup(
    name="qr-pdf",                     
    version="1.0.1",                       
    description="Python package to generate severals QR codes at once in PDF format", 
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="manish",
    author_email="manishkumarpandit12@gmail.com",
    url="https://github.com/manishk129/qr-pdf",
    packages=find_packages(),              # Automatically find sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
