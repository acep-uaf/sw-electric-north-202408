DROP TABLE aetr_generation;
CREATE TABLE aetr_generation(
    "year" BIGINT,
    plant_name VARCHAR,
    aea_energy_region VARCHAR,
    source VARCHAR,
    data_version VARCHAR,
    fuel_type VARCHAR,
    generation NUMERIC,
    acep_region VARCHAR);