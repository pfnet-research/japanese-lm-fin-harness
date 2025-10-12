TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python api_models.py --model self-hosted-chat-1 --model_args "model=plamo-2.1-prime" --tasks $TASK --num_fewshot 0 --output_path "models/pfnet/plamo-2.1-prime/result-default.json"
# as of 2024/08/06
