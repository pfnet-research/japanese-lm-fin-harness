MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-sft"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.3,cpa_audit-1.0-0.2,security_sales_1,fp2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,0,4,2" --no_cache --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-sft/result.json"
# Estimated results: chabsa:0.7321889023160921,cma_basics:0.39473684210526316,cpa_audit:0.20100502512562815,security_sales_1:0.5087719298245614,fp2:0.2736842105263158
