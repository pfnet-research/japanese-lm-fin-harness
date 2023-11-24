# Japanese Language Model Financial Evaluation Harness
This is a harness for Japanese language model evaluation in the financial domain.

## Leaderboard
<!-- lb start -->
| Model | Ave. | chabsa | cma_basics | cpa_audit | fp2 | security_sales_1 |
| --- | --- | --- | --- | --- | --- | --- |
| [meta-llama/Llama-2-70b-hf](https://huggingface.co/meta-llama/Llama-2-70b-hf) | 41.68 | 54.05 | 47.37 | 18.84 | 32.00 | 56.14 |
| [meta-llama/Llama-2-70b-chat-hf](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) | 41.58 | 58.81 | 42.11 | 19.35 | 28.00 | 59.65 |
| [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) | 39.08 | 55.77 | 42.11 | 19.35 | 29.05 | 49.12 |
| [rinna/youri-7b-instruction](https://huggingface.co/rinna/youri-7b-instruction) | 37.89 | 56.26 | 31.58 | 20.35 | 28.63 | 52.63 |
| [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) | 35.88 | 49.70 | 39.47 | 18.84 | 24.00 | 47.37 |
| [meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf) | 34.87 | 51.59 | 34.21 | 13.32 | 26.11 | 49.12 |
| [pfnet/plamo-13b](https://huggingface.co/pfnet/plamo-13b) | 34.79 | 51.41 | 34.21 | 14.57 | 24.63 | 49.12 |
| [meta-llama/Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) | 34.78 | 45.40 | 39.47 | 17.09 | 26.32 | 45.61 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft) | 34.78 | 48.02 | 34.21 | 18.59 | 25.68 | 47.37 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) | 34.76 | 50.21 | 28.95 | 18.59 | 26.95 | 49.12 |
| [rinna/youri-7b](https://huggingface.co/rinna/youri-7b) | 34.68 | 48.70 | 34.21 | 14.57 | 25.05 | 50.88 |
| [llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0) | 34.67 | 53.50 | 31.58 | 16.08 | 24.84 | 47.37 |
| [llm-jp/llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) | 34.57 | 41.65 | 36.84 | 18.34 | 23.37 | 52.63 |
| [meta-llama/Llama-2-13b-hf](https://huggingface.co/meta-llama/Llama-2-13b-hf) | 34.42 | 45.27 | 31.58 | 11.31 | 27.79 | 56.14 |
| [stabilityai/japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) | 33.94 | 44.73 | 28.95 | 17.34 | 27.79 | 50.88 |
| [matsuo-lab/weblab-10b](https://huggingface.co/matsuo-lab/weblab-10b) | 33.93 | 51.84 | 31.58 | 17.09 | 25.26 | 43.86 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b) | 33.78 | 48.39 | 28.95 | 18.09 | 26.11 | 47.37 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2) | 33.51 | 47.03 | 31.58 | 18.34 | 26.74 | 43.86 |
| [cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 32.56 | 32.15 | 31.58 | 18.09 | 24.84 | 56.14 |
| [cyberagent/calm2-7b](https://huggingface.co/cyberagent/calm2-7b) | 32.53 | 50.91 | 26.32 | 16.08 | 25.47 | 43.86 |
| [line-corporation/japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) | 31.61 | 43.25 | 26.32 | 17.59 | 25.26 | 45.61 |
| [line-corporation/japanese-large-lm-1.7b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft) | 31.10 | 36.99 | 28.95 | 15.58 | 24.84 | 49.12 |
| [line-corporation/japanese-large-lm-3.6b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft) | 31.08 | 37.89 | 28.95 | 17.84 | 28.63 | 42.11 |
| [cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large) | 30.82 | 34.67 | 31.58 | 17.59 | 24.63 | 45.61 |
| [cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) | 30.64 | 32.39 | 28.95 | 18.34 | 24.42 | 49.12 |
| [cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small) | 30.21 | 33.50 | 26.32 | 17.09 | 25.05 | 49.12 |
| [cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) | 30.01 | 36.17 | 23.68 | 18.84 | 24.00 | 47.37 |
| [line-corporation/japanese-large-lm-1.7b](https://huggingface.co/line-corporation/japanese-large-lm-1.7b) | 29.44 | 34.97 | 26.32 | 17.84 | 24.21 | 43.86 |
| [cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) | 26.04 | 23.96 | 26.32 | 13.82 | 24.00 | 42.11 |
| [cyberagent/calm2-7b-chat](https://huggingface.co/cyberagent/calm2-7b-chat) | 26.04 | 23.96 | 26.32 | 13.82 | 24.00 | 42.11 |
| [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) | 26.04 | 23.96 | 26.32 | 13.82 | 24.00 | 42.11 |
| [rinna/bilingual-gpt-neox-4b-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft) | 26.04 | 23.96 | 26.32 | 13.82 | 24.00 | 42.11 |
| [rinna/japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) | 26.04 | 23.96 | 26.32 | 13.82 | 24.00 | 42.11 |
| [llm-jp/llm-jp-13b-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0) | 26.04 | 23.96 | 26.32 | 13.82 | 24.00 | 42.11 |
<!-- lb end -->

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
    year={2024},
    url = {https://github.com/pfnet-research/japanese-lm-fin-harness}
}
```
