TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python api_models.py --model vertexai --model_args model=gemini-1.5-flash-preview-0514 --tasks $TASK --num_fewshot 0 --output_path "models/gemini/gemini-1.5-flash/result-default.json" --use_cache ./cache/gemini-1.5-flash/
