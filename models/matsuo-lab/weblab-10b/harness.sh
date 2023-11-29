MODEL_ARGS="pretrained=matsuo-lab/weblab-10b,trust_remote_code=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.3,cpa_audit-1.0-0.5,security_sales_1-1.0-0.1,fp2-1.0-0.5"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,1,2,3,2" --no_cache --output_path "models/matsuo-lab/weblab-10b/result.json"
# Estimated results: chabsa:0.7683692386347885,cma_basics:0.34210526315789475,cpa_audit:0.21105527638190955,security_sales_1:0.5087719298245614,fp2:0.3031578947368421
