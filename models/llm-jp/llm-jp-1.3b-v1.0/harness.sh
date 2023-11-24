MODEL_ARGS="pretrained=llm-jp/llm-jp-1.3b-v1.0,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1,cpa_audit-1.0-0.1,security_sales_1-1.0-0.2.1,fp2-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/llm-jp/llm-jp-1.3b-v1.0/result.json"
# Estimated results: chabsa:0.41644950709264256,cma_basics:0.39473684210526316,cpa_audit:0.18341708542713567,security_sales_1:0.543859649122807,fp2:0.24421052631578946
