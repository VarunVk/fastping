import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fast-ping-VarunVk", # Replace with your own username
    version="0.0.1",
    author="Varun Vijaya Kumar",
    author_email="nurav91@gmail.com",
    description="Ping network analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VarunVk/fastping",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)