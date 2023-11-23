MODEL_ARGS="pretrained=cyberagent/open-calm-3b,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.6,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1,fp2-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.3277672510973066,cma_basics:0.3157894736842105,cpa_audit:0.1934673366834171,security_sales_1:0.49122807017543857,fp2:0.2505263157894737
