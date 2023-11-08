MODEL_ARGS="pretrained=abeja/gpt-neox-japanese-2.7b,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics,cpa-1.0-0.2,security_sales_1-1.0-0.5"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,4,4,1" --device "cuda" --output_path "models/abeja-gpt-neox-japanese-2.7b/result.json"