MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-instruct-beta-70b,trust_remote_code=True,dtype=float32,tensor_parallel_size=4"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.6,cpa_audit-1.0-0.6,fp2-1.0-0.6,security_sales_1-1.0-0.6"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/stabilityai/japanese-stablelm-instruct-beta-70b/result-1.0-0.6.json"
# a100-80gb: 4
# a30-24gb: 0
# v100-32gb: 8
# v100-16gb: 0
