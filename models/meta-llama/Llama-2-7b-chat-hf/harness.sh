MODEL_ARGS="pretrained=meta-llama/Llama-2-7b-chat-hf"
TASK="chabsa,cma_basics-1.0-0.1,cpa_audit-1.0-0.2,security_sales_1,fp2-1.0-0.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,2,0,0" --no_cache --output_path "models/meta-llama/Llama-2-7b-chat-hf/result.json"
# Estimated results: chabsa:0.8369428257796767,cma_basics:0.39473684210526316,cpa_audit:0.20351758793969849,security_sales_1:0.5087719298245614,fp2:0.30105263157894735
