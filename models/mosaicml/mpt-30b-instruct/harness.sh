MODEL_ARGS="pretrained=mosaicml/mpt-30b-instruct,use_accelerate=True,device_map_option=auto,trust_remote_code=True"
TASK="chabsa-1.0-0.3,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.4,security_sales_1-1.0-0.2.1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,2,1,4" --no_cache --output_path "models/mosaicml/mpt-30b-instruct/result.json"
# Estimated results: chabsa:0.8327466401954796,cma_basics:0.42105263157894735,cpa_audit:0.2135678391959799,security_sales_1:0.6491228070175439,fp2:0.3178947368421053
