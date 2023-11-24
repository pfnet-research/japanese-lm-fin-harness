MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-v1.0,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.6,cpa_audit-1.0-0.4,security_sales_1-1.0-0.1,fp2-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/llm-jp/llm-jp-13b-v1.0/result.json"
# Estimated results: chabsa:0.5222048411163065,cma_basics:0.34210526315789475,cpa_audit:0.1457286432160804,security_sales_1:0.5087719298245614,fp2:0.2463157894736842
