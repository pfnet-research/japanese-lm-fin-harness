MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-7b-instruct"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.2,cpa_audit,security_sales_1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "2,2,0,3,2" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-7b-instruct/result.json"
# Estimated results: chabsa:0.8570787043192742,cma_basics:0.39473684210526316,cpa_audit:0.18592964824120603,security_sales_1:0.543859649122807,fp2:0.28
