MODEL_ARGS="pretrained=pfnet/plamo-13b-instruct-nc,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.3,cpa_audit-1.0-0.6,security_sales_1-1.0-0.2,fp2-1.0-0.6"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/pfnet/plamo-13b-instruct-nc/result.json"
# Estimated results: chabsa:0.47240811598714205,cma_basics:0.34210526315789475,cpa_audit:0.16331658291457288,security_sales_1:0.47368421052631576,fp2:0.26105263157894737
