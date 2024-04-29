MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-instruct-beta-70b,trust_remote_code=True,dtype=float32"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/stabilityai/japanese-stablelm-instruct-beta-70b/result-default.json"
# a100-80gb: 2
# a30-24gb: 0
# v100-32gb: 8
# v100-16gb: 0
