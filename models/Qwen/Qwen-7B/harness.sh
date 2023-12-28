MODEL_ARGS="pretrained=Qwen/Qwen-7B,trust_remote_code=True"
TASK="chabsa-1.0-0.1,cma_basics,cpa_audit-1.0-0.5,security_sales_1,fp2-1.0-0.1.2"
python main.py --model hf-causal-experimental --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "4,0,2,4,0" --no_cache --output_path "models/Qwen/Qwen-7B/result.json"
# Estimated results: chabsa:0.8515393521971477,cma_basics:0.5526315789473685,cpa_audit:0.20100502512562815,security_sales_1:0.631578947368421,fp2:0.3178947368421053
