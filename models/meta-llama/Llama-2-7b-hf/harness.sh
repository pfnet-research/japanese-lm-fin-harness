MODEL_ARGS="pretrained=meta-llama/Llama-2-7b-hf,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1,cpa-1.0-0.1.2,security_sales_1-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0" --device "cuda" --output_path "models/meta-llama/Llama-2-7b-hf/result.json"