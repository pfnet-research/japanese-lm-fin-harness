MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b-instruction-sft,trust_remote_code=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1-1.0-0.3,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,2,4,3" --no_cache --output_path "models/line-corporation/japanese-large-lm-1.7b-instruction-sft/result.json"
# Estimated results: chabsa:0.5521598475179808,cma_basics:0.39473684210526316,cpa_audit:0.18341708542713567,security_sales_1:0.5087719298245614,fp2:0.27157894736842103
