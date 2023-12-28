MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-13b-fast"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "2,3,3,1,1" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-13b-fast/result.json"
# Estimated results: chabsa:0.863666340443713,cma_basics:0.39473684210526316,cpa_audit:0.20603015075376885,security_sales_1:0.5087719298245614,fp2:0.31157894736842107
