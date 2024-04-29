MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-sft-v2,dtype=float16"
    TASK="chabsa,cma_basics,cpa_audit,fp2,security_sales_1"
    python main.py --model vllm --model_args $MODEL_ARGS --tasks $TASK --num_fewshot 0 --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2/result-.json"
    # a100-80gb: 0
    # a30-24gb: 0
    # v100-32gb: 0
    # v100-16gb: 0
    