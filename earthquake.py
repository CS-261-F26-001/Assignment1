import csv
import math
from datetime import datetime, timedelta


class Earthquake:
    def __init__(self, id: str, magnitude: float, significance: int, depth: float,
                 distance: float, latitude: float, longitude: float,
                 location: str, epoch: int, time: datetime) -> None:
        self.id = id
        self.magnitude = magnitude
        self.significance = significance
        self.depth = depth
        self.distance = distance
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
        self.epoch = epoch
        self.time = time

    def __repr__(self) -> str:
        return f"{self.time} [{self.id}] {self.location}, M{self.magnitude}"


class EarthquakeDatabase:
    def __init__(self) -> None:
        self.earthquakes: list[Earthquake] = []
        
    def load_data(self, path: str) -> None:
        with open(path, newline="") as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                quake = Earthquake(
                    row[0],
                    float(row[1]),
                    int(row[2]),
                    float(row[3]),
                    float(row[4]),
                    float(row[5]),
                    float(row[6]),
                    row[7],
                    int(row[8]),
                    datetime.strptime(row[9], "%Y-%m-%d %H:%M:%S"),
                )
                self.earthquakes.append(quake)


    def find_by_id(self, id: str) -> Earthquake | None:
        for quake in self.earthquakes:
            if quake.id == id:
                return quake
        return None
    
    
    def find_by_location(self, location: str) -> list[Earthquake]:
        target = location.lower()
        results = []
        # go backwards so results are newest to oldest
        for i in range(len(self.earthquakes) - 1, -1, -1):
            if self.earthquakes[i].location.lower() == target:
                results.append(self.earthquakes[i])
        return results
        
        
    def find_strongest(self) -> Earthquake | None:
        if len(self.earthquakes) == 0:
            return None
        strongest = self.earthquakes[0]
        for quake in self.earthquakes:
            if quake.magnitude > strongest.magnitude:
                strongest = quake
        return strongest


    def find_nearby(self, latitude: float, longitude: float, radius_km: float) -> list[Earthquake]:
        R = 6367.445  # earth radius in km
        phi1 = math.radians(latitude)
        lam1 = math.radians(longitude)
        results = []
        for quake in self.earthquakes:
            phi2 = math.radians(quake.latitude)
            lam2 = math.radians(quake.longitude)
            d_phi = (phi2 - phi1) / 2
            d_lam = (lam2 - lam1) / 2
            a = math.sin(d_phi) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lam) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            if R * c <= radius_km:
                results.append(quake)
        return results


    def find_k_strongest(self, k: int) -> list[Earthquake]:
        remaining = self.earthquakes.copy()  # copy so the original list is not changed
        results = []
        for _ in range(min(k, len(remaining))):
            best = 0
            for i in range(1, len(remaining)):
                if remaining[i].magnitude > remaining[best].magnitude:
                    best = i
            results.append(remaining.pop(best))
        return results
    
    
    def find_duplicate(self) -> str:
        seen = set()
        for quake in self.earthquakes:
            if quake.id in seen:
                return quake.id
            seen.add(quake.id)
        return "Not found"
    
    
    def find_busiest_day(self) -> int:
        window = timedelta(hours=24)
        best = 0
        start = 0
        for end in range(len(self.earthquakes)):
            # move the start forward until the window is under 24 hours
            while self.earthquakes[end].time - self.earthquakes[start].time >= window:
                start += 1
            best = max(best, end - start + 1)
        return best
    

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
