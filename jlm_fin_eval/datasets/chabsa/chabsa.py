import glob
import json
import os

import datasets

_DESCRIPTION = "TBD"
_CITATION = "TBD"
_LICENSE = "TBD"
_HOMEPAGE = "TBD"


class Chabsa(datasets.GeneratorBasedBuilder):
    """chABSA dataset."""

    VERSION = datasets.Version("0.0.1")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="chABSA",
            version=VERSION,
            description="The chABSA dataset.",
        ),
    ]

    def _info(self):
        features = datasets.Features(
            {
                "id": datasets.Value("int32"),
                "sentence": datasets.Value("string"),
                "target": datasets.Value("string"),
                "polarity": datasets.Value("string"),
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
                    "filepath": dl_manager.download_and_extract(
                        "https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/chABSA-dataset.zip"
                    ),
                    "split": datasets.Split.TEST,
                },
            )
        ]

    def _generate_examples(self, filepath, split):
        files = glob.glob(os.path.join(filepath, "chABSA-dataset", "*.json"))
        i_count = 0
        for data_file in files:
            with open(data_file, encoding="utf-8") as f:
                data = json.load(f)
                for row in data["sentences"]:
                    sentence = row["sentence"]
                    for opinion_row in row["opinions"]:
                        id = i_count
                        i_count += 1
                        target = opinion_row["target"]
                        polarity = opinion_row["polarity"]
                        yield id, {
                            "id": id,
                            "sentence": sentence,
                            "target": target,
                            "polarity": polarity,
                        }


if __name__ == "__main__":
    Chabsa().download_and_prepare()
