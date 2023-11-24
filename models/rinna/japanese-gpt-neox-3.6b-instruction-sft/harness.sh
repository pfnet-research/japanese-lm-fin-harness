MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-sft,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.3,cpa_audit-1.0-0.2,security_sales_1-1.0-0.5,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-sft/result.json"
# Estimated results: chabsa:0.4775162886950737,cma_basics:0.3684210526315789,cpa_audit:0.20100502512562815,security_sales_1:0.49122807017543857,fp2:0.25684210526315787
