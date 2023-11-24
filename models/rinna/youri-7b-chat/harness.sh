MODEL_ARGS="pretrained=rinna/youri-7b-chat,load_in_8bit=True"
TASK="chabsa,cma_basics-1.0-0.1,cpa_audit-1.0-0.4,security_sales_1-1.0-0.1,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/youri-7b-chat/result.json"
# Estimated results: chabsa:0.579614321326877,cma_basics:0.42105263157894735,cpa_audit:0.1934673366834171,security_sales_1:0.5087719298245614,fp2:0.30526315789473685
