MODEL_ARGS="pretrained=Qwen/Qwen-14B-Chat,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2,security_sales_1,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,2,1,3,3" --no_cache --output_path "models/Qwen/Qwen-14B-Chat/result.json"
# Estimated results: chabsa:0.9156254986320542,cma_basics:0.6578947368421053,cpa_audit:0.2236180904522613,security_sales_1:0.6140350877192983,fp2:0.32421052631578945
