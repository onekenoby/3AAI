from openai.types.chat import ChatCompletionMessageParam
import openai

def build_prompt(query, context):
    system: ChatCompletionMessageParam = {
        "role": "system",
        "content": "Ti faccio una domanda alla quale vorrei che tu rispondessi, capendo il significato e trasformandolo"
                   " generando solamente una query SQL per un database PostgreSQL,"
                   " basandoti solo sulla DDL fornita qui di seguito e il contesto in input."
                   " Utilizza solamente SELECT statements."
                   " Se non puoi dare una risposta: rispondi N/A"
        """"
        --
-- PostgreSQL database dump

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alert; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alert (
    id bigint NOT NULL,
    id_topic integer NOT NULL,
    trigger_time timestamp with time zone DEFAULT now() NOT NULL,
    expired_time timestamp with time zone,
    pkt_uid text NOT NULL,
    ae_value double precision NOT NULL
);


ALTER TABLE public.alert OWNER TO postgres;

--
-- Name: alert_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alert_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.alert_id_seq OWNER TO postgres;

--
-- Name: alert_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alert_id_seq OWNED BY public.alert.id;


--
-- Name: alert_severity; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alert_severity (
    id smallint NOT NULL,
    severity smallint NOT NULL,
    label character varying(30) NOT NULL,
    display_color_hex character varying(7) NOT NULL,
    threshold numeric(18,3)
);


ALTER TABLE public.alert_severity OWNER TO postgres;

--
-- Name: alert_state_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alert_state_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.alert_state_id_seq OWNER TO postgres;

--
-- Name: alert_state_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alert_state_id_seq OWNED BY public.alert_severity.id;


--
-- Name: alert_work; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alert_work (
    id bigint NOT NULL,
    id_alert bigint NOT NULL,
    evt_time timestamp with time zone DEFAULT now() NOT NULL,
    evt_type_id smallint NOT NULL,
    notes text
);


ALTER TABLE public.alert_work OWNER TO postgres;

--
-- Name: alert_work_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alert_work_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.alert_work_id_seq OWNER TO postgres;

--
-- Name: alert_work_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alert_work_id_seq OWNED BY public.alert_work.id;


--
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id integer DEFAULT nextval(('public.customer_id_seq'::text)::regclass) NOT NULL,
    label character varying(30) NOT NULL
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: sensor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sensor (
    id integer NOT NULL,
    site_id integer NOT NULL,
    topic text NOT NULL,
    label character varying(30),
    alias character varying(30)
);


ALTER TABLE public.sensor OWNER TO postgres;

--
-- Name: sensor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sensor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sensor_id_seq OWNER TO postgres;

--
-- Name: sensor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sensor_id_seq OWNED BY public.sensor.id;


--
-- Name: site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.site (
    id integer NOT NULL,
    id_customer integer NOT NULL,
    label character varying(64) NOT NULL,
    location_address character varying(64),
    location_city character varying(30),
    location_zip character varying(12),
    location_province character varying(24),
    location_country character varying(2) DEFAULT 'IT'::character varying,
    location_coordinate point
);


ALTER TABLE public.site OWNER TO postgres;

--
-- Name: site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.site_id_seq OWNER TO postgres;

--
-- Name: site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.site_id_seq OWNED BY public.site.id;


--
-- Name: alert id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert ALTER COLUMN id SET DEFAULT nextval('public.alert_id_seq'::regclass);


--
-- Name: alert_severity id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert_severity ALTER COLUMN id SET DEFAULT nextval('public.alert_state_id_seq'::regclass);


--
-- Name: alert_work id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert_work ALTER COLUMN id SET DEFAULT nextval('public.alert_work_id_seq'::regclass);


--
-- Name: sensor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor ALTER COLUMN id SET DEFAULT nextval('public.sensor_id_seq'::regclass);


--
-- Name: site id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.site ALTER COLUMN id SET DEFAULT nextval('public.site_id_seq'::regclass);


--
-- Data for Name: alert; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alert (id, id_topic, trigger_time, expired_time, pkt_uid, ae_value) VALUES (1, 5, '2022-10-14 09:58:25.211802+02', NULL, 'cd4hav0uke1r4evog9d0', 0.317388000000000003);


--
-- Name: alert_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alert_id_seq', 1, true);


--
-- Data for Name: alert_severity; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alert_severity (id, severity, label, display_color_hex, threshold) VALUES (1, 10, 'GIALLO', '#ffcc00', 0.550);
INSERT INTO public.alert_severity (id, severity, label, display_color_hex, threshold) VALUES (3, 1000, 'ROSSO', '#cc3300', 0.400);
INSERT INTO public.alert_severity (id, severity, label, display_color_hex, threshold) VALUES (2, 100, 'ARANCIO', '#ff9966', 0.450);


--
-- Name: alert_state_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alert_state_id_seq', 3, true);


--
-- Data for Name: alert_work; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alert_work (id, id_alert, evt_time, evt_type_id, notes) VALUES (3, 1, '2022-10-14 11:31:54.375525+02', 33, 'est');


--
-- Name: alert_work_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alert_work_id_seq', 3, true);


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.customer (id, label) VALUES (1, 'SAE');


--
-- Data for Name: sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.sensor (id, site_id, topic, label, alias) VALUES (3, 3, '/sensors/delta/lab03/9ca525849f27-00', 'Sensore 01 LF', NULL);
INSERT INTO public.sensor (id, site_id, topic, label, alias) VALUES (2, 3, '/sensors/delta/lab03/9ca525849f35-00', 'Sensore 01 HF', NULL);
INSERT INTO public.sensor (id, site_id, topic, label, alias) VALUES (1, 3, '/sensors/delta/lab03/0050c2de0007-00', 'Sensore Test 101', NULL);
INSERT INTO public.sensor (id, site_id, topic, label, alias) VALUES (5, 3, '/sensors/delta/lab03/0050c2de0030-00', 'Sensore Test 102', NULL);
INSERT INTO public.sensor (id, site_id, topic, label, alias) VALUES (6, 3, '/sensors/delta/lab03/0050c2de0032-00', 'Sensore Test 103', NULL);
INSERT INTO public.sensor (id, site_id, topic, label, alias) VALUES (4, 3, '/sensors/delta/lab03/0050c2de0035-00', 'Sensore Test 104', NULL);


--
-- Name: sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_id_seq', 6, true);


--
-- Data for Name: site; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.site (id, id_customer, label, location_address, location_city, location_zip, location_province, location_country, location_coordinate) VALUES (3, 1, 'LAB03', NULL, 'Roma', '00100', 'RM', 'IT', NULL);


--
-- Name: site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.site_id_seq', 3, true);


--
-- Name: alert alert_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert
    ADD CONSTRAINT alert_pkey PRIMARY KEY (id);


--
-- Name: alert_severity alert_severity_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert_severity
    ADD CONSTRAINT alert_severity_pkey PRIMARY KEY (id);


--
-- Name: alert_work alert_work_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert_work
    ADD CONSTRAINT alert_work_pkey PRIMARY KEY (id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);


--
-- Name: alert idx_alert-trigger_time_pkt_uid; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert
    ADD CONSTRAINT "idx_alert-trigger_time_pkt_uid" UNIQUE (trigger_time, pkt_uid);


--
-- Name: sensor idx_sensor-topic; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT "idx_sensor-topic" UNIQUE (topic);


--
-- Name: site idx_site-id_customer; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.site
    ADD CONSTRAINT "idx_site-id_customer" UNIQUE (id_customer) WITH (fillfactor='100');


--
-- Name: sensor sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_pkey PRIMARY KEY (id);


--
-- Name: site site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.site
    ADD CONSTRAINT site_pkey PRIMARY KEY (id);


--
-- Name: idx_alert-expired_time; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "idx_alert-expired_time" ON public.alert USING btree (expired_time) WITH (fillfactor='100');


--
-- Name: idx_alert-id_topic; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "idx_alert-id_topic" ON public.alert USING btree (id_topic);


--
-- Name: idx_alert_work-evt_time; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "idx_alert_work-evt_time" ON public.alert_work USING btree (evt_time);


--
-- Name: idx_alert_work-evt_type_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "idx_alert_work-evt_type_id" ON public.alert_work USING btree (evt_type_id);


--
-- Name: idx_alert_work-id_alert; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "idx_alert_work-id_alert" ON public.alert_work USING btree (id_alert);


--
-- Name: idx_customer-label; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "idx_customer-label" ON public.customer USING btree (label);


--
-- Name: idx_sensor-id_site; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "idx_sensor-id_site" ON public.sensor USING btree (site_id) WITH (fillfactor='100');


--
-- Name: alert_work fk_alert_work-alert_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alert_work
    ADD CONSTRAINT "fk_alert_work-alert_id" FOREIGN KEY (id_alert) REFERENCES public.alert(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: sensor fk_sensor-site_id_site-id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT "fk_sensor-site_id_site-id" FOREIGN KEY (site_id) REFERENCES public.site(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: site fk_site-id_customer_customer_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.site
    ADD CONSTRAINT "fk_site-id_customer_customer_id" FOREIGN KEY (id_customer) REFERENCES public.customer(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: TABLE customer; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.customer TO grafreader;


--
-- Name: TABLE sensor; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.sensor TO grafreader;


--
-- Name: TABLE site; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.site TO grafreader;


--
-- PostgreSQL database dump complete
--



--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.24
-- Dumped by pg_dump version 9.6.24

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: measurement; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.measurement (
    pkt_time timestamp with time zone NOT NULL,
    sndr_host text,
    id_topic integer,
    pkt_uid text NOT NULL,
    pkt_metric json,
    pkt_mode smallint,
    ae_value double precision
);


ALTER TABLE public.measurement OWNER TO postgres;

--
-- Name: idx_measurement-pkt_time; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "idx_measurement-pkt_time" ON public.measurement USING btree (pkt_time DESC);


--
-- Name: idx_measurement-pkt_time_pkt_uid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "idx_measurement-pkt_time_pkt_uid" ON public.measurement USING btree (pkt_time DESC, pkt_uid DESC);


--
-- Name: measurement ts_insert_blocker; Type: TRIGGER; Schema: public; Owner: postgres
--



--
-- Name: measurement fk_measure-id_topic_sensor_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.measurement
    ADD CONSTRAINT "fk_measure-id_topic_sensor_id" FOREIGN KEY (id_topic) REFERENCES public.sensor(id) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: TABLE measurement; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.measurement TO grafreader;


--
-- PostgreSQL database dump complete
--

--Function: public.record_alert()

CREATE OR REPLACE FUNCTION record_alert()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
  IF NEW.ae_value < 0.55 THEN
    INSERT INTO alert(id_topic, pkt_uid, ae_value)
    VALUES(NEW.id_topic, NEW.pkt_uid, NEW.ae_value);
  END IF;

	RETURN NEW;
END;
$$

--Trigger: public.measurement.check_aevalue_for_alert

CREATE TRIGGER check_aevalue_for_alert
  AFTER INSERT
  ON public.measurement
  FOR EACH ROW
  EXECUTE PROCEDURE public.record_alert();
  """

    }
    user: ChatCompletionMessageParam = {
        "role": "user",
        "content": f"La domanda è {query}. Questo è tutto il contesto che hai:"
        f'{(" ").join(context)}',
    }

    return [system, user]



def get_chatGPT_response(query, context, model_name):
    response = openai.chat.completions.create(
        model=model_name,
        messages=build_prompt(query, context),
    )
    return response.choices[0].message.content  # type: ignore
