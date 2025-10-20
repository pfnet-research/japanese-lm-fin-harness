TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
pip install "tiktoken>=0.7.0"
python api_models.py --model azure-openai --model_args model=gpt-4o-mini-2024-07-18 --tasks $TASK --num_fewshot 0 --output_path "models/openai/gpt-4o-mini/result-default.json" --use_cache ./cache/gpt-4o-mini/
# azure model 2024-07-18