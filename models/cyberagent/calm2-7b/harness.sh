MODEL_ARGS="pretrained=cyberagent/calm2-7b,use_fast=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2,security_sales_1-1.0-0.2.1,fp2-1.0-0.5"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,4,4,0,2" --no_cache --output_path "models/cyberagent/calm2-7b/result.json"
# Estimated results: chabsa:0.800173273539309,cma_basics:0.42105263157894735,cpa_audit:0.19095477386934673,security_sales_1:0.5263157894736842,fp2:0.29473684210526313
