MODEL_ARGS="pretrained=abeja/gpt-neox-japanese-2.7b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.1,security_sales_1-1.0-0.2,fp2-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.33410834433047915,cma_basics:0.3157894736842105,cpa_audit:0.18341708542713567,security_sales_1:0.49122807017543857,fp2:0.2694736842105263
