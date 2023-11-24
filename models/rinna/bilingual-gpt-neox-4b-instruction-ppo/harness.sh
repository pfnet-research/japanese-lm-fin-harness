MODEL_ARGS="pretrained=rinna/bilingual-gpt-neox-4b-instruction-ppo,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.5,cpa_audit-1.0-0.6,security_sales_1-1.0-0.5,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/rinna/bilingual-gpt-neox-4b-instruction-ppo/result.json"
# Estimated results: chabsa:0.5058044811331905,cma_basics:0.2894736842105263,cpa_audit:0.18090452261306533,security_sales_1:0.43859649122807015,fp2:0.24
