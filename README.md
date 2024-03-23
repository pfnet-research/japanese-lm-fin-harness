# Japanese Language Model Financial Evaluation Harness
This is a harness for Japanese language model evaluation in the financial domain.

## Leaderboard
<!-- lb start -->
| Model | Ave. | chabsa | cma_basics | cpa_audit | fp2 | security_sales_1 |
| --- | --- | --- | --- | --- | --- | --- |
| openai/gpt-4-32k | 66.27 | 93.16 | 81.58 | 37.44 | 50.74 | 68.42 |
| openai/gpt-4 | 66.07 | 93.20 | 78.95 | 37.69 | 50.32 | 70.18 |
| openai/gpt-4-turbo | 64.59 | 92.86 | 76.32 | 36.18 | 50.95 | 66.67 |
| [Qwen/Qwen-72B](https://huggingface.co/Qwen/Qwen-72B) | 62.18 | 92.36 | 78.95 | 32.91 | 40.00 | 66.67 |
| [Qwen/Qwen-72B-Chat](https://huggingface.co/Qwen/Qwen-72B-Chat) | 57.89 | 92.52 | 78.95 | 29.90 | 28.42 | 59.65 |
| [rinna/nekomata-14b](https://huggingface.co/rinna/nekomata-14b) | 56.03 | 89.70 | 63.16 | 25.13 | 42.53 | 59.65 |
| [Qwen/Qwen-14B](https://huggingface.co/Qwen/Qwen-14B) | 55.95 | 90.73 | 63.16 | 22.61 | 38.32 | 64.91 |
| [Qwen/Qwen-14B-Chat](https://huggingface.co/Qwen/Qwen-14B-Chat) | 54.71 | 91.56 | 65.79 | 22.36 | 32.42 | 61.40 |
| [rinna/nekomata-14b-instruction](https://huggingface.co/rinna/nekomata-14b-instruction) | 54.43 | 91.27 | 63.16 | 24.12 | 37.47 | 56.14 |
| [stabilityai/japanese-stablelm-base-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-70b) | 53.07 | 90.87 | 60.53 | 22.36 | 33.68 | 57.89 |
| [stabilityai/japanese-stablelm-instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b) | 52.77 | 91.85 | 60.53 | 22.86 | 36.00 | 52.63 |
| [tokyotech-llm/Swallow-13b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-hf) | 52.32 | 87.79 | 60.53 | 19.60 | 35.79 | 57.89 |
| openai/gpt-35-turbo | 50.27 | 89.98 | 52.63 | 18.09 | 29.26 | 61.40 |
| [meta-llama/Llama-2-70b-hf](https://huggingface.co/meta-llama/Llama-2-70b-hf) | 50.21 | 89.37 | 57.89 | 20.85 | 30.32 | 52.63 |
| [lightblue/qarasu-14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed) | 50.04 | 89.69 | 57.89 | 20.35 | 31.37 | 50.88 |
| [rinna/nekomata-7b-instruction](https://huggingface.co/rinna/nekomata-7b-instruction) | 49.90 | 90.34 | 47.37 | 22.61 | 27.79 | 61.40 |
| [Qwen/Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat) | 49.86 | 86.38 | 50.00 | 20.85 | 32.42 | 59.65 |
| [meta-llama/Llama-2-70b-chat-hf](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) | 49.53 | 90.29 | 52.63 | 18.84 | 28.00 | 57.89 |
| [Qwen/Qwen-7B](https://huggingface.co/Qwen/Qwen-7B) | 48.67 | 85.11 | 57.89 | 19.35 | 30.11 | 50.88 |
| [elyza/ELYZA-japanese-Llama-2-13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b) | 48.37 | 88.37 | 47.37 | 19.35 | 28.84 | 57.89 |
| [tokyotech-llm/Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) | 48.31 | 87.59 | 52.63 | 19.60 | 32.63 | 49.12 |
| [Xwin-LM/Xwin-LM-13B-V0.2](https://huggingface.co/Xwin-LM/Xwin-LM-13B-V0.2) | 47.53 | 88.11 | 52.63 | 22.11 | 25.68 | 49.12 |
| [rinna/nekomata-7b](https://huggingface.co/rinna/nekomata-7b) | 47.12 | 79.18 | 42.11 | 21.61 | 33.05 | 59.65 |
| [meta-llama/Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) | 46.98 | 87.95 | 52.63 | 19.60 | 27.37 | 47.37 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) | 46.04 | 82.52 | 44.74 | 17.84 | 30.74 | 54.39 |
| [elyza/ELYZA-japanese-Llama-2-13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast) | 45.70 | 86.37 | 39.47 | 20.60 | 31.16 | 50.88 |
| [lmsys/vicuna-13b-v1.5-16k](https://huggingface.co/lmsys/vicuna-13b-v1.5-16k) | 45.57 | 85.81 | 52.63 | 19.10 | 28.21 | 42.11 |
| [mosaicml/mpt-30b-instruct](https://huggingface.co/mosaicml/mpt-30b-instruct) | 45.18 | 83.27 | 42.11 | 21.36 | 26.53 | 52.63 |
| [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) | 44.86 | 83.70 | 39.47 | 20.35 | 29.89 | 50.88 |
| [llm-jp/llm-jp-13b-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0) | 44.66 | 85.91 | 39.47 | 20.10 | 26.95 | 50.88 |
| [elyza/ELYZA-japanese-Llama-2-13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct) | 44.27 | 89.40 | 44.74 | 18.59 | 26.53 | 42.11 |
| [meta-llama/Llama-2-13b-hf](https://huggingface.co/meta-llama/Llama-2-13b-hf) | 44.19 | 82.04 | 36.84 | 20.85 | 30.32 | 50.88 |
| [rinna/youri-7b-instruction](https://huggingface.co/rinna/youri-7b-instruction) | 43.84 | 86.88 | 34.21 | 21.61 | 27.37 | 49.12 |
| [llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0) | 43.76 | 83.23 | 39.47 | 19.60 | 27.37 | 49.12 |
| [rinna/youri-7b-chat](https://huggingface.co/rinna/youri-7b-chat) | 43.67 | 86.67 | 36.84 | 19.60 | 26.11 | 49.12 |
| [cyberagent/calm2-7b-chat](https://huggingface.co/cyberagent/calm2-7b-chat) | 43.67 | 81.09 | 36.84 | 18.09 | 29.68 | 52.63 |
| [llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0) | 43.60 | 86.83 | 39.47 | 18.59 | 24.00 | 49.12 |
| [elyza/ELYZA-japanese-Llama-2-13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct) | 43.59 | 87.27 | 42.11 | 18.59 | 26.11 | 43.86 |
| [lmsys/vicuna-33b-v1.3](https://huggingface.co/lmsys/vicuna-33b-v1.3) | 43.44 | 87.81 | 34.21 | 19.60 | 28.21 | 47.37 |
| [lmsys/vicuna-7b-v1.5-16k](https://huggingface.co/lmsys/vicuna-7b-v1.5-16k) | 43.21 | 84.78 | 39.47 | 19.60 | 24.84 | 47.37 |
| [mosaicml/mpt-30b-chat](https://huggingface.co/mosaicml/mpt-30b-chat) | 43.10 | 86.40 | 39.47 | 21.36 | 24.42 | 43.86 |
| [elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) | 42.99 | 83.48 | 42.11 | 19.60 | 25.89 | 43.86 |
| [tokyotech-llm/Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) | 42.91 | 72.27 | 39.47 | 19.60 | 28.84 | 54.39 |
| [pfnet/plamo-13b](https://huggingface.co/pfnet/plamo-13b) | 42.87 | 76.97 | 39.47 | 21.61 | 27.16 | 49.12 |
| [mosaicml/mpt-30b](https://huggingface.co/mosaicml/mpt-30b) | 42.80 | 83.44 | 36.84 | 19.60 | 26.74 | 47.37 |
| [stabilityai/japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) | 42.73 | 78.74 | 34.21 | 19.10 | 30.74 | 50.88 |
| [Xwin-LM/Xwin-LM-7B-V0.2](https://huggingface.co/Xwin-LM/Xwin-LM-7B-V0.2) | 42.73 | 82.79 | 42.11 | 19.85 | 25.05 | 43.86 |
| [llm-jp/llm-jp-13b-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0) | 42.39 | 81.24 | 39.47 | 19.10 | 26.53 | 45.61 |
| [cyberagent/calm2-7b](https://huggingface.co/cyberagent/calm2-7b) | 41.96 | 80.02 | 42.11 | 17.84 | 24.21 | 45.61 |
| [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) | 41.89 | 74.71 | 44.74 | 20.60 | 23.79 | 45.61 |
| [rinna/youri-7b](https://huggingface.co/rinna/youri-7b) | 41.84 | 73.60 | 34.21 | 19.10 | 29.68 | 52.63 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) | 41.59 | 82.53 | 39.47 | 20.10 | 25.47 | 40.35 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b) | 41.43 | 78.94 | 34.21 | 19.35 | 23.79 | 50.88 |
| [tokyotech-llm/Swallow-7b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf) | 41.36 | 83.61 | 31.58 | 18.09 | 24.42 | 49.12 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2) | 41.36 | 78.62 | 34.21 | 19.10 | 24.00 | 50.88 |
| [pfnet/plamo-13b-instruct](https://huggingface.co/pfnet/plamo-13b-instruct) | 41.13 | 77.33 | 39.47 | 21.11 | 27.37 | 40.35 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) | 41.03 | 75.36 | 39.47 | 19.10 | 27.37 | 43.86 |
| [meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf) | 40.99 | 77.41 | 39.47 | 18.59 | 27.37 | 42.11 |
| [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) | 40.71 | 78.38 | 31.58 | 20.60 | 27.37 | 45.61 |
| [rinna/bilingual-gpt-neox-4b-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft) | 40.31 | 78.23 | 34.21 | 19.35 | 25.89 | 43.86 |
| [llm-jp/llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) | 39.70 | 75.48 | 36.84 | 19.85 | 24.21 | 42.11 |
| [elyza/ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) | 39.65 | 85.71 | 39.47 | 18.59 | 24.63 | 29.82 |
| [rinna/japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) | 39.33 | 53.75 | 39.47 | 22.11 | 26.95 | 54.39 |
| [line-corporation/japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) | 39.06 | 65.01 | 34.21 | 20.85 | 26.11 | 49.12 |
| [line-corporation/japanese-large-lm-1.7b](https://huggingface.co/line-corporation/japanese-large-lm-1.7b) | 39.06 | 54.30 | 42.11 | 19.60 | 28.42 | 50.88 |
| [pfnet/plamo-13b-instruct-nc](https://huggingface.co/pfnet/plamo-13b-instruct-nc) | 39.03 | 73.58 | 39.47 | 20.60 | 24.63 | 36.84 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft) | 38.92 | 73.21 | 42.11 | 19.35 | 24.84 | 35.09 |
| [matsuo-lab/weblab-10b](https://huggingface.co/matsuo-lab/weblab-10b) | 37.73 | 76.84 | 34.21 | 21.11 | 23.16 | 33.33 |
| openai/text-davinci-003 | 37.68 | 53.92 | 44.74 | 17.59 | 26.53 | 45.61 |
| [cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) | 37.67 | 62.89 | 34.21 | 20.35 | 25.26 | 45.61 |
| [line-corporation/japanese-large-lm-3.6b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft) | 37.00 | 59.79 | 36.84 | 21.61 | 24.63 | 42.11 |
| [rinna/bilingual-gpt-neox-4b](https://huggingface.co/rinna/bilingual-gpt-neox-4b) | 36.80 | 60.51 | 34.21 | 19.60 | 27.58 | 42.11 |
| [cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 36.14 | 56.06 | 36.84 | 19.60 | 26.11 | 42.11 |
| [cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small) | 36.06 | 50.28 | 34.21 | 19.10 | 27.58 | 49.12 |
| [cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) | 35.85 | 52.40 | 39.47 | 20.35 | 23.16 | 43.86 |
| [abeja/gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 35.63 | 49.67 | 39.47 | 20.10 | 25.05 | 43.86 |
| [line-corporation/japanese-large-lm-1.7b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft) | 35.25 | 55.22 | 39.47 | 18.34 | 24.63 | 38.60 |
| [cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large) | 34.60 | 51.68 | 34.21 | 20.10 | 23.16 | 43.86 |
| [cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) | 34.48 | 56.86 | 31.58 | 17.84 | 24.00 | 42.11 |
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
   - Japanese annual reports included in chabsa is allowed to be used only if chabsa's sentiment data is not used for training/tuning.
 - No license violation or concerns is argued for the model

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
In addition, this dataset was built using data from the [Institute of Certified Public Accountants and Auditing Oversight Board Web site](https://www.fsa.go.jp/cpaaob/kouninkaikeishi-shiken/index.html) and is [subject to a CC-BY 4.0 license https://www.fsa.go.jp/cpaaob/copyright.html](https://www.fsa.go.jp/cpaaob/copyright.html).
We got special permission to include this data directly for this evaluation. Thanks to their contribution.

[1] Tatsuki Masuda, Kei Nakagawa, Takahiro Hoshino, Can ChatGPT pass the JCPA exam?: Challenge for the short-answer method test on Auditing, JSAI Technical Report, Type 2 SIG, 2023, Volume 2023, Issue FIN-031, Pages 81-88, Released on J-STAGE October 12, 2023, Online ISSN 2436-5556, https://doi.org/10.11517/jsaisigtwo.2023.FIN-031_81

# Contribution
This project is owned by [Preferred Networks](https://www.preferred.jp) and maintained by [Masanori Hirano](https://mhirano.jp).

If you want to add models or evaluation dataset, please let me know via issues or pull requests.
