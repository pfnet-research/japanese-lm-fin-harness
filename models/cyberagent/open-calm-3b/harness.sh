MODEL_ARGS="pretrained=cyberagent/open-calm-3b,use_fast=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.3,cpa_audit-1.0-0.5,security_sales_1-1.0-0.1,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,2,0,4" --no_cache --output_path "models/cyberagent/open-calm-3b/result.json"
# Estimated results: chabsa:0.5606049857077943,cma_basics:0.3684210526315789,cpa_audit:0.19597989949748743,security_sales_1:0.543859649122807,fp2:0.28
