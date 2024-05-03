TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python api_models.py --model anthropic --model_args model=claude-3-opus-20240229 --tasks $TASK --num_fewshot 0 --output_path "models/anthropic/claude-3-opus/result-default.json" --limit 10  --use_cache ./cache/claude-3-opus/
