MODEL_ARGS="pretrained=cyberagent/open-calm-small,use_fast=True,load_in_8bit=True"
TASK="chabsa-1.0-0.1,cma_basics-1.0-0.3,cpa_audit-1.0-0.6,security_sales_1-1.0-0.2.1,fp2-1.0-0.6"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/abeja/abeja-gpt-neox-japanese-2.7b/result.json"
# Estimated results: chabsa:0.33546033361652294,cma_basics:0.2894736842105263,cpa_audit:0.17336683417085427,security_sales_1:0.45614035087719296,fp2:0.2505263157894737
