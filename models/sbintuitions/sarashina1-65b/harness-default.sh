MODEL_ARGS="pretrained=sbintuitions/sarashina1-65b,dtype=float16,tensor_parallel_size=4"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/sbintuitions/sarashina1-65b/result-default.json"
# a100-80gb: 4
# a30-24gb: 0
# v100-32gb: 8
# v100-16gb: 0
