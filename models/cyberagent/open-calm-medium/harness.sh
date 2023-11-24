MODEL_ARGS="pretrained=cyberagent/open-calm-medium,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.6,security_sales_1-1.0-0.2.1,fp2-1.0-0.6"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/cyberagent/open-calm-medium/result.json"
# Estimated results: chabsa:0.34045934851397286,cma_basics:0.2894736842105263,cpa_audit:0.19597989949748743,security_sales_1:0.49122807017543857,fp2:0.24421052631578946
