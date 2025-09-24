def serve_chai(flavour):
    if flavour not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported tea")
    print(f"Brewing {flavour} tea")

serve_chai("ginger")