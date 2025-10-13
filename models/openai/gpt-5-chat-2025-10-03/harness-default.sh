TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
pip install tiktoken==0.7.0
python api_models.py --model azure-openai --model_args model=gpt-5-chat-2025-10-03 --tasks $TASK --num_fewshot 0 --output_path "models/openai/gpt-5-chat-2025-10-03/result-default.json" --use_cache ./cache/gpt-5-chat-2025-10-03/
