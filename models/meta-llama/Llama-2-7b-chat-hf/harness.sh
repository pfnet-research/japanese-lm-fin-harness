MODEL_ARGS="pretrained=meta-llama/Llama-2-7b-chat-hf,load_in_8bit=True"
TASK="chabsa,cma_basics-1.0-0.1,cpa_audit,security_sales_1,fp2-1.0-0.2"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.5613138852799328,cma_basics:0.42105263157894735,cpa_audit:0.19597989949748743,security_sales_1:0.5789473684210527,fp2:0.2926315789473684
