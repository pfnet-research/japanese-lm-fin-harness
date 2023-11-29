MODEL_ARGS="pretrained=lmsys/vicuna-13b-v1.5-16k"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.2,security_sales_1-1.0-0.1.2,fp2-1.0-0.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,1,1,3,2" --no_cache --output_path "models/lmsys/vicuna-13b-v1.5-16k/result.json"
# Estimated results: chabsa:0.8580657315595651,cma_basics:0.5263157894736842,cpa_audit:0.19095477386934673,security_sales_1:0.5789473684210527,fp2:0.3136842105263158
