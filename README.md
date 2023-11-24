# Japanese Language Model Financial Evaluation Harness
This is a harness for Japanese language model evaluation in the financial domain.

## Leaderboard
<!-- lb start -->
<!-- lb end -->

# How to evaluate your model
 1. git clone this repository
 2. Install the requirements
    ```
    poetry install
    ```
 3. Choose your prompt template based on docs/prompt_templates.md and num_fewshots (In this official leaderboard, we use prompt template peforming the best score.)
 4. Replace `TEMPLATE` to the version and change `MODEL_PATH` . And, save the script as harness.sh
    ```
    MODEL_ARGS="pretrained=MODEL_PATH,load_in_8bit=True,other_options"
    TASK="chabsa-1.0-TEMPLATE,cma_basics-1.0-TEMPLATE,cpa_audit-1.0-TEMPLATE,security_sales_1-1.0-0.2,fp2-1.0-TEMPLATE"
    python main.py --model hf --model_args $MODEL_ARGS --tasks $TASK --num_fewshot "0,0,0,0,0" --device "cuda" --output_path "result.json"
    ```
    For reducing the computational burden, our leaderboard uses the 8bit calculation.
 5. Run the script
    ```
    poetry run bash harness.sh
    ```

Note: if you want to check the actual prompt, you can chack using the following command:
```
poetry run python check_prompt.py
```

# Citation
If you use this repository, please cite the following paper:
```
TBD
```

Or cite directory this repository:
```
@misc{Hirano2023-jlfh
    title={{Japanese Language Model Financial Evaluation Harness}},
    autors={Masanori Hirano},
    year={2024},
    url = {https://github.com/pfnet-research/japanese-lm-fin-harness}
}
```
