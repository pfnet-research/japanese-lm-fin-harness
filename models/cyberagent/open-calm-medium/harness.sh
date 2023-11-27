MODEL_ARGS="pretrained=cyberagent/open-calm-medium,use_fast=True"
TASK="chabsa-1.0-0.5,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.2,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,4,3,2" --no_cache --output_path "models/cyberagent/open-calm-medium/result.json"
# Estimated results: chabsa:0.5242614422387071,cma_basics:0.39473684210526316,cpa_audit:0.20351758793969849,security_sales_1:0.5263157894736842,fp2:0.2863157894736842
