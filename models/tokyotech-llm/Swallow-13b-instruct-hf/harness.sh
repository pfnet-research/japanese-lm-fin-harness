MODEL_ARGS="pretrained=tokyotech-llm/Swallow-13b-instruct-hf"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.1.2,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,2,3,3" --no_cache --output_path "models/tokyotech-llm/Swallow-13b-instruct-hf/result.json"
# Estimated results: chabsa:0.877945713498328,cma_basics:0.6052631578947368,cpa_audit:0.19597989949748743,security_sales_1:0.5789473684210527,fp2:0.35789473684210527
