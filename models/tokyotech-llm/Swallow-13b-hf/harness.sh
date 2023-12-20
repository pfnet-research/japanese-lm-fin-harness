MODEL_ARGS="pretrained=tokyotech-llm/Swallow-13b-hf"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.1.2,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,4,1,3,4" --no_cache --output_path "models/tokyotech-llm/Swallow-13b-hf/result.json"
# Estimated results: chabsa:0.87586467060832,cma_basics:0.5263157894736842,cpa_audit:0.19597989949748743,security_sales_1:0.5614035087719298,fp2:0.3410526315789474
