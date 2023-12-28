MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-13b-fast-instruct"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit,security_sales_1-1.0-0.1.2,fp2-1.0-0.6"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,1,3,0" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct/result.json"
# Estimated results: chabsa:0.8727219174344796,cma_basics:0.42105263157894735,cpa_audit:0.18592964824120603,security_sales_1:0.5263157894736842,fp2:0.30736842105263157
