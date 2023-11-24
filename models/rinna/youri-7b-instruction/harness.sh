MODEL_ARGS="pretrained=rinna/youri-7b-instruction,load_in_8bit=True"
TASK="chabsa-1.0-0.3,cma_basics-1.0-0.6,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.2,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/youri-7b-instruction/result.json"
# Estimated results: chabsa:0.5622732069222228,cma_basics:0.34210526315789475,cpa_audit:0.20351758793969849,security_sales_1:0.5263157894736842,fp2:0.2863157894736842
