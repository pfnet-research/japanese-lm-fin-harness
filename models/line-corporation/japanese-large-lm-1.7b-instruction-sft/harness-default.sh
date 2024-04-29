MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b-instruction-sft,trust_remote_code=True,dtype=float16"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/line-corporation/japanese-large-lm-1.7b-instruction-sft/result-default.json"
# a100-80gb: 1
# a30-24gb: 1
# v100-32gb: 1
# v100-16gb: 1
