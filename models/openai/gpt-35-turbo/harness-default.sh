TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python api_models.py --model openai --model_args model=gpt-35-turbo --tasks $TASK --num_fewshot 0 --output_path "models/openai/gpt-35-turbo/result-default.json"
# azure 0613: Data up to Sep 2021