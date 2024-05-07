MODEL_ARGS="pretrained=mistralai/Mixtral-8x7B-v0.1,dtype=bfloat16,tensor_parallel_size=2"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.1.2,cpa_audit-1.0-0.1.2,fp2-1.0-0.1.2,security_sales_1-1.0-0.1.2"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/mistralai/Mixtral-8x7B-v0.1/result-1.0-0.1.2.json"
# a100-80gb: 2
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
