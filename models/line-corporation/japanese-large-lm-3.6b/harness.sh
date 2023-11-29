MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-3.6b,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.6,cpa_audit-1.0-0.2,security_sales_1-1.0-0.6,fp2-1.0-0.5"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,4,3,1" --no_cache --output_path "models/line-corporation/japanese-large-lm-3.6b/result.json"
# Estimated results: chabsa:0.650070934405717,cma_basics:0.34210526315789475,cpa_audit:0.20854271356783918,security_sales_1:0.5614035087719298,fp2:0.29473684210526313
