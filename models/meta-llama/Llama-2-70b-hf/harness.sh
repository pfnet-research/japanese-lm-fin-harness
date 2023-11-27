MODEL_ARGS="pretrained=meta-llama/Llama-2-70b-hf,use_accelerate=True,device_map_option=auto"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1,cpa_audit,security_sales_1-1.0-0.1.2,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,0,3,1" --no_cache --output_path "models/meta-llama/Llama-2-70b-hf/result.json"
# Estimated results: chabsa:0.8936983519122839,cma_basics:0.5789473684210527,cpa_audit:0.20854271356783918,security_sales_1:0.631578947368421,fp2:0.3642105263157895
