MODEL_ARGS="pretrained=cyberagent/open-calm-1b,use_fast=True"
TASK="chabsa,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1-1.0-0.1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,2,4,0,1" --no_cache --output_path "models/cyberagent/open-calm-1b/result.json"
# Estimated results: chabsa:0.5736248297807955,cma_basics:0.3157894736842105,cpa_audit:0.19597989949748743,security_sales_1:0.5614035087719298,fp2:0.27789473684210525
