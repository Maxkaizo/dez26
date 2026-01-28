import pandas as pd
from sqlalchemy import create_engine

# ---- Config ----
CSV_PATH   = "01_docker_tf/hw/taxi_zone_lookup.csv"  # ruta al CSV
TABLE_NAME = "taxi_zones"
DB_NAME    = "ny_taxi"
DB_USER    = "postgres"
DB_PASS    = "postgres"
DB_HOST    = "localhost"
DB_PORT    = "5433"
SCHEMA     = "public"

# ---- Engine ----
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---- Read CSV ----
df = pd.read_csv(CSV_PATH)

# Limpieza básica de columnas
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# ---- Load ----
df.to_sql(
    TABLE_NAME,
    engine,
    schema=SCHEMA,
    if_exists="replace",   # tabla pequeña, se puede recrear sin problema
    index=False,
    method="multi"
)

print(f"Loaded {len(df):,} rows into {SCHEMA}.{TABLE_NAME}")
