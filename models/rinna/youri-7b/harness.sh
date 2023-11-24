MODEL_ARGS="pretrained=rinna/youri-7b,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.1,security_sales_1-1.0-0.1,fp2-1.0-0.4"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/youri-7b/result.json"
# Estimated results: chabsa:0.4883357870843432,cma_basics:0.34210526315789475,cpa_audit:0.15577889447236182,security_sales_1:0.5087719298245614,fp2:0.2736842105263158
