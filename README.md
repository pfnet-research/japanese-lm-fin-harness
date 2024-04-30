# Japanese Language Model Financial Evaluation Harness
This is a harness for Japanese language model evaluation in the financial domain.

## 0-shot Leaderboard
<!-- lb start -->
| Model | Ave. | chabsa | cma_basics | cpa_audit | fp2 | security_sales_1 | prompt | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| openai/gpt-4-32k | 66.27 | 93.16 | 81.58 | 37.44 | 50.74 | 68.42 | default |
| openai/gpt-4 | 66.07 | 93.20 | 78.95 | 37.69 | 50.32 | 70.18 | default |
| openai/gpt-4-turbo | 64.59 | 92.86 | 76.32 | 36.18 | 50.95 | 66.67 | default |
| [Qwen/Qwen-72B](https://huggingface.co/Qwen/Qwen-72B) | 59.08 | 89.46 | 76.32 | 28.64 | 39.58 | 61.40 | 1.0-0.1.2 |
| [Qwen/Qwen1.5-72B](https://huggingface.co/Qwen/Qwen1.5-72B) | 58.82 | 90.77 | 71.05 | 26.38 | 37.47 | 68.42 | 1.0-0.1 |
| [meta-llama/Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) | 58.48 | 90.61 | 76.32 | 29.90 | 42.95 | 52.63 | 1.0-0.2.1 |
| [tokyotech-llm/Swallow-70b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-instruct-hf) | 58.32 | 90.72 | 63.16 | 21.11 | 53.47 | 63.16 | default |
| [Qwen/Qwen-72B-Chat](https://huggingface.co/Qwen/Qwen-72B-Chat) | 57.33 | 92.10 | 71.05 | 25.38 | 40.21 | 57.89 | 1.0-0.1.2 |
| [meta-llama/Meta-Llama-3-70B](https://huggingface.co/meta-llama/Meta-Llama-3-70B) | 56.87 | 90.19 | 73.68 | 24.87 | 37.68 | 57.89 | 1.0-0.1.2 |
| [tokyotech-llm/Swallow-70b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-hf) | 56.26 | 86.42 | 60.53 | 20.10 | 52.84 | 61.40 | default |
| [tokyotech-llm/Swallow-70b-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-hf) | 54.86 | 89.28 | 68.42 | 19.85 | 45.89 | 50.88 | default |
| [Qwen/Qwen1.5-32B-Chat](https://huggingface.co/Qwen/Qwen1.5-32B-Chat) | 54.51 | 91.52 | 57.89 | 25.38 | 38.11 | 59.65 | 1.0-0.1.2 |
| [tokyotech-llm/Swallow-70b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-hf) | 54.46 | 91.36 | 65.79 | 20.35 | 45.68 | 49.12 | default |
| [tokyotech-llm/Swallow-MX-8x7b-NVE-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MX-8x7b-NVE-v0.1) | 53.50 | 88.64 | 65.79 | 20.10 | 31.58 | 61.40 | 1.0-0.1.2 |
| [Qwen/Qwen1.5-32B](https://huggingface.co/Qwen/Qwen1.5-32B) | 53.34 | 91.37 | 68.42 | 27.89 | 29.89 | 49.12 | default |
| [Qwen/Qwen1.5-14B-Chat](https://huggingface.co/Qwen/Qwen1.5-14B-Chat) | 52.82 | 90.43 | 57.89 | 25.63 | 35.79 | 54.39 | 1.0-0.1.2 |
| [pfnet/nekomata-14b-pfn-qfin](https://huggingface.co/pfnet/nekomata-14b-pfn-qfin) | 52.74 | 88.87 | 47.37 | 25.13 | 39.16 | 63.16 | 1.0-0.2.1 |
| [Qwen/Qwen1.5-14B](https://huggingface.co/Qwen/Qwen1.5-14B) | 52.20 | 84.55 | 65.79 | 20.60 | 33.89 | 56.14 | 1.0-0.1.2 |
| [pfnet/nekomata-14b-pfn-qfin-inst-merge](https://huggingface.co/pfnet/nekomata-14b-pfn-qfin-inst-merge) | 51.12 | 88.93 | 50.00 | 24.62 | 37.68 | 54.39 | 1.0-0.2.1 |
| [rinna/nekomata-14b-instruction](https://huggingface.co/rinna/nekomata-14b-instruction) | 50.91 | 89.40 | 52.63 | 20.35 | 36.00 | 56.14 | 1.0-0.2.1 |
| [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) | 50.63 | 91.02 | 57.89 | 24.37 | 30.74 | 49.12 | 1.0-0.2 |
| [rinna/nekomata-14b](https://huggingface.co/rinna/nekomata-14b) | 50.46 | 85.88 | 63.16 | 20.60 | 31.79 | 50.88 | 1.0-0.1.2 |
| [Qwen/Qwen-14B](https://huggingface.co/Qwen/Qwen-14B) | 50.30 | 86.14 | 63.16 | 19.10 | 32.21 | 50.88 | 1.0-0.1.2 |
| openai/gpt-35-turbo | 50.27 | 89.98 | 52.63 | 18.09 | 29.26 | 61.40 | default |
| [Qwen/Qwen1.5-7B-Chat](https://huggingface.co/Qwen/Qwen1.5-7B-Chat) | 49.73 | 86.27 | 50.00 | 24.87 | 31.37 | 56.14 | 1.0-0.2.1 |
| [Qwen/Qwen-14B-Chat](https://huggingface.co/Qwen/Qwen-14B-Chat) | 49.13 | 91.03 | 55.26 | 16.83 | 29.89 | 52.63 | default |
| [rinna/nekomata-7b-instruction](https://huggingface.co/rinna/nekomata-7b-instruction) | 47.75 | 86.71 | 44.74 | 17.34 | 30.32 | 59.65 | default |
| [Qwen/Qwen1.5-MoE-A2.7B-Chat](https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B-Chat) | 46.64 | 82.10 | 42.11 | 22.86 | 28.21 | 57.89 | 1.0-0.1 |
| [Qwen/Qwen-7B](https://huggingface.co/Qwen/Qwen-7B) | 45.99 | 82.30 | 47.37 | 19.60 | 31.58 | 49.12 | 1.0-0.1.2 |
| [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) | 45.80 | 87.59 | 39.47 | 17.84 | 29.68 | 54.39 | default |
| [Qwen/Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat) | 45.33 | 85.40 | 47.37 | 19.85 | 28.42 | 45.61 | 1.0-0.1.2 |
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | 44.70 | 86.77 | 39.47 | 16.83 | 33.05 | 47.37 | 1.0-0.2.1 |
| [karakuri-ai/karakuri-lm-70b-chat-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-chat-v0.1) | 44.59 | 88.59 | 36.84 | 18.09 | 30.32 | 49.12 | 1.0-0.2.1 |
| [mistralai/Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) | 44.29 | 89.39 | 42.11 | 15.58 | 25.26 | 49.12 | default |
| [meta-llama/Llama-2-70b-chat-hf](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) | 44.23 | 85.67 | 44.74 | 17.09 | 26.32 | 47.37 | 1.0-0.1 |
| [Qwen/Qwen1.5-7B](https://huggingface.co/Qwen/Qwen1.5-7B) | 43.99 | 85.54 | 39.47 | 18.09 | 29.47 | 47.37 | 1.0-0.1.2 |
| [Qwen/Qwen1.5-MoE-A2.7B](https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B) | 43.12 | 69.29 | 42.11 | 21.61 | 28.21 | 54.39 | 1.0-0.1 |
| [Qwen/Qwen1.5-4B](https://huggingface.co/Qwen/Qwen1.5-4B) | 42.68 | 82.82 | 42.11 | 13.82 | 29.05 | 45.61 | 1.0-0.1.2 |
| [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) | 42.13 | 85.77 | 36.84 | 19.85 | 26.11 | 42.11 | default |
| [meta-llama/Llama-2-70b-hf](https://huggingface.co/meta-llama/Llama-2-70b-hf) | 41.96 | 84.07 | 34.21 | 16.83 | 29.05 | 45.61 | 1.0-0.1.2 |
| [cyberagent/calm2-7b-chat-dpo-experimental](https://huggingface.co/cyberagent/calm2-7b-chat-dpo-experimental) | 41.71 | 77.96 | 34.21 | 15.83 | 29.68 | 50.88 | 1.0-0.1 |
| [rinna/nekomata-7b](https://huggingface.co/rinna/nekomata-7b) | 41.55 | 81.34 | 31.58 | 20.85 | 24.84 | 49.12 | default |
| [stabilityai/japanese-stablelm-instruct-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-gamma-7b) | 41.46 | 79.09 | 31.58 | 17.34 | 33.68 | 45.61 | 1.0-0.2.1 |
| [tokyotech-llm/Swallow-MS-7b-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MS-7b-v0.1) | 41.37 | 79.22 | 23.68 | 17.09 | 25.47 | 61.40 | 1.0-0.2.1 |
| [llm-jp/llm-jp-13b-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0) | 41.36 | 84.48 | 34.21 | 21.11 | 23.16 | 43.86 | 1.0-0.1 |
| [Qwen/Qwen1.5-4B-Chat](https://huggingface.co/Qwen/Qwen1.5-4B-Chat) | 41.26 | 78.40 | 39.47 | 13.57 | 29.26 | 45.61 | 1.0-0.1.2 |
| [llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0) | 41.10 | 82.28 | 28.95 | 13.57 | 26.32 | 54.39 | 1.0-0.3 |
| [karakuri-ai/karakuri-lm-70b-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-v0.1) | 41.04 | 58.60 | 39.47 | 18.09 | 31.16 | 57.89 | default |
| [tokyotech-llm/Swallow-7b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-hf) | 41.03 | 81.34 | 39.47 | 20.10 | 27.37 | 36.84 | 1.0-0.1 |
| [mosaicml/mpt-30b-instruct](https://huggingface.co/mosaicml/mpt-30b-instruct) | 40.95 | 83.25 | 34.21 | 19.60 | 27.37 | 40.35 | default |
| [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) | 40.67 | 80.32 | 28.95 | 19.85 | 23.37 | 50.88 | default |
| [elyza/ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) | 40.59 | 81.39 | 36.84 | 18.84 | 23.79 | 42.11 | default |
| [rinna/youri-7b-chat](https://huggingface.co/rinna/youri-7b-chat) | 40.40 | 85.08 | 26.32 | 17.84 | 27.16 | 45.61 | default |
| [meta-llama/Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) | 40.29 | 80.36 | 39.47 | 13.82 | 25.68 | 42.11 | 1.0-0.1 |
| [tokyotech-llm/Swallow-13b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-hf) | 40.24 | 80.08 | 42.11 | 13.82 | 24.84 | 40.35 | 1.0-0.2 |
| [stabilityai/japanese-stablelm-base-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-gamma-7b) | 40.17 | 74.80 | 31.58 | 18.34 | 30.53 | 45.61 | 1.0-0.2.1 |
| [lmsys/vicuna-7b-v1.5-16k](https://huggingface.co/lmsys/vicuna-7b-v1.5-16k) | 39.91 | 79.91 | 28.95 | 16.33 | 25.26 | 49.12 | 1.0-0.1 |
| [cyberagent/calm2-7b](https://huggingface.co/cyberagent/calm2-7b) | 39.80 | 78.27 | 31.58 | 16.58 | 26.95 | 45.61 | 1.0-0.1 |
| [elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) | 39.78 | 79.76 | 36.84 | 13.82 | 24.63 | 43.86 | default |
| [cyberagent/calm2-7b-chat](https://huggingface.co/cyberagent/calm2-7b-chat) | 39.68 | 79.97 | 31.58 | 16.83 | 24.42 | 45.61 | 1.0-0.2 |
| [tokyotech-llm/Swallow-7b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-instruct-hf) | 39.56 | 74.24 | 34.21 | 18.34 | 27.16 | 43.86 | 1.0-0.1 |
| [tokyotech-llm/Swallow-13b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-NVE-hf) | 39.49 | 60.92 | 31.58 | 15.08 | 32.00 | 57.89 | 1.0-0.1 |
| [rinna/youri-7b-instruction](https://huggingface.co/rinna/youri-7b-instruction) | 39.47 | 78.82 | 36.84 | 19.10 | 24.00 | 38.60 | 1.0-0.3 |
| [elyza/ELYZA-japanese-Llama-2-13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct) | 39.42 | 73.46 | 34.21 | 14.32 | 29.47 | 45.61 | 1.0-0.1 |
| [lmsys/vicuna-13b-v1.3](https://huggingface.co/lmsys/vicuna-13b-v1.3) | 39.20 | 78.86 | 31.58 | 16.58 | 23.37 | 45.61 | 1.0-0.2 |
| [elyza/ELYZA-japanese-Llama-2-13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct) | 39.08 | 55.28 | 47.37 | 18.84 | 26.53 | 47.37 | 1.0-0.1 |
| [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) | 38.90 | 73.66 | 34.21 | 14.07 | 26.95 | 45.61 | default |
| [mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) | 38.86 | 79.85 | 31.58 | 14.82 | 24.21 | 43.86 | default |
| [lmsys/vicuna-7b-v1.3](https://huggingface.co/lmsys/vicuna-7b-v1.3) | 38.51 | 76.81 | 23.68 | 15.08 | 26.11 | 50.88 | 1.0-0.1 |
| [elyza/ELYZA-japanese-Llama-2-13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b) | 38.43 | 76.69 | 36.84 | 14.07 | 24.21 | 40.35 | default |
| [mosaicml/mpt-30b-chat](https://huggingface.co/mosaicml/mpt-30b-chat) | 38.30 | 74.85 | 26.32 | 18.34 | 24.63 | 47.37 | default |
| [lmsys/vicuna-33b-v1.3](https://huggingface.co/lmsys/vicuna-33b-v1.3) | 38.28 | 66.31 | 26.32 | 17.59 | 25.05 | 56.14 | 1.0-0.1 |
| [rinna/bilingual-gpt-neox-4b-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft) | 38.17 | 77.67 | 23.68 | 17.59 | 26.32 | 45.61 | default |
| [stabilityai/japanese-stablelm-3b-4e1t-instruct](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-instruct) | 38.13 | 68.37 | 34.21 | 16.33 | 26.11 | 45.61 | 1.0-0.1 |
| [stabilityai/japanese-stablelm-instruct-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-ja_vocab-beta-7b) | 38.06 | 75.29 | 28.95 | 15.83 | 24.63 | 45.61 | 1.0-0.1.2 |
| [lmsys/longchat-7b-v1.5-32k](https://huggingface.co/lmsys/longchat-7b-v1.5-32k) | 37.89 | 79.53 | 31.58 | 14.07 | 25.68 | 38.60 | 1.0-0.2.1 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft) | 37.73 | 73.00 | 23.68 | 18.84 | 24.00 | 49.12 | 1.0-0.2.1 |
| openai/text-davinci-003 | 37.68 | 53.92 | 44.74 | 17.59 | 26.53 | 45.61 | default |
| [tokyotech-llm/Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) | 37.54 | 61.28 | 28.95 | 16.08 | 25.26 | 56.14 | 1.0-0.1 |
| [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) | 37.45 | 74.75 | 26.32 | 17.34 | 26.74 | 42.11 | 1.0-0.1.2 |
| [rinna/youri-7b](https://huggingface.co/rinna/youri-7b) | 37.39 | 68.04 | 31.58 | 19.85 | 27.16 | 40.35 | 1.0-0.1 |
| [mosaicml/mpt-30b](https://huggingface.co/mosaicml/mpt-30b) | 37.35 | 76.95 | 23.68 | 16.83 | 27.16 | 42.11 | 1.0-0.2.1 |
| [tokyotech-llm/Swallow-7b-plus-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-plus-hf) | 37.25 | 79.04 | 31.58 | 12.81 | 24.21 | 38.60 | 1.0-0.1.2 |
| [moneyforward/houou-instruction-7b-v3](https://huggingface.co/moneyforward/houou-instruction-7b-v3) | 37.22 | 73.42 | 26.32 | 16.58 | 25.89 | 43.86 | 1.0-0.1.2 |
| [Qwen/Qwen1.5-1.8B](https://huggingface.co/Qwen/Qwen1.5-1.8B) | 37.03 | 69.33 | 28.95 | 19.10 | 25.68 | 42.11 | 1.0-0.1 |
| [google/recurrentgemma-2b-it](https://huggingface.co/google/recurrentgemma-2b-it) | 36.94 | 61.04 | 36.84 | 17.84 | 23.37 | 45.61 | 1.0-0.2.1 |
| [google/gemma-2b](https://huggingface.co/google/gemma-2b) | 36.93 | 67.09 | 28.95 | 15.08 | 24.42 | 49.12 | 1.0-0.6 |
| [meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf) | 36.89 | 71.97 | 31.58 | 13.82 | 26.74 | 40.35 | 1.0-0.2 |
| [llm-jp/llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) | 36.81 | 57.66 | 31.58 | 18.34 | 27.37 | 49.12 | 1.0-0.1 |
| [google/gemma-1.1-2b-it](https://huggingface.co/google/gemma-1.1-2b-it) | 36.47 | 61.68 | 34.21 | 13.32 | 24.00 | 49.12 | 1.0-0.2.1 |
| [stabilityai/japanese-stablelm-base-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-7b) | 36.36 | 62.03 | 36.84 | 15.33 | 25.47 | 42.11 | 1.0-0.1.2 |
| [matsuo-lab/weblab-10b](https://huggingface.co/matsuo-lab/weblab-10b) | 36.31 | 69.82 | 31.58 | 13.82 | 24.21 | 42.11 | default |
| [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) | 36.23 | 74.15 | 23.68 | 15.33 | 25.89 | 42.11 | 1.0-0.1 |
| [google/gemma-2b-it](https://huggingface.co/google/gemma-2b-it) | 36.17 | 66.75 | 28.95 | 15.33 | 24.21 | 45.61 | 1.0-0.1 |
| [moneyforward/houou-instruction-7b-v2](https://huggingface.co/moneyforward/houou-instruction-7b-v2) | 36.15 | 72.26 | 28.95 | 14.82 | 26.11 | 38.60 | 1.0-0.1 |
| [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) | 36.06 | 68.52 | 21.05 | 17.59 | 24.00 | 49.12 | 1.0-0.2.1 |
| [stabilityai/japanese-stablelm-base-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-ja_vocab-beta-7b) | 36.02 | 63.14 | 36.84 | 13.82 | 24.21 | 42.11 | default |
| [Qwen/Qwen1.5-1.8B-Chat](https://huggingface.co/Qwen/Qwen1.5-1.8B-Chat) | 35.98 | 65.54 | 26.32 | 16.83 | 27.37 | 43.86 | 1.0-0.2 |
| [moneyforward/houou-instruction-7b-v1](https://huggingface.co/moneyforward/houou-instruction-7b-v1) | 35.45 | 66.86 | 26.32 | 16.33 | 27.37 | 40.35 | 1.0-0.1 |
| [llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0) | 35.40 | 66.91 | 23.68 | 13.07 | 24.21 | 49.12 | 1.0-0.6 |
| [lmsys/vicuna-13b-v1.5-16k](https://huggingface.co/lmsys/vicuna-13b-v1.5-16k) | 35.36 | 69.08 | 26.32 | 13.82 | 25.47 | 42.11 | 1.0-0.2 |
| [pfnet/plamo-13b-instruct](https://huggingface.co/pfnet/plamo-13b-instruct) | 35.27 | 63.10 | 26.32 | 16.08 | 25.26 | 45.61 | 1.0-0.6 |
| [tokyotech-llm/Swallow-7b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf) | 34.88 | 49.40 | 31.58 | 20.60 | 25.47 | 47.37 | default |
| [cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large) | 34.81 | 53.58 | 28.95 | 16.83 | 23.79 | 50.88 | 1.0-0.1 |
| [meta-llama/Llama-2-13b-hf](https://huggingface.co/meta-llama/Llama-2-13b-hf) | 34.75 | 56.30 | 36.84 | 13.32 | 26.95 | 40.35 | 1.0-0.2.1 |
| [stabilityai/japanese-stablelm-3b-4e1t-base](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base) | 34.58 | 52.32 | 34.21 | 15.58 | 26.95 | 43.86 | 1.0-0.1 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) | 34.49 | 37.54 | 36.84 | 17.59 | 26.11 | 54.39 | 1.0-0.1 |
| [pfnet/plamo-13b](https://huggingface.co/pfnet/plamo-13b) | 34.26 | 59.69 | 28.95 | 12.81 | 24.21 | 45.61 | 1.0-0.6 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b) | 34.20 | 53.43 | 26.32 | 15.83 | 26.32 | 49.12 | 1.0-0.3 |
| [elyza/ELYZA-japanese-Llama-2-13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast) | 34.06 | 59.12 | 31.58 | 14.82 | 24.42 | 40.35 | default |
| [rinna/bilingual-gpt-neox-4b](https://huggingface.co/rinna/bilingual-gpt-neox-4b) | 33.79 | 58.63 | 31.58 | 14.82 | 23.58 | 40.35 | 1.0-0.4 |
| [rinna/japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) | 33.57 | 45.72 | 23.68 | 14.57 | 24.21 | 59.65 | 1.0-0.5 |
| [pfnet/plamo-13b-instruct-nc](https://huggingface.co/pfnet/plamo-13b-instruct-nc) | 33.18 | 54.15 | 23.68 | 16.33 | 26.11 | 45.61 | 1.0-0.6 |
| [google/gemma-7b-it](https://huggingface.co/google/gemma-7b-it) | 32.41 | 53.15 | 26.32 | 17.34 | 23.16 | 42.11 | default |
| [llm-jp/llm-jp-13b-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0) | 32.36 | 60.76 | 21.05 | 13.07 | 24.84 | 42.11 | 1.0-0.6 |
| [elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) | 32.18 | 36.16 | 39.47 | 18.59 | 26.32 | 40.35 | 1.0-0.1.2 |
| [line-corporation/japanese-large-lm-1.7b](https://huggingface.co/line-corporation/japanese-large-lm-1.7b) | 32.10 | 46.77 | 34.21 | 13.82 | 23.58 | 42.11 | 1.0-0.4 |
| [cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) | 32.02 | 49.12 | 26.32 | 13.32 | 24.00 | 47.37 | 1.0-0.2.1 |
| [google/recurrentgemma-2b](https://huggingface.co/google/recurrentgemma-2b) | 31.84 | 49.51 | 26.32 | 15.08 | 24.42 | 43.86 | 1.0-0.6 |
| [google/gemma-7b](https://huggingface.co/google/gemma-7b) | 31.75 | 48.91 | 23.68 | 16.33 | 24.21 | 45.61 | 1.0-0.3 |
| [tokyotech-llm/Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) | 31.59 | 42.00 | 28.95 | 16.33 | 25.05 | 45.61 | 1.0-0.1 |
| [line-corporation/japanese-large-lm-1.7b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft) | 31.51 | 50.50 | 26.32 | 13.32 | 23.58 | 43.86 | 1.0-0.5 |
| [google/gemma-1.1-7b-it](https://huggingface.co/google/gemma-1.1-7b-it) | 31.36 | 36.68 | 28.95 | 17.09 | 26.74 | 47.37 | 1.0-0.2 |
| [llm-jp/llm-jp-13b-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1) | 30.87 | 42.11 | 23.68 | 18.09 | 24.84 | 45.61 | 1.0-0.4 |
| [Qwen/Qwen1.5-0.5B](https://huggingface.co/Qwen/Qwen1.5-0.5B) | 30.82 | 50.40 | 21.05 | 15.58 | 26.74 | 40.35 | 1.0-0.6 |
| [cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 30.76 | 37.49 | 26.32 | 15.33 | 23.79 | 50.88 | 1.0-0.1 |
| [stabilityai/japanese-stablelm-instruct-alpha-7b-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2) | 30.55 | 35.95 | 26.32 | 17.09 | 22.53 | 50.88 | 1.0-0.2.1 |
| [cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) | 30.46 | 30.08 | 28.95 | 16.83 | 23.79 | 52.63 | 1.0-0.1 |
| [abeja/gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 30.17 | 40.43 | 31.58 | 14.07 | 24.42 | 40.35 | 1.0-0.1.2 |
| [stabilityai/japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) | 30.16 | 35.95 | 31.58 | 16.33 | 24.84 | 42.11 | default |
| [Qwen/Qwen1.5-0.5B-Chat](https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat) | 29.98 | 36.69 | 34.21 | 15.33 | 25.05 | 38.60 | 1.0-0.1 |
| [line-corporation/japanese-large-lm-3.6b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft) | 29.54 | 35.95 | 26.32 | 14.07 | 24.00 | 47.37 | 1.0-0.2.1 |
| [line-corporation/japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) | 29.54 | 35.95 | 26.32 | 14.07 | 24.00 | 47.37 | 1.0-0.1 |
| [cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small) | 29.48 | 35.95 | 23.68 | 18.59 | 23.58 | 45.61 | 1.0-0.6 |
| [cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) | 28.80 | 37.83 | 28.95 | 13.07 | 23.79 | 40.35 | 1.0-0.4 |
<!-- lb end -->
Note: Prompt selection is not performed only for Open AI models. For Open AI models, results are counted as wrong when the content filter is applied.

Recently, we updated the evaluation policy. Please refer to the [UPDATE.md](UPDATE.md) for more details.

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
    python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "result.json"
    ```
 5. Run the script
    ```
    poetry run bash harness.sh
    ```

vllm is also supported. Please refer to model examples and lm_eval official pages.

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
@preprint{Hirano2023-pre-jfin-benchmark,
  title={{Construction of a Japanese Financial Benchmark for Large Language Models}},
  author={Masahiro Hirano},
  doi={10.2139/ssrn.4769124},
  archivePrefix={arXiv},
  arxivId={2403.15062},
  year={2024}
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
