from setuptools import setup, find_packages

setup(
    name="svp_kernel",
    version="1.0.0-enterprise",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    author="SVP Infrastructure Labs",
    description="Zero-Trust Semantic Validation Protocol for AI Agents",
    url="https://github.com/gokuljayaprakash8/SVP-Semantic-Vector-Protocol-KERNEL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
