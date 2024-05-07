MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-13b-fast-instruct,dtype=float16,tensor_parallel_size=2"
TASK="chabsa-1.0-0.5,cma_basics-1.0-0.5,cpa_audit-1.0-0.5,fp2-1.0-0.5,security_sales_1-1.0-0.5"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct/result-1.0-0.5.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 4
# v100-16gb: 0
