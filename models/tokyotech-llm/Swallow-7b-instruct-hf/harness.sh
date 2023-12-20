MODEL_ARGS="pretrained=tokyotech-llm/Swallow-7b-instruct-hf"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1.2,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,3,3,4,0" --no_cache --output_path "models/tokyotech-llm/Swallow-7b-instruct-hf/result.json"
# Estimated results: chabsa:0.8364126896511341,cma_basics:0.3157894736842105,cpa_audit:0.19095477386934673,security_sales_1:0.5614035087719298,fp2:0.29473684210526313
