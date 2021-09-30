# PokemonExcelParser
Parse my excel sheets to insert pokemon name and rarity from set number and set abbreviation in an excel spreadsheet


## Getting Set Information
Run the following command from the pipeline
``` bash
python -m retrieval.pokemon_tcg_api_cli get_set_info -s <SET_ID>
```
Where **SET_ID** is something like **swsh4**


### Before Running
1. **Install all required dependencies with the following command:**
    ``` cmd
    pip install -r dependencies.txt
    ```
