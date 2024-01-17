MODEL_ARGS="pretrained=Qwen/Qwen-72B-Chat,trust_remote_code=True,use_accelerate=True,device_map_option=auto"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1.2,cpa_audit,security_sales_1,fp2-1.0-0.1"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,3,0,4,0" --no_cache --output_path "models/Qwen/Qwen-72B-Chat/result.json"
# Estimated results: chabsa:0.9252459396434084,cma_basics:0.7894736842105263,cpa_audit:0.2989949748743719,security_sales_1:0.7192982456140351,fp2:0.40842105263157896
