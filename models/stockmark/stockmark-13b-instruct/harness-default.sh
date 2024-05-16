MODEL_ARGS="pretrained=stockmark/stockmark-13b-instruct,dtype=bfloat16"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/stockmark/stockmark-13b-instruct/result-default.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
