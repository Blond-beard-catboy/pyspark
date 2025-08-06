import random, json
from datetime import datetime, timedelta


def generate_record():
    countries = ["US", "CN", "DE", "JP", "IN", "BR", "RU"]
    return {
        "month": f"{random.randint(1,12)}/2023",
        "country": random.choice(countries),
        "code": str(random.randint(1000000000, 9999999999)),
        "value": round(random.uniform(100, 100000), 2),
        "netto": random.randint(1, 100),
        "quantity": random.randint(0, 50),
        "region": random.randint(10000, 99999),
        "district": random.randint(1, 99),
        "direction_eng": random.choice(["IM", "EX"]),
        "measure_eng": random.choice(["ShT", "KG", "L"]),
        "load_date": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
    }

# Генерация 1000 записей
with open("/home/alex/pyspark/data/large_data.json", 'w') as f:
    for _ in range(1000):
        f.write(json.dumps(generate_record()) + '\n')