MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.4,cma_basics-1.0-0.5,cpa_audit-1.0-0.1,security_sales_1-1.0-0.1,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.3553951052549831,cma_basics:0.2894736842105263,cpa_audit:0.17839195979899497,security_sales_1:0.43859649122807015,fp2:0.24210526315789474
