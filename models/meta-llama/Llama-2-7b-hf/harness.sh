MODEL_ARGS="pretrained=meta-llama/Llama-2-7b-hf,load_in_8bit=True"
TASK="chabsa-1.0-0.2,cma_basics-1.0-0.1,cpa_audit-1.0-0.1.2,security_sales_1-1.0-0.2.1,fp2-1.0-0.5"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.5153580033131003,cma_basics:0.34210526315789475,cpa_audit:0.1407035175879397,security_sales_1:0.5263157894736842,fp2:0.27578947368421053
