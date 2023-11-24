MODEL_ARGS="pretrained=pfnet/plamo-13b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.4,cma_basics-1.0-0.1,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.2.1,fp2-1.0-0.4"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/pfnet/plamo-13b/result.json"
# Estimated results: chabsa:0.517610707684293,cma_basics:0.34210526315789475,cpa_audit:0.15326633165829145,security_sales_1:0.49122807017543857,fp2:0.24842105263157896
