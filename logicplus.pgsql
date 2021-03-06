PGDMP     /                    v         	   logicplus    9.5.12    9.5.12 �    }	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            ~	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �	           1262    24855 	   logicplus    DATABASE     o   CREATE DATABASE logicplus WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_IN' LC_CTYPE = 'en_IN';
    DROP DATABASE logicplus;
             postgres    false            	            2615    24856    lp    SCHEMA        CREATE SCHEMA lp;
    DROP SCHEMA lp;
             postgres    false            �	           0    0 	   SCHEMA lp    ACL     p   REVOKE ALL ON SCHEMA lp FROM PUBLIC;
REVOKE ALL ON SCHEMA lp FROM postgres;
GRANT ALL ON SCHEMA lp TO postgres;
                  postgres    false    9                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �	           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    8            �	           0    0    SCHEMA public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    8                        3079    12393    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �	           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1                        3079    24857    citext 	   EXTENSION     :   CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;
    DROP EXTENSION citext;
                  false    8            �	           0    0    EXTENSION citext    COMMENT     S   COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';
                       false    2            k           1247    24941    email    DOMAIN     �   CREATE DOMAIN public.email AS public.citext
	CONSTRAINT email_check CHECK ((VALUE OPERATOR(public.~) '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zAZ0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'::public.citext));
    DROP DOMAIN public.email;
       public       postgres    false    2    2    8    2    8    2    8    2    8    8    2    8    2    2    8    2    8    2    8    2    8    8    2    2    8    2    8    2    8    2    8    8    2    8    2    2    8    2    8    2    8    2    8    8    2    2    8    2    8    2    8    2    8    8    2    8    8    2    2    8    2    8    2    8    2    8    8    2    8            m           1247    24943    phone    DOMAIN     �   CREATE DOMAIN public.phone AS public.citext
	CONSTRAINT phone_check CHECK ((VALUE OPERATOR(public.~) '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'::public.citext));
    DROP DOMAIN public.phone;
       public       postgres    false    2    2    8    2    8    2    8    2    8    8    2    8    2    2    8    2    8    2    8    2    8    8    2    2    8    2    8    2    8    2    8    8    2    8    2    2    8    2    8    2    8    2    8    8    2    2    8    2    8    2    8    2    8    8    8    2    8    2    8    2    2    8    2    8    2    8    2    8    8            �            1259    25137    admission_batch    TABLE     �   CREATE TABLE lp.admission_batch (
    aid integer NOT NULL,
    bid integer NOT NULL,
    id integer NOT NULL,
    "time" character varying(50) DEFAULT ''::character varying NOT NULL,
    fees integer DEFAULT 0 NOT NULL
);
    DROP TABLE lp.admission_batch;
       lp         postgres    false    9            �            1259    25150    admission_batch_id_seq    SEQUENCE     {   CREATE SEQUENCE lp.admission_batch_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE lp.admission_batch_id_seq;
       lp       postgres    false    204    9            �	           0    0    admission_batch_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE lp.admission_batch_id_seq OWNED BY lp.admission_batch.id;
            lp       postgres    false    205            �            1259    24950    admission_trnxs    TABLE       CREATE TABLE lp.admission_trnxs (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    phone public.phone,
    email public.email,
    study character varying(50) NOT NULL,
    course character varying(50) NOT NULL,
    address character varying(100) NOT NULL,
    gender boolean DEFAULT true,
    join_date character varying(25) NOT NULL,
    fees integer NOT NULL,
    active boolean DEFAULT true,
    dp character varying(30) NOT NULL,
    details character varying(1000) NOT NULL,
    bid integer DEFAULT 0
);
    DROP TABLE lp.admission_trnxs;
       lp         postgres    false    9    619    621            �	           0    0    TABLE admission_trnxs    ACL     �   REVOKE ALL ON TABLE lp.admission_trnxs FROM PUBLIC;
REVOKE ALL ON TABLE lp.admission_trnxs FROM postgres;
GRANT ALL ON TABLE lp.admission_trnxs TO postgres;
            lp       postgres    false    183            �            1259    24961    admission_trnxs_id_seq    SEQUENCE     {   CREATE SEQUENCE lp.admission_trnxs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE lp.admission_trnxs_id_seq;
       lp       postgres    false    183    9            �	           0    0    admission_trnxs_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE lp.admission_trnxs_id_seq OWNED BY lp.admission_trnxs.id;
            lp       postgres    false    184            �            1259    33398    batch_faculty    TABLE     �   CREATE TABLE lp.batch_faculty (
    id integer NOT NULL,
    fid integer NOT NULL,
    bid integer NOT NULL,
    "time" character varying(50) NOT NULL
);
    DROP TABLE lp.batch_faculty;
       lp         postgres    false    9            �            1259    33401    batch_faculty_id_seq    SEQUENCE     y   CREATE SEQUENCE lp.batch_faculty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE lp.batch_faculty_id_seq;
       lp       postgres    false    206    9            �	           0    0    batch_faculty_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE lp.batch_faculty_id_seq OWNED BY lp.batch_faculty.id;
            lp       postgres    false    207            �            1259    24963    batch_trnxs    TABLE     �   CREATE TABLE lp.batch_trnxs (
    bid integer NOT NULL,
    cid integer NOT NULL,
    fid integer NOT NULL,
    day text NOT NULL,
    "time" text NOT NULL,
    active boolean DEFAULT false NOT NULL,
    entries integer DEFAULT 0 NOT NULL
);
    DROP TABLE lp.batch_trnxs;
       lp         postgres    false    9            �	           0    0    TABLE batch_trnxs    ACL     �   REVOKE ALL ON TABLE lp.batch_trnxs FROM PUBLIC;
REVOKE ALL ON TABLE lp.batch_trnxs FROM postgres;
GRANT ALL ON TABLE lp.batch_trnxs TO postgres;
            lp       postgres    false    185            �            1259    24970    batch_trnxs_bid_seq    SEQUENCE     x   CREATE SEQUENCE lp.batch_trnxs_bid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE lp.batch_trnxs_bid_seq;
       lp       postgres    false    9    185            �	           0    0    batch_trnxs_bid_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE lp.batch_trnxs_bid_seq OWNED BY lp.batch_trnxs.bid;
            lp       postgres    false    186            �            1259    24972    chat    TABLE     �   CREATE TABLE lp.chat (
    id integer NOT NULL,
    name character varying(10) NOT NULL,
    message character varying(100) NOT NULL,
    date date,
    "time" time without time zone
);
    DROP TABLE lp.chat;
       lp         postgres    false    9            �	           0    0 
   TABLE chat    ACL     |   REVOKE ALL ON TABLE lp.chat FROM PUBLIC;
REVOKE ALL ON TABLE lp.chat FROM postgres;
GRANT ALL ON TABLE lp.chat TO postgres;
            lp       postgres    false    187            �            1259    24975    chat_id_seq    SEQUENCE     p   CREATE SEQUENCE lp.chat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
    DROP SEQUENCE lp.chat_id_seq;
       lp       postgres    false    187    9            �	           0    0    chat_id_seq    SEQUENCE OWNED BY     3   ALTER SEQUENCE lp.chat_id_seq OWNED BY lp.chat.id;
            lp       postgres    false    188            �            1259    24977    course_trnxs    TABLE     �   CREATE TABLE lp.course_trnxs (
    id integer NOT NULL,
    cname character varying(20),
    duration character varying(30) NOT NULL,
    details character varying(1000) NOT NULL,
    active boolean DEFAULT true,
    fees integer
);
    DROP TABLE lp.course_trnxs;
       lp         postgres    false    9            �	           0    0    TABLE course_trnxs    ACL     �   REVOKE ALL ON TABLE lp.course_trnxs FROM PUBLIC;
REVOKE ALL ON TABLE lp.course_trnxs FROM postgres;
GRANT ALL ON TABLE lp.course_trnxs TO postgres;
            lp       postgres    false    189            �            1259    24984    course_trxns_id_seq    SEQUENCE     x   CREATE SEQUENCE lp.course_trxns_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE lp.course_trxns_id_seq;
       lp       postgres    false    9    189            �	           0    0    course_trxns_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE lp.course_trxns_id_seq OWNED BY lp.course_trnxs.id;
            lp       postgres    false    190            �            1259    24986    faculty    TABLE     �  CREATE TABLE lp.faculty (
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
    DROP TABLE lp.faculty;
       lp         postgres    false    621    9    619            �	           0    0    TABLE faculty    ACL     �   REVOKE ALL ON TABLE lp.faculty FROM PUBLIC;
REVOKE ALL ON TABLE lp.faculty FROM postgres;
GRANT ALL ON TABLE lp.faculty TO postgres;
            lp       postgres    false    191            �            1259    24994    faculty_id_seq    SEQUENCE     s   CREATE SEQUENCE lp.faculty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 !   DROP SEQUENCE lp.faculty_id_seq;
       lp       postgres    false    191    9            �	           0    0    faculty_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE lp.faculty_id_seq OWNED BY lp.faculty.id;
            lp       postgres    false    192            �            1259    44192    inquiry_notes    TABLE     �   CREATE TABLE lp.inquiry_notes (
    id integer NOT NULL,
    iid integer,
    notes character varying(150) NOT NULL,
    active boolean DEFAULT true,
    date date
);
    DROP TABLE lp.inquiry_notes;
       lp         postgres    false    9            �            1259    44190    inquiry_notes_id_seq    SEQUENCE     y   CREATE SEQUENCE lp.inquiry_notes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE lp.inquiry_notes_id_seq;
       lp       postgres    false    212    9            �	           0    0    inquiry_notes_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE lp.inquiry_notes_id_seq OWNED BY lp.inquiry_notes.id;
            lp       postgres    false    211            �            1259    24996    inquiry_trnxs    TABLE     �  CREATE TABLE lp.inquiry_trnxs (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    phone public.phone NOT NULL,
    email public.email NOT NULL,
    course character varying(50) NOT NULL,
    study character varying(20) NOT NULL,
    details character varying(20) NOT NULL,
    active boolean DEFAULT true,
    date date NOT NULL,
    gender boolean DEFAULT true,
    status character varying(10) DEFAULT 'opened'::character varying
);
    DROP TABLE lp.inquiry_trnxs;
       lp         postgres    false    621    619    9            �	           0    0    TABLE inquiry_trnxs    ACL     �   REVOKE ALL ON TABLE lp.inquiry_trnxs FROM PUBLIC;
REVOKE ALL ON TABLE lp.inquiry_trnxs FROM postgres;
GRANT ALL ON TABLE lp.inquiry_trnxs TO postgres;
            lp       postgres    false    193            �            1259    25004    inquiry_trnxs_id_seq    SEQUENCE     y   CREATE SEQUENCE lp.inquiry_trnxs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE lp.inquiry_trnxs_id_seq;
       lp       postgres    false    9    193            �	           0    0    inquiry_trnxs_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE lp.inquiry_trnxs_id_seq OWNED BY lp.inquiry_trnxs.id;
            lp       postgres    false    194            �            1259    25006    invoice_trnxs    TABLE     "  CREATE TABLE lp.invoice_trnxs (
    id integer NOT NULL,
    invoice_no character varying(10) DEFAULT 0,
    aid integer NOT NULL,
    fees integer NOT NULL,
    payment_type boolean DEFAULT false,
    bank text DEFAULT 'payment type is cash.'::text,
    chq_no text,
    active boolean
);
    DROP TABLE lp.invoice_trnxs;
       lp         postgres    false    9            �	           0    0    TABLE invoice_trnxs    ACL     �   REVOKE ALL ON TABLE lp.invoice_trnxs FROM PUBLIC;
REVOKE ALL ON TABLE lp.invoice_trnxs FROM postgres;
GRANT ALL ON TABLE lp.invoice_trnxs TO postgres;
            lp       postgres    false    195            �            1259    25015    invoice_trnxs_id_seq    SEQUENCE     y   CREATE SEQUENCE lp.invoice_trnxs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE lp.invoice_trnxs_id_seq;
       lp       postgres    false    9    195            �	           0    0    invoice_trnxs_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE lp.invoice_trnxs_id_seq OWNED BY lp.invoice_trnxs.id;
            lp       postgres    false    196            �            1259    25017    programe    TABLE     �   CREATE TABLE lp.programe (
    id integer NOT NULL,
    tech character varying(20) NOT NULL,
    framework character varying(20) NOT NULL,
    defination character varying(1000) NOT NULL
);
    DROP TABLE lp.programe;
       lp         postgres    false    9            �	           0    0    TABLE programe    ACL     �   REVOKE ALL ON TABLE lp.programe FROM PUBLIC;
REVOKE ALL ON TABLE lp.programe FROM postgres;
GRANT ALL ON TABLE lp.programe TO postgres;
            lp       postgres    false    197            �            1259    25023    programe_id_seq    SEQUENCE     t   CREATE SEQUENCE lp.programe_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE lp.programe_id_seq;
       lp       postgres    false    9    197            �	           0    0    programe_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE lp.programe_id_seq OWNED BY lp.programe.id;
            lp       postgres    false    198            �            1259    25025 
   technology    TABLE     �   CREATE TABLE lp.technology (
    id integer NOT NULL,
    tech character varying(20) NOT NULL,
    framework character varying(20),
    active boolean DEFAULT true
);
    DROP TABLE lp.technology;
       lp         postgres    false    9            �	           0    0    TABLE technology    ACL     �   REVOKE ALL ON TABLE lp.technology FROM PUBLIC;
REVOKE ALL ON TABLE lp.technology FROM postgres;
GRANT ALL ON TABLE lp.technology TO postgres;
            lp       postgres    false    199            �            1259    25029    technology_id_seq    SEQUENCE     v   CREATE SEQUENCE lp.technology_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE lp.technology_id_seq;
       lp       postgres    false    199    9            �	           0    0    technology_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE lp.technology_id_seq OWNED BY lp.technology.id;
            lp       postgres    false    200            �            1259    25031    test    TABLE     u   CREATE TABLE lp.test (
    mobile public.phone NOT NULL,
    email public.email NOT NULL,
    id integer NOT NULL
);
    DROP TABLE lp.test;
       lp         postgres    false    621    619    9            �	           0    0 
   TABLE test    ACL     |   REVOKE ALL ON TABLE lp.test FROM PUBLIC;
REVOKE ALL ON TABLE lp.test FROM postgres;
GRANT ALL ON TABLE lp.test TO postgres;
            lp       postgres    false    201            �            1259    41590    test_id_seq    SEQUENCE     p   CREATE SEQUENCE lp.test_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
    DROP SEQUENCE lp.test_id_seq;
       lp       postgres    false    9    201            �	           0    0    test_id_seq    SEQUENCE OWNED BY     3   ALTER SEQUENCE lp.test_id_seq OWNED BY lp.test.id;
            lp       postgres    false    208            �            1259    25037    user    TABLE     �  CREATE TABLE lp."user" (
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
    DROP TABLE lp."user";
       lp         postgres    false    9    619            �	           0    0    TABLE "user"    ACL     �   REVOKE ALL ON TABLE lp."user" FROM PUBLIC;
REVOKE ALL ON TABLE lp."user" FROM postgres;
GRANT ALL ON TABLE lp."user" TO postgres;
            lp       postgres    false    202            �            1259    25047    user_id_seq    SEQUENCE     p   CREATE SEQUENCE lp.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
    DROP SEQUENCE lp.user_id_seq;
       lp       postgres    false    202    9            �	           0    0    user_id_seq    SEQUENCE OWNED BY     5   ALTER SEQUENCE lp.user_id_seq OWNED BY lp."user".id;
            lp       postgres    false    203            �            1259    43437 
   logicplus1    TABLE     0   CREATE TABLE public.logicplus1 (
    c1 text
);
    DROP TABLE public.logicplus1;
       public         postgres    false    8            �            1259    43431    new    TABLE     )   CREATE TABLE public.new (
    c1 text
);
    DROP TABLE public.new;
       public         postgres    false    8            �           2604    42523    id    DEFAULT     p   ALTER TABLE ONLY lp.admission_batch ALTER COLUMN id SET DEFAULT nextval('lp.admission_batch_id_seq'::regclass);
 =   ALTER TABLE lp.admission_batch ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    205    204            �           2604    42524    id    DEFAULT     p   ALTER TABLE ONLY lp.admission_trnxs ALTER COLUMN id SET DEFAULT nextval('lp.admission_trnxs_id_seq'::regclass);
 =   ALTER TABLE lp.admission_trnxs ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    184    183            �           2604    42526    id    DEFAULT     l   ALTER TABLE ONLY lp.batch_faculty ALTER COLUMN id SET DEFAULT nextval('lp.batch_faculty_id_seq'::regclass);
 ;   ALTER TABLE lp.batch_faculty ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    207    206            �           2604    42527    bid    DEFAULT     j   ALTER TABLE ONLY lp.batch_trnxs ALTER COLUMN bid SET DEFAULT nextval('lp.batch_trnxs_bid_seq'::regclass);
 :   ALTER TABLE lp.batch_trnxs ALTER COLUMN bid DROP DEFAULT;
       lp       postgres    false    186    185            �           2604    42528    id    DEFAULT     Z   ALTER TABLE ONLY lp.chat ALTER COLUMN id SET DEFAULT nextval('lp.chat_id_seq'::regclass);
 2   ALTER TABLE lp.chat ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    188    187            �           2604    42529    id    DEFAULT     j   ALTER TABLE ONLY lp.course_trnxs ALTER COLUMN id SET DEFAULT nextval('lp.course_trxns_id_seq'::regclass);
 :   ALTER TABLE lp.course_trnxs ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    190    189            �           2604    42530    id    DEFAULT     `   ALTER TABLE ONLY lp.faculty ALTER COLUMN id SET DEFAULT nextval('lp.faculty_id_seq'::regclass);
 5   ALTER TABLE lp.faculty ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    192    191            �           2604    44195    id    DEFAULT     l   ALTER TABLE ONLY lp.inquiry_notes ALTER COLUMN id SET DEFAULT nextval('lp.inquiry_notes_id_seq'::regclass);
 ;   ALTER TABLE lp.inquiry_notes ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    212    211    212            �           2604    42531    id    DEFAULT     l   ALTER TABLE ONLY lp.inquiry_trnxs ALTER COLUMN id SET DEFAULT nextval('lp.inquiry_trnxs_id_seq'::regclass);
 ;   ALTER TABLE lp.inquiry_trnxs ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    194    193            �           2604    42532    id    DEFAULT     l   ALTER TABLE ONLY lp.invoice_trnxs ALTER COLUMN id SET DEFAULT nextval('lp.invoice_trnxs_id_seq'::regclass);
 ;   ALTER TABLE lp.invoice_trnxs ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    196    195            �           2604    42533    id    DEFAULT     b   ALTER TABLE ONLY lp.programe ALTER COLUMN id SET DEFAULT nextval('lp.programe_id_seq'::regclass);
 6   ALTER TABLE lp.programe ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    198    197            �           2604    42534    id    DEFAULT     f   ALTER TABLE ONLY lp.technology ALTER COLUMN id SET DEFAULT nextval('lp.technology_id_seq'::regclass);
 8   ALTER TABLE lp.technology ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    200    199            �           2604    42535    id    DEFAULT     Z   ALTER TABLE ONLY lp.test ALTER COLUMN id SET DEFAULT nextval('lp.test_id_seq'::regclass);
 2   ALTER TABLE lp.test ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    208    201            �           2604    42536    id    DEFAULT     \   ALTER TABLE ONLY lp."user" ALTER COLUMN id SET DEFAULT nextval('lp.user_id_seq'::regclass);
 4   ALTER TABLE lp."user" ALTER COLUMN id DROP DEFAULT;
       lp       postgres    false    203    202            r	          0    25137    admission_batch 
   TABLE DATA               A   COPY lp.admission_batch (aid, bid, id, "time", fees) FROM stdin;
    lp       postgres    false    204   m�       �	           0    0    admission_batch_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('lp.admission_batch_id_seq', 34, true);
            lp       postgres    false    205            ]	          0    24950    admission_trnxs 
   TABLE DATA               �   COPY lp.admission_trnxs (id, name, phone, email, study, course, address, gender, join_date, fees, active, dp, details, bid) FROM stdin;
    lp       postgres    false    183   Ȟ       �	           0    0    admission_trnxs_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('lp.admission_trnxs_id_seq', 6, true);
            lp       postgres    false    184            t	          0    33398    batch_faculty 
   TABLE DATA               9   COPY lp.batch_faculty (id, fid, bid, "time") FROM stdin;
    lp       postgres    false    206   �       �	           0    0    batch_faculty_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('lp.batch_faculty_id_seq', 12, true);
            lp       postgres    false    207            _	          0    24963    batch_trnxs 
   TABLE DATA               N   COPY lp.batch_trnxs (bid, cid, fid, day, "time", active, entries) FROM stdin;
    lp       postgres    false    185   ?�       �	           0    0    batch_trnxs_bid_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('lp.batch_trnxs_bid_seq', 11, true);
            lp       postgres    false    186            a	          0    24972    chat 
   TABLE DATA               ;   COPY lp.chat (id, name, message, date, "time") FROM stdin;
    lp       postgres    false    187   à       �	           0    0    chat_id_seq    SEQUENCE SET     5   SELECT pg_catalog.setval('lp.chat_id_seq', 7, true);
            lp       postgres    false    188            c	          0    24977    course_trnxs 
   TABLE DATA               N   COPY lp.course_trnxs (id, cname, duration, details, active, fees) FROM stdin;
    lp       postgres    false    189   v�       �	           0    0    course_trxns_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('lp.course_trxns_id_seq', 7, true);
            lp       postgres    false    190            e	          0    24986    faculty 
   TABLE DATA               o   COPY lp.faculty (id, name, email, phone, website, company, post, dob, address, gender, dp, active) FROM stdin;
    lp       postgres    false    191   1�       �	           0    0    faculty_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('lp.faculty_id_seq', 6, true);
            lp       postgres    false    192            z	          0    44192    inquiry_notes 
   TABLE DATA               A   COPY lp.inquiry_notes (id, iid, notes, active, date) FROM stdin;
    lp       postgres    false    212   R�       �	           0    0    inquiry_notes_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('lp.inquiry_notes_id_seq', 1, false);
            lp       postgres    false    211            g	          0    24996    inquiry_trnxs 
   TABLE DATA               q   COPY lp.inquiry_trnxs (id, name, phone, email, course, study, details, active, date, gender, status) FROM stdin;
    lp       postgres    false    193   o�       �	           0    0    inquiry_trnxs_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('lp.inquiry_trnxs_id_seq', 11, true);
            lp       postgres    false    194            i	          0    25006    invoice_trnxs 
   TABLE DATA               b   COPY lp.invoice_trnxs (id, invoice_no, aid, fees, payment_type, bank, chq_no, active) FROM stdin;
    lp       postgres    false    195   ~�       �	           0    0    invoice_trnxs_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('lp.invoice_trnxs_id_seq', 14, true);
            lp       postgres    false    196            k	          0    25017    programe 
   TABLE DATA               ?   COPY lp.programe (id, tech, framework, defination) FROM stdin;
    lp       postgres    false    197   �       �	           0    0    programe_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('lp.programe_id_seq', 1, false);
            lp       postgres    false    198            m	          0    25025 
   technology 
   TABLE DATA               =   COPY lp.technology (id, tech, framework, active) FROM stdin;
    lp       postgres    false    199   �       �	           0    0    technology_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('lp.technology_id_seq', 19, true);
            lp       postgres    false    200            o	          0    25031    test 
   TABLE DATA               -   COPY lp.test (mobile, email, id) FROM stdin;
    lp       postgres    false    201   x�       �	           0    0    test_id_seq    SEQUENCE SET     6   SELECT pg_catalog.setval('lp.test_id_seq', 32, true);
            lp       postgres    false    208            p	          0    25037    user 
   TABLE DATA               e   COPY lp."user" (id, username, password, email, mobile, last_login, status, live, active) FROM stdin;
    lp       postgres    false    202   �       �	           0    0    user_id_seq    SEQUENCE SET     5   SELECT pg_catalog.setval('lp.user_id_seq', 5, true);
            lp       postgres    false    203            x	          0    43437 
   logicplus1 
   TABLE DATA               (   COPY public.logicplus1 (c1) FROM stdin;
    public       postgres    false    210   ͦ       w	          0    43431    new 
   TABLE DATA               !   COPY public.new (c1) FROM stdin;
    public       postgres    false    209   `�       �           2606    25154    admission_batch_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY lp.admission_batch
    ADD CONSTRAINT admission_batch_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY lp.admission_batch DROP CONSTRAINT admission_batch_pkey;
       lp         postgres    false    204    204            �           2606    25064    admission_trnxs_email_key 
   CONSTRAINT     a   ALTER TABLE ONLY lp.admission_trnxs
    ADD CONSTRAINT admission_trnxs_email_key UNIQUE (email);
 O   ALTER TABLE ONLY lp.admission_trnxs DROP CONSTRAINT admission_trnxs_email_key;
       lp         postgres    false    183    183            �           2606    25066    admission_trnxs_phone_key 
   CONSTRAINT     a   ALTER TABLE ONLY lp.admission_trnxs
    ADD CONSTRAINT admission_trnxs_phone_key UNIQUE (phone);
 O   ALTER TABLE ONLY lp.admission_trnxs DROP CONSTRAINT admission_trnxs_phone_key;
       lp         postgres    false    183    183            �           2606    25068    admission_trnxs_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY lp.admission_trnxs
    ADD CONSTRAINT admission_trnxs_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY lp.admission_trnxs DROP CONSTRAINT admission_trnxs_pkey;
       lp         postgres    false    183    183            �           2606    33417    batch_faculty_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY lp.batch_faculty
    ADD CONSTRAINT batch_faculty_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY lp.batch_faculty DROP CONSTRAINT batch_faculty_pkey;
       lp         postgres    false    206    206            �           2606    25070    batch_trnxs_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY lp.batch_trnxs
    ADD CONSTRAINT batch_trnxs_pkey PRIMARY KEY (bid);
 B   ALTER TABLE ONLY lp.batch_trnxs DROP CONSTRAINT batch_trnxs_pkey;
       lp         postgres    false    185    185            �           2606    25072 	   chat_pkey 
   CONSTRAINT     H   ALTER TABLE ONLY lp.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (id);
 4   ALTER TABLE ONLY lp.chat DROP CONSTRAINT chat_pkey;
       lp         postgres    false    187    187            �           2606    25074    course_trxns_cname_key 
   CONSTRAINT     [   ALTER TABLE ONLY lp.course_trnxs
    ADD CONSTRAINT course_trxns_cname_key UNIQUE (cname);
 I   ALTER TABLE ONLY lp.course_trnxs DROP CONSTRAINT course_trxns_cname_key;
       lp         postgres    false    189    189            �           2606    25076    course_trxns_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY lp.course_trnxs
    ADD CONSTRAINT course_trxns_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY lp.course_trnxs DROP CONSTRAINT course_trxns_pkey;
       lp         postgres    false    189    189            �           2606    25078    faculty_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY lp.faculty
    ADD CONSTRAINT faculty_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY lp.faculty DROP CONSTRAINT faculty_email_key;
       lp         postgres    false    191    191            �           2606    25080    faculty_phone_key 
   CONSTRAINT     Q   ALTER TABLE ONLY lp.faculty
    ADD CONSTRAINT faculty_phone_key UNIQUE (phone);
 ?   ALTER TABLE ONLY lp.faculty DROP CONSTRAINT faculty_phone_key;
       lp         postgres    false    191    191            �           2606    25082    faculty_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY lp.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY lp.faculty DROP CONSTRAINT faculty_pkey;
       lp         postgres    false    191    191            �           2606    44198    inquiry_notes_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY lp.inquiry_notes
    ADD CONSTRAINT inquiry_notes_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY lp.inquiry_notes DROP CONSTRAINT inquiry_notes_pkey;
       lp         postgres    false    212    212            �           2606    25084    inquiry_trnxs_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY lp.inquiry_trnxs
    ADD CONSTRAINT inquiry_trnxs_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY lp.inquiry_trnxs DROP CONSTRAINT inquiry_trnxs_pkey;
       lp         postgres    false    193    193            �           2606    25086    invoice_trnxs_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY lp.invoice_trnxs
    ADD CONSTRAINT invoice_trnxs_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY lp.invoice_trnxs DROP CONSTRAINT invoice_trnxs_pkey;
       lp         postgres    false    195    195            �           2606    25088    programe_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY lp.programe
    ADD CONSTRAINT programe_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY lp.programe DROP CONSTRAINT programe_pkey;
       lp         postgres    false    197    197            �           2606    25090    technology_framework_key 
   CONSTRAINT     _   ALTER TABLE ONLY lp.technology
    ADD CONSTRAINT technology_framework_key UNIQUE (framework);
 I   ALTER TABLE ONLY lp.technology DROP CONSTRAINT technology_framework_key;
       lp         postgres    false    199    199            �           2606    25092    technology_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY lp.technology
    ADD CONSTRAINT technology_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY lp.technology DROP CONSTRAINT technology_pkey;
       lp         postgres    false    199    199            �           2606    41594 	   test_pkey 
   CONSTRAINT     H   ALTER TABLE ONLY lp.test
    ADD CONSTRAINT test_pkey PRIMARY KEY (id);
 4   ALTER TABLE ONLY lp.test DROP CONSTRAINT test_pkey;
       lp         postgres    false    201    201            �           2606    25094 	   user_pkey 
   CONSTRAINT     J   ALTER TABLE ONLY lp."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 6   ALTER TABLE ONLY lp."user" DROP CONSTRAINT user_pkey;
       lp         postgres    false    202    202            �           2606    25096    user_username_key 
   CONSTRAINT     S   ALTER TABLE ONLY lp."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);
 >   ALTER TABLE ONLY lp."user" DROP CONSTRAINT user_username_key;
       lp         postgres    false    202    202            �           2606    25140    admission_batch_aid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY lp.admission_batch
    ADD CONSTRAINT admission_batch_aid_fkey FOREIGN KEY (aid) REFERENCES lp.admission_trnxs(id);
 N   ALTER TABLE ONLY lp.admission_batch DROP CONSTRAINT admission_batch_aid_fkey;
       lp       postgres    false    204    2237    183            �           2606    25145    admission_batch_bid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY lp.admission_batch
    ADD CONSTRAINT admission_batch_bid_fkey FOREIGN KEY (bid) REFERENCES lp.batch_trnxs(bid);
 N   ALTER TABLE ONLY lp.admission_batch DROP CONSTRAINT admission_batch_bid_fkey;
       lp       postgres    false    2239    185    204            �           2606    33418    batch_faculty_bid_fkey    FK CONSTRAINT     ~   ALTER TABLE ONLY lp.batch_faculty
    ADD CONSTRAINT batch_faculty_bid_fkey FOREIGN KEY (bid) REFERENCES lp.batch_trnxs(bid);
 J   ALTER TABLE ONLY lp.batch_faculty DROP CONSTRAINT batch_faculty_bid_fkey;
       lp       postgres    false    185    2239    206            �           2606    33423    batch_faculty_fid_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY lp.batch_faculty
    ADD CONSTRAINT batch_faculty_fid_fkey FOREIGN KEY (fid) REFERENCES lp.faculty(id);
 J   ALTER TABLE ONLY lp.batch_faculty DROP CONSTRAINT batch_faculty_fid_fkey;
       lp       postgres    false    2251    206    191            �           2606    25097    batch_trnxs_cid_fkey    FK CONSTRAINT     z   ALTER TABLE ONLY lp.batch_trnxs
    ADD CONSTRAINT batch_trnxs_cid_fkey FOREIGN KEY (cid) REFERENCES lp.course_trnxs(id);
 F   ALTER TABLE ONLY lp.batch_trnxs DROP CONSTRAINT batch_trnxs_cid_fkey;
       lp       postgres    false    185    189    2245            �           2606    25102    batch_trnxs_fid_fkey    FK CONSTRAINT     u   ALTER TABLE ONLY lp.batch_trnxs
    ADD CONSTRAINT batch_trnxs_fid_fkey FOREIGN KEY (fid) REFERENCES lp.faculty(id);
 F   ALTER TABLE ONLY lp.batch_trnxs DROP CONSTRAINT batch_trnxs_fid_fkey;
       lp       postgres    false    191    185    2251            �           2606    44199    inquiry_notes_iid_fkey    FK CONSTRAINT        ALTER TABLE ONLY lp.inquiry_notes
    ADD CONSTRAINT inquiry_notes_iid_fkey FOREIGN KEY (iid) REFERENCES lp.inquiry_trnxs(id);
 J   ALTER TABLE ONLY lp.inquiry_notes DROP CONSTRAINT inquiry_notes_iid_fkey;
       lp       postgres    false    212    2253    193            �           2606    25107    invoice_trnxs_aid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY lp.invoice_trnxs
    ADD CONSTRAINT invoice_trnxs_aid_fkey FOREIGN KEY (aid) REFERENCES lp.admission_trnxs(id);
 J   ALTER TABLE ONLY lp.invoice_trnxs DROP CONSTRAINT invoice_trnxs_aid_fkey;
       lp       postgres    false    183    195    2237            �           2606    25112    programe_framework_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY lp.programe
    ADD CONSTRAINT programe_framework_fkey FOREIGN KEY (framework) REFERENCES lp.technology(framework);
 F   ALTER TABLE ONLY lp.programe DROP CONSTRAINT programe_framework_fkey;
       lp       postgres    false    2259    197    199            r	   K   x�U�Q
�0C��aF����e�?Ǣc|$/���ޣ��$��v6�+��
-��z�(U���T�w����^���      ]	     x����n�0���S�x���-MU=Tʡ�R�@�!�)v�x��&=���h��f&����>���(.���*��Kp����y[uT�A1t��o�_�0[=�����h���4�)OX@�#�)۰� !b��?�p2�Q��FqЌS^L ���R\F��2���
n���Å�i�!O��q��VN�0'����+��� @�;jK�t���T�66�Z{���t�5��]�'!rV�L�O*k6��]R���wq[��D\S>����$C.�{�y�%�q�      t	   A   x�-�� !ߡ�����r��!
�g���S���_�zj/1S���TO�^~X�����l:!      _	   t   x�3�4�4����KI��	OM�K-�܊2���������)��,�4�2�4�4�)�(
�(-3�KJ���*�L���8��BLƦŘ����A�pr� ������� �B�      a	   �   x�]�=�0��9E�K�����t��
�A� U�����[>��!�m=�����"FZ��1�(�g���ZO��Q��R�A��b&0�ޏ�{�QlX:�\\�}x���}�@/B3���C:�Ç痯�@�	J�@�=��L1���5RD�G�}���\fim�8+���!DI      c	   �   x�u��
� ����S� n�kT�QDDѢ��nl��:Ԃ�}ZDW;w�p8�]�j��F��8e�����yA��7�baK�xY������p(��x�A�nn�j�?����P�`1��t.�Ә3(z������y��j�{��8_w<l��.tmȾ2�d��iM�����5E�	�?]      e	     x����N�0���S�X�I�pBh$&MqBB�eKX��	k�ӓV;����,[�}�+x�tqg�6���E?�ru��5�yY�MU*6��~��1��w��k�u��=��~��c������p�a��W|��t��u�����*����!�W6�x�Ǣ�R����a����L��f/Rcb�+���K�0����@�q�Y����ͫ�(�Z�'�~
�k��\�7�>��V���60"o��w�9;�D���u�m\l#GD�����<˲?ޭ��      z	      x������ � �      g	   �   x����n�0�y�>@�B�.�U5mҴv�%JHBW[2T�~���i�ԣ���o��}CBV4}�r�@]�]]yJ]�����}�Mca�C���Q�_���$C�!���iK[ʈ���A�W����o}͡�R��Ǉ�+���;�/�������N#�#L�&���p
ҩªC,�)��ǣ�3��IH0(=�-���Bys �E����$�����i�]�6�;��V��-	som�vmlK�ܛ��|�#�����#      i	   ]   x����)0�4�4500�L�,H��M�+Q(�,HU�,VHN,�����,�24 ��$J�P�!P!�9P-g	g��'�����)H�$i�$hN� )�(�      k	      x������ � �      m	   `   x�3��J,K�,.(��K�,�2��K�JK��|#΀ʒ��<N���| ��w�I,�
�R���AJL Fdd&��%���,8���R!D	W� �C$`      o	   �   x���A
1E��a�&M�f7qS,���㠛
�����)pL�ջ��k-�}:?�#�	C�@��ȁлv�w��;�}�r]��>DG�T=�0kt�r�K�����'18���'x���{{���4�'�~3      p	   �   x��α
�0�9y��@�]�6�L������T���Zi��o�`�:�����Iv��G�"�뢉�=�>z?���w�@)��2�$�@��K��i"G�}��X�2��2��C$��hM�K���"�ҡŘDŢ������]�J���X��#m�ʁ�>Ӭ:u����!)&C딝�]�9?W�      x	      x��][o۸~ϯ ��Prt��������:v7q�,ȶ��Ա]Kn7��I�(q(�,%]`�ƢH~3��3�a|zzrzJ>o��q���6&K/��^���yG����W���������7�qϜ3C��_���_n��E�>��触nNu�Tw�a��ιc������hF�ȋ�g=D���=D�D���������:`���b�6�����٧��������/��j��-�hO�
i��&��ɧ]��ED��0�=����[�~a��ó��#o���oh_q����C�/� za��V:C?�^�������b�!1{�C��WĴN�#k5��s��]��ˎ�����������={���L�o��9�Ś��.oG��(i�^?99�g���#2�cB�M�7����,�����Z��v��c�u��o��l4���N�)�S���Od2��������׳_���5��km�}d8�s4m�L���9�|~W���,�"��;'F>�|���/�77��L=��9�oJ}��J��g�ȸ��o����d�mtm��.ɗ��/�wD�?Qg⍻+J�0_�d�zɚ�d��>J��T�\��!�P�9��&�7a�|�Uo�-"OsYs���~����'J��V\Oe�=��b6L��(ŵA)C�������ZPH"�*^Ư�ݐa���������8�Q�����y7�9Ǐ�9��X�J�`M���;�����k?�y������߃��a,�,�^�Ʌ�$�rKd��|x/Z<���r�0�[!޺��pB�^�$�&���d4�܏�2W>Q>x�v�w�r���_�z��������~<��:?�Zd�|̷xޘ�f�=H����C��;��l�v?�\⅜�����n6��Ŷ��\O��ܲ��W��dJn�'��������ϗCj�Q#�dT��l�FXQ��Tv|�+
�^���_-ì���`	m���W��*VA���vC0�UB0%Y6t|U�c�[�3�C�yl~�����atX��z^l�7	o���C���K�ٺٓ�v���M��hH���-�I�	�m:��V>u\a!�W��i����/���OOj-��tH��r���lpͺ�5���ӵ�*��v֫8.�~����n.�.,��d�x�3��b��`�=�bEt������jh���1k�i*��V�z/�����z_Z�e�a�{��[P���NV�n[�AV:�jW�8/�#8 �f�Jl�Q�������� ��I�x�(�p��*�? �fӒ4����IȢ^��#x��^O5�$�(�"���2a�{��3�4l��ȶ����êx�w��B�oC�H�:f��7Y[�8����\E?��2��b��ɋ����d�eH>}�!�8<ta�H�$,�Ò���i�&��G�Sbg����kE
KL}�Ds<1���`��!WuXȡ�8��F$�SG�����1Yㇽǎ�^!~���ň���#׀t0�!���.~:}u^�Cb���RI6Y�)p�|V��w&�s�ز�P	$��}���*	�ݟ��G����y�mp�A6e�o��~�M�G$Ui�Z{"[�&��dזQg6�mCƣ�E�os-���7� �&4t��+��`���_��Ʌ��42�dsPkG��y0Ձ`�n�ܶ>u�:�xc!��(~�cY]�U��3�C��6��1�V �2��l&��m�	���J� ��z�.|��|�BGuv!m��*b�,m�՜�W��������ձ���$��m��Y��H?y5.�	BV�t�����J���W6���"�!���H39����!q�^_���H�Z�L��o&�6�U I�+<UH6Q͋1�n�}����l�G]#��W�������
6���g�|�掣�xrt���J�6�J�a��IB�.ZL���?gL�@y�$��nE3��f��>����^ފ0G���$q�@*�J���7�._�ҀX~�JɌ�:�!0Α���%@���-�����{?a��v��t ����L]�l�q��Wx�VG�P�U�HxP��D�f=����P����]â[t�}�5��u�ξ�F���05�KT�ZZ$��RIE�&~zF��N>�ˣj������p�a�������G�j�N�CXa����Glp��p�c�n�Lg�:{m�CaI�*��Q�9���ys��:U���oŘ=�Rn�M���Wӫ���N,��t2���I��r:���0[�.D�ksC�o���{����f�?�91	U�L��a�1�1,S�$z�*�uQ�
WZ�Z���o��:�V� �+���)�#�yw� %ͫ�
u���5	8����]PZ�*�7�ٻ]�^,3���Ϭh@�f��iD�����oF���9($Щ@����f���s�H<r��t���,ǈ�RJ`!P�L��2B(R����-�s$!��
�%bs7��w��'�j���\;+On�K�e�^^����^w��\r5�a����=�����y����ҏ���􆆌�`sq���g�-x��D*��oRQ׃��G�3��Y�W��.5�*��/]���l��=�J��g���'9�eZaI-����܃�Gh�����OZR���5�jkI����NK+&��qʶQu��\v�Lݥh�*\����m��@j~g�c@��k�%8�=�2%���U��j�zKW���]e���m�^�/����-3k�Kv%�T^j=�^�ٔ�M!��E�����j&7��������N4UO����``J�J.��� EI�J�h(�S����Z���h�L=5��BK5��F�j�۲�!��puH�����P���y�#�� l�)U�v�T��PL�B��
R�W+�')*)o/c1E��a
{K���!Jܣ�4]K��5މ�
�/�9C�*�J�������W����:V��N]��D���d�{�����+�.6�����\�o\8�R�`�H#�J5�e�"�-��<
u-i35
Iy����j�G�q�!xj��SK�2RU�۴~������4�j�=��j��4���&��
��X"I�K�4���D�QqZK��3|��[v=���r�����&
K�@�4ቃ���B�T�����1ܲ���@�q@>�T!�L�<*���v#l��A��;��
ηY��r�ɯ�`�<y(�%��4xZ��~Z��e�8�
R���2ZRӢ�ʕ�$A��U-%f�k�$���z�o#����?�L�����vx=��������N��������_���_L˪�~@��`d�v�W�C��x���J ��k����
� Dث@�}��0�@���@h� �A�	�:[BfYv�G1;��B�*y\$&�%����t�H���E4s5YEN�W�t����F���|}寉�I�Ό���рCg���~O�;�4��@Sh���}Ky���TAi@�^d��� �n� �f{��~`BH�D�U������B�y\,&����.1	���"1� �"���Cgp�!$�Ѱ @�.�d�z����y�"�Й%�>U���k��:�UM�f�]��P���<���?c��/L����M<� @S����� ����w��):�Eq���*,.�*������+ҧ_�<c�N�|�ގ���
�X�v�it�.w�HN���P�v*�0��B��B��� JaQ� #W�op�� �S��fG���/�M_�X�+���=i]a�Њ�Ɋ�Z�
hT|� /J��p�5�F��@�:�F��J�}p_�cwm����vr3Ä��ܙ�?�7/]Ry�͊���:w��G��iS��y��q���ݎ~��:"��}Y�y�|���O��ˋ�F�Eןo�T(R��eX ��8P�@�/�j	2�TlX6iY \�.��l �!)��R��"r�Kf*DU�B��kS�0��Ak��5��W
Bl]+U�.PF�[==�_������˛�Ŕǵ��������������UW*|e��h�����+��-�A�����{�x�h��"�Z �+�Pl_/TV�v;�X
��ԼFb�ZaX�> ~   C���h9deu�"(��D�5���RZ]0�r���Ѕ�Z�嶕����@¤`L�k=Dl}y��!b��/)Ԓ볎��i�B�U�MJp���y���߁��߁��s�������u���*��&�      w	      x������ � �     