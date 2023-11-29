MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-7b-fast"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.5,cpa_audit-1.0-0.1.2,security_sales_1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,3,0,0,0" --no_cache --output_path "models/elyza/ELYZA-japanese-Llama-2-7b-fast/result.json"
# Estimated results: chabsa:0.8246875839552572,cma_basics:0.4473684210526316,cpa_audit:0.18090452261306533,security_sales_1:0.543859649122807,fp2:0.30736842105263157
