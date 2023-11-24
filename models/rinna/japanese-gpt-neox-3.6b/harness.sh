MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.2,cpa_audit-1.0-0.3,security_sales_1-1.0-0.3,fp2-1.0-0.4"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/japanese-gpt-neox-3.6b/result.json"
# Estimated results: chabsa:0.34772935307011327,cma_basics:0.3684210526315789,cpa_audit:0.16834170854271358,security_sales_1:0.5087719298245614,fp2:0.26105263157894737
