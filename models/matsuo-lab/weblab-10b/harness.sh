MODEL_ARGS="pretrained=matsuo-lab/weblab-10b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1-1.0-0.1,fp2-1.0-0.1.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.5184026766699211,cma_basics:0.3157894736842105,cpa_audit:0.1708542713567839,security_sales_1:0.43859649122807015,fp2:0.25263157894736843
