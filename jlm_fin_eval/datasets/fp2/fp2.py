import json

import datasets

_DESCRIPTION = "TBD"
_CITATION = "TBD"
_LICENSE = "TBD"
_HOMEPAGE = "TBD"


class FP2(datasets.GeneratorBasedBuilder):
    """FP2 dataset."""

    VERSION = datasets.Version("0.0.1")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="fp2",
            version=VERSION,
            description="The FP2 dataset.",
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
    FP2().download_and_prepare()
