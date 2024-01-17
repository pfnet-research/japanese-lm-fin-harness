MODEL_ARGS="pretrained=Qwen/Qwen-72B,trust_remote_code=True,use_accelerate=True,device_map_option=auto"
TASK="chabsa,cma_basics-1.0-0.2,cpa_audit-1.0-0.3,security_sales_1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,3,0,0,4" --no_cache --output_path "models/Qwen/Qwen-72B/result.json"
# Estimated results: chabsa:0.9235857879413606,cma_basics:0.7894736842105263,cpa_audit:0.32914572864321606,security_sales_1:0.7192982456140351,fp2:0.45263157894736844
