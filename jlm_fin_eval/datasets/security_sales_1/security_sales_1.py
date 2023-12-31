import json

import datasets

_DESCRIPTION = "This data is a collection of Japanese Security Sales 1st grade exam questions and answers."
_CITATION = "https://www.bks.co.jp/layout_design/gaimuin/1111shintoku1_mogi.pdf https://www.bks.co.jp/layout_design/gaimuin/tokukai1_1110.pdf"
_LICENSE = "MIT"
_HOMEPAGE = "https://www.bks.co.jp/layout_design/gaimuin/1111shintoku1_mogi.pdf https://www.bks.co.jp/layout_design/gaimuin/tokukai1_1110.pdf"


class SecuritySales1(datasets.GeneratorBasedBuilder):
    """SecuritySales1 dataset."""

    VERSION = datasets.Version("0.0.1")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="security_sales_1",
            version=VERSION,
            description="The SecuritySales1 dataset.",
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
    SecuritySales1().download_and_prepare()
