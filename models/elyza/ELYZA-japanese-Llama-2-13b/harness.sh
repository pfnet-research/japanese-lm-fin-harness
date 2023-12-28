MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-13b"
TASK="chabsa,cma_basics-1.0-0.6,cpa_audit,security_sales_1-1.0-0.1.2,fp2-1.0-0.5"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,2,2,1,1" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-13b/result.json"
# Estimated results: chabsa:0.883730724070144,cma_basics:0.47368421052631576,cpa_audit:0.1934673366834171,security_sales_1:0.5789473684210527,fp2:0.28842105263157897
