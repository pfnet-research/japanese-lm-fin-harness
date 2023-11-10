MODEL_ARGS="pretrained=llm-jp/llm-jp-13b-v1.0,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.6,cpa-1.0-0.4,security_sales_1-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0" --device "cuda" --output_path "models/llm-jp/llm-jp-13b-v1.0/result.json"