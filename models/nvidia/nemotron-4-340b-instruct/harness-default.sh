export OPENAI_API_BASE="https://integrate.api.nvidia.com/v1"
export OPENAI_API_KEY="nvapi-"
export OPENAI_API_VERSION="none"
TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python api_models.py --model self-hosted-chat-1 --model_args model=nvidia/nemotron-4-340b-instruct --tasks $TASK --num_fewshot 0 --output_path "models/nvidia/nemotron-4-340b-instruct/result-default.json"  --use_cache ./cache/nemotron-4-340b-instruct/
