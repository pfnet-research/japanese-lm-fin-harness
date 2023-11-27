MODEL_ARGS="pretrained=rinna/bilingual-gpt-neox-4b"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.6,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,1,3,2,1" --no_cache --output_path "models/rinna/bilingual-gpt-neox-4b/result.json"
# Estimated results: chabsa:0.6057272449266062,cma_basics:0.34210526315789475,cpa_audit:0.20100502512562815,security_sales_1:0.543859649122807,fp2:0.29473684210526313
