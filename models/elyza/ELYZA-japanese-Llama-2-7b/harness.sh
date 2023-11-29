MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-7b"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.2,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.1.2,fp2-1.0-0.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "2,4,2,3,0" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-7b/result.json"
# Estimated results: chabsa:0.8350953577875555,cma_basics:0.42105263157894735,cpa_audit:0.1984924623115578,security_sales_1:0.5263157894736842,fp2:0.29473684210526313
