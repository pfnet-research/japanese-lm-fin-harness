MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-7b-fast-instruct"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.1.2,security_sales_1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,2,0,3,4" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct/result.json"
# Estimated results: chabsa:0.8252203269782445,cma_basics:0.39473684210526316,cpa_audit:0.20100502512562815,security_sales_1:0.543859649122807,fp2:0.28842105263157897
