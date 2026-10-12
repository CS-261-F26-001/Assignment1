import csv
import math
from datetime import datetime, timedelta


class Earthquake:
    # TODO: implement me
    pass


class EarthquakeDatabase:
    def __init__(self) -> None:
        self.earthquakes: list[Earthquake] = []
        
    def load_data(self, path: str) -> None:
        # TODO: implement me
        pass


    def find_by_id(self, id: str) -> Earthquake | None:
        # TODO: implement me
        return None
    
    
    def find_by_location(self, location: str) -> list[Earthquake]:
        # TODO: implement me
        return []
        
        
    def find_strongest(self) -> Earthquake | None:
        # TODO: implement me
        return None


    def find_nearby(self, latitude: float, longitude: float, radius_km: float) -> list[Earthquake]:
        # TODO: implement me
        return []


    def find_k_strongest(self, k: int) -> list[Earthquake]:
        # TODO: implement me
        return []
    
    
    def find_duplicate(self) -> str:
        # TODO: implement me
        return "Not found"
    
    
    def find_busiest_day(self) -> int:
        return -1
    

def main() -> None:
    earthquake_db = EarthquakeDatabase()
    earthquake_db.load_data("earthquakes.csv")
    
    strongest = earthquake_db.find_strongest()
    print(f"Strongest earthquake: {strongest}")

    local_earthquakes = earthquake_db.find_by_location("Oregon")
    print(f"Earthquakes in Oregon: {len(local_earthquakes)}")

    nearby = earthquake_db.find_nearby(44.565720, -123.278931, 100.0)
    print(f"Earthquakes within 100 km of Corvallis: {len(nearby)}")

    duplicate = earthquake_db.find_duplicate()
    print(f"Duplicate earthquake is: {duplicate}")

    k = 5
    k_strongest = earthquake_db.find_k_strongest(k)
    print(f"Top {k} strongest earthquakes:")
    for i, strongest in enumerate(k_strongest):
        print(f"{i + 1}. {strongest}")

    busiest = earthquake_db.find_busiest_day()
    print(f"Busiest 24-hour window contains: {busiest} earthquakes")


if __name__ == "__main__":
    main()
