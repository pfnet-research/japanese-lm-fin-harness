MODEL_ARGS="pretrained=pfnet/plamo-13b-instruct,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.6,security_sales_1-1.0-0.2.1,fp2-1.0-0.5"
python main.py --model hf-causal --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,3,2,1,4" --no_cache --output_path "models/pfnet/plamo-13b-instruct/result.json"
# Estimated results: chabsa:0.7732757491525104,cma_basics:0.39473684210526316,cpa_audit:0.21105527638190955,security_sales_1:0.5087719298245614,fp2:0.28210526315789475
