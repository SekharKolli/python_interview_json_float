'''
Read float data from a JSON file.
'''

import json
import random

DATA_FILE_JSON = "sensor.json"


def create_json_data(filename, no_of_rows=30):
    data = []
    for i in range(1, no_of_rows+1):
        data.append({
            "id": i,
            "sensor_name": f"Sensor_{random.randint(100, 999)}",
            "temperature": round(random.uniform(20.0, 100.0), 2),  # Float
            "pressure": round(random.uniform(1.0, 5.0), 4),       # Float
            # Float that looks like Int
            "status_code": float(random.randint(200, 204))
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"File '{filename}' created with 30 rows.")


def main():
    create_json_data(DATA_FILE_JSON)


if __name__ == "__main__":
    main()
