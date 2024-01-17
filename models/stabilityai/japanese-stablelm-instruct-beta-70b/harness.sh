MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-instruct-beta-70b,trust_remote_code=True,use_accelerate=True,device_map_option=auto"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.3,cpa_audit,security_sales_1-1.0-0.1.2,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,4,2,3,4" --no_cache --output_path "models/stabilityai/japanese-stablelm-instruct-beta-70b/result.json"
# Estimated results: chabsa:0.9184625118262304,cma_basics:0.6052631578947368,cpa_audit:0.228643216080402,security_sales_1:0.5789473684210527,fp2:0.37473684210526315
