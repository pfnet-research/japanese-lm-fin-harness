MODEL_ARGS="pretrained=rinna/nekomata-7b,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit,security_sales_1-1.0-0.4,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,0,2,2" --no_cache --output_path "models/rinna/nekomata-7b/result.json"
# Estimated results: chabsa:0.7917500260983081,cma_basics:0.4473684210526316,cpa_audit:0.21608040201005024,security_sales_1:0.5964912280701754,fp2:0.32842105263157895
