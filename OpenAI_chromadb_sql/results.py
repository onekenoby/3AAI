

"""#Results

1) Dammi il range temporale solamente per il sensore 2 e aggiungi commenti ✅

SELECT
    min(pkt_time) AS range_temporale_minimo, -- Minimum timestamp for the given sensor
    max(pkt_time) AS range_temporale_massimo, -- Maximum timestamp for the given sensor
    id_topic AS sensori                    -- Sensor ID
FROM
    measurement
WHERE
    id_topic = 2                            -- Filter for sensor with id_topic 2
GROUP BY
    id_topic;                            -- Group by sensor ID

2) Mostrami tutti gli alert per il sensore 1 ✅

SELECT
    a.trigger_time,
    a.ae_value
FROM
    alert a
JOIN
    sensor s ON a.id_topic = s.id
WHERE
    s.id = 1

3) Mostrami per il sensore 1, 100 elementi, con timestamp, knt, ae, ae_cl,
dove ae_cl è 0, 1 o 2 per valori compresi rispettivamente tra 0 e 0.4, 0.4 e 0.55, 0.55 e 1.0, e i valori rv ✅

SELECT
    tm,
    knt,
    ae,
    CASE
        WHEN ae >= 0 AND ae <= 0.40 THEN 0
        WHEN ae > 0.40 AND ae <= 0.55 THEN 1
        WHEN ae > 0.55 AND ae <= 1.00 THEN 2
    END AS ae_cl,
    TRANSLATE(TRANSLATE(rv, '[', ''), ']', '') AS rv
FROM (
    SELECT
        pkt_time::TIMESTAMP tm,
        ae_value ae,
        (
            SELECT jsonb_agg(t ->> 'rv')::TEXT
            FROM json_array_elements(pkt_metric) AS x(t)
        ) AS rv,
        jsonb_array_length(
            (
                SELECT jsonb_agg(t ->> 'rv')::JSONB
                FROM json_array_elements(pkt_metric) AS x(t)
            )
        ) AS knt
    FROM
        measurement
    WHERE
        id_topic = 1
        AND ae_value >= 0
        AND ae_value <> 'NaN'::NUMERIC
    LIMIT 100
) r_v;
4) Per il sensore 3 mostrami la media, la minima e la massima del valore ae, su un intervallo di 3 minuti ❌

Bisogna utilizzare come keyword "time bucket" altrmienti non riesce a capire. La query seguente ha dato un risultato corretto:

Per il sensore 3 mostrami su un time bucket di 1 minuto la media, la minima e la massima del valore ae ✅

SELECT
  time_bucket('1 minute', pkt_time) as bucket,
  id_topic,
  avg(ae_value) as avg,
  max(ae_value) as max,
  min(ae_value) as min
FROM
  measurement
where id_topic = 3
GROUP BY bucket, id_topic
order by bucket;

5) Per il sensore 5 mostrami su un time bucket di 15 minuti la media, la minima e la massima del valore ae ✅

SELECT time_bucket('15 minute', pkt_time) as bucket, id_topic, avg(ae_value) as avg, max(ae_value) as max, min(ae_value) as min FROM measurement where id_topic = 5 GROUP BY bucket, id_topic order by bucket;
"""