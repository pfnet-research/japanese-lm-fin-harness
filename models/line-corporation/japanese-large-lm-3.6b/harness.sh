MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-3.6b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.5,cpa-1.0-0.1,security_sales_1-1.0-0.5"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,3,2" --device "cuda" --output_path "models/line-corporation/japanese-large-lm-3.6b/result.json"