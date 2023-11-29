MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-instruct-full-jaster-v1.0,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.4,cpa_audit,security_sales_1-1.0-0.3,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,2,2,1,1" --no_cache --output_path "models/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0/result.json"
# Estimated results: chabsa:0.8590758377764691,cma_basics:0.39473684210526316,cpa_audit:0.20100502512562815,security_sales_1:0.5087719298245614,fp2:0.2694736842105263
