MODEL_ARGS="pretrained=mosaicml/mpt-30b-chat,use_accelerate=True,device_map_option=auto,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2,security_sales_1,fp2-1.0-0.5"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,0,2,4" --no_cache --output_path "models/mosaicml/mpt-30b-chat/result.json"
# Estimated results: chabsa:0.8639618745066888,cma_basics:0.39473684210526316,cpa_audit:0.2135678391959799,security_sales_1:0.5789473684210527,fp2:0.30736842105263157
