MODEL_ARGS="pretrained=meta-llama/Llama-2-13b-hf"
TASK="chabsa-1.0-0.4,cma_basics-1.0-0.5,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.1.2,fp2-1.0-0.3"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,4,2,3,3" --no_cache --output_path "models/meta-llama/Llama-2-13b-hf/result.json"
# Estimated results: chabsa:0.8204454059024106,cma_basics:0.3684210526315789,cpa_audit:0.21105527638190955,security_sales_1:0.5087719298245614,fp2:0.3031578947368421
