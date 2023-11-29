MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.6,cpa_audit-1.0-0.2,security_sales_1-1.0-0.1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,2,2,0,4" --no_cache --output_path "models/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0/result.json"
# Estimated results: chabsa:0.86826766679553,cma_basics:0.39473684210526316,cpa_audit:0.18592964824120603,security_sales_1:0.543859649122807,fp2:0.27578947368421053
