export OPENAI_API_BASE=""
export OPENAI_API_KEY=""
export OPENAI_API_VERSION="none"
TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python api_models.py --model self-hosted-chat-1 --model_args model=plamo-1.0-prime-beta --tasks $TASK --num_fewshot 0 --output_path "models/pfnet/plamo-1.0-prime-beta/result-default.json"
# as of 2024/08/06
