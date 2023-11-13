MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-ppo,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1.2,cpa-1.0-0.2,security_sales_1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,3,0,3" --device "cuda" --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-ppo/result.json"