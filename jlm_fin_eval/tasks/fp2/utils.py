def doc_to_text_00(doc):
    doc_text = "【問題】\n" + doc["question"] + "\n"
    if doc["context"] and doc["context"] != "":
        doc_text += doc["context"] + "\n"
    doc_text += "\n【答え】\n"
    # doc_text += chr(int(doc["answer"]) + 65)
    return doc_text


def doc_to_target_00(doc):
    answer = doc["choices"]["text"][doc["choices"]["id"].index(doc["answer"])]
    return answer


def doc_to_choices_00(doc):
    choices = [choice for choice in doc["choices"]["text"]]
    return choices


def doc_to_text_01(doc):
    q_doc_text = doc["question"] + "\n"
    if doc["context"] and doc["context"] != "":
        q_doc_text += doc["context"] + "\n"
    return f"[問題]:{q_doc_text}[選択肢]:[{', '.join(doc['choices']['text'])}]\n[答え]:"


def doc_to_text_01_2(doc):
    q_doc_text = doc["question"] + "\n"
    if doc["context"] and doc["context"] != "":
        q_doc_text += doc["context"] + "\n"
    choice_doc_text = []
    for choice_id, choice_text in zip(doc["choices"]["id"], doc["choices"]["text"]):
        choice_doc_text.append(chr(choice_id + 65) + ":" + choice_text)
    return f"[問題]:{q_doc_text}[選択肢]:[{', '.join(choice_doc_text)}]\n[答え]:"


def doc_to_target_01_2(doc):
    answer = chr(doc["choices"]["id"].index(doc["answer"]) + 65)
    return answer


def doc_to_choices_01_2(doc):
    choices = [chr(i + 65) for i, _ in enumerate(doc["choices"]["id"])]
    return choices


def doc_to_text_02(doc):
    q_doc_text = doc["question"] + "\n"
    if doc["context"] and doc["context"] != "":
        q_doc_text += doc["context"] + "\n"
    choices = ",".join(
        [
            f"{idx}.{choice}"
            for idx, choice in zip(doc["choices"]["id"], doc["choices"]["text"])
        ]
    )
    return f"質問:{q_doc_text}" f"選択肢:{choices}\n" "回答:"


def doc_to_target_02(doc):
    return [
        str(choice_id)
        for choice_id in doc["choices"]["id"]
        if choice_id == doc["answer"]
    ][0]


def doc_to_choices_02(doc):
    return [str(choice) for choice in doc["choices"]["id"]]


def doc_to_text_02_1(doc):
    q_doc_text = doc["question"] + "\n"
    if doc["context"] and doc["context"] != "":
        q_doc_text += doc["context"] + "\n"
    return f"質問:{q_doc_text}\n回答:"


def doc_to_text_03(doc):
    q_doc_text = doc["question"] + "\n"
    if doc["context"] and doc["context"] != "":
        q_doc_text += doc["context"] + "\n"
    input_text = f"{q_doc_text}"
    return f"### 入力:\n{input_text}\n### 応答:\n"


def doc_to_text_04(doc, SEP="<NL>"):
    q_doc_text = doc["question"]
    if doc["context"] and doc["context"] != "":
        q_doc_text += "\n" + doc["context"]
    input_text = f"{q_doc_text}"
    return f"ユーザー: {input_text}{SEP}システム: "


def doc_to_text_05(doc):
    return doc_to_text_04(doc, SEP="\n")


def doc_to_text_06(doc):
    INSTRUCTION = "与えられた選択肢の中から、最適な答えを選んでください。"
    q_doc_text = doc["question"]
    if doc["context"] and doc["context"] != "":
        q_doc_text += "\n" + doc["context"]
    input_text = f"質問：{q_doc_text}"
    return f"{INSTRUCTION}\n\n{input_text} [/INST] "
