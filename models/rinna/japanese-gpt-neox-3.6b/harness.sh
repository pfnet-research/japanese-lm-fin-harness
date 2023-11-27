MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2,cpa_audit-1.0-0.2,security_sales_1,fp2-1.0-0.6"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,2,4,4,4" --no_cache --output_path "models/rinna/japanese-gpt-neox-3.6b/result.json"
# Estimated results: chabsa:0.5374957437461074,cma_basics:0.39473684210526316,cpa_audit:0.22110552763819097,security_sales_1:0.543859649122807,fp2:0.2694736842105263
