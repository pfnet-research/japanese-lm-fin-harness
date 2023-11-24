MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-instruct-full-jaster-v1.0,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa,cma_basics,cpa_audit-1.0-0.1,security_sales_1-1.0-0.2.1,fp2-1.0-0.1.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0/result.json"
# Estimated results: chabsa:0.5681879050226346,cma_basics:0.34210526315789475,cpa_audit:0.1934673366834171,security_sales_1:0.49122807017543857,fp2:0.24842105263157896
