MODEL_ARGS="pretrained=Xwin-LM/Xwin-LM-7B-V0.2,dtype=float32"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/Xwin-LM/Xwin-LM-7B-V0.2/result-default.json"
# a100-80gb: 1
# a30-24gb: 0
# v100-32gb: 1
# v100-16gb: 0
