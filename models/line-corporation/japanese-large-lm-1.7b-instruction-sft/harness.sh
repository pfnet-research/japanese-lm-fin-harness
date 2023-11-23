MODEL_ARGS="pretrained=line-corporation/japanese-large-lm-1.7b-instruction-sft,trust_remote_code=True,load_in_8bit=True"
TASK="chabsa-1.0-0.6,cma_basics-1.0-0.4,cpa_audit-1.0-0.4,security_sales_1-1.0-0.3,fp2-1.0-0.2.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.3667776476849265,cma_basics:0.2894736842105263,cpa_audit:0.15829145728643215,security_sales_1:0.49122807017543857,fp2:0.24842105263157896
