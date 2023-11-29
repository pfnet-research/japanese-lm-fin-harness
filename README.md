# Japanese Language Model Financial Evaluation Harness
This is a harness for Japanese language model evaluation in the financial domain.

## Leaderboard
<!-- lb start -->
| Model | Ave. | chabsa | cma_basics | cpa_audit | fp2 | security_sales_1 |
| --- | --- | --- | --- | --- | --- | --- |
| openai/gpt-4-32k | 66.27 | 93.16 | 81.58 | 37.44 | 50.74 | 68.42 |
| openai/gpt-4 | 66.07 | 93.20 | 78.95 | 37.69 | 50.32 | 70.18 |
| openai/gpt-4-turbo | 64.59 | 92.86 | 76.32 | 36.18 | 50.95 | 66.67 |
| openai/gpt-35-turbo | 50.27 | 89.98 | 52.63 | 18.09 | 29.26 | 61.40 |
| [meta-llama/Llama-2-70b-hf](https://huggingface.co/meta-llama/Llama-2-70b-hf) | 50.21 | 89.37 | 57.89 | 20.85 | 30.32 | 52.63 |
| [meta-llama/Llama-2-70b-chat-hf](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) | 49.53 | 90.29 | 52.63 | 18.84 | 28.00 | 57.89 |
| [Xwin-LM/Xwin-LM-13B-V0.2](https://huggingface.co/Xwin-LM/Xwin-LM-13B-V0.2) | 47.53 | 88.11 | 52.63 | 22.11 | 25.68 | 49.12 |
| [meta-llama/Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) | 46.98 | 87.95 | 52.63 | 19.60 | 27.37 | 47.37 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) | 46.04 | 82.52 | 44.74 | 17.84 | 30.74 | 54.39 |
| [lmsys/vicuna-13b-v1.5-16k](https://huggingface.co/lmsys/vicuna-13b-v1.5-16k) | 45.57 | 85.81 | 52.63 | 19.10 | 28.21 | 42.11 |
| [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) | 44.86 | 83.70 | 39.47 | 20.35 | 29.89 | 50.88 |
| [llm-jp/llm-jp-13b-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0) | 44.66 | 85.91 | 39.47 | 20.10 | 26.95 | 50.88 |
| [meta-llama/Llama-2-13b-hf](https://huggingface.co/meta-llama/Llama-2-13b-hf) | 44.19 | 82.04 | 36.84 | 20.85 | 30.32 | 50.88 |
| [llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0) | 43.76 | 83.23 | 39.47 | 19.60 | 27.37 | 49.12 |
| [rinna/youri-7b-chat](https://huggingface.co/rinna/youri-7b-chat) | 43.67 | 86.67 | 36.84 | 19.60 | 26.11 | 49.12 |
| [cyberagent/calm2-7b-chat](https://huggingface.co/cyberagent/calm2-7b-chat) | 43.67 | 81.09 | 36.84 | 18.09 | 29.68 | 52.63 |
| [llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0) | 43.60 | 86.83 | 39.47 | 18.59 | 24.00 | 49.12 |
| [lmsys/vicuna-33b-v1.3](https://huggingface.co/lmsys/vicuna-33b-v1.3) | 43.44 | 87.81 | 34.21 | 19.60 | 28.21 | 47.37 |
| [lmsys/vicuna-7b-v1.5-16k](https://huggingface.co/lmsys/vicuna-7b-v1.5-16k) | 43.21 | 84.78 | 39.47 | 19.60 | 24.84 | 47.37 |
| [elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) | 42.99 | 83.48 | 42.11 | 19.60 | 25.89 | 43.86 |
| [pfnet/plamo-13b](https://huggingface.co/pfnet/plamo-13b) | 42.87 | 76.97 | 39.47 | 21.61 | 27.16 | 49.12 |
| [stabilityai/japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) | 42.73 | 78.74 | 34.21 | 19.10 | 30.74 | 50.88 |
| [Xwin-LM/Xwin-LM-7B-V0.2](https://huggingface.co/Xwin-LM/Xwin-LM-7B-V0.2) | 42.73 | 82.79 | 42.11 | 19.85 | 25.05 | 43.86 |
| [llm-jp/llm-jp-13b-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0) | 42.39 | 81.24 | 39.47 | 19.10 | 26.53 | 45.61 |
| [cyberagent/calm2-7b](https://huggingface.co/cyberagent/calm2-7b) | 41.96 | 80.02 | 42.11 | 17.84 | 24.21 | 45.61 |
| [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) | 41.89 | 74.71 | 44.74 | 20.60 | 23.79 | 45.61 |
| [rinna/youri-7b](https://huggingface.co/rinna/youri-7b) | 41.84 | 73.60 | 34.21 | 19.10 | 29.68 | 52.63 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) | 41.59 | 82.53 | 39.47 | 20.10 | 25.47 | 40.35 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b) | 41.43 | 78.94 | 34.21 | 19.35 | 23.79 | 50.88 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2) | 41.36 | 78.62 | 34.21 | 19.10 | 24.00 | 50.88 |
| [pfnet/plamo-13b-instruct](https://huggingface.co/pfnet/plamo-13b-instruct) | 41.13 | 77.33 | 39.47 | 21.11 | 27.37 | 40.35 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) | 41.03 | 75.36 | 39.47 | 19.10 | 27.37 | 43.86 |
| [meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf) | 40.99 | 77.41 | 39.47 | 18.59 | 27.37 | 42.11 |
| [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) | 40.71 | 78.38 | 31.58 | 20.60 | 27.37 | 45.61 |
| [rinna/bilingual-gpt-neox-4b-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft) | 40.31 | 78.23 | 34.21 | 19.35 | 25.89 | 43.86 |
| [llm-jp/llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) | 39.70 | 75.48 | 36.84 | 19.85 | 24.21 | 42.11 |
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

# Citation
If you use this repository, please cite the following paper:
```
TBD
```

Or cite directory this repository:
```
@misc{Hirano2023-jlfh
    title={{Japanese Language Model Financial Evaluation Harness}},
    autors={Masanori Hirano},
    year={2023},
    url = {https://github.com/pfnet-research/japanese-lm-fin-harness}
}
```
