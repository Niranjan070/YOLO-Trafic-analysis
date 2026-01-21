import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tracking_output.csv")

print("Total rows:", len(df))
print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

vehicle_classes = ["car", "truck", "bus", "motorbike", "bicycle"]
df = df[df["class"].isin(vehicle_classes)]

unique_vehicles = df["track_id"].nunique()
print("Unique vehicles:", unique_vehicles)

print(df.groupby("class")["track_id"].nunique())

df["time_sec"] = df["frame"] / 30
df["minute"] = (df["time_sec"] // 60).astype(int)

vehicles_per_min = df.groupby("minute")["track_id"].nunique()
print(vehicles_per_min)



vehicles_per_min.plot(kind="bar")
plt.title("Vehicles per Minute")
plt.xlabel("Minute")
plt.ylabel("Vehicle Count")
plt.tight_layout()
plt.show()
