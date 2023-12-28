MODEL_ARGS="pretrained=Qwen/Qwen-14B,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2.1,security_sales_1-1.0-0.1,fp2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,0,3,3,3" --no_cache --output_path "models/Qwen/Qwen-14B/result.json"
# Estimated results: chabsa:0.9073072641819879,cma_basics:0.631578947368421,cpa_audit:0.22613065326633167,security_sales_1:0.6491228070175439,fp2:0.3831578947368421
