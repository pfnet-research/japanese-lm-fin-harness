TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
pip install tiktoken==0.7.0
python api_models.py --model openai --model_args model=gpt-4o --tasks $TASK --num_fewshot 0 --output_path "models/openai/gpt-4o/result-default.json" --use_cache ./cache/gpt-4o/
# azure model 2024-05-13