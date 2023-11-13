MODEL_ARGS="pretrained=rinna/japanese-gpt-neox-3.6b-instruction-sft-v2,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics,cpa-1.0-0.6,security_sales_1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,2,2,4" --device "cuda" --output_path "models/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2/result.json"