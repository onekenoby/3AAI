		select  
			tm tm,
			knt,
			ae,
			case 
				when ae >=0 and ae <=0.40 then 0
				when ae >0.40 and ae <=0.55 then 1
				when ae >0.55 and ae <=1.00 then 2 END
			as ae_cl,
			translate(translate(rv,'[',''),']','') rv
		from 
		(
			select 	
			pkt_time::timestamp tm, 
			ae_value ae,	   
			(select jsonb_agg(t -> 'rv')::text from json_array_elements(pkt_metric) as x(t)) as rv,
			jsonb_array_length((select jsonb_agg(t -> 'rv')::jsonb from json_array_elements(pkt_metric) as x(t))) knt
			from measurement
			where id_topic = 4 and (ae_value >=0 and ae_value <=0.40 ) and ae_value <> 'NaN'::NUMERIC
			limit 10000
		) r_v

union all

		select  
			tm tm,
			knt,
			ae,
			case 
				when ae >=0 and ae <=0.40 then 0
				when ae >0.40 and ae <=0.55 then 1
				when ae >0.55 and ae <=1.00 then 2 END
			as ae_cl,
			translate(translate(rv,'[',''),']','') rv
		from 
		(
			select 	
			pkt_time::timestamp tm, 
			ae_value ae,	   
			(select jsonb_agg(t -> 'rv')::text from json_array_elements(pkt_metric) as x(t)) as rv,
			jsonb_array_length((select jsonb_agg(t -> 'rv')::jsonb from json_array_elements(pkt_metric) as x(t))) knt
			from measurement
			where id_topic = 4 and (ae_value >0.40 and ae_value <=0.55 ) and ae_value <> 'NaN'::NUMERIC
			limit 5000
		) r_v
		
union all

		select  
			tm tm,
			knt,
			ae,
			case 
				when ae >=0 and ae <=0.40 then 0
				when ae >0.40 and ae <=0.55 then 1
				when ae >0.55 and ae <=1.00 then 2 END
			as ae_cl,
			translate(translate(rv,'[',''),']','') rv
		from 
		(
			select 	
			pkt_time::timestamp tm, 
			ae_value ae,	   
			(select jsonb_agg(t -> 'rv')::text from json_array_elements(pkt_metric) as x(t)) as rv,
			jsonb_array_length((select jsonb_agg(t -> 'rv')::jsonb from json_array_elements(pkt_metric) as x(t))) knt
			from measurement
			where id_topic = 4 and (ae_value >0.55 and ae_value <=1 ) and ae_value <> 'NaN'::NUMERIC
			limit 5000
		) r_v