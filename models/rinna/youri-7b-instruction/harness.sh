MODEL_ARGS="pretrained=rinna/youri-7b-instruction"
TASK="chabsa-1.0-0.3,cma_basics-1.0-0.1,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1.2,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,0,0,2,0" --no_cache --output_path "models/rinna/youri-7b-instruction/result.json"
# Estimated results: chabsa:0.8692005713658217,cma_basics:0.34210526315789475,cpa_audit:0.21608040201005024,security_sales_1:0.5614035087719298,fp2:0.28
