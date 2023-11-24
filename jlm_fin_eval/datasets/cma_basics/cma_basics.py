import json

import datasets

_DESCRIPTION = "Basics sample questions for CMA (Certiﬁed Member Analyst of the Securities Analysts Association of Japan). Crawled from https://www.saa.or.jp/curriculum/foundation/pdf/sample_qa.pdf and modified it. Please note that this is not the same as the 1st and 2nd grade of the CMA exam."
_CITATION = "https://www.saa.or.jp/curriculum/foundation/pdf/sample_qa.pdf"
_LICENSE = "MIT"
_HOMEPAGE = "https://www.saa.or.jp/curriculum/foundation/pdf/sample_qa.pdf"


class CmaBasics(datasets.GeneratorBasedBuilder):
    """CMA Basics dataset."""

    VERSION = datasets.Version("0.0.1")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="cma_basics",
            version=VERSION,
            description="The CMA basics dataset.",
        ),
    ]

    def _info(self):
        features = datasets.Features(
            {
                "id": datasets.Value("int32"),
                "question": datasets.Value("string"),
                "context": datasets.Value("string"),
                "choices": datasets.features.Sequence(
                    {
                        "id": datasets.Value("int32"),
                        "text": datasets.Value("string"),
                    }
                ),
                "answer": datasets.Value("int32"),
                "comment": datasets.Value("string"),
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,  # type: ignore
                gen_kwargs={
                    "filepath": dl_manager.download("data.json"),
                    "split": datasets.Split.TEST,
                },
            )
        ]

    def _generate_examples(self, filepath, split):
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
            for row in data["data"]:
                id = row["id"]
                question = row["question"]
                context = row["context"]
                choices = [
                    {"id": choice["id"], "text": choice["text"]}
                    for choice in row["choices"]
                ]
                answer = row["answer"]
                comment = row["comment"]
                yield row["id"], {
                    "id": id,
                    "question": question,
                    "context": context,
                    "choices": choices,
                    "answer": answer,
                    "comment": comment,
                }


if __name__ == "__main__":
    CmaBasics().download_and_prepare()
