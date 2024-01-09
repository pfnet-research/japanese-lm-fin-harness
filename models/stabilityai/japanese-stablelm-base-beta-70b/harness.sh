MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-base-beta-70b,trust_remote_code=True,use_accelerate=True,device_map_option=auto"
TASK="chabsa-1.0-0.3,cma_basics-1.0-0.3,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.2,fp2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,2,2,4" --no_cache --output_path "models/stabilityai/japanese-stablelm-base-beta-70b/result.json"
# Estimated results: chabsa:0.9087199417170575,cma_basics:0.6052631578947368,cpa_audit:0.2236180904522613,security_sales_1:0.631578947368421,fp2:0.40210526315789474
