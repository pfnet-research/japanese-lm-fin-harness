MODEL_ARGS="pretrained=rinna/nekomata-14b-instruction,trust_remote_code=True"
TASK="chabsa-1.0-0.3,cma_basics-1.0-0.1,cpa_audit-1.0-0.2,security_sales_1-1.0-0.3,fp2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,2,3,4,2" --no_cache --output_path "models/rinna/nekomata-14b-instruction/result.json"
# Estimated results: chabsa:0.9126562862383774,cma_basics:0.631578947368421,cpa_audit:0.24120603015075376,security_sales_1:0.631578947368421,fp2:0.3873684210526316
