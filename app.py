import requests
from bs4 import BeautifulSoup

def get_croads_menu(meal=""):
    url = "https://dining.berkeley.edu/menus/"
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
    except Exception:
        return "Failed to fetch menu."

    # Locate Crossroads section
    croads_node = soup.select_one("li.location-name.Crossroads")
    if not croads_node:
        return "Crossroads location not found."

    menus = {"Lunch": [], "Dinner": []}
    
    # Iterate through periods (Lunch/Dinner)
    for period in croads_node.select("li.preiod-name"):
        period_name = period.select_one("span").get_text(strip=True)
        key = "Lunch" if "unch" in period_name else "Dinner" if "Dinner" in period_name else None
        
        if key:
            # Filter by specific categories
            for cat in period.select("div.cat-name"):
                cat_name = cat.select_one("span").get_text(strip=True).lower()
                if any(x in cat_name for x in ["center plate", "lemon grass", "grill"]):
                    recipes = cat.select("ul.recipe-name > li.recip > span:first-child")
                    menus[key].extend([r.get_text(strip=True) for r in recipes if not r.find("img")])

    # Formatting Logic
    meal = meal.lower()
    include_lunch = meal in ["lunch", "", "all"]
    include_dinner = meal in ["dinner", "", "all"]

    if not include_lunch and not include_dinner:
        return "Invalid option. Use `lunch` or `dinner`."

    response = ["**Crossroads Menu**\n"]
    if include_lunch:
        response.append("**Lunch**")
        response.extend([f"- {i}" for i in menus["Lunch"]] if menus["Lunch"] else ["No lunch menu found."])
    
    if include_lunch and include_dinner:
        response.append("")

    if include_dinner:
        response.append("**Dinner**")
        response.extend([f"- {i}" for i in menus["Dinner"]] if menus["Dinner"] else ["No dinner menu found."])

    full_text = "\n".join(response)
    return (full_text[:1900] + "...\n(Truncated)") if len(full_text) > 1900 else full_text

print(get_croads_menu())
