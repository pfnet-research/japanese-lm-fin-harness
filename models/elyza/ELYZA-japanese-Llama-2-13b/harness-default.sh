MODEL_ARGS="pretrained=elyza/ELYZA-japanese-Llama-2-13b,dtype=float16,tensor_parallel_size=2"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/elyza/ELYZA-japanese-Llama-2-13b/result-default.json"
# a100-80gb: 0
# a30-24gb: 2
# v100-32gb: 2
# v100-16gb: 0
