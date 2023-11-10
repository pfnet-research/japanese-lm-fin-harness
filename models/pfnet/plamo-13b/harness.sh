MODEL_ARGS="pretrained=pfnet/plamo-13b,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.4,cma_basics-1.0-0.4,cpa-1.0-0.6,security_sales_1-1.0-0.5"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,2,1" --device "cuda" --output_path "models/pfnet/plamo-13b/result.json"