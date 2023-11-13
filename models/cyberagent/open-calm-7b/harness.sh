MODEL_ARGS="pretrained=cyberagent/open-calm-7b,use_fast=True,load_in_8bit=True"
TASK="chabsa,cma_basics,cpa,security_sales_1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "3,3,3,3" --device "cuda" --output_path "models/cyberagent/open-calm-7b/result.json"