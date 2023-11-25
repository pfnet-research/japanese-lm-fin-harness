MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-3.6b-instruction-sft,trust_remote_code=True"
TASK="chabsa,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2,security_sales_1-1.0-0.2,fp2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,1,2,4,0" --output_path "models/line-corporation/japanese-large-lm-3.6b-instruction-sft/result.json"
# Estimated results: chabsa:0.3986313841508314,cma_basics:0.3684210526315789,cpa_audit:0.21608040201005024,security_sales_1:0.49122807017543857,fp2:0.30526315789473685
