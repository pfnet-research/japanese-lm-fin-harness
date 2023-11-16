MODEL_ARGS="pretrained=meta-llama/Llama-2-70b-hf,load_in_8bit=True"
TASK="chabsa-1.0-0.4,cma_basics,cpa-1.0-0.2.1,security_sales_1-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0" --device "cuda" --output_path "models/meta-llama/Llama-2-70b-hf/result.json"