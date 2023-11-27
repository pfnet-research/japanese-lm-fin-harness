MODEL_ARGS="pretrained=rinna/bilingual-gpt-neox-4b-instruction-ppo"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.4,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.1,fp2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "1,3,2,1,4" --no_cache --output_path "models/rinna/bilingual-gpt-neox-4b-instruction-ppo/result.json"
# Estimated results: chabsa:0.7837565108225448,cma_basics:0.3157894736842105,cpa_audit:0.20603015075376885,security_sales_1:0.5087719298245614,fp2:0.2968421052631579
