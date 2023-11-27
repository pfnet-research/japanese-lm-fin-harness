MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b,trust_remote_code=True"
TASK="chabsa-1.0-0.4,cma_basics-1.0-0.2,cpa_audit-1.0-0.1,security_sales_1-1.0-0.2.1,fp2-1.0-0.5"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,4,2,2" --no_cache --output_path "models/line-corporation/japanese-large-lm-1.7b/result.json"
# Estimated results: chabsa:0.542972743672392,cma_basics:0.42105263157894735,cpa_audit:0.19597989949748743,security_sales_1:0.5087719298245614,fp2:0.28421052631578947
