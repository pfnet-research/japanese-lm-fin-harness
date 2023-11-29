MODEL_ARGS="pretrained=cyberagent/open-calm-large,use_fast=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1-1.0-0.1,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,4,4,0,1" --no_cache --output_path "models/cyberagent/open-calm-large/result.json"
# Estimated results: chabsa:0.5177128322721404,cma_basics:0.3684210526315789,cpa_audit:0.20351758793969849,security_sales_1:0.5087719298245614,fp2:0.28421052631578947
