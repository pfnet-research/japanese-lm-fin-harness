MODEL_ARGS="pretrained=rinna/nekomata-7b-instruction,trust_remote_code=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1.2,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,2,0,4,0" --no_cache --output_path "models/rinna/nekomata-7b-instruction/result.json"
# Estimated results: chabsa:0.9041316584123904,cma_basics:0.47368421052631576,cpa_audit:0.22613065326633167,security_sales_1:0.6140350877192983,fp2:0.32421052631578945
