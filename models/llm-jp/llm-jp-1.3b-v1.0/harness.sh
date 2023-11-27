MODEL_ARGS="pretrained=llm-jp/llm-jp-1.3b-v1.0,trust_remote_code=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.2.1,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,0,4,0,2" --no_cache --output_path "models/llm-jp/llm-jp-1.3b-v1.0/result.json"
# Estimated results: chabsa:0.7548311660553979,cma_basics:0.3684210526315789,cpa_audit:0.1984924623115578,security_sales_1:0.5263157894736842,fp2:0.27578947368421053
