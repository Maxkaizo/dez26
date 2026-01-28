import os
import pandas as pd
from sqlalchemy import create_engine

# ---- Config (ajusta esto) ----
PARQUET_PATH = "01_docker_tf/hw/green_tripdata_2025-11.parquet"     # ruta al parquet en tu host
TABLE_NAME   = "green_trips"
DB_NAME      = "ny_taxi"
DB_USER      = "postgres"
DB_PASS      = "postgres"
DB_HOST      = "localhost"
DB_PORT      = "5433"                  # el puerto mapeado en docker-compose
SCHEMA       = "public"                # opcional

# ---- Engine ----
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---- Read parquet ----
df = pd.read_parquet(PARQUET_PATH)

# (opcional) limpia nombres de columnas problemáticos
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# ---- Load ----
# if_exists: "replace" crea de cero, "append" agrega
df.to_sql(TABLE_NAME, engine, schema=SCHEMA, if_exists="replace", index=False, method="multi")

print(f"Loaded {len(df):,} rows into {SCHEMA}.{TABLE_NAME}")
