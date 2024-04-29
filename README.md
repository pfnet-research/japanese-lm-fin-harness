# Japanese Language Model Financial Evaluation Harness
This is a harness for Japanese language model evaluation in the financial domain.

## 0-shot Leaderboard
<!-- lb start -->
| Model | Ave. | chabsa | cma_basics | cpa_audit | fp2 | security_sales_1 | prompt | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai/gpt-4-32k | 66.27 | 93.16 | 81.58 | 37.44 | 50.74 | 68.42 | default |
| openai/gpt-4 | 66.07 | 93.20 | 78.95 | 37.69 | 50.32 | 70.18 | default |
| openai/gpt-4-turbo | 64.59 | 92.86 | 76.32 | 36.18 | 50.95 | 66.67 | default |
| [pfnet/nekomata-14b-pfn-qfin](https://huggingface.co/pfnet/nekomata-14b-pfn-qfin) | 52.74 | 88.87 | 47.37 | 25.13 | 39.16 | 63.16 | 1.0-0.2.1 |
| [rinna/nekomata-14b-instruction](https://huggingface.co/rinna/nekomata-14b-instruction) | 50.91 | 89.40 | 52.63 | 20.35 | 36.00 | 56.14 | 1.0-0.2.1 |
| openai/gpt-35-turbo | 50.27 | 89.98 | 52.63 | 18.09 | 29.26 | 61.40 | default |
| [tokyotech-llm/Swallow-MS-7b-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MS-7b-v0.1) | 41.37 | 79.22 | 23.68 | 17.09 | 25.47 | 61.40 | 1.0-0.2.1 |
| [cyberagent/calm2-7b](https://huggingface.co/cyberagent/calm2-7b) | 39.80 | 78.27 | 31.58 | 16.58 | 26.95 | 45.61 | 1.0-0.1 |
| [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) | 38.90 | 73.66 | 34.21 | 14.07 | 26.95 | 45.61 | default |
| openai/text-davinci-003 | 37.68 | 53.92 | 44.74 | 17.59 | 26.53 | 45.61 | default |
| [tokyotech-llm/Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) | 37.54 | 61.28 | 28.95 | 16.08 | 25.26 | 56.14 | 1.0-0.1 |
| [llm-jp/llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) | 36.81 | 57.66 | 31.58 | 18.34 | 27.37 | 49.12 | 1.0-0.1 |
| [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) | 36.23 | 74.15 | 23.68 | 15.33 | 25.89 | 42.11 | 1.0-0.1 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) | 36.06 | 68.52 | 21.05 | 17.59 | 24.00 | 49.12 | 1.0-0.2.1 |
| [cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large) | 34.81 | 53.58 | 28.95 | 16.83 | 23.79 | 50.88 | 1.0-0.1 |
| [stabilityai/japanese-stablelm-3b-4e1t-base](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base) | 34.58 | 52.32 | 34.21 | 15.58 | 26.95 | 43.86 | 1.0-0.1 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) | 34.49 | 37.54 | 36.84 | 17.59 | 26.11 | 54.39 | 1.0-0.1 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) | 32.18 | 36.16 | 39.47 | 18.59 | 26.32 | 40.35 | 1.0-0.1.2 |
| [cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) | 32.02 | 49.12 | 26.32 | 13.32 | 24.00 | 47.37 | 1.0-0.2.1 |
| [Qwen/Qwen1.5-0.5B](https://huggingface.co/Qwen/Qwen1.5-0.5B) | 30.82 | 50.40 | 21.05 | 15.58 | 26.74 | 40.35 | 1.0-0.6 |
| [cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 30.76 | 37.49 | 26.32 | 15.33 | 23.79 | 50.88 | 1.0-0.1 |
| [cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) | 30.46 | 30.08 | 28.95 | 16.83 | 23.79 | 52.63 | 1.0-0.1 |
| [Qwen/Qwen1.5-0.5B-Chat](https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat) | 29.98 | 36.69 | 34.21 | 15.33 | 25.05 | 38.60 | 1.0-0.1 |
| [line-corporation/japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) | 29.54 | 35.95 | 26.32 | 14.07 | 24.00 | 47.37 | 1.0-0.1 |
| [cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small) | 29.48 | 35.95 | 23.68 | 18.59 | 23.58 | 45.61 | 1.0-0.6 |
| [cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) | 28.80 | 37.83 | 28.95 | 13.07 | 23.79 | 40.35 | 1.0-0.4 |
<!-- lb end -->
Note: Prompt selection is not performed only for Open AI models. For Open AI models, results are counted as wrong when the content filter is applied.

# How to evaluate your model
 1. git clone this repository
 2. Install the requirements
    ```
    poetry install
    ```
 3. Choose your prompt template based on docs/prompt_templates.md and num_fewshots (In this official leaderboard, we use prompt template peforming the best score.)
 4. Replace `TEMPLATE` to the version and change `MODEL_PATH` . And, save the script as harness.sh
    ```
    MODEL_ARGS="pretrained=MODEL_PATH,other_options"
    TASK="chabsa-1.0-TEMPLATE,cma_basics-1.0-TEMPLATE,cpa_audit-1.0-TEMPLATE,security_sales_1-1.0-0.2,fp2-1.0-TEMPLATE"
    python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "result.json"
    ```
 5. Run the script
    ```
    poetry run bash harness.sh
    ```

Note: if you want to check the actual prompt, you can chack using the following command:
```
poetry run python check_prompt.py
```

# Model Regulation
 - Training/Tuning data of the model must not include this evaluation dataset
   - Japanese annual reports included in chabsa are allowed to be used only if chabsa's sentiment data is not used for training/tuning.
 - No license violation or concerns are argued for the model (e.g. using ShareGPT or Alpaca for training corpus)

# Citation
If you use this repository, please cite the following paper:
```
@preprint{Hirano2023-pre-finllm,
  title={{金融分野における言語モデル性能評価のための日本語金融ベンチマーク構築}},
  author={平野, 正徳},
  doi={10.51094/jxiv.564},
  year={2023}
}
@preprint{Hirano2023-pre-finllm,
  title={{金融分野における言語モデル性能評価のための日本語金融ベンチマーク構築}},
  author={平野, 正徳},
  doi={10.51094/jxiv.564},
  year={2023}
}
```

Or cite directory this repository:
```
@misc{Hirano2023-jlfh
    title={{Japanese Language Model Financial Evaluation Harness}},
    author={Masanori Hirano},
    year={2023},
    url = {https://github.com/pfnet-research/japanese-lm-fin-harness}
}
```

# Note:
cpa_audit data comes from an existing collection of Japanese CPA Audit exam questions and answers [1].
In addition, this dataset was built using data from the [Institute of Certified Public Accountants and Auditing Oversight Board Web site](https://www.fsa.go.jp/cpaaob/kouninkaikeishi-shiken/index.html) and is [subject to a CC-BY 4.0 license](https://www.fsa.go.jp/cpaaob/copyright.html).
We got special permission to include this data directly for this evaluation. Thanks to their contribution.

[1] Tatsuki Masuda, Kei Nakagawa, Takahiro Hoshino, Can ChatGPT pass the JCPA exam?: Challenge for the short-answer method test on Auditing, JSAI Technical Report, Type 2 SIG, 2023, Volume 2023, Issue FIN-031, Pages 81-88, Released on J-STAGE October 12, 2023, Online ISSN 2436-5556, https://doi.org/10.11517/jsaisigtwo.2023.FIN-031_81

# Contribution
This project is owned by [Preferred Networks](https://www.preferred.jp) and maintained by [Masanori Hirano](https://mhirano.jp).

If you want to add models or evaluation dataset, please let me know via issues or pull requests.
