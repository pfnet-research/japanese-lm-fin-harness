MODEL_ARGS="pretrained=rinna/youri-7b,load_in_8bit=True "
TASK="chabsa-1.0-0.2,cma_basics,cpa-1.0-0.3,security_sales_1-1.0-0.1.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,1,3,3" --device "cuda" --output_path "models/rinna/youri-7b/result.json"