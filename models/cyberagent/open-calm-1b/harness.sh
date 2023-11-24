MODEL_ARGS="pretrained=cyberagent/open-calm-1b,use_fast=True,load_in_8bit=True"
TASK="chabsa,cma_basics,cpa_audit-1.0-0.6,security_sales_1-1.0-0.5,fp2-1.0-0.4"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/cyberagent/open-calm-1b/result.json"
# Estimated results: chabsa:0.3695709484473828,cma_basics:0.2631578947368421,cpa_audit:0.20603015075376885,security_sales_1:0.5263157894736842,fp2:0.25684210526315787
