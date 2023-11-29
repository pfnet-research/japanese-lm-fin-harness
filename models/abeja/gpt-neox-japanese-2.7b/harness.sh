MODEL_ARGS="pretrained=abeja/gpt-neox-japanese-2.7b,trust_remote_code=True"
TASK="chabsa-1.0-0.2,cma_basics,cpa_audit-1.0-0.2,security_sales_1-1.0-0.5,fp2-1.0-0.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,2,2,1,2" --no_cache --output_path "models/abeja/gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.49667825778017904,cma_basics:0.39473684210526316,cpa_audit:0.20100502512562815,security_sales_1:0.49122807017543857,fp2:0.28210526315789475
