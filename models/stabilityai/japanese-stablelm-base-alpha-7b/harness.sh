MODEL_ARGS="pretrained=stabilityai/japanese-stablelm-base-alpha-7b,trust_remote_code=True,load_in_8bit=True,tokenizer=novelai/nerdstash-tokenizer-v1"
TASK="chabsa-1.0-0.6,cma_basics,cpa_audit-1.0-0.4,security_sales_1-1.0-0.2.1,fp2-1.0-0.1"
python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "models/stabilityai/japanese-stablelm-base-alpha-7b/result.json"
# Estimated results: chabsa:0.44539608369395606,cma_basics:0.2894736842105263,cpa_audit:0.1708542713567839,security_sales_1:0.5087719298245614,fp2:0.2863157894736842
