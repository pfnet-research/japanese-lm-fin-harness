MODEL_ARGS="pretrained=rinna/bilingual-gpt-neox-4b,load_in_8bit=True"
TASK="chabsa,cma_basics,cpa,security_sales_1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0" --device "cuda" --output_path "models/rinna/bilingual-gpt-neox-4b/result.json"