MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-ppo,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-ppo/result.json"
# Estimated results: chabsa:0.49581605366822723,cma_basics:0.39473684210526316,cpa_audit:0.1984924623115578,security_sales_1:0.49122807017543857,fp2:0.25684210526315787
