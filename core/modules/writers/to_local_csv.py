from configs.dev import BASE_DIR, SAMPLES_DIR

def write_stock_current_price(data):
    stock = data["stock"]
    date = data["date"]
    csv_path = f"{SAMPLES_DIR}/{date}/{stock}.csv"
    with open(csv_path, "w+") as f:
        pass