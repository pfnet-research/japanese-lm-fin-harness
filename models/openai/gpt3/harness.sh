MODEL_ARGS="engine=text-davinci-003"
TASK="chabsa,cma_basics,cpa_audit,security_sales_1,fp2"
python main.py --model gpt3 --model_args engine=text-davinci-003 --tasks $TASK --num_fewshot "0,0,0,0,0" --output_path "models/openai/gpt3/result.json"
