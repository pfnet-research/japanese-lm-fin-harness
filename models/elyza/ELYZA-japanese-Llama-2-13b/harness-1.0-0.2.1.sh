MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-13b,dtype=float16,tensor_parallel_size=2"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.2.1,cpa_audit-1.0-0.2.1,fp2-1.0-0.2.1,security_sales_1-1.0-0.2.1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/elyza/ELYZA-japanese-Llama-2-13b/result-1.0-0.2.1.json"
# a100-80gb: 0
# a30-24gb: 2
# v100-32gb: 2
# v100-16gb: 0
