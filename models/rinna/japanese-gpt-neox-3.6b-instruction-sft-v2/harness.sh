MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-sft-v2"
TASK="chabsa-1.0-0.2,cma_basics,cpa_audit-1.0-0.6,security_sales_1,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,2,2,4,2" --no_cache --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2/result.json"
# Estimated results: chabsa:0.7547176483713054,cma_basics:0.39473684210526316,cpa_audit:0.19597989949748743,security_sales_1:0.543859649122807,fp2:0.28421052631578947
