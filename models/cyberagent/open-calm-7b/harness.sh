MODEL_ARGS="pretrained=cyberagent/open-calm-7b,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1,cpa_audit-1.0-0.1,security_sales_1-1.0-0.1,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.23963949019933095,cma_basics:0.2631578947368421,cpa_audit:0.13819095477386933,security_sales_1:0.42105263157894735,fp2:0.24
