TEMPLATES = {
    "home_decor": "Enhance your home with the {name}. This exquisite piece is "
                  "handcrafted from {material} by {artisan_origin}. "
                  "Measuring {dimensions}, it's perfect for {use_case}. "
                  "Each item is unique, reflecting the skill of its creator.",

    "jewelry":    "Adorn yourself with the stunning {name}. This piece features "
                  "{material} and {special_feature}, meticulously crafted by "
                  "{artisan_origin}. It's the perfect accessory for {use_case} "
                  "and adds a touch of ethnic elegance to any look.",

    "fashion":    "Step out in style with the {name}. Made from {material}, "
                  "this item showcases {special_feature} from {artisan_origin}. "
                  "It's comfortable, stylish, and perfect for {use_case}.",
    
    "default":    "Presenting the {name}. A wonderful item crafted from {material}. "
                  "Ideal for {use_case}."
}



PRODUCT_DATA = [
    {
        "category": "home_decor",
        "name": "Hand-carved Wooden Elephant",
        "material": "sustainably-sourced Mango Wood",
        "artisan_origin": "artisans in Rajasthan",
        "dimensions": "6 inches tall",
        "use_case": "your mantelpiece or bookshelf"
    },
    {
        "category": "jewelry",
        "name": "Turquoise Silver Ring",
        "material": "Sterling Silver (925)",
        "artisan_origin": "silversmiths of Jaipur",
        "special_feature": "a genuine turquoise gemstone",
        "use_case": "special occasions or daily wear"
    },
    {
        "category": "fashion",
        "name": "Kantha Stitch Silk Scarf",
        "material": "pure Tussar silk",
        "artisan_origin": "women's co-operatives in West Bengal",
        "special_feature": "intricate Kantha embroidery",
        "use_case": "pairing with both casual and formal outfits"
    },
    {
        "category": "unknown_category",
        "name": "Simple Clay Pot",
        "material": "terracotta",
        "use_case": "planting small herbs"
    }
]



def generate_description(product: dict) -> str:
   
    try:
        
        category = product.get("category", "default")
        
        template = TEMPLATES.get(category, TEMPLATES["default"])
        
        return template.format(**product)

    except KeyError as e:

        print(f"Warning: Missing key {e} for product '{product.get('name')}'")
       
        try:
            return TEMPLATES["default"].format(**product)
        except KeyError as e2:
            return f"Error: Could not generate description for {product.get('name')}. Missing {e2}."
    except Exception as e:
        print(f"An unexpected error occurred for {product.get('name')}: {e}")
        return "Error: Could not generate description."


if __name__ == "__main__":
    print("--- Generating Product Descriptions for Indikraft ---")
    
    for item in PRODUCT_DATA:
       
        description = generate_description(item)
       
        print(f"\nPRODUCT NAME: {item.get('name')}")
        print("-------------------------------------------------")
        print("GENERATED DESCRIPTION:")
        print(description)
        print("=================================================")