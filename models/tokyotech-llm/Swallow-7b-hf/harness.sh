MODEL_ARGS="pretrained=tokyotech-llm/Swallow-7b-hf"
TASK="chabsa-1.0-0.5,cma_basics,cpa_audit-1.0-0.2.1,security_sales_1,fp2-1.0-0.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,3,4,4" --no_cache --output_path "models/tokyotech-llm/Swallow-7b-hf/result.json"
# Estimated results: chabsa:0.7226681189785884,cma_basics:0.39473684210526316,cpa_audit:0.19597989949748743,security_sales_1:0.543859649122807,fp2:0.2968421052631579
