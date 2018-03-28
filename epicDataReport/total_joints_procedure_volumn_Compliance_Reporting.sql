/*
Import Epic data into postgresql
http://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/
import errors references:
https://stackoverflow.com/questions/18297980/pg-copy-error-invalid-input-syntax-for-integer
*/

-- Database: "Epic_Implants"
/* SQL pane */
-- DROP DATABASE "Epic_Implants";

CREATE DATABASE "Epic_Implants"
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'English_United States.1252'
       LC_CTYPE = 'English_United States.1252'
       CONNECTION LIMIT = -1;
/*
1. Create the following 8 tables
*/
/* cap_info */
drop table if exists cap_info;
CREATE TABLE cap_info
(
	id serial NOT NULL,
	log_id varchar,	
	proc_code varchar,
	implanted_date timestamp,
	sap varchar,
	model_number varchar,
	qty	numeric,
	implant_name varchar,
	cap_price money,
	vendor_num varchar,
	vendor_name varchar
);
/* case_info */
drop table if exists case_info;
CREATE TABLE case_info
(
	id serial NOT NULL,
	case_nbr varchar,	
	surgery_date timestamp,
	mth varchar,
	sort_mth numeric, 
	sort_yr numeric, 
	area varchar
);
/* diag_info */
drop table if exists diag_info;
CREATE TABLE diag_info
(
	id serial NOT NULL,
	case_nbr varchar,
	diag_code varchar,
	diag_name varchar,
	final_drg varchar 
);

/* eap_proced_info */
drop table if exists eap_proced_info;
CREATE TABLE eap_proced_info
(
	id serial NOT NULL,
	case_nbr varchar, 
	eap_code varchar,
	eap_name varchar 
);

/* pat_info */
drop table if exists pat_info;
CREATE TABLE pat_info 
(
	id serial NOT NULL,
	log_id varchar, 
	surgery_date timestamp,
	adm_time timestamp,
	dischtime timestamp,
	los numeric,
	age numeric,
	last_name varchar,
	first_name varchar,
	mrn varchar
);

/* supply_info */
drop table if exists supply_info;
CREATE TABLE supply_info
(
	id serial NOT NULL,
	case_nbr varchar, 
	model_number varchar, 
	implant_name varchar,
	cost_per_unit money,
	vendor varchar, 
	sap varchar, 
	vendor_id varchar,
	qty numeric
);

/* surg_info */
drop table if exists surg_info;
CREATE TABLE surg_info
(
	id serial NOT NULL,
	case_nbr varchar,
	surgeon_id varchar,
	surgeon varchar,
	service varchar,
	department varchar
);

/* surg_proced_info */
drop table if exists surg_proced_info;
CREATE TABLE surg_proced_info
(
	id serial NOT NULL,
	case_nbr varchar,
	or_procedure varchar,
	or_procedure_name varchar
);


-- Total Joints Procedure Volumn Compliance Reporting(Quarterly)

/* qryOrtho-Joints Total -- MS-SQL version
SELECT Case_info.case_nbr, Pat_info.mrn, Case_info.sort_mth, Case_info.sort_yr, Case_info.surgery_date, Pat_info.last_name, Pat_info.first_name, Surg_proced_info.or_procedure, Surg_proced_info.or_procedure_name, Supply_info.vendor, Supply_info.vendor_id, Supply_info.model_number, Supply_info.sap, Supply_info.implant_name, Supply_info.qty, Supply_info.cost_per_unit, Surg_info.surgeon, Surg_info.service, Surg_info.department
FROM Case_info INNER JOIN (Pat_info INNER JOIN ((Supply_info INNER JOIN Surg_proced_info ON Supply_info.case_nbr = Surg_proced_info.case_nbr) INNER JOIN Surg_info ON Supply_info.case_nbr = Surg_info.case_nbr) ON Pat_info.log_id = Surg_proced_info.case_nbr) ON Case_info.case_nbr = Pat_info.log_id
WHERE (((Case_info.surgery_date) Between #1/1/2017# And #3/31/2017#) AND ((Surg_proced_info.or_procedure_name) Like "*arthroplasty*" And (Surg_proced_info.or_procedure_name) Like "*total*"));
*/

/*
total-joints --> Add Surgery year and month
*/
drop table if exists joints_total;
SELECT case_info.case_nbr, pat_info.mrn, case_info.sort_mth, case_info.sort_yr, case_info.surgery_date, pat_info.last_name, pat_info.first_name, surg_proced_info.or_procedure, surg_proced_info.or_procedure_name, supply_info.vendor, supply_info.vendor_id, supply_info.model_number, supply_info.sap, supply_info.implant_name, supply_info.qty, supply_info.cost_per_unit, surg_info.surgeon, surg_info.service, surg_info.department,
to_char(case_info.surgery_date, 'YYYY-MM') As surgery_month
INTO joints_total
FROM case_info
INNER JOIN pat_info ON case_info.case_nbr = pat_info.log_id
INNER JOIN surg_proced_info ON pat_info.log_id = surg_proced_info.case_nbr
INNER JOIN supply_info ON supply_info.case_nbr = surg_proced_info.case_nbr 
INNER JOIN surg_info ON supply_info.case_nbr = surg_info.case_nbr 
WHERE
	to_char(case_info.surgery_date, 'YYYY-MM') between '2017-01' and '2017-07' 
	AND 
		surg_proced_info.or_procedure_name Like '%ARTHROPLASTY%'
	/* Q: OR or AND ?????????????? */
	OR surg_proced_info.or_procedure_name Like '%TOTAL%'
	--AND supply_info.implant_name Like '%TOTAL%'
	AND surg_proced_info.or_procedure_name Like '%UNICONDYLAR%'
;
--ALTER TABLE joints_total ADD COLUMN id SERIAL PRIMARY KEY;

/*  
total
*/
drop table if exists pre_total;
SELECT * 
	INTO pre_total
FROM 
	joints_total
where 
		or_procedure_name LIKE '%TOTAL%'
	OR 
		or_procedure_name LIKE '%UNICONDYLAR%'
	AND
		implant_name LIKE '%TOTAL%'
ORDER BY 
	case_nbr DESC, cost_per_unit DESC
;
ALTER TABLE pre_total ADD COLUMN id SERIAL PRIMARY KEY;
-- rm revisions data
DELETE FROM pre_total
WHERE or_procedure_name LIKE '%REVISION%'
OR implant_name LIKE '%REVISION%'
;
-- deduplicate case_nbr
drop table if exists total;
SELECT *
	INTO total
FROM 
	pre_total
WHERE id IN (
  SELECT MIN(id) FROM pre_total GROUP BY case_nbr
)
;

SELECT * from total;



/*
Revisions
*/
drop table if exists pre_revisions;
SELECT * 
	INTO	pre_revisions
FROM 
	joints_total
where 
	or_procedure_name LIKE '%REVISION%'
	OR
		implant_name LIKE '%REVISION%'
ORDER BY 
	case_nbr DESC, cost_per_unit DESC
;
ALTER TABLE pre_revisions ADD COLUMN id SERIAL PRIMARY KEY;

-- deduplicate case_nbr
drop table if exists revisions;
SELECT *
	INTO 	revisions
FROM 
	pre_revisions
WHERE id IN (
  SELECT MIN(id) FROM pre_revisions GROUP BY case_nbr
)
;
SELECT * from revisions;


/*
Run revision/total reports
*/
drop table if exists revisions_sum;
select 	vendor,
		or_procedure_name,
       sum((sort_mth = 6)::int) as JUN,
       sum((sort_mth = 5)::int) as MAY,
       sum((sort_mth = 4)::int) as APR
into 	revisions_sum
from 	revisions
group by vendor, or_procedure_name
order by vendor;
select * from revisions_sum;


drop table if exists total_sum;
select 	vendor,
		or_procedure_name,
       sum((sort_mth = 6)::int) as JUN,
       sum((sort_mth = 5)::int) as MAY,
       sum((sort_mth = 4)::int) as APR
into 	total_sum
from 	total
group by vendor, or_procedure_name
order by vendor;
/*save as csv*/

COPY revisions_sum TO 'E:\ComplianceReport_TotalJoints\revisions_sum.csv' DELIMITER ',' CSV HEADER;
COPY total_sum TO 'E:\ComplianceReport_TotalJoints\total_sum.csv' DELIMITER ',' CSV HEADER;

