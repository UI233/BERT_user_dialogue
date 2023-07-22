from setuptools import setup
from setuptools import find_packages

setup(
    name="bert_summarizer",
    version="0.0.1",
    description="A bert-based natrual language neural network for chinese dialogue generation trained on CSDS dataset",
    author="uiui",
    author_email="mocoui@outlook.com",
    install_requires=[
        "torch>=1.6",
        "transformers>=4.0.0",
        "jieba",
        "tqdm"
    ],
    packages=find_packages(where="./"),
    package_dir={"bert_summarizer": "bert_summarizer"},
    include_package_data=True
)
