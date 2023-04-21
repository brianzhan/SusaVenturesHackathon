import pandas as pd

# Synthetic data (use real data as needed)
data = {
    "location_id": [1, 2, 3, 4],
    "population": [10000, 15000, 12000, 8000],
    "energy_demand_5_years": [50000, 55000, 45000, 30000],
    "current_capacity": [40000, 45000, 40000, 25000],
    "wind_potential": [0.7, 0.3, 0.5, 0.6],
    "solar_potential": [0.3, 0.7, 0.5, 0.4]
}

df = pd.DataFrame(data)

# Assumptions
fixed_budget_per_capita = 1000

def calculate_energy_deficit(row):
    return row["energy_demand_5_years"] - row["current_capacity"]

def calculate_investment_needed(row, budget_per_capita):
    return row["population"] * budget_per_capita

def optimal_wind_solar_mix(row):
    total_potential = row["wind_potential"] + row["solar_potential"]
    wind_share = row["wind_potential"] / total_potential
    solar_share = row["solar_potential"] / total_potential
    return wind_share, solar_share

# Calculate energy deficit, investment needed, and optimal wind-solar mix
df["energy_deficit"] = df.apply(calculate_energy_deficit, axis=1)
df["investment_needed"] = df.apply(calculate_investment_needed, axis=1, args=(fixed_budget_per_capita,))
df[["wind_share", "solar_share"]] = df.apply(optimal_wind_solar_mix, axis=1, result_type="expand")

# Sort locations by energy deficit (descending)
df_sorted = df.sort_values(by="energy_deficit", ascending=False)

# Print the resulting DataFrame
print(df_sorted)