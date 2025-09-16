def serve_chai(flavour):
    try:
        print(flavour)
        if flavour == "unknown":
            raise ValueError("We don't know that flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} tea is served")
    finally:
        print("Next customer pls")

serve_chai("unknown")