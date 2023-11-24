MODEL_ARGS="pretrained=meta-llama/Llama-2-13b-hf,load_in_8bit=True"
TASK="chabsa-1.0-0.4,cma_basics,cpa_audit-1.0-0.4,security_sales_1-1.0-0.2.1,fp2-1.0-0.6"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/meta-llama/Llama-2-13b-hf/result.json"
# Estimated results: chabsa:0.45227840958616716,cma_basics:0.3157894736842105,cpa_audit:0.1457286432160804,security_sales_1:0.543859649122807,fp2:0.27157894736842103
