MODEL_ARGS="pretrained=pfnet/plamo-13b,trust_remote_code=True"
TASK="chabsa-1.0-0.4,cma_basics-1.0-0.4,cpa_audit-1.0-0.6,security_sales_1-1.0-0.1,fp2-1.0-0.6"
python main.py --model hf-causal --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,2,1,1" --no_cache --output_path "models/pfnet/plamo-13b/result.json"
# Estimated results: chabsa:0.7696752080017737,cma_basics:0.39473684210526316,cpa_audit:0.21608040201005024,security_sales_1:0.49122807017543857,fp2:0.27157894736842103
