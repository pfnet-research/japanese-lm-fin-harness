MODEL_ARGS="pretrained=rinna/youri-7b-chat"
TASK="chabsa,cma_basics-1.0-0.1,cpa_audit,security_sales_1-1.0-0.3,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,2,1,0" --no_cache --output_path "models/rinna/youri-7b-chat/result.json"
# Estimated results: chabsa:0.8662833666534813,cma_basics:0.3684210526315789,cpa_audit:0.19095477386934673,security_sales_1:0.5614035087719298,fp2:0.29894736842105263
