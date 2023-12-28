MODEL_ARGS="pretrained=Qwen/Qwen-7B-Chat,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.2.1,security_sales_1,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,4,0,4,4" --no_cache --output_path "models/Qwen/Qwen-7B-Chat/result.json"
# Estimated results: chabsa:0.8637905587699874,cma_basics:0.5,cpa_audit:0.2135678391959799,security_sales_1:0.5964912280701754,fp2:0.31157894736842107
