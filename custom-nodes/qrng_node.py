import requests
import csv
import os
from pathlib import Path

class QRNG_Node_CSV:
    CSV_PATH = Path(__file__).parent.resolve()
    CSV_FILE = os.path.join(CSV_PATH, 'random_values.csv')  # Joining path with filename

    API_URL = "https://api.quantumnumbers.anu.edu.au"
    API_KEY = "x"

    def __init__(self):
        print("Initializing QRNG_Node...")
        self.init_csv()
        self.random_values = self.load_random_values_from_csv()
        print(f"Loaded {len(self.random_values)} random values from CSV.")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {}
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "test"
    CATEGORY = "Example"
    IS_OUTPUT = True

    def init_csv(self):
        print("Initializing CSV...")
        if not os.path.exists(self.CSV_FILE):
            with open(self.CSV_FILE, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['id', 'value'])
        print("CSV initialized.")

    def load_random_values_from_csv(self):
        print("Loading random values from CSV...")
        values = []
        with open(self.CSV_FILE, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            values = list(reader)

        if len(values) < 4:
            print("Fewer than 4 values found in CSV. Fetching from API...")
            random_values = self.get_random_values()
            with open(self.CSV_FILE, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for value in random_values:
                    writer.writerow([None, value])
            return self.load_random_values_from_csv()

        return values

    def get_random_values(self):
        print("Fetching random values from API...")
        headers = {"x-api-key": self.API_KEY}
        params = {
            "length": 1024,
            "type": "uint16"
        }
        response = requests.get(self.API_URL, headers=headers, params=params)
        if response.status_code == 200:
            print("Random values fetched successfully.")
            return response.json()["data"]
        else:
            print("Error fetching random values")
            return []
            
    def IS_CHANGED():
        return float("nan")

    def test(self):
        print("Test method called.")
        if len(self.random_values) < 4:
            print("Random values list is running low. Reloading...")
            self.random_values = self.load_random_values_from_csv()

        noise_seed_64 = 0
        row_ids_to_delete = []
        for _ in range(4):
            row_id, noise_seed_16 = self.random_values.pop(0)
            noise_seed_64 = (noise_seed_64 << 16) | int(noise_seed_16)
            print(f"Using value {noise_seed_16} with ID {row_id}.")
            row_ids_to_delete.append(row_id)

        # Update CSV by removing deleted rows
        with open(self.CSV_FILE, 'r') as csvfile:
            rows = list(csv.reader(csvfile))
        with open(self.CSV_FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'value'])  # Write header
            writer.writerows(row for row in rows if row[0] not in row_ids_to_delete)

        print(f"{noise_seed_64}")

        return (noise_seed_64,)

NODE_CLASS_MAPPINGS = {
    "QRNG_Node_CSV": QRNG_Node_CSV
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QRNG_Node_CSV": "QRNG Node CSV"
}
