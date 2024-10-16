DROP TABLE es_monthly_gen;
CREATE TABLE es_monthly_gen(
    "Year" BIGINT,
    "Month" BIGINT,
    "PLANTS_AEA plant ID" VARCHAR,
    "EIA Plant ID" NUMERIC,
    "PCE reporting ID" NUMERIC,
    "Combined Heat and Power Plant" NUMERIC,
    "PLANTS_Plant Name" VARCHAR,
    "OPERATOR_AEA Operator ID" VARCHAR,
    "OPERATOR_Operator Name" VARCHAR,
    "OPERATOR_EIA Operator ID" NUMERIC,
    "RCA CPCN" NUMERIC,
    "INTERTIES_Intertie ID" VARCHAR,
    "INTERTIES_Intertie Name" VARCHAR,
    "AEA Energy Region" VARCHAR,
    "Reported Prime Move" VARCHAR,
    "Data source" VARCHAR,
    "Reported Fuel Type Code" VARCHAR,
    "OPERATOR_Power Generation End Use" VARCHAR,
    "Fuel price" NUMERIC,
    "Physical Unit Label" VARCHAR,
    "Quantity Consumed in Physical Units for Electric Generation" NUMERIC,
    "Quantity Consumed For Electricity (MMBtu)" NUMERIC,
    "Electricity Generation [PCE=Gross, EIA=Net] 
    (MWh)" NUMERIC,
    "Unnamed: 23" NUMERIC);