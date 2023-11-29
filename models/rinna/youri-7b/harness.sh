MODEL_ARGS="pretrained=rinna/youri-7b"
TASK="chabsa-1.0-0.2,cma_basics,cpa_audit-1.0-0.3,security_sales_1-1.0-0.2.1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,1,3,1,1" --no_cache --output_path "models/rinna/youri-7b/result.json"
# Estimated results: chabsa:0.7352744292813791,cma_basics:0.3684210526315789,cpa_audit:0.1934673366834171,security_sales_1:0.5263157894736842,fp2:0.2968421052631579
