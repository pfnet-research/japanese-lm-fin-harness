MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.2,cpa-1.0-0.1,security_sales_1-1.0-0.3"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,4,4" --device "cuda" --output_path "models/line-corporation/japanese-large-lm-1.7b/result.json"