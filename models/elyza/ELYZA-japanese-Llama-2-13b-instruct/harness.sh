MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-13b-instruct"
TASK="chabsa-1.0-0.6,cma_basics,cpa_audit-1.0-0.2,security_sales_1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,3,3,1" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-13b-instruct/result.json"
# Estimated results: chabsa:0.8939804746249456,cma_basics:0.4473684210526316,cpa_audit:0.18592964824120603,security_sales_1:0.5789473684210527,fp2:0.3094736842105263
