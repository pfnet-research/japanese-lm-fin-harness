MODEL_ARGS="pretrained=meta-llama/Llama-2-13b-chat-hf,load_in_8bit=True"
TASK="chabsa,cma_basics-1.0-0.2,cpa_audit-1.0-0.2,security_sales_1-1.0-0.1,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.4542860374790487,cma_basics:0.3684210526315789,cpa_audit:0.16834170854271358,security_sales_1:0.47368421052631576,fp2:0.2631578947368421
