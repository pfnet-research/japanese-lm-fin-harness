MODEL_ARGS="pretrained=rinna/bilingual-gpt-neox-4b-instruction-sft,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.4,cpa_audit-1.0-0.5,security_sales_1-1.0-0.2.1,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/bilingual-gpt-neox-4b-instruction-sft/result.json"
# Estimated results: chabsa:0.46522255452637,cma_basics:0.34210526315789475,cpa_audit:0.18090452261306533,security_sales_1:0.45614035087719296,fp2:0.2631578947368421
