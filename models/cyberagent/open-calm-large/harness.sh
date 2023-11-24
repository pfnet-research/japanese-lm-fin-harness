MODEL_ARGS="pretrained=cyberagent/open-calm-large,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.5,security_sales_1-1.0-0.1,fp2-1.0-0.5"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/cyberagent/open-calm-large/result.json"
# Estimated results: chabsa:0.3481583891531918,cma_basics:0.34210526315789475,cpa_audit:0.1934673366834171,security_sales_1:0.5087719298245614,fp2:0.25263157894736843
