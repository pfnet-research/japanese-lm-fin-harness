MODEL_ARGS="pretrained=pfnet/plamo-13b-instruct-nc,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1,fp2-1.0-0.5"
python main.py --model hf-causal --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,3,3,0,4" --no_cache --output_path "models/pfnet/plamo-13b-instruct-nc/result.json"
# Estimated results: chabsa:0.7357526870417581,cma_basics:0.39473684210526316,cpa_audit:0.20603015075376885,security_sales_1:0.543859649122807,fp2:0.2926315789473684
