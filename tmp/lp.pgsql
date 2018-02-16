--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;
CREATE ROLE srmehta;
ALTER ROLE srmehta WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'md5ddaed0838ac16bb27d172635e29b2c18';






--
-- Database creation
--

CREATE DATABASE logicplus WITH TEMPLATE = template0 OWNER = srmehta;
REVOKE ALL ON DATABASE logicplus FROM srmehta;
GRANT TEMPORARY ON DATABASE logicplus TO srmehta;
GRANT CREATE,CONNECT ON DATABASE logicplus TO srmehta WITH GRANT OPTION;
REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


\connect logicplus

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 9.6.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: lp; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA lp;


ALTER SCHEMA lp OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: citext; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;


--
-- Name: EXTENSION citext; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';


SET search_path = public, pg_catalog;

--
-- Name: email; Type: DOMAIN; Schema: public; Owner: srmehta
--

CREATE DOMAIN email AS citext
	CONSTRAINT email_check CHECK ((VALUE ~ '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zAZ0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'::citext));


ALTER DOMAIN email OWNER TO srmehta;

--
-- Name: phone; Type: DOMAIN; Schema: public; Owner: srmehta
--

CREATE DOMAIN phone AS citext
	CONSTRAINT phone_check CHECK ((VALUE ~ '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'::citext));


ALTER DOMAIN phone OWNER TO srmehta;

SET search_path = lp, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: admission_trnxs; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE admission_trnxs (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    phone public.phone,
    email public.email,
    study character varying(50) NOT NULL,
    course character varying(20) NOT NULL,
    address character varying(100) NOT NULL,
    gender boolean DEFAULT true,
    join_date character varying(25) NOT NULL,
    fees integer NOT NULL,
    active boolean DEFAULT true,
    dp character varying(30) NOT NULL,
    details character varying(1000) NOT NULL
);


ALTER TABLE admission_trnxs OWNER TO srmehta;

--
-- Name: admission_trnxs_fees_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE admission_trnxs_fees_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE admission_trnxs_fees_seq OWNER TO srmehta;

--
-- Name: admission_trnxs_fees_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE admission_trnxs_fees_seq OWNED BY admission_trnxs.fees;


--
-- Name: admission_trnxs_id_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE admission_trnxs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE admission_trnxs_id_seq OWNER TO srmehta;

--
-- Name: admission_trnxs_id_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE admission_trnxs_id_seq OWNED BY admission_trnxs.id;


--
-- Name: batch_trnxs; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE batch_trnxs (
    bid integer NOT NULL,
    cid integer NOT NULL,
    fid integer NOT NULL,
    day text NOT NULL,
    "time" text NOT NULL,
    active boolean DEFAULT false NOT NULL
);


ALTER TABLE batch_trnxs OWNER TO srmehta;

--
-- Name: batch_trnxs_bid_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE batch_trnxs_bid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE batch_trnxs_bid_seq OWNER TO srmehta;

--
-- Name: batch_trnxs_bid_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE batch_trnxs_bid_seq OWNED BY batch_trnxs.bid;


--
-- Name: course_trnxs; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE course_trnxs (
    id integer NOT NULL,
    cname character varying(20),
    duration character varying(30) NOT NULL,
    details character varying(1000) NOT NULL,
    active boolean DEFAULT true,
    fees integer
);


ALTER TABLE course_trnxs OWNER TO srmehta;

--
-- Name: course_trxns_id_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE course_trxns_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE course_trxns_id_seq OWNER TO srmehta;

--
-- Name: course_trxns_id_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE course_trxns_id_seq OWNED BY course_trnxs.id;


--
-- Name: faculty; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE faculty (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    email public.email,
    phone public.phone,
    website character varying(100) NOT NULL,
    company character varying(50) NOT NULL,
    post character varying(20) NOT NULL,
    dob date NOT NULL,
    address character varying(200) NOT NULL,
    gender boolean DEFAULT true,
    dp character varying(30),
    active boolean DEFAULT true
);


ALTER TABLE faculty OWNER TO srmehta;

--
-- Name: faculty_id_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE faculty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE faculty_id_seq OWNER TO srmehta;

--
-- Name: faculty_id_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE faculty_id_seq OWNED BY faculty.id;


--
-- Name: inquiry_trnxs; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE inquiry_trnxs (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    phone public.phone NOT NULL,
    email public.email NOT NULL,
    course character varying(20) NOT NULL,
    study character varying(20) NOT NULL,
    details character varying(20) NOT NULL,
    active boolean DEFAULT true,
    date date NOT NULL,
    gender boolean DEFAULT true
);


ALTER TABLE inquiry_trnxs OWNER TO srmehta;

--
-- Name: inquiry_trnxs_id_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE inquiry_trnxs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE inquiry_trnxs_id_seq OWNER TO srmehta;

--
-- Name: inquiry_trnxs_id_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE inquiry_trnxs_id_seq OWNED BY inquiry_trnxs.id;


--
-- Name: programe; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE programe (
    id integer NOT NULL,
    tech character varying(20) NOT NULL,
    framework character varying(20) NOT NULL,
    defination character varying(1000) NOT NULL
);


ALTER TABLE programe OWNER TO srmehta;

--
-- Name: programe_id_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE programe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE programe_id_seq OWNER TO srmehta;

--
-- Name: programe_id_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE programe_id_seq OWNED BY programe.id;


--
-- Name: technology; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE technology (
    id integer NOT NULL,
    tech character varying(20) NOT NULL,
    framework character varying(20),
    active boolean DEFAULT true
);


ALTER TABLE technology OWNER TO srmehta;

--
-- Name: technology_id_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE technology_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE technology_id_seq OWNER TO srmehta;

--
-- Name: technology_id_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE technology_id_seq OWNED BY technology.id;


--
-- Name: test; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE test (
    mobile public.phone NOT NULL,
    email public.email NOT NULL
);


ALTER TABLE test OWNER TO srmehta;

--
-- Name: user; Type: TABLE; Schema: lp; Owner: srmehta
--

CREATE TABLE "user" (
    id integer NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(20) NOT NULL,
    email public.email NOT NULL,
    mobile character varying(10) NOT NULL,
    last_login timestamp without time zone DEFAULT '2017-08-19 13:04:00'::timestamp without time zone,
    status boolean DEFAULT false,
    live boolean DEFAULT false,
    active boolean DEFAULT true
);


ALTER TABLE "user" OWNER TO srmehta;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: lp; Owner: srmehta
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE user_id_seq OWNER TO srmehta;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: lp; Owner: srmehta
--

ALTER SEQUENCE user_id_seq OWNED BY "user".id;


--
-- Name: admission_trnxs id; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY admission_trnxs ALTER COLUMN id SET DEFAULT nextval('admission_trnxs_id_seq'::regclass);


--
-- Name: admission_trnxs fees; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY admission_trnxs ALTER COLUMN fees SET DEFAULT nextval('admission_trnxs_fees_seq'::regclass);


--
-- Name: batch_trnxs bid; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY batch_trnxs ALTER COLUMN bid SET DEFAULT nextval('batch_trnxs_bid_seq'::regclass);


--
-- Name: course_trnxs id; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY course_trnxs ALTER COLUMN id SET DEFAULT nextval('course_trxns_id_seq'::regclass);


--
-- Name: faculty id; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY faculty ALTER COLUMN id SET DEFAULT nextval('faculty_id_seq'::regclass);


--
-- Name: inquiry_trnxs id; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY inquiry_trnxs ALTER COLUMN id SET DEFAULT nextval('inquiry_trnxs_id_seq'::regclass);


--
-- Name: programe id; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY programe ALTER COLUMN id SET DEFAULT nextval('programe_id_seq'::regclass);


--
-- Name: technology id; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY technology ALTER COLUMN id SET DEFAULT nextval('technology_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY "user" ALTER COLUMN id SET DEFAULT nextval('user_id_seq'::regclass);


--
-- Data for Name: admission_trnxs; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY admission_trnxs (id, name, phone, email, study, course, address, gender, join_date, fees, active, dp, details) FROM stdin;
2	mehta smit	9904274495	mehtasmit44@gmail.com	BE-IT	Python	arihant aashish,6/10 gayakwadi plot	t	09/14/2017 - 09/14/2017	0	t	2_201709141412.jpg	GEC,Modasa
\.


--
-- Name: admission_trnxs_fees_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('admission_trnxs_fees_seq', 1, false);


--
-- Name: admission_trnxs_id_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('admission_trnxs_id_seq', 3, true);


--
-- Data for Name: batch_trnxs; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY batch_trnxs (bid, cid, fid, day, "time", active) FROM stdin;
1	1	6	Monday,Wednsday,Friday	12:00,15:00	t
2	2	6	Tuesday,Thursday,Saturday	12:00,15:00	t
3	3	1	Monday,Wednsday,Friday	10:00,12:00	t
4	4	1	Tuesday,Thursday,Saturday	10:00,12:00	t
5	1	1	Wednsday,Thursday,Friday,Saturday	15:00	t
\.


--
-- Name: batch_trnxs_bid_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('batch_trnxs_bid_seq', 5, true);


--
-- Data for Name: course_trnxs; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY course_trnxs (id, cname, duration, details, active, fees) FROM stdin;
1	Python	09/01/2017 - 12/31/2017	Flask,PostgresSQL,Django,Odoo Technology	t	15000
2	Asp.net	09/12/2017 - 09/12/2017	MVC,3-tier architecture	t	10000
3	Java	09/12/2017 - 09/12/2017	Hibernate	t	12500
4	Php	09/12/2017 - 09/12/2017	Wordpress	t	8500
\.


--
-- Name: course_trxns_id_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('course_trxns_id_seq', 7, true);


--
-- Data for Name: faculty; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY faculty (id, name, email, phone, website, company, post, dob, address, gender, dp, active) FROM stdin;
1	mehta smit	mehtasmit44@gmail.com	9904274495	http://www.hrsinfomania.com	ITMusketeers Pvt. Ltd.	Python Devloper	1997-06-25	arihant aashish,6/10 gayakwadi plot	t	1_201709072051.jpg	t
6	Bhavik Vyas	bhavik@gmail.com	9033986379	http://www.hrsinfomania.com	ITMusketeers Pvt. Ltd.	MD	1991-08-19	hello	t	6_201709141757.jpg	t
5	bhavik	xx@gmail.com	1234567891	http://www.xx.com	xxzz	xxyy	2017-08-02	xxxx	t	5_201709072059.jpg	f
\.


--
-- Name: faculty_id_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('faculty_id_seq', 6, true);


--
-- Data for Name: inquiry_trnxs; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY inquiry_trnxs (id, name, phone, email, course, study, details, active, date, gender) FROM stdin;
2	mehta smit	9904274495	mehtasmit44@gmail.com	Python	BE-IT	GEC,Modasa	t	2017-09-08	t
3	sr	1234567891	mehtasmit44@gmail.com	Python	BE-IT	sdhfkq	t	2017-09-08	t
4	jhg	1234567891	mehtasmit44@gmail.com	Python	gyiyu	smit mehtA	t	2017-09-08	t
\.


--
-- Name: inquiry_trnxs_id_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('inquiry_trnxs_id_seq', 4, true);


--
-- Data for Name: programe; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY programe (id, tech, framework, defination) FROM stdin;
\.


--
-- Name: programe_id_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('programe_id_seq', 1, false);


--
-- Data for Name: technology; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY technology (id, tech, framework, active) FROM stdin;
5	Java	spring	t
4	Java	hibernate	t
6	Java	struts	t
2	Python	Odoo	t
1	Python	Flask	t
3	Python	django	t
\.


--
-- Name: technology_id_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('technology_id_seq', 6, true);


--
-- Data for Name: test; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY test (mobile, email) FROM stdin;
9904274495	mehtasmit44@k
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: lp; Owner: srmehta
--

COPY "user" (id, username, password, email, mobile, last_login, status, live, active) FROM stdin;
2	bhavik1991	bhavik1991	bhavik@itmusketeers.com	9033986379	2017-09-06 17:17:00	f	f	t
3	test	ITMCS	test@itmusketeers.com	1234567890	2017-08-19 13:04:00	f	f	t
1	srmehta	srmehta	sr_mehta@itmusketeers.com	9904274495	2017-09-28 20:12:00	f	t	t
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: lp; Owner: srmehta
--

SELECT pg_catalog.setval('user_id_seq', 3, true);


--
-- Name: admission_trnxs admission_trnxs_email_key; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY admission_trnxs
    ADD CONSTRAINT admission_trnxs_email_key UNIQUE (email);


--
-- Name: admission_trnxs admission_trnxs_phone_key; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY admission_trnxs
    ADD CONSTRAINT admission_trnxs_phone_key UNIQUE (phone);


--
-- Name: admission_trnxs admission_trnxs_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY admission_trnxs
    ADD CONSTRAINT admission_trnxs_pkey PRIMARY KEY (id);


--
-- Name: batch_trnxs batch_trnxs_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY batch_trnxs
    ADD CONSTRAINT batch_trnxs_pkey PRIMARY KEY (bid);


--
-- Name: course_trnxs course_trxns_cname_key; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY course_trnxs
    ADD CONSTRAINT course_trxns_cname_key UNIQUE (cname);


--
-- Name: course_trnxs course_trxns_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY course_trnxs
    ADD CONSTRAINT course_trxns_pkey PRIMARY KEY (id);


--
-- Name: faculty faculty_email_key; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY faculty
    ADD CONSTRAINT faculty_email_key UNIQUE (email);


--
-- Name: faculty faculty_phone_key; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY faculty
    ADD CONSTRAINT faculty_phone_key UNIQUE (phone);


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);


--
-- Name: inquiry_trnxs inquiry_trnxs_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY inquiry_trnxs
    ADD CONSTRAINT inquiry_trnxs_pkey PRIMARY KEY (id);


--
-- Name: programe programe_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY programe
    ADD CONSTRAINT programe_pkey PRIMARY KEY (id);


--
-- Name: technology technology_framework_key; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY technology
    ADD CONSTRAINT technology_framework_key UNIQUE (framework);


--
-- Name: technology technology_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY technology
    ADD CONSTRAINT technology_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: admission_trnxs admission_trnxs_course_fkey; Type: FK CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY admission_trnxs
    ADD CONSTRAINT admission_trnxs_course_fkey FOREIGN KEY (course) REFERENCES course_trnxs(cname);


--
-- Name: batch_trnxs batch_trnxs_cid_fkey; Type: FK CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY batch_trnxs
    ADD CONSTRAINT batch_trnxs_cid_fkey FOREIGN KEY (cid) REFERENCES course_trnxs(id);


--
-- Name: batch_trnxs batch_trnxs_fid_fkey; Type: FK CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY batch_trnxs
    ADD CONSTRAINT batch_trnxs_fid_fkey FOREIGN KEY (fid) REFERENCES faculty(id);


--
-- Name: programe programe_framework_fkey; Type: FK CONSTRAINT; Schema: lp; Owner: srmehta
--

ALTER TABLE ONLY programe
    ADD CONSTRAINT programe_framework_fkey FOREIGN KEY (framework) REFERENCES technology(framework);


--
-- Name: lp; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA lp TO srmehta;


--
-- PostgreSQL database dump complete
--

\connect postgres

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 9.6.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- PostgreSQL database dump complete
--

\connect template1

SET default_transaction_read_only = off;

--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 9.6.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: template1; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

