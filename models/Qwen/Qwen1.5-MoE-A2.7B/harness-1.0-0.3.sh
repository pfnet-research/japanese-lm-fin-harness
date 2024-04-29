MODEL_ARGS="pretrained=Qwen/Qwen1.5-MoE-A2.7B,trust_remote_code=True,dtype=bfloat16"
TASK="chabsa-1.0-0.3,cma_basics-1.0-0.3,cpa_audit-1.0-0.3,fp2-1.0-0.3,security_sales_1-1.0-0.3"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/Qwen/Qwen1.5-MoE-A2.7B/result-1.0-0.3.json"
# a100-80gb: 1
# a30-24gb: 1
# v100-32gb: 0
# v100-16gb: 0
