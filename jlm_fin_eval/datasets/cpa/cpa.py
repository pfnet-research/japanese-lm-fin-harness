import datasets
import pandas as pd

_DESCRIPTION = "TBD"
_CITATION = "TBD"
_LICENSE = "TBD"
_HOMEPAGE = "TBD"


class CPA(datasets.GeneratorBasedBuilder):
    """CPA dataset."""

    VERSION = datasets.Version("0.0.1")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="CPA",
            version=VERSION,
            description="The CPAdataset.",
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
                    "filepath": dl_manager.download(
                        "https://drive.google.com/uc?export=download&id=1Wf3YybZ9MAPA33Z6B9-yhZiToOVnFLJH"
                    ),
                    "split": datasets.Split.TEST,
                },
            )
        ]

    def _generate_examples(self, filepath, split):
        df = pd.read_excel(filepath, index_col=0)
        df["question"] = df["question"].astype(str)
        df["ア"] = df["ア"].astype(str)
        df["イ"] = df["イ"].astype(str)
        df["ウ"] = df["ウ"].astype(str)
        df["エ"] = df["エ"].astype(str)
        df["オ"] = df["オ"].astype(str)
        df["カ"] = df["カ"].astype(str)
        i_count = 0
        for row in df.to_dict(orient="records"):
            if row["question"] == "" or row["question"] == "nan":
                continue
            if row["abnormal_flg"] == 1:
                continue
            id = i_count
            i_count += 1
            question = row["question"]
            contexts = []
            if "ア" in row and row["ア"] != "" and row["ア"] != "nan":
                contexts.append("ア: " + row["ア"])
            if "イ" in row and row["イ"] != "" and row["イ"] != "nan":
                contexts.append("イ: " + row["イ"])
            if "ウ" in row and row["ウ"] != "" and row["ウ"] != "nan":
                contexts.append("ウ: " + row["ウ"])
            if "エ" in row and row["エ"] != "" and row["エ"] != "nan":
                contexts.append("エ: " + row["エ"])
            if "オ" in row and row["オ"] != "" and row["オ"] != "nan":
                contexts.append("オ: " + row["オ"])
            if "カ" in row and row["カ"] != "" and row["カ"] != "nan":
                contexts.append("カ: " + row["カ"])
            context = "\n".join(contexts)
            choices = [{"id": i, "text": row[i + 1]} for i in range(6)]
            answer = row["a_no"] - 1
            yield id, {
                "id": id,
                "question": question,
                "context": context,
                "choices": choices,
                "answer": answer,
            }


if __name__ == "__main__":
    CPA().download_and_prepare()
