MODEL_ARGS="pretrained=cyberagent/calm2-7b,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1.2,fp2-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/cyberagent/calm2-7b/result.json"
# Estimated results: chabsa:0.5102274267039738,cma_basics:0.39473684210526316,cpa_audit:0.16834170854271358,security_sales_1:0.5614035087719298,fp2:0.25894736842105265
