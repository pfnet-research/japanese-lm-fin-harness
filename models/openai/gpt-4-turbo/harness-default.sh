TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python api_models.py --model openai --model_args model=gpt-4-turbo --tasks $TASK --num_fewshot 0 --output_path "models/openai/gpt-4-turbo/result-default.json"
# azure 1106-preview = gpt-4-turbo: Data up to Apr 2023