MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-ppo"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,2,3,2" --no_cache --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-ppo/result.json"
# Estimated results: chabsa:0.74712386969307,cma_basics:0.4473684210526316,cpa_audit:0.20603015075376885,security_sales_1:0.5087719298245614,fp2:0.27157894736842103
