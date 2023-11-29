MODEL_ARGS="pretrained=meta-llama/Llama-2-7b-hf"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.2.1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,2,0,4" --no_cache --output_path "models/meta-llama/Llama-2-7b-hf/result.json"
# Estimated results: chabsa:0.774087075263302,cma_basics:0.3684210526315789,cpa_audit:0.18592964824120603,security_sales_1:0.5263157894736842,fp2:0.28210526315789475
