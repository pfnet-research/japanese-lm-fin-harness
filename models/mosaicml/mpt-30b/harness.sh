MODEL_ARGS="pretrained=mosaicml/mpt-30b,use_accelerate=True,device_map_option=auto,trust_remote_code=True"
TASK="chabsa-1.0-0.2,cma_basics,cpa_audit-1.0-0.4,security_sales_1-1.0-0.1,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,2,2,3,2" --no_cache --output_path "models/mosaicml/mpt-30b/result.json"
# Estimated results: chabsa:0.8343706633956594,cma_basics:0.3684210526315789,cpa_audit:0.19597989949748743,security_sales_1:0.5263157894736842,fp2:0.28210526315789475
