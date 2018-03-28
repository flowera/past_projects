/*
Import Epic data into postgresql
http://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/
import errors references:
https://stackoverflow.com/questions/18297980/pg-copy-error-invalid-input-syntax-for-integer
*/
drop table cap_info;
CREATE TABLE cap_info
(
	id serial NOT NULL,
	log_id numeric,	
	proc_code numeric,
	implanted_date timestamp,
	sap varchar,
	model_number varchar,
	qty	int,
	implant_name varchar,
	cap_price money,
	vendor_num varchar,
	vendor_name varchar
);
COPY 
	cap_info(log_id, proc_code, implanted_date, sap, model_number, qty, implant_name, cap_price, vendor_num, vendor_name)
FROM '\\hosp1serv1\SS_OPERSCH\Databases\Epic_Implants_Database\Epic_Downloads\Implants\201603 Implants\cap_info_fixed.csv' DELIMITER ',' CSV HEADER;

/* 
Add primary key to implants table 
*/
ALTER TABLE implants ADD COLUMN id SERIAL PRIMARY KEY;
/*
implants: Add month column and rm trailing-spaces-with-postgresql
*/
SELECT 	*,
	regexp_replace(vendor, '\s+$', '') as vendor_name,
	regexp_replace(or_procedure_name, '\s+$', '') as procedure_name,
	to_char( surgery_date, 'MON') as surgery_month
INTO 	implants_cp
from 	implants;

/*  
total
*/
SELECT * 
	INTO pre_total
FROM 
	implants_cp
where 
		procedure_name LIKE '%TOTAL%'
	OR 
		procedure_name LIKE '%UNICONDYLAR%'
	OR
		implant_name LIKE '%TOTAL%'
ORDER BY 
	case_nbr DESC, cost_per_unit DESC
;

-- rm revisions data
DELETE FROM pre_total
WHERE procedure_name LIKE '%REVISION%'
OR implant_name LIKE '%REVISION%'
;
-- deduplicate case_nbr
SELECT *
	INTO total
FROM 
	pre_total
WHERE id IN (
  SELECT MIN(id) FROM total GROUP BY case_nbr
)
;

SELECT * from total;
/*Permission better use E: drive*/
COPY total TO 'E:\ComplianceReport_TotalJoints\total.csv' DELIMITER ',' CSV HEADER;

/*
Back to Implants
*/
SELECT * 
	INTO 	pre_revisions
FROM 
	implants_cp
where 
	procedure_name LIKE '%REVISION%'
	OR
		implant_name LIKE '%REVISION%'
ORDER BY 
	case_nbr DESC, cost_per_unit DESC
;
-- deduplicate case_nbr
SELECT *
	INTO 	revisions
FROM 
	pre_revisions
WHERE id IN (
  SELECT MIN(id) FROM revisions GROUP BY case_nbr
)
;

/*
Run revision reports
*/

SELECT 
	r.id, 
	r.case_nbr,
	r.sort_yr,
	r.surgery_month,
	r.procedure_name,
	r.vendor_name
	INTO 	pre_revisions_report
FROM	
		pre_revisions r
;
select 	procedure_name,
		vendor_name,
		sort_yr,
		sum((month = 'JUN')::int) as JUN,
		sum((month = 'MAY')::int) as MAY,
		sum((month = 'APR')::int) as APR
into 	revisions_summary
from 	pre_revisions_report
group by 	vendor_name, procedure_name
order by 	procedure_name;

SELECT *,
COALESCE(jun,0) + COALESCE(may,0) + COALESCE(apr,0) AS sum
INTO revisions_f
FROM revisions_summary;


/*
Run total reports
*/
SELECT 
		r.id, 
		r.case_nbr,
		r.sort_yr,
		r.surgery_month,
		r.procedure_name,
		r.vendor_name
	INTO 	pre_total_report
FROM	
		pre_total r
;
select 	procedure_name,
		vendor_name,
		sort_yr,
		sum((month = 'JUN')::int) as JUN,
		sum((month = 'MAY')::int) as MAY,
		sum((month = 'APR')::int) as APR
into 	total_summary
from 	pre_total_report
group by 	vendor_name, procedure_name
order by 	procedure_name;

SELECT *,
COALESCE(jun,0) + COALESCE(may,0) + COALESCE(apr,0) AS grand_total
INTO total_f
FROM total_summary;


/*save as csv*/

COPY revisions_f TO 'E:\ComplianceReport_TotalJoints\revisions_f.csv' DELIMITER ',' CSV HEADER;
COPY total_f TO 'E:\ComplianceReport_TotalJoints\total_f.csv' DELIMITER ',' CSV HEADER;










/*final report*/

select 	vendor_name,
		procedure_name,
       sum((month = 'JUN')::int) as JUN,
       sum((month = 'MAY')::int) as MAY,
       sum((month = 'APR')::int) as APR
into 	final_revisions
from 	pre_revisions_report
group by vendor_name, procedure_name
order by vendor_name;


/*final report*/

select vendor_name,
		procedure_name,
       sum((month = 'JUN')::int) as JUN,
       sum((month = 'MAY')::int) as MAY,
       sum((month = 'APR')::int) as APR
	   
into final_rep_total
from total_report_1
group by vendor_name, procedure_name
order by vendor_name;


/* Check if it's right */
SELECT implant_name, case_nbr, cost_per_unit, vendor from revisions
WHERE 
--vendor like '%DEP%'
case_nbr = 460943
or case_nbr = 459727
or case_nbr = 454042
;

/*
revision: Add month column and rm trailing-spaces-with-postgresql
*/
SELECT 	*,
	regexp_replace(vendor, '\s+$', '') as vendor_name,
	regexp_replace(or_procedure_name, '\s+$', '') as procedure_name,
	to_char( surgery_date, 'MON') as month
INTO 	revisions_report
from 	pre_revisions_report;

/*
total: Add month column and rm trailing-spaces-with-postgresql
*/
SELECT 	*,
	regexp_replace(vendor, '\s+$', '') as vendor_name,
	regexp_replace(or_procedure_name, '\s+$', '') as procedure_name,
	to_char( surgery_date, 'MON') as month
INTO 	total_report
from 	pre_total_report;







/*
find ans: 
https://www.postgresql.org

*/





/*Permission better use E: drive*/
COPY total_res TO 'E:\ComplianceReport_TotalJoints\total_joints_procedures.csv' DELIMITER ',' CSV HEADER;

COPY 
(SELECT 	r.case_nbr,
	r.sort_yr,
	r.surgery_date,
	r.or_procedure_name,
	r.vendor
FROM	
	revisions r

)
TO 'E:\ComplianceReport_TotalJoints\report.csv' DELIMITER ',' CSV HEADER;

/*test*/


select 	
		vendor,
		date_trunc('month',surgery_date) as mon,
		count(id)
        INTO report_1
from report
group by mon,vendor
order by vendor
;



CREATE EXTENSION tablefunc;

SELECT *
FROM   crosstab(
      'SELECT vendor, month, count
       FROM   report_2
       ORDER  BY 1,2')
AS count ("vendor" text, "APR" text, "MAY" text, "JUN" text);

/*test*/
select extract(month from surgery_date) from report;


/*
https://stackoverflow.com/questions/22699535/trim-trailing-spaces-with-postgresql
https://www.postgresql.org
remove trailing-spaces-with-postgresql
*/
SELECT regexp_replace(vendor, '\s+$', '') FROM report;


/*test*/
select 	
		vendor,
		month,
		count(id) AS qty
        INTO report_2
from report_1
group by month,vendor
order by vendor
;
SELECT *
FROM   crosstab(
      'SELECT vendor, month, qty
       FROM   report_2
       ORDER  BY 1,2')
AS qty ("vendor" text, "APR" text, "MAY" text, "JUN" text);

































