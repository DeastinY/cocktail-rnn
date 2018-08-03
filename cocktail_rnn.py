import json
import requests
from tqdm import tqdm
from pathlib import Path


def download_data():
    cocktails = []
    api_key = "ENTER_API_KEY"
    for i in tqdm(reversed(range(17830)), total=17830):
        r = requests.get(url=f"https://www.thecocktaildb.com/api/json/v1/{api_key}/lookup.php?i={i}")
        data = r.json()
        if data['drinks']:
            cocktails.append(data)
            print(f"Crawled {len(cocktails)} Cocktails")
    Path("data.json").write_text(json.dumps(cocktails, indent=2, sort_keys=True))


def format_data():
    data = json.loads(Path("data.json").read_text())
    data_format = []
    for d in tqdm(data):
        d = d['drinks'][0]
        text = f"{d['strDrink']}\n"
        for i in range(1, 15):
            if d['strIngredient'+str(i)]:
                text += f"{d['strMeasure'+str(i)]} {d['strIngredient'+str(i)]}\n"
        text += "\n"
        instructions = d['strInstructions']
        instructions = instructions.replace('\n', '')
        instructions = instructions.replace('. ', '.\n')
        instructions = instructions.replace('.', '.\n')
        text += instructions
        text += f"\nServe in {d['strGlass']}"
        data_format.append(text)
    Path("data_format.txt").write_text("\n--------------------------------------\n".join(data_format))


if __name__ == "__main__":
    if not Path("data.json").exists():
        download_data()
    if not Path("data_format.txt").exists():
        format_data()

