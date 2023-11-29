MODEL_ARGS="pretrained=lmsys/vicuna-33b-v1.3,use_accelerate=True,device_map_option=auto"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.2.1,cpa_audit,security_sales_1-1.0-0.1.2,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,4,4,3,2" --no_cache --output_path "models/lmsys/vicuna-33b-v1.3/result.json"
# Estimated results: chabsa:0.8781375223332344,cma_basics:0.34210526315789475,cpa_audit:0.19597989949748743,security_sales_1:0.5614035087719298,fp2:0.2863157894736842
