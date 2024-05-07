MODEL_ARGS="pretrained=Xwin-LM/Xwin-LM-70B-V0.1,dtype=float32,tensor_parallel_size=4"
TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/Xwin-LM/Xwin-LM-70B-V0.1/result-default.json"
# a100-80gb: 4
# a30-24gb: 0
# v100-32gb: 0
# v100-16gb: 0
