MODEL_ARGS="pretrained=Qwen/Qwen1.5-72B-Chat,trust_remote_code=True,dtype=bfloat16,tensor_parallel_size=2"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2,cpa_audit-1.0-0.2,fp2-1.0-0.2,security_sales_1-1.0-0.2"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/Qwen/Qwen1.5-72B-Chat/result-1.0-0.2.json"
# a100-80gb: 2
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
