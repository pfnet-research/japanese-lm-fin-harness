MODEL_ARGS="pretrained=meta-llama/Llama-2-70b-chat-hf,use_accelerate=True,device_map_option=auto"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.1.2,security_sales_1,fp2-1.0-0.2.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,3,3,3,2" --no_cache --output_path "models/meta-llama/Llama-2-70b-chat-hf/result.json"
# Estimated results: chabsa:0.9029204395139568,cma_basics:0.5263157894736842,cpa_audit:0.1884422110552764,security_sales_1:0.631578947368421,fp2:0.3263157894736842
