class ChaiUtils:
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water , milk , ginger "

obj = ChaiUtils()
print(obj.clean_ingredients(raw))