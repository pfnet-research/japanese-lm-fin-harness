MODEL_ARGS="pretrained=meta-llama/Llama-2-13b-chat-hf"
TASK="chabsa,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2,security_sales_1-1.0-0.1.2,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,2,3,1" --no_cache --output_path "models/meta-llama/Llama-2-13b-chat-hf/result.json"
# Estimated results: chabsa:0.8796316606926049,cma_basics:0.5263157894736842,cpa_audit:0.19597989949748743,security_sales_1:0.543859649122807,fp2:0.2926315789473684
