--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO campmanager;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO campmanager;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO campmanager;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO campmanager;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO campmanager;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO campmanager;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO campmanager;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO campmanager;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO campmanager;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO campmanager;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO campmanager;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO campmanager;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO campmanager;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO campmanager;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO campmanager;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO campmanager;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO campmanager;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO campmanager;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO campmanager;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: finances_transaction; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE finances_transaction (
    id integer NOT NULL,
    transaction_id character varying(16) NOT NULL,
    transaction_type character varying(16) NOT NULL,
    transaction_date date,
    amount numeric(6,2) NOT NULL,
    origin character varying(128) NOT NULL,
    destination character varying(128) NOT NULL
);


ALTER TABLE public.finances_transaction OWNER TO campmanager;

--
-- Name: finances_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE finances_transaction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.finances_transaction_id_seq OWNER TO campmanager;

--
-- Name: finances_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE finances_transaction_id_seq OWNED BY finances_transaction.id;


--
-- Name: logistics_smallgroup; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE logistics_smallgroup (
    id integer NOT NULL,
    title character varying(32) NOT NULL,
    generation integer NOT NULL,
    cabin character varying(16) NOT NULL,
    bus character varying(16) NOT NULL,
    structure character varying(16) NOT NULL,
    CONSTRAINT ck_generation_pstv_7f10a6f064f57002 CHECK ((generation >= 0))
);


ALTER TABLE public.logistics_smallgroup OWNER TO campmanager;

--
-- Name: logistics_smallgroup_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE logistics_smallgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.logistics_smallgroup_id_seq OWNER TO campmanager;

--
-- Name: logistics_smallgroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE logistics_smallgroup_id_seq OWNED BY logistics_smallgroup.id;


--
-- Name: signup_camper; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE signup_camper (
    id integer NOT NULL,
    first_name character varying(64) NOT NULL,
    second_name character varying(64) NOT NULL,
    first_surname character varying(64) NOT NULL,
    second_surname character varying(64) NOT NULL,
    gender character varying(1) NOT NULL,
    birth_date timestamp with time zone,
    state character varying(3) NOT NULL,
    province character varying(32) NOT NULL,
    occupation character varying(32) NOT NULL,
    balance numeric(5,2) NOT NULL,
    no_pay boolean NOT NULL,
    badge_name character varying(64) NOT NULL,
    cabin character varying(16) NOT NULL,
    passport character varying(16) NOT NULL,
    birth_cert_num integer,
    birth_cert_fol integer,
    birth_cert_book integer,
    registrar character varying(256) NOT NULL,
    mother_id integer,
    father_id integer,
    counselor_id integer NOT NULL,
    generation integer NOT NULL,
    structure character varying(16) NOT NULL,
    bus character varying(16) NOT NULL,
    small_group_id integer,
    registrar_title character varying(16) NOT NULL,
    registrar_position character varying(16) NOT NULL,
    reg_state character varying(3) NOT NULL,
    reg_province character varying(32) NOT NULL,
    permission_status integer NOT NULL,
    lawyer character varying(16) NOT NULL,
    signed_up boolean NOT NULL,
    CONSTRAINT ck_generation_pstv_b4c69f1d7dd2cb6 CHECK ((generation >= 0)),
    CONSTRAINT signup_camper_birth_cert_book_check CHECK ((birth_cert_book >= 0)),
    CONSTRAINT signup_camper_birth_cert_fol_check CHECK ((birth_cert_fol >= 0)),
    CONSTRAINT signup_camper_birth_cert_num_check CHECK ((birth_cert_num >= 0))
);


ALTER TABLE public.signup_camper OWNER TO campmanager;

--
-- Name: signup_camper_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE signup_camper_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.signup_camper_id_seq OWNER TO campmanager;

--
-- Name: signup_camper_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE signup_camper_id_seq OWNED BY signup_camper.id;


--
-- Name: signup_counselor; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE signup_counselor (
    id integer NOT NULL,
    first_name character varying(64) NOT NULL,
    second_name character varying(64) NOT NULL,
    first_surname character varying(64) NOT NULL,
    second_surname character varying(64) NOT NULL,
    gender character varying(1) NOT NULL,
    balance numeric(5,2) NOT NULL,
    no_pay boolean NOT NULL,
    badge_name character varying(64) NOT NULL,
    cabin character varying(16) NOT NULL,
    small_group_id integer NOT NULL,
    generation integer NOT NULL,
    structure character varying(16) NOT NULL,
    bus character varying(16) NOT NULL,
    signed_up boolean NOT NULL,
    CONSTRAINT ck_generation_pstv_2cabac3ebb459333 CHECK ((generation >= 0))
);


ALTER TABLE public.signup_counselor OWNER TO campmanager;

--
-- Name: signup_counselor_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE signup_counselor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.signup_counselor_id_seq OWNER TO campmanager;

--
-- Name: signup_counselor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE signup_counselor_id_seq OWNED BY signup_counselor.id;


--
-- Name: signup_guest; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE signup_guest (
    id integer NOT NULL,
    first_name character varying(64) NOT NULL,
    second_name character varying(64) NOT NULL,
    first_surname character varying(64) NOT NULL,
    second_surname character varying(64) NOT NULL,
    gender character varying(1) NOT NULL,
    balance numeric(5,2) NOT NULL,
    no_pay boolean NOT NULL,
    badge_name character varying(64) NOT NULL,
    cabin character varying(16) NOT NULL,
    signed_up boolean NOT NULL
);


ALTER TABLE public.signup_guest OWNER TO campmanager;

--
-- Name: signup_guest_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE signup_guest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.signup_guest_id_seq OWNER TO campmanager;

--
-- Name: signup_guest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE signup_guest_id_seq OWNED BY signup_guest.id;


--
-- Name: signup_parent; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE signup_parent (
    id integer NOT NULL,
    first_name character varying(64) NOT NULL,
    second_name character varying(64) NOT NULL,
    first_surname character varying(64) NOT NULL,
    second_surname character varying(64) NOT NULL,
    gender character varying(1) NOT NULL,
    birth_date timestamp with time zone,
    state character varying(3) NOT NULL,
    province character varying(32) NOT NULL,
    occupation character varying(32) NOT NULL,
    gov_id character varying(10) NOT NULL,
    known_as character varying(255) NOT NULL
);


ALTER TABLE public.signup_parent OWNER TO campmanager;

--
-- Name: signup_parent_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE signup_parent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.signup_parent_id_seq OWNER TO campmanager;

--
-- Name: signup_parent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE signup_parent_id_seq OWNED BY signup_parent.id;


--
-- Name: signup_payment; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE signup_payment (
    id integer NOT NULL,
    receipt_id character varying(16) NOT NULL,
    payment_date date,
    amount numeric(5,2) NOT NULL,
    notes character varying(256) NOT NULL,
    content_type_id integer NOT NULL,
    object_id integer NOT NULL,
    CONSTRAINT signup_payment_object_id_check CHECK ((object_id >= 0))
);


ALTER TABLE public.signup_payment OWNER TO campmanager;

--
-- Name: signup_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE signup_payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.signup_payment_id_seq OWNER TO campmanager;

--
-- Name: signup_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE signup_payment_id_seq OWNED BY signup_payment.id;


--
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO campmanager;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: campmanager
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO campmanager;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: campmanager
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY finances_transaction ALTER COLUMN id SET DEFAULT nextval('finances_transaction_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY logistics_smallgroup ALTER COLUMN id SET DEFAULT nextval('logistics_smallgroup_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_camper ALTER COLUMN id SET DEFAULT nextval('signup_camper_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_counselor ALTER COLUMN id SET DEFAULT nextval('signup_counselor_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_guest ALTER COLUMN id SET DEFAULT nextval('signup_guest_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_parent ALTER COLUMN id SET DEFAULT nextval('signup_parent_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_payment ALTER COLUMN id SET DEFAULT nextval('signup_payment_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY auth_group (id, name) FROM stdin;
1	Asistente de inscripción
2	Encargado de inscripción
3	Encargado de finanzas
4	Asistente de migración
5	Encargado de logística
6	Encargado de diseño
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_group_id_seq', 6, true);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
39	1	32
40	1	33
41	1	36
42	1	38
43	1	39
44	1	40
45	1	25
46	1	26
47	1	27
48	1	31
49	2	32
50	2	33
51	2	36
52	2	38
53	2	39
54	2	40
55	2	45
56	2	25
57	2	26
58	2	27
59	2	31
60	3	48
61	3	49
62	3	46
63	3	47
64	4	32
65	4	34
66	4	45
67	4	28
68	4	29
69	4	30
70	4	31
71	5	42
72	5	44
73	5	45
74	5	39
75	6	42
76	6	45
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 76, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add site	6	add_site
17	Can change site	6	change_site
18	Can delete site	6	delete_site
19	Can add log entry	7	add_logentry
20	Can change log entry	7	change_logentry
21	Can delete log entry	7	delete_logentry
22	Can add migration history	8	add_migrationhistory
23	Can change migration history	8	change_migrationhistory
24	Can delete migration history	8	delete_migrationhistory
25	Can add Payment	9	add_payment
26	Can change Payment	9	change_payment
27	Can delete Payment	9	delete_payment
28	Can add Parent	10	add_parent
29	Can change Parent	10	change_parent
30	Can delete Parent	10	delete_parent
31	Can add Camper	11	add_camper
32	Can change Camper	11	change_camper
33	Can delete Camper	11	delete_camper
34	Generate Permission	11	generate_permission
35	Can add Counselor	12	add_counselor
36	Can change Counselor	12	change_counselor
37	Can delete Counselor	12	delete_counselor
38	Can add Guest	13	add_guest
39	Can change Guest	13	change_guest
40	Can delete Guest	13	delete_guest
41	Can add Small Group	14	add_smallgroup
42	Can change Small Group	14	change_smallgroup
43	Can delete Small Group	14	delete_smallgroup
44	View Reports	14	view_reports
45	Attendant Report	14	attendant_report
46	Can add Transaction	15	add_transaction
47	Can change Transaction	15	change_transaction
48	Can delete Transaction	15	delete_transaction
49	View Reports	15	view_reports
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_permission_id_seq', 49, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
3	pbkdf2_sha256$10000$5V8PwSkpRY0U$e1AaDTTHR7w76u7SOmi9xhvV/qEcQJ8zej5nGi3eotk=	2013-07-16 10:23:16-06	f	clari	Clarissa	Rodriguez		t	f	2013-06-01 21:15:56-06
4	pbkdf2_sha256$10000$WcOrxnEGbMut$NDmhxA+kYwWxPi2VyjaUeWVWxSw0Mg1/AUnwgnJmUlc=	2013-06-09 14:41:22-06	f	erik	Erik	Miranda		t	f	2013-06-01 21:17:04-06
5	pbkdf2_sha256$10000$dDM6IuCwWtqa$/c9AH1EzC+HLftaTlizpeIzeUW6390wQYx2Mw1XPSKY=	2013-08-01 09:28:23-06	f	ale	Ale	Durán		t	f	2013-06-01 21:17:32-06
6	pbkdf2_sha256$10000$rbz83N7UrAkF$wDzZPys+M3TRVNwtWMoKLhvnqDIZXKKmL7uvIaHnwgw=	2013-07-31 15:10:25-06	f	maricela	Maricela	de León		t	f	2013-06-01 21:18:23-06
7	pbkdf2_sha256$10000$UIjIub2rH21k$AIim9uk4x4iTUYVLjgUZw5bFzVi1nHMh6iPw2rtNUWU=	2013-08-02 00:01:55-06	f	ricardo	Ricardo	Medrano		t	f	2013-06-02 16:34:34-06
12	pbkdf2_sha256$12000$tSisjVNN0Pyo$Zql15AsAM+XwzPLX3sumcfmYQlRtDhPimy2ihb+VCjo=	2014-07-27 02:15:26.434523-06	f	mou				t	t	2014-07-20 11:55:54-06
8	pbkdf2_sha256$12000$lfwoYDYmJyTW$DaRACNpij7XWuA5FVoMs3Df7sJnjOfofhAF7/AuJ0Ow=	2014-08-02 00:53:33.858835-06	f	mike	Mike	Guardado		t	t	2013-07-10 06:28:40-06
10	pbkdf2_sha256$12000$hSH9MKz9U24t$GVi458PagPAgbNkjGvRPdGFpaIQoS+43Lx+Ay4Ycdm0=	2014-09-04 08:17:42.915146-06	f	aby	Abigail	González de Santillana		t	t	2014-06-08 15:00:10-06
11	pbkdf2_sha256$12000$WjeicIsyBa9N$Q60pH4RfcAb9O6IBufyw+9P5tKYQ8OelObzTIm8tJA0=	2014-07-20 11:55:25-06	f	javo	Javier	Santillana		t	t	2014-07-20 11:55:25-06
9	pbkdf2_sha256$12000$tlKgKSNve98R$09ka0y8doVbP5Xzl8JyMAZvU1Ohaiq2cF/KwrT4RIsI=	2014-07-24 18:47:45.553387-06	f	sarai	Saraí	Navarrete		t	t	2013-07-16 23:47:14-06
1	pbkdf2_sha256$12000$rmZHayexS4ei$Mhmx3oHGH29OV5Ccc9/ocs+8kSKc/h+ByMeHMb1s+Zw=	2015-01-14 21:42:56.390666-06	t	jerivas	Eduardo	Rivas	e@jerivas.com	t	t	2013-05-29 12:23:50-06
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
12	3	1
13	4	1
14	5	1
15	6	1
16	7	4
19	10	2
20	10	3
21	9	6
22	8	5
25	11	5
26	12	5
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 26, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_user_id_seq', 12, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
7	2014-05-29 18:02:23.414956-06	1	3	2	rebe	3	
8	2014-05-29 18:03:34.095102-06	1	10	4	Vicente Cruz García	2	Modificado/a first_name, first_surname y second_surname.
9	2014-05-29 18:03:53.207148-06	1	10	10	Blanca Gloria Elizabeth Salinas de Mata	2	Modificado/a known_as y occupation.
10	2014-05-29 18:04:21.454003-06	1	10	3	Sara Noemy Vásquz de Cruz	2	Modificado/a first_name, second_name, first_surname, second_surname y occupation.
11	2014-06-03 13:46:29.739817-06	1	14	40	Elí	1	
12	2014-06-03 13:46:43.666286-06	1	12	33	Tarquino Aldair Hernández Cañenguez	1	
13	2014-06-03 13:47:01.47621-06	1	14	41	Dodava	1	
14	2014-06-03 13:47:45.313671-06	1	12	34	Marcela Roxana Melara Rodríguez	1	
15	2014-06-03 13:48:24.951953-06	1	14	42	Magdiel	1	
16	2014-06-03 13:48:39.774282-06	1	12	35	Elia Fernanda Carranza Ríos	1	
17	2014-06-03 13:48:52.59744-06	1	14	43	Asael	1	
18	2014-06-03 13:49:18.921436-06	1	12	36	Gerardo Josué Osorio Portillo	1	
19	2014-06-03 14:00:06.873585-06	1	10	8	Rene Moisés Sevillano Martinez	2	Modificado/a second_name.
20	2014-06-08 15:00:10.54022-06	1	3	10	aby	1	
21	2014-06-08 15:00:45.022073-06	1	3	10	aby	2	Modificado/a first_name, last_name, is_staff y groups.
22	2014-06-22 10:37:27.555426-06	10	12	5	Ricardo Josué Medrano Guerrero	2	Añadido/a "001 - $5" abono.
23	2014-06-22 10:39:46.828061-06	10	11	23	Karla Tatiana Duke Monchez	2	Añadido/a "002 - $5" abono.
24	2014-06-22 10:41:53.573608-06	10	11	139	Roger Ellebien Torres Díaz	1	
25	2014-06-22 10:44:54.510694-06	10	11	140	Jonathan Josué González Sosa	1	
26	2014-06-22 10:47:22.296015-06	10	11	141	Krisia Díaz	1	
27	2014-06-22 10:48:12.87525-06	10	11	20	Stephanie Elizabeth Ramos Ramirez	2	Añadido/a "007 - $5" abono.
28	2014-06-22 10:48:52.238944-06	10	11	71	Jonathan Eduardo Hernández Díaz	2	Añadido/a "008 - $5" abono.
29	2014-06-22 10:49:35.167892-06	10	12	21	Clarissa Esmeralda Rodriguez Monge	2	Añadido/a "009 - $20" abono.
30	2014-06-22 10:50:55.074992-06	10	11	142	Sara Ester Martínez Francia	1	
31	2014-06-22 10:51:41.297102-06	10	11	2	Adriana Saraí Vasquez   Rodríguez	2	Añadido/a "011 - $5" abono.
32	2014-06-22 10:52:30.008573-06	10	11	83	Miguel Alejandro Soriano Beltrán	2	Añadido/a "012 - $5" abono.
33	2014-06-22 10:53:18.092946-06	10	12	2	José David Nery Maravilla	2	Añadido/a "014 - $5" abono.
34	2014-06-22 10:54:28.907826-06	10	12	22	Ruth Abigail Méndez Alfaro	2	Añadido/a "015 - $5" abono.
35	2014-06-22 10:55:07.969727-06	10	11	15	Marco Stefano Barrientos Melgar	2	Añadido/a "016 - $20" abono.
36	2014-06-22 10:55:35.999719-06	10	12	19	Pamela Alejandra Chacón Rodríguez	2	Añadido/a "017 - $10" abono.
37	2014-06-22 10:56:09.372716-06	10	12	4	María Alejandra Durán Castellanos	2	Añadido/a "018 - $20" abono.
38	2014-06-22 10:56:46.949328-06	10	11	13	Guillermo Arturo Alvarado Araujo	2	Añadido/a "019 - $15" abono.
39	2014-06-22 10:57:19.736753-06	10	11	105	Josué David Lainez Castro	2	Añadido/a "020 - $50" abono.
40	2014-06-22 10:57:54.215263-06	10	11	102	William Rodrigo Huezo Orantes	2	Añadido/a "021 - $5" abono.
41	2014-06-22 11:05:07.932512-06	10	11	53	Jonathan Alexander Arteaga Segovia	2	Añadido/a "022 - $75" abono.
42	2014-06-22 11:08:45.968533-06	10	11	143	Irma Elizabeth Claros Alemán	1	
43	2014-06-22 11:09:46.323976-06	10	11	12	Eugenia Beatriz Alvarado Araujo	2	Modificado/a badge_name. Añadido/a "024 - $20" abono.
44	2014-06-22 11:10:18.596377-06	10	11	13	Guillermo Arturo Alvarado Araujo	2	Añadido/a "025 - $60" abono.
45	2014-06-22 11:12:14.506861-06	10	11	144	David Alejandro Gómez Elias	1	
46	2014-06-22 11:12:57.847196-06	10	11	70	Adriana María Rodríguez Monge	2	Añadido/a "027 - $5" abono.
47	2014-06-22 11:15:56.282645-06	10	12	24	Christian Steve Domínguez Vallecillos	2	Añadido/a "028 - $75" abono.
48	2014-06-22 11:17:30.408084-06	10	12	34	Marcela Roxana Melara Rodríguez	2	Añadido/a "029 - $20" abono.
49	2014-06-22 11:18:03.877291-06	10	11	86	Carlos Ernesto Medrano Guerrero	2	Añadido/a "030 - $20" abono.
50	2014-06-22 11:18:25.537335-06	10	11	36	Gabriela María Melara Rodríguez	2	Añadido/a "031 - $20" abono.
51	2014-06-22 11:21:22.358356-06	10	11	61	Andrea Fernanda Matínez González	2	Añadido/a "041 - $5" abono.
52	2014-06-22 11:21:57.38107-06	10	11	39	Marlon Edgardo Figueroa Martínez	2	Añadido/a "042 - $10" abono.
53	2014-06-22 11:22:45.144865-06	10	11	96	Ana Margarita Santamaría Hernández	2	Modificado/a badge_name. Añadido/a "043 - $5" abono.
54	2014-06-22 11:24:05.455356-06	10	11	145	Ariel Josué Martínez Márquez	1	
55	2014-06-22 11:24:56.750945-06	10	11	119	Irina Lucia Orantes Regalado	2	Añadido/a "045 - $5" abono.
56	2014-06-22 11:25:05.301086-06	10	11	119	Irina Lucia Orantes Regalado	2	Modificado/a badge_name.
57	2014-06-22 11:28:40.245497-06	10	11	146	Ana Elizabeth Montoya Ardón	1	
58	2014-06-22 11:30:25.934898-06	10	11	21	Roxana Abigail Comandari Rodríguez	2	Añadido/a "047 - $10" abono.
59	2014-06-22 11:31:17.850797-06	10	11	2	Adriana Saraí Vasquez   Rodríguez	2	Añadido/a "048 - $7" abono.
60	2014-06-22 11:32:22.80009-06	10	11	127	Diego Alfredo Ochoa Gómez	2	Añadido/a "1b - $75" abono.
61	2014-06-22 11:33:33.32916-06	10	11	126	Alejandro Alfredo Ochoa Gómez	2	Añadido/a "2b - $75" abono.
62	2014-06-22 11:35:23.386231-06	10	11	147	Rebeca Aracely Alvarado Granados	1	
63	2014-06-22 11:38:54.680893-06	10	11	56	Julieta Elizabeth Ponce Martir	2	Añadido/a "5b - $5" abono.
64	2014-06-22 11:39:46.415582-06	10	11	148	Andrea Roxana Ponce Martir	1	
65	2014-06-22 11:40:26.414777-06	10	11	139	Roger Ellebien Torres Díaz	2	Añadido/a "6b - $10" abono.
66	2014-06-22 11:42:21.31343-06	10	11	149	Karla Iliana Baires Escobar	1	
67	2014-06-22 11:43:22.133979-06	10	11	150	Luis Rebe Baires Escobar	1	
68	2014-06-22 11:43:52.417508-06	10	11	99	Cristian Alexander Ayala Serrano	2	Añadido/a "9b - $5" abono.
69	2014-06-22 11:54:34.027902-06	10	15	44	 - $1007.00 (Ingreso)	1	
70	2014-06-25 23:47:17.115327-06	1	3	1	jerivas	2	Modificado/a first_name.
71	2014-06-28 23:40:22.089789-06	10	13	9	Mauricio Alberto Paz Herrera	1	
72	2014-06-28 23:41:23.922536-06	10	11	82	Alejandra Poulette Montalvo Meza	2	Añadido/a "083 - $5" abono.
73	2014-06-28 23:42:43.509577-06	10	12	36	Gerardo Josué Osorio Portillo	2	Añadido/a "083b - $20" abono.
74	2014-06-28 23:44:25.879736-06	10	11	151	Juan  Carlos Morales Sosa	1	
75	2014-06-28 23:45:54.076636-06	10	11	152	Adriana Contreras Pujol	1	
76	2014-06-28 23:46:50.958321-06	10	11	152	Adriana Contreras Pujol	2	No ha cambiado ningún campo.
77	2014-06-28 23:47:59.61717-06	10	11	153	Nicoles Contreras Pujol	1	
78	2014-06-28 23:49:06.253618-06	10	11	154	Emilton Daniel Alvarenga Flores	1	
79	2014-06-28 23:49:28.346883-06	10	11	48	Ivy Vanessa Gutiérrez Padilla	2	Añadido/a "088 - $5" abono.
80	2014-06-28 23:50:05.997-06	10	11	22	Marcela Alejandra Mendoza Orellana	2	Añadido/a "089 - $20" abono.
81	2014-06-28 23:50:39.445906-06	10	12	30	Oliver Stanley Larín Aguirre	2	Añadido/a "090 - $5" abono.
82	2014-06-28 23:51:12.174849-06	10	12	27	Karen Noemi López Dimas	2	Modificado/a badge_name. Añadido/a "091 - $5" abono.
83	2014-06-28 23:54:04.710982-06	10	12	12	Jacob Benjamín Zelaya Chicas	2	Añadido/a "035 - $75" abono.
84	2014-06-28 23:54:42.556818-06	10	13	9	Mauricio Alberto Paz Herrera	2	Añadido/a "032 - $20" abono.
85	2014-06-28 23:55:17.558753-06	10	11	65	Mauricio Javier Castellón Cerritos	2	Añadido/a "033 - $20" abono.
86	2014-06-28 23:55:53.435287-06	10	11	27	Christian Alessandro Calderón Castillo	2	Añadido/a "034 - $20" abono.
87	2014-06-28 23:56:38.718789-06	10	11	142	Sara Ester Martínez Francia	2	Añadido/a "036 - $20" abono.
88	2014-06-29 00:12:06.040761-06	10	15	45	001 - $310.00 (Ingreso)	1	
89	2014-06-29 00:13:48.51661-06	10	15	46	002 - $10.00 (Ingreso)	1	
90	2014-06-29 08:37:44.150788-06	10	11	41	Ludwing Alfredo Contreras Menjívar	2	Modificado/a badge_name. Añadido/a "049 - $25" abono.
91	2014-06-29 08:40:09.135403-06	10	11	42	Katherine Haydee Contreras Menjívar	2	Añadido/a "050 - $25" abono.
92	2014-06-29 08:57:18.798305-06	10	12	12	Jacob Benjamín Zelaya Chicas	2	Modificados amount para "035 - $70.00" abono.
93	2014-07-13 09:03:48.873824-06	10	11	54	David Godofredo Campos  Aguilar	2	Añadido/a "081b - $10" abono.
94	2014-07-13 09:06:22.215732-06	10	11	155	María José Alvarado Argueta	1	
95	2014-07-13 09:07:33.524975-06	10	11	140	Jonathan Josué González Sosa	2	Añadido/a "083.1 - $40" abono.
96	2014-07-13 09:08:48.640943-06	10	11	147	Rebeca Aracely Alvarado Granados	2	Añadido/a "084b - $40" abono.
97	2014-07-13 09:10:35.831165-06	10	11	94	Cinthya Gissellie Pineda  Bonilla	2	Añadido/a "085b - $5" abono.
98	2014-07-13 09:11:46.450768-06	10	11	25	Dalia Marcela Huezo Pacheco	2	Añadido/a "086b - $5" abono.
99	2014-07-13 09:12:15.758742-06	10	11	8	Diana Saraí Santos Martir	2	Añadido/a "087b - $5" abono.
100	2014-07-13 09:13:17.316978-06	10	11	156	Paola Rebeca Lara Cruz	1	
101	2014-07-13 09:13:54.645286-06	10	11	2	Adriana Saraí Vasquez   Rodríguez	2	Añadido/a "089b - $26.80" abono.
102	2014-07-13 09:14:59.675858-06	10	13	10	Javier Ernesto Santillana Meléndez	1	
103	2014-07-13 09:15:40.292091-06	10	13	11	Grisel Abigail González de Santillana	1	
104	2014-07-13 09:16:21.197274-06	10	15	47	092b - $30.00 (Egreso)	1	
105	2014-07-13 09:17:21.276094-06	10	11	157	Karen Adriana Recinos Orellana	1	
106	2014-07-13 09:17:52.131063-06	10	12	2	José David Nery Maravilla	2	Añadido/a "094b - $20" abono.
107	2014-07-13 09:18:27.257645-06	10	11	46	Katherine Rebeca Medrano Guerrero	2	Añadido/a "095b - $5" abono.
108	2014-07-13 09:18:56.482204-06	10	11	17	Florence Natalia Perdomo de la O	2	Añadido/a "096b - $5" abono.
109	2014-07-13 09:19:26.252736-06	10	11	65	Mauricio Javier Castellón Cerritos	2	Añadido/a "097 - $20" abono.
110	2014-07-13 09:19:51.434219-06	10	11	120	Eduardo Enrique Herrera	2	Añadido/a "098 - $75" abono.
111	2014-07-13 09:20:14.954099-06	10	11	21	Roxana Abigail Comandari Rodríguez	2	Añadido/a "099 - $40" abono.
112	2014-07-13 09:20:54.200407-06	10	11	17	Florence Natalia Perdomo de la O	2	Añadido/a "100 - $30" abono.
113	2014-07-13 09:21:12.31279-06	10	11	155	María José Alvarado Argueta	2	Añadido/a "101 - $5" abono.
114	2014-07-13 09:21:39.10694-06	10	11	128	Carlos  Samuel Flores Olivares	2	Modificado/a badge_name. Añadido/a "102 - $5" abono.
115	2014-07-13 09:22:37.895966-06	10	11	158	Carlos Alejandro Montoya Cáceres	1	
116	2014-07-13 09:23:06.967262-06	10	11	8	Diana Saraí Santos Martir	2	Añadido/a "104 - $25" abono.
117	2014-07-13 09:24:00.220456-06	10	11	87	Alejandra Maria Claros Burgos	2	Modificado/a first_surname, second_surname y badge_name. Añadido/a "105 - $5" abono.
118	2014-07-13 09:24:24.687405-06	10	11	73	Carmen Elena Yanes Peña	2	Añadido/a "106 - $10" abono.
119	2014-07-13 09:24:51.646662-06	10	11	77	Raúl  David Yanes Peña	2	Modificado/a badge_name. Añadido/a "107 - $10" abono.
120	2014-07-13 09:26:21.451469-06	10	11	27	Christian Alessandro Calderón Castillo	2	Añadido/a "108 - $5" abono.
121	2014-07-13 09:27:26.26897-06	10	11	159	Denise Elizabeth Hernández Pineda	1	
122	2014-07-13 09:28:35.992195-06	10	11	160	Diana Marcela Pacheco Guerrero	1	
123	2014-07-13 09:29:30.833476-06	10	11	161	Mauricio Alejandro Pacheco Guerrero	1	
124	2014-07-13 09:30:44.386857-06	10	11	162	José Eduardo Pacheco Guerrero	1	
125	2014-07-13 09:31:45.121457-06	10	11	163	Daniel Alberto Alcoleas Jaime	1	
126	2014-07-13 09:32:03.18166-06	10	11	66	Emely Nohemi Sevillano Platero	2	Añadido/a "113 - $10" abono.
127	2014-07-13 09:32:54.513166-06	10	11	164	María Fernanda Balibrerra Barahona	1	
128	2014-07-13 09:33:37.788143-06	10	15	48	115 - $255.00 (Egreso)	1	
129	2014-07-16 21:38:42.497592-06	10	11	38	Laura Celina Gil Henríquez	2	Añadido/a "037 - $10" abono.
130	2014-07-16 21:39:24.548053-06	10	13	9	Mauricio Alberto Paz Herrera	2	Añadido/a "038 - $50" abono.
131	2014-07-16 21:40:13.801013-06	10	11	24	Andrea Lizzeth Letona Hernández	2	Añadido/a "039 - $78" abono.
132	2014-07-16 21:42:51.073697-06	10	11	145	Ariel Josué Martínez Márquez	2	Añadido/a "040 - $20" abono.
133	2014-07-16 21:48:11.50621-06	10	11	82	Alejandra Poulette Montalvo Meza	2	Modificados receipt_id para "082b - $5.00" abono.
134	2014-07-16 21:48:54.118189-06	10	12	36	Gerardo Josué Osorio Portillo	2	Modificados receipt_id para "083 - $20.00" abono.
135	2014-07-16 21:52:23.806429-06	10	11	19	Francisco Ariel Linares Melgar	2	Añadido/a "120 - $5" abono.
136	2014-07-16 21:54:21.160539-06	10	11	165	Gloria Campos Gutiérrez Quinteros	1	
137	2014-07-16 21:54:47.472146-06	10	11	55	Jorge Antonio Campos Miranda	2	Añadido/a "122 - $10" abono.
138	2014-07-16 21:55:38.277471-06	10	11	70	Adriana María Rodríguez Monge	2	Añadido/a "123 - $70" abono.
139	2014-07-16 21:56:52.538463-06	10	11	166	Katherine Lisbeth Vásquez Chávez	1	
140	2014-07-16 21:57:20.27476-06	10	11	9	Adriana Elizabeth Gutiérrez Padilla	2	Añadido/a "125 - $75" abono.
141	2014-07-16 21:58:05.76742-06	10	11	146	Ana Elizabeth Montoya Ardón	2	Añadido/a "126 - $60" abono.
142	2014-07-16 22:02:53.044314-06	10	11	167	Niña Exodo 1	1	
143	2014-07-16 22:04:18.938884-06	10	11	168	Niña exodo 2	1	
144	2014-07-16 22:05:35.294967-06	10	11	169	Niña exodo 3	1	
145	2014-07-16 22:06:28.97196-06	10	11	170	niña exodo 4	1	
146	2014-07-17 03:17:28.61958-06	10	11	47	Astrid Margarita Hernández Villacorta	2	Añadido/a "131 - $78" abono.
147	2014-07-17 03:18:04.602067-06	10	11	76	Mónica Gabriela Hernández Villacorta	2	Modificado/a badge_name. Añadido/a "131.b - $78" abono.
148	2014-07-17 03:18:31.910257-06	10	11	17	Florence Natalia Perdomo de la O	2	Añadido/a "132 - $43" abono.
149	2014-07-17 03:18:54.856277-06	10	11	159	Denise Elizabeth Hernández Pineda	2	Añadido/a "133 - $20" abono.
150	2014-07-17 03:20:22.207866-06	10	11	171	Moisés Daniel Mejía Henríquez	1	
151	2014-07-17 03:21:21.285491-06	10	11	172	Cindy Nayeli Bonilla Beltran	1	
152	2014-07-17 03:22:04.538362-06	10	11	108	Melany Sofia Bonilla Beltrán	2	Añadido/a "136 - $8" abono.
153	2014-07-17 03:22:55.006492-06	10	11	173	Nicole Estefania Rodas Chávez	1	
154	2014-07-17 03:23:20.780973-06	10	11	140	Jonathan Josué González Sosa	2	Añadido/a "138 - $20" abono.
155	2014-07-17 03:24:53.947085-06	10	11	174	Joaquin Cornejo Viches	1	
156	2014-07-17 03:25:27.92447-06	10	11	12	Eugenia Beatriz Alvarado Araujo	2	Añadido/a "140 - $55" abono.
157	2014-07-17 03:26:11.609176-06	10	11	58	Nicole Jasmin Mata Salinas	2	Añadido/a "141 - $20" abono.
158	2014-07-17 03:27:27.915389-06	10	11	46	Katherine Rebeca Medrano Guerrero	2	Añadido/a "116 - $70" abono.
159	2014-07-17 03:27:47.08541-06	10	11	23	Karla Tatiana Duke Monchez	2	Añadido/a "117 - $70" abono.
160	2014-07-17 03:28:08.901782-06	10	11	86	Carlos Ernesto Medrano Guerrero	2	Añadido/a "118 - $50" abono.
161	2014-07-17 03:29:54.4165-06	10	11	175	Maria Beatriz Zuniga Ramirez	1	
162	2014-07-17 03:31:49.536701-06	10	12	23	Priscila Saraí Sevillano Platero	2	Añadido/a "124.1 - $12" abono.
163	2014-07-17 03:32:13.10223-06	10	12	29	René Moisés Sevillano Platero	2	Añadido/a "125.1 - $5" abono.
164	2014-07-20 08:49:43.420871-06	10	11	150	Luis Rene Baires Escobar	2	Modificado/a second_name.
165	2014-07-20 10:37:44.967434-06	1	3	9	sarai	2	Modificado/a password.
166	2014-07-20 10:37:54.092903-06	1	3	9	sarai	2	Modificado/a is_active.
167	2014-07-20 11:45:45.505406-06	1	3	8	mike	2	Modificado/a is_active.
168	2014-07-20 11:55:25.757357-06	1	3	11	javo	1	
169	2014-07-20 11:55:45.125698-06	1	3	11	javo	2	Modificado/a first_name, last_name y groups.
170	2014-07-20 11:55:54.868731-06	1	3	12	mou	1	
171	2014-07-20 11:56:04.751392-06	1	3	12	mou	2	Modificado/a groups.
172	2014-07-20 11:56:27.775889-06	1	3	11	javo	2	Modificado/a is_staff.
173	2014-07-20 11:56:37.418098-06	1	3	12	mou	2	Modificado/a is_staff.
174	2014-07-23 22:47:55.343473-06	10	11	167	María Beatriz Zuniga Ramirez	2	Modificado/a first_name, second_name, first_surname, second_surname y badge_name. Añadido/a "119b - $5" abono.
175	2014-07-23 22:48:47.762968-06	10	11	168	Tania Gisselle Cárcamo Hernández	2	Modificado/a first_name, second_name, first_surname y second_surname. Añadido/a "120b - $5" abono.
176	2014-07-23 22:49:59.32263-06	10	11	169	Karla Veronica Bonilla Peña	2	Modificado/a first_name, second_name, first_surname, second_surname y badge_name. Añadido/a "121b - $5" abono.
177	2014-07-23 22:50:34.253158-06	10	11	170	Reina Dolores Barrera	2	Modificado/a first_name, second_name, first_surname y badge_name. Añadido/a "122b - $5" abono.
178	2014-07-23 22:51:16.151217-06	10	12	4	María Alejandra Durán Castellanos	2	Añadido/a "123b - $30" abono.
179	2014-07-23 22:52:01.257328-06	10	12	23	Priscila Saraí Sevillano Platero	2	No ha cambiado ningún campo.
180	2014-07-23 22:57:02.932102-06	10	11	176	Nelson Edgardo Linares Arias	1	
181	2014-07-23 22:59:15.736709-06	10	11	43	Natalia Daniela González Tobar	2	Añadido/a "127 - $10" abono.
182	2014-07-23 22:59:56.488223-06	10	11	150	Luis Rene Baires Escobar	2	Añadido/a "128 - $30" abono.
183	2014-07-23 23:00:17.962376-06	10	11	150	Luis Rene Baires Escobar	2	No ha cambiado ningún campo.
184	2014-07-23 23:01:08.336988-06	10	12	33	Tarquino Aldair Hernández Cañenguez	2	Modificado/a badge_name. Añadido/a "129 - $5" abono.
185	2014-07-23 23:02:12.405876-06	10	11	48	Ivy Vanessa Gutiérrez Padilla	2	Añadido/a "130B - $70" abono.
186	2014-07-23 23:02:51.623808-06	10	11	79	Alexia Rosibel Ochoa González	2	Añadido/a "131B - $10" abono.
187	2014-07-23 23:04:21.489942-06	10	11	177	Debora Elizabeth Romero Martínez	1	
188	2014-07-23 23:05:02.657711-06	10	11	157	Karen Adriana Recinos Orellana	2	Añadido/a "133b - $73" abono.
189	2014-07-23 23:05:37.665878-06	10	11	152	Adriana Contreras Pujol	2	Añadido/a "134b - $65" abono.
190	2014-07-23 23:06:07.253364-06	10	11	153	Nicole Contreras Pujol	2	Modificado/a first_name. Añadido/a "135b - $65" abono.
191	2014-07-23 23:06:48.012981-06	10	11	81	Carlos  Raúl Dominguez Hernández	2	Modificado/a badge_name. Añadido/a "136b - $50" abono.
192	2014-07-23 23:07:59.476105-06	10	11	40	Andrés Gerardo López Guevara	2	Modificado/a badge_name. Añadido/a "137b - $5" abono.
193	2014-07-23 23:09:03.652941-06	10	11	37	Raúl  Ernesto López Hernández	2	Añadido/a "138b - $70" abono.
194	2014-07-23 23:09:38.87388-06	10	11	159	Denise Elizabeth Hernández Pineda	2	Añadido/a "139b - $20" abono.
195	2014-07-23 23:11:09.552032-06	10	11	178	Nicole Astrid Rivas Cruz	1	
196	2014-07-23 23:11:37.490289-06	10	11	57	Sara Eunice Arteaga Funes	2	Añadido/a "142b - $50" abono.
197	2014-07-23 23:12:00.911834-06	10	11	38	Laura Celina Gil Henríquez	2	Añadido/a "143b - $68" abono.
198	2014-07-23 23:12:32.647339-06	10	11	143	Irma Elizabeth Claros Alemán	2	Añadido/a "144b - $45" abono.
199	2014-07-23 23:13:24.471599-06	10	12	16	Milton Josué Méndez Alfaro	2	Añadido/a "147 - $5" abono.
200	2014-07-23 23:13:49.697358-06	10	12	21	Clarissa Esmeralda Rodriguez Monge	2	Añadido/a "145b - $30" abono.
201	2014-07-23 23:14:17.515173-06	10	12	28	Sara Carolina Moreno Sandoval	2	Añadido/a "148b - $5" abono.
202	2014-07-25 00:00:01.530888-06	10	11	151	Juan  Carlos Morales Sosa	2	No ha cambiado ningún campo.
203	2014-07-25 00:00:20.650534-06	10	11	152	Adriana Contreras Pujol	2	No ha cambiado ningún campo.
204	2014-07-25 00:02:09.131547-06	10	12	27	Karen Noemi López Dimas	2	No ha cambiado ningún campo.
205	2014-07-25 00:02:39.326977-06	10	12	30	Oliver Stanley Larín Aguirre	2	Añadido/a "91b - $70" abono.
206	2014-07-25 00:03:13.919763-06	10	11	82	Alejandra Poulette Montalvo Meza	2	Añadido/a "92b - $20" abono.
207	2014-07-25 00:03:38.876552-06	10	11	18	Adriana Coello Gómez	2	Añadido/a "93b - $10" abono.
208	2014-07-25 00:03:57.04357-06	10	11	63	Roberto Benjamín Coello Gómez	2	Añadido/a "95b - $10" abono.
209	2014-07-25 00:04:27.85311-06	10	11	145	Ariel Josué Martínez Márquez	2	Añadido/a "96b - $25" abono.
210	2014-07-25 00:06:30.928977-06	10	11	179	Iker Gabriel Pérez Andrade	1	
211	2014-07-25 00:06:57.949102-06	10	11	22	Marcela Alejandra Mendoza Orellana	2	Añadido/a "98b - $15" abono.
212	2014-07-25 00:07:16.349796-06	10	11	20	Stephanie Elizabeth Ramos Ramirez	2	Añadido/a "99b - $70" abono.
213	2014-07-25 00:08:29.71474-06	10	11	180	Jose  Luis Monterrosa	1	
214	2014-07-25 00:09:21.458367-06	10	11	181	Mayra Fabiola Monterrosa	1	
215	2014-07-25 00:09:50.478133-06	10	11	45	Doris Esmeralda Alfaro  Castillo	2	Añadido/a "102b - $38" abono.
216	2014-07-25 00:10:22.894147-06	10	11	92	Gloria María Campos Fernández	2	Modificado/a badge_name. Añadido/a "103b - $5" abono.
217	2014-07-25 00:10:42.565536-06	10	11	91	Rene Rafael Campos Fernández	2	Añadido/a "104b - $5" abono.
218	2014-07-25 00:11:10.536962-06	10	11	141	Krisia Díaz	2	Añadido/a "105b - $35" abono.
219	2014-07-25 00:11:37.713549-06	10	11	37	Raúl  Ernesto López Hernández	2	Añadido/a "106b - $5" abono.
220	2014-07-25 00:12:18.265027-06	10	12	1	José Eduardo Rivas Melgar	2	Añadido/a "107b - $75" abono.
221	2014-07-25 00:13:36.088634-06	10	11	19	Francisco Ariel Linares Melgar	2	No ha cambiado ningún campo.
222	2014-07-25 00:14:29.528126-06	10	11	165	Gloria Campos Gutiérrez Quinteros	2	No ha cambiado ningún campo.
223	2014-07-25 00:14:58.698619-06	10	11	165	Gloria Raquel Gutiérrez Quinteros	2	Modificado/a second_name.
224	2014-07-25 00:16:12.261985-06	10	11	55	Jorge Antonio Campos Miranda	2	No ha cambiado ningún campo.
225	2014-07-25 07:07:48.292264-06	10	11	125	Emilio Armando Aguilar Obando	2	Añadido/a "129b - $78" abono.
226	2014-07-25 07:09:01.217082-06	10	11	170	Reina Dolores Barrera	2	No ha cambiado ningún campo.
227	2014-07-25 07:14:36.591438-06	10	11	27	Christian Alessandro Calderón Castillo	2	Añadido/a "142 - $15" abono.
228	2014-07-25 07:16:09.018243-06	10	11	140	Jonathan Josué González Sosa	2	Añadido/a "142.1 - $10" abono.
229	2014-07-25 07:27:09.457589-06	10	11	182	Raquel Alejandra Pérez Martínez	1	
230	2014-07-25 07:31:57.31718-06	10	11	105	Josué David Lainez Castro	2	Añadido/a "144.1 - $15" abono.
231	2014-07-25 07:33:07.940323-06	10	11	183	Rafaela Nicole Guardado Zelaya	1	
232	2014-07-25 07:34:39.078107-06	10	11	110	Rodrigo Alberto Martinez Renderos	2	Modificado/a badge_name. Añadido/a "146 - $5" abono.
233	2014-07-25 07:35:34.028671-06	10	11	21	Roxana Abigail Comandari Rodríguez	2	Añadido/a "146.1 - $25" abono.
234	2014-07-25 07:36:26.345268-06	10	11	21	Roxana Abigail Comandari Rodríguez	2	Modificados receipt_id para "147.1 - $25.00" abono.
235	2014-07-25 07:37:29.138164-06	10	11	146	Ana Elizabeth Montoya Ardón	2	Añadido/a "148 - $10" abono.
236	2014-07-25 07:38:21.169865-06	10	11	184	Pablo Ricardo Rodriguez Paz	1	
237	2014-07-25 07:44:57.456263-06	10	11	173	Nicole Estefania Rodas Chávez	2	Añadido/a "150 - $68" abono.
238	2014-07-25 07:46:29.675132-06	10	11	185	Abel Ernesto Magaña Rivera	1	
239	2014-07-26 09:08:12.933698-06	8	14	43	Asael	2	Modificado/a bus.
240	2014-07-26 09:08:12.938127-06	8	14	42	Magdiel	2	Modificado/a bus.
241	2014-07-26 09:08:12.942708-06	8	14	41	Dodava	2	Modificado/a bus.
242	2014-07-26 09:08:12.947113-06	8	14	40	Elí	2	Modificado/a bus.
243	2014-07-26 09:08:12.951693-06	8	14	34	Manos	2	Modificado/a bus.
244	2014-07-26 09:08:12.958358-06	8	14	33	Adriel	2	Modificado/a bus.
245	2014-07-26 09:08:12.96331-06	8	14	32	Karmi	2	Modificado/a bus.
246	2014-07-26 09:08:12.968195-06	8	14	31	Zuria	2	Modificado/a bus.
247	2014-07-26 09:08:52.8904-06	8	14	30	Keilah	2	Modificado/a bus.
248	2014-07-26 09:08:52.894876-06	8	14	29	Mati	2	Modificado/a bus.
249	2014-07-26 09:08:52.89963-06	8	14	28	Kyrios	2	Modificado/a bus.
250	2014-07-26 09:08:52.904353-06	8	14	27	Kadisha	2	Modificado/a bus.
251	2014-07-26 09:08:52.909-06	8	14	26	Febe	2	Modificado/a bus.
252	2014-07-26 09:08:52.913607-06	8	14	20	Jezreel	2	Modificado/a bus.
253	2014-07-26 09:08:52.917436-06	8	14	38	Uriel	2	Modificado/a bus.
254	2014-07-26 09:09:18.710728-06	8	14	19	Zabdi	2	Modificado/a bus.
255	2014-07-26 09:09:18.715638-06	8	14	12	Abdi	2	Modificado/a bus.
256	2014-07-26 09:09:18.72018-06	8	14	11	Yoel	2	Modificado/a bus.
257	2014-07-26 09:09:18.724046-06	8	14	10	Bitia	2	Modificado/a bus.
258	2014-07-26 09:09:18.72778-06	8	14	6	Jesed	2	Modificado/a bus.
259	2014-07-26 09:09:18.732219-06	8	14	4	Samuel	2	Modificado/a bus.
260	2014-07-26 09:10:17.577325-06	8	14	15	Abdiel	2	Modificado/a bus.
261	2014-07-26 09:10:17.581676-06	8	14	14	Ester	2	Modificado/a bus.
262	2014-07-26 09:10:17.586443-06	8	14	3	Eliana	2	Modificado/a bus.
263	2014-07-26 09:10:17.591226-06	8	14	18	Abigail	2	Modificado/a bus.
264	2014-07-26 09:10:17.595202-06	8	14	16	Elyon	2	Modificado/a bus.
265	2014-07-26 09:10:17.599422-06	8	14	13	Ithiel	2	Modificado/a bus.
266	2014-07-26 09:10:17.6033-06	8	14	5	Migdal	2	Modificado/a bus.
267	2014-07-26 09:10:17.608054-06	8	14	2	Abiatar	2	Modificado/a bus.
268	2014-07-26 09:10:17.61288-06	8	14	1	Abiel	2	Modificado/a bus.
269	2014-07-26 09:17:54.342017-06	8	14	16	Elyon	2	Modificado/a cabin.
270	2014-07-26 09:17:54.347515-06	8	14	2	Abiatar	2	Modificado/a cabin.
271	2014-07-26 09:17:54.35207-06	8	14	1	Abiel	2	Modificado/a cabin.
272	2014-07-26 09:17:54.35633-06	8	14	12	Abdi	2	Modificado/a cabin.
273	2014-07-26 09:17:54.361318-06	8	14	11	Yoel	2	Modificado/a cabin.
274	2014-07-26 09:17:54.365375-06	8	14	10	Bitia	2	Modificado/a cabin.
275	2014-07-26 09:17:54.369502-06	8	14	6	Jesed	2	Modificado/a cabin.
276	2014-07-26 09:19:49.735626-06	8	14	43	Asael	2	Modificado/a cabin.
277	2014-07-26 09:19:49.740626-06	8	14	40	Elí	2	Modificado/a cabin.
278	2014-07-26 09:19:49.745165-06	8	14	34	Manos	2	Modificado/a cabin.
279	2014-07-26 09:19:49.749645-06	8	14	33	Adriel	2	Modificado/a cabin.
280	2014-07-26 09:19:49.754497-06	8	14	38	Uriel	2	Modificado/a cabin.
281	2014-07-26 09:22:13.7986-06	8	14	19	Zabdi	2	Modificado/a cabin.
282	2014-07-26 09:22:13.804826-06	8	14	15	Abdiel	2	Modificado/a cabin.
283	2014-07-26 09:22:13.80873-06	8	14	14	Ester	2	Modificado/a cabin.
284	2014-07-26 09:22:13.815552-06	8	14	3	Eliana	2	Modificado/a cabin.
285	2014-07-26 09:22:13.82024-06	8	14	18	Abigail	2	Modificado/a cabin.
286	2014-07-26 09:22:13.82404-06	8	14	13	Ithiel	2	Modificado/a cabin.
287	2014-07-26 09:22:13.827694-06	8	14	5	Migdal	2	Modificado/a cabin.
288	2014-07-26 09:22:13.832128-06	8	14	2	Abiatar	2	Modificado/a cabin.
289	2014-07-26 09:22:13.836494-06	8	14	1	Abiel	2	Modificado/a cabin.
290	2014-07-26 09:23:40.613624-06	8	14	42	Magdiel	2	Modificado/a cabin.
291	2014-07-26 09:23:40.618632-06	8	14	41	Dodava	2	Modificado/a cabin.
292	2014-07-26 09:23:40.623357-06	8	14	32	Karmi	2	Modificado/a cabin.
293	2014-07-26 09:23:40.627789-06	8	14	31	Zuria	2	Modificado/a cabin.
294	2014-07-26 09:26:33.018399-06	8	14	30	Keilah	2	Modificado/a cabin.
295	2014-07-26 09:26:33.022845-06	8	14	29	Mati	2	Modificado/a cabin.
296	2014-07-26 09:26:33.027709-06	8	14	28	Kyrios	2	Modificado/a cabin.
297	2014-07-26 09:26:33.032107-06	8	14	27	Kadisha	2	Modificado/a cabin.
298	2014-07-26 09:26:33.03647-06	8	14	26	Febe	2	Modificado/a cabin.
299	2014-07-26 09:26:33.040914-06	8	14	20	Jezreel	2	Modificado/a cabin.
300	2014-07-26 09:26:58.458023-06	8	14	4	Samuel	2	Modificado/a cabin.
301	2014-07-26 09:34:33.24255-06	8	14	2	Abiatar	2	Modificado/a cabin.
302	2014-07-26 09:34:33.247773-06	8	14	1	Abiel	2	Modificado/a cabin.
303	2014-07-26 09:34:33.252312-06	8	14	11	Yoel	2	Modificado/a cabin.
304	2014-07-26 09:34:33.257435-06	8	14	4	Samuel	2	Modificado/a cabin.
305	2014-07-26 09:35:50.057777-06	8	14	29	Mati	2	Modificado/a cabin.
306	2014-07-26 09:35:50.063188-06	8	14	28	Kyrios	2	Modificado/a cabin.
307	2014-07-26 09:35:50.067217-06	8	14	38	Uriel	2	Modificado/a cabin.
308	2014-07-26 09:36:23.107546-06	8	14	15	Abdiel	2	Modificado/a cabin.
309	2014-07-26 09:37:09.94597-06	8	14	10	Bitia	2	Modificado/a cabin.
310	2014-07-26 09:37:47.58769-06	8	14	30	Keilah	2	Modificado/a cabin.
311	2014-07-26 09:37:47.594839-06	8	14	27	Kadisha	2	Modificado/a cabin.
312	2014-07-26 09:37:47.601243-06	8	14	26	Febe	2	Modificado/a cabin.
313	2014-07-26 09:37:47.60807-06	8	14	20	Jezreel	2	Modificado/a cabin.
314	2014-07-26 09:39:37.562554-06	8	14	14	Ester	2	Modificado/a cabin.
315	2014-07-26 09:40:20.87985-06	8	14	19	Zabdi	2	Modificado/a cabin.
316	2014-07-26 09:41:33.9096-06	8	14	3	Eliana	2	Modificado/a cabin.
317	2014-07-26 09:43:58.465467-06	8	14	12	Abdi	2	Modificado/a cabin.
318	2014-07-26 09:43:58.47179-06	8	14	6	Jesed	2	Modificado/a cabin.
319	2014-07-26 09:47:09.037223-06	8	14	30	Keilah	2	Modificado/a bus.
320	2014-07-26 09:47:09.041818-06	8	14	29	Mati	2	Modificado/a bus.
321	2014-07-26 09:47:09.046365-06	8	14	28	Kyrios	2	Modificado/a bus.
322	2014-07-26 09:47:09.050745-06	8	14	27	Kadisha	2	Modificado/a bus.
323	2014-07-26 09:47:09.057233-06	8	14	26	Febe	2	Modificado/a bus.
324	2014-07-26 09:47:09.063757-06	8	14	20	Jezreel	2	Modificado/a bus.
325	2014-07-26 09:49:04.549929-06	8	14	19	Zabdi	2	Modificado/a bus.
326	2014-07-26 09:49:04.555305-06	8	14	15	Abdiel	2	Modificado/a bus.
327	2014-07-26 09:49:04.560026-06	8	14	3	Eliana	2	Modificado/a bus.
328	2014-07-26 09:49:04.564813-06	8	14	18	Abigail	2	Modificado/a bus.
329	2014-07-26 09:49:04.568768-06	8	14	16	Elyon	2	Modificado/a bus.
330	2014-07-26 09:49:04.57291-06	8	14	13	Ithiel	2	Modificado/a bus.
331	2014-07-26 09:49:04.576889-06	8	14	5	Migdal	2	Modificado/a bus.
332	2014-07-26 09:49:04.581692-06	8	14	2	Abiatar	2	Modificado/a bus.
333	2014-07-26 09:49:25.042128-06	8	14	38	Uriel	2	Modificado/a bus.
334	2014-07-26 09:50:01.51387-06	8	14	12	Abdi	2	Modificado/a bus.
335	2014-07-26 09:50:01.518968-06	8	14	11	Yoel	2	Modificado/a bus.
336	2014-07-26 09:50:01.52303-06	8	14	10	Bitia	2	Modificado/a bus.
337	2014-07-26 09:50:01.527722-06	8	14	6	Jesed	2	Modificado/a bus.
338	2014-07-26 16:35:11.190977-06	10	11	116	Josué Israel Guevara Aguilar	2	Añadido/a "152 - $20" abono.
339	2014-07-26 16:35:25.882935-06	10	11	116	Josué Israel Guevara Aguilar	2	Añadido/a "152b - $20" abono.
340	2014-07-26 16:39:49.483525-06	10	11	98	Alessandra Jeanneth Vega Hernández	2	Añadido/a "153 - $75" abono.
341	2014-07-26 16:40:50.294063-06	10	11	186	Ronald Navas López	1	
342	2014-07-26 16:41:38.574905-06	10	12	15	Jacqueline Beatriz Aquino Fuentes	2	Añadido/a "155 - $75" abono.
343	2014-07-26 16:44:15.576343-06	10	11	115	Nicole Azucena Barahona Castro	2	Añadido/a "63 - $10" abono.
344	2014-07-26 16:44:45.053036-06	10	11	99	Cristian Alexander Ayala Serrano	2	Añadido/a "62 - $70" abono.
345	2014-07-26 16:52:28.604881-06	10	11	187	José Carlos Sequeira Alvarado	1	
346	2014-07-26 16:55:12.032331-06	10	11	2	Adriana Saraí Vasquez   Rodríguez	2	Añadido/a "60 - $9.10" abono.
347	2014-07-26 16:55:47.193709-06	10	11	15	Marco Stefano Barrientos Melgar	2	Añadido/a "59 - $55" abono.
348	2014-07-26 16:56:18.085328-06	10	11	119	Irina Lucia Orantes Regalado	2	Añadido/a "58 - $50" abono.
349	2014-07-26 16:57:54.965844-06	10	12	35	Elia Fernanda Carranza Ríos	2	Añadido/a "57 - $5" abono.
350	2014-07-26 17:00:08.996638-06	10	11	142	Sara Ester Martínez Francia	2	Añadido/a "056 - $15" abono.
351	2014-07-26 17:02:56.219482-06	10	12	1	José Eduardo Rivas Melgar	2	Modificados amount para "107b - $70.00" abono.
352	2014-07-26 17:04:42.632979-06	10	11	188	Bryan Dennis Castillo Flores	1	
353	2014-07-26 17:05:03.998732-06	10	11	80	Evelyn Janet Trinidad García	2	Añadido/a "55 - $5" abono.
354	2014-07-26 17:06:17.294462-06	10	11	189	David Alejandro Torres Andino	1	
355	2014-07-26 17:06:40.004674-06	10	11	100	Margareth Rachelle Escamilla Zuniga	2	Añadido/a "53 - $5" abono.
356	2014-07-26 17:07:05.684797-06	10	11	1	Jacqueline Pamela Rodríguez Pineda	2	Modificado/a badge_name. Añadido/a "52 - $5" abono.
357	2014-07-26 17:07:28.122557-06	10	12	36	Gerardo Josué Osorio Portillo	2	Añadido/a "51 - $5" abono.
358	2014-07-26 18:41:20.343337-06	10	11	190	Allison Michel Santos	1	
359	2014-07-27 08:43:42.125682-06	10	11	175	Maria Beatriz Zuniga Ramirez	2	Eliminado/a "119 - $5" abono.
360	2014-07-27 08:44:26.339791-06	10	11	167	María Beatriz Zuniga Ramirez	2	Eliminado/a "119b - $5" abono.
361	2014-07-27 08:47:36.019738-06	10	11	167	María Beatriz Zuniga Ramirez	2	Añadido/a "151b - $40" abono.
362	2014-07-27 11:52:20.511521-06	10	11	125	Emilio Armando Aguilar Obando	2	No ha cambiado ningún campo.
363	2014-07-27 11:58:35.157459-06	1	11	63	Roberto Benjamín Coello Gómez	2	Añadido/a "200 - $65" abono.
364	2014-07-27 11:59:10.395552-06	10	11	114	David Gonzalo Castillo Dimas	2	Añadido/a "149.1 - $70" abono.
365	2014-07-27 11:59:21.004158-06	1	11	18	Adriana Coello Gómez	2	Añadido/a "201 - $65" abono.
366	2014-07-27 11:59:55.837228-06	1	11	114	David Gonzalo Castillo Dimas	2	Añadido/a "202 - $5" abono.
367	2014-07-27 12:00:03.471162-06	10	11	81	Carlos  Raúl Dominguez Hernández	2	Añadido/a "150.1 - $25" abono.
368	2014-07-27 12:01:30.428346-06	10	11	175	Maria Beatriz Zuniga Ramirez	3	
369	2014-07-27 12:02:25.30455-06	1	11	189	David Alejandro Torres Andino	2	Añadido/a "203 - $78" abono.
370	2014-07-27 12:02:40.965996-06	10	11	167	María Beatriz Zuniga Ramirez	2	Añadido/a "119 - $5" abono.
371	2014-07-27 12:03:31.007828-06	10	11	168	Tania Gisselle Cárcamo Hernández	2	Añadido/a "108.1 - $40" abono.
372	2014-07-27 12:04:07.451354-06	10	11	169	Karla Veronica Bonilla Peña	2	Añadido/a "109.1 - $40" abono.
373	2014-07-27 12:04:40.418917-06	1	11	191	Josué David Mejía	1	
374	2014-07-27 12:04:44.359587-06	10	11	124	Reina Dolores Barrera Mijango	3	
375	2014-07-27 12:05:06.033704-06	10	11	170	Reina Dolores Barrera Mijano	2	Modificado/a second_surname. Añadido/a "110.1 - $40" abono.
376	2014-07-27 12:05:43.712884-06	10	12	17	Miguel Antonio Guardado Salmerón	2	Añadido/a "111.1 - $75" abono.
377	2014-07-27 12:06:14.36577-06	1	11	192	Natalia Daniela González	1	
378	2014-07-27 12:06:46.72239-06	1	11	147	Rebeca Aracely Alvarado Granados	2	Añadido/a "207 - $18" abono.
379	2014-07-27 12:07:08.816621-06	10	11	193	Bryan Josué Andrade Delgado	1	
380	2014-07-27 12:07:12.419222-06	1	11	22	Marcela Alejandra Mendoza Orellana	2	Añadido/a "208 - $30" abono.
381	2014-07-27 12:07:43.891544-06	10	11	105	Josué David Lainez Castro	2	Añadido/a "113.1 - $10" abono.
382	2014-07-27 12:08:00.320077-06	1	11	116	Josué Israel Guevara Aguilar	2	Añadido/a "209 - $50" abono.
383	2014-07-27 12:08:30.987639-06	10	12	19	Pamela Alejandra Chacón Rodríguez	2	Añadido/a "114.1 - $50" abono.
384	2014-07-27 12:08:50.288713-06	1	11	192	Natalia Daniela González	3	
385	2014-07-27 12:09:16.392239-06	10	11	57	Sara Eunice Arteaga Funes	2	Añadido/a "115.1 - $25" abono.
386	2014-07-27 12:09:22.40854-06	1	11	43	Natalia Daniela González Tobar	2	Añadido/a "205.1 - $65" abono.
387	2014-07-27 12:09:46.931515-06	1	11	128	Carlos  Samuel Flores Olivares	2	Añadido/a "210 - $73" abono.
388	2014-07-27 12:10:00.696623-06	10	11	182	Raquel Alejandra Pérez Martínez	2	Añadido/a "116.1 - $38" abono.
389	2014-07-27 12:10:04.091274-06	1	11	128	Carlos  Samuel Flores Olivares	2	Modificado/a badge_name.
390	2014-07-27 12:10:30.48206-06	1	11	154	Emilton Daniel Alvarenga Flores	2	Añadido/a "211 - $35" abono.
391	2014-07-27 12:11:05.139399-06	1	11	64	Luis Hernán Orellana Reyes	2	Añadido/a "212 - $75" abono.
392	2014-07-27 12:12:27.940934-06	1	11	194	Alejandro Orellana	1	
393	2014-07-27 12:12:58.777174-06	1	11	177	Debora Elizabeth Romero Martínez	2	Añadido/a "214 - $60" abono.
394	2014-07-27 12:12:59.652334-06	10	11	195	Frances Melana García Díaz	1	
395	2014-07-27 12:14:14.309153-06	1	11	196	Margorie Prieto Castro	1	
396	2014-07-27 12:15:53.699042-06	1	11	187	José Carlos Sequeira Alvarado	2	Añadido/a "216 - $39" abono.
397	2014-07-27 12:16:29.426361-06	1	12	35	Elia Fernanda Carranza Ríos	2	Añadido/a "217 - $70" abono.
398	2014-07-27 12:16:59.686405-06	1	11	151	Juan  Carlos Morales Sosa	2	Añadido/a "218 - $70" abono.
399	2014-07-27 12:17:20.220712-06	10	11	100	Margareth Rachelle Escamilla Zuniga	2	Añadido/a "159 - $73" abono.
400	2014-07-27 12:17:46.976754-06	1	12	27	Karen Noemi López Dimas	2	Añadido/a "219 - $70" abono.
401	2014-07-27 12:18:47.54755-06	1	11	40	Andrés Gerardo López Guevara	2	Añadido/a "220 - $73" abono.
402	2014-07-27 12:18:48.628013-06	10	11	25	Dalia Marcela Huezo Pacheco	2	Añadido/a "160 - $70" abono.
403	2014-07-27 12:19:17.929793-06	1	11	58	Nicole Jasmin Mata Salinas	2	Añadido/a "221 - $58" abono.
404	2014-07-27 12:19:43.720229-06	10	11	7	Angélica Yamileth López Pérez	2	Añadido/a "161 - $75" abono.
405	2014-07-27 12:20:02.273254-06	1	12	22	Ruth Abigail Méndez Alfaro	2	Añadido/a "222 - $70" abono.
406	2014-07-27 12:20:16.345535-06	10	11	94	Cinthya Gissellie Pineda  Bonilla	2	Añadido/a "162 - $73" abono.
407	2014-07-27 12:20:34.901289-06	1	11	19	Francisco Ariel Linares Melgar	2	Añadido/a "223 - $70" abono.
408	2014-07-27 12:20:50.622023-06	10	11	164	María Fernanda Balibrerra Barahona	2	Añadido/a "163 - $28" abono.
409	2014-07-27 12:21:08.241821-06	1	13	11	Grisel Abigail González de Santillana	2	Añadido/a "224 - $37.5" abono.
410	2014-07-27 12:21:16.615458-06	10	11	92	Gloria María Campos Fernández	2	Añadido/a "164 - $60" abono.
411	2014-07-27 12:21:32.972464-06	10	11	91	Rene Rafael Campos Fernández	2	Añadido/a "165 - $60" abono.
412	2014-07-27 12:22:14.336254-06	10	12	21	Clarissa Esmeralda Rodriguez Monge	2	Añadido/a "166 - $25" abono.
413	2014-07-27 12:23:05.067515-06	10	11	56	Julieta Elizabeth Ponce Martir	2	Añadido/a "167 - $70" abono.
414	2014-07-27 12:25:04.703171-06	10	11	197	Ana Marcela Chavarría Hernández	1	
415	2014-07-27 12:26:01.577172-06	10	11	197	Ana Marcela Chavarría Hernández	2	No ha cambiado ningún campo.
416	2014-07-27 12:28:38.322008-06	10	11	198	Patricia Elizabeth Chavarría Hernández	1	
417	2014-07-27 12:30:38.851962-06	10	11	83	Miguel Alejandro Soriano Beltrán	2	Añadido/a "170 - $70" abono.
418	2014-07-27 12:34:00.060118-06	1	9	603	205 - $65.00	2	Modificado/a receipt_id.
419	2014-07-27 12:36:40.133684-06	10	11	39	Marlon Edgardo Figueroa Martínez	2	Añadido/a "172 - $50" abono.
420	2014-07-27 12:37:16.226877-06	10	11	39	Marlon Edgardo Figueroa Martínez	2	No ha cambiado ningún campo.
421	2014-07-27 12:38:07.551699-06	10	11	184	Pablo Ricardo Rodriguez Paz	2	Añadido/a "173 - $70" abono.
422	2014-07-27 12:38:17.852943-06	1	15	49	140 - $40.00 (Egreso)	1	
423	2014-07-27 12:38:44.022585-06	10	11	36	Gabriela María Melara Rodríguez	2	Añadido/a "174 - $55" abono.
424	2014-07-27 12:39:20.30668-06	1	15	50	146 - $10.00 (Egreso)	1	
425	2014-07-27 12:39:26.098215-06	10	12	34	Marcela Roxana Melara Rodríguez	2	Añadido/a "174.1 - $55" abono.
426	2014-07-27 12:39:43.237636-06	1	15	50	146 - $10.00 (Egreso)	2	Modificado/a destination.
427	2014-07-27 12:40:01.506244-06	10	11	71	Jonathan Eduardo Hernández Díaz	2	Añadido/a "175 - $70" abono.
428	2014-07-27 12:41:00.21027-06	10	11	199	Victor Josué Yanez López	1	
429	2014-07-27 12:41:23.400761-06	10	11	178	Nicole Astrid Rivas Cruz	2	Añadido/a "177 - $70" abono.
430	2014-07-27 12:41:41.532321-06	10	11	148	Andrea Roxana Ponce Martir	2	Añadido/a "178 - $20" abono.
431	2014-07-27 12:42:08.875157-06	10	11	16	María José Rivera Recinos	2	Añadido/a "179 - $75" abono.
432	2014-07-27 12:42:31.028969-06	10	11	129	Aldo Andrés Palacios Escamilla	2	Añadido/a "180 - $75" abono.
433	2014-07-27 12:43:03.892004-06	10	11	54	David Godofredo Campos  Aguilar	2	Añadido/a "181 - $65" abono.
434	2014-07-27 12:43:25.143643-06	10	11	1	Jacqueline Pamela Rodríguez Pineda	2	Añadido/a "182 - $75" abono.
435	2014-07-27 12:43:43.015194-06	10	11	1	Jacqueline Pamela Rodríguez Pineda	2	Modificados amount para "182 - $70" abono.
436	2014-07-27 12:44:25.730315-06	10	15	51	183 - $70.00 (Egreso)	1	
437	2014-07-27 12:45:18.581655-06	10	15	52	186 - $50.00 (Egreso)	1	
438	2014-07-27 12:45:59.990252-06	10	11	148	Andrea Roxana Ponce Martir	2	Añadido/a "184 - $50" abono.
439	2014-07-27 12:46:52.355544-06	10	11	185	Abel Ernesto Magaña Rivera	2	Añadido/a "185 - $73" abono.
440	2014-07-27 12:48:07.329791-06	10	11	200	Karla Gabriela Aguilar Pérez	1	
441	2014-07-27 12:48:32.10965-06	10	11	65	Mauricio Javier Castellón Cerritos	2	Añadido/a "188 - $35" abono.
442	2014-07-27 12:48:40.560657-06	1	12	28	Sara Carolina Moreno Sandoval	2	Añadido/a "225 - $70" abono.
443	2014-07-27 12:49:22.299879-06	10	11	96	Ana Margarita Santamaría Hernández	2	Añadido/a "189 - $70" abono.
444	2014-07-27 12:49:53.74047-06	10	11	183	Rafaela Nicole Guardado Zelaya	2	Añadido/a "190 - $70" abono.
445	2014-07-27 13:02:02.245504-06	10	11	2	Adriana Saraí Vasquez   Rodríguez	2	Añadido/a "073 - $27.1" abono.
446	2014-07-27 13:03:00.542223-06	10	12	16	Milton Josué Méndez Alfaro	2	Añadido/a "191 - $70" abono.
447	2014-07-27 13:03:34.545229-06	10	12	4	María Alejandra Durán Castellanos	2	Añadido/a "193 - $25" abono.
448	2014-07-27 13:04:11.061153-06	10	11	8	Diana Saraí Santos Martir	2	Añadido/a "192 - $30" abono.
449	2014-07-27 13:05:02.993784-06	10	11	165	Gloria Raquel Gutiérrez Quinteros	2	Añadido/a "194 - $63" abono.
450	2014-07-27 13:05:49.947922-06	10	12	26	Imelda Margarita Aguilar Palma	2	Añadido/a "66 - $75" abono.
451	2014-07-27 13:06:24.458408-06	10	11	139	Roger Ellebien Torres Díaz	2	Añadido/a "67 - $55" abono.
452	2014-07-27 13:08:58.808402-06	10	11	201	Oscar Daniel Renderos	1	
453	2014-07-27 13:10:12.293432-06	10	11	202	Boris Emilio Quixada	1	
454	2014-07-27 13:10:59.498926-06	10	11	172	Cindy Nayeli Bonilla Beltran	2	Añadido/a "70 - $70" abono.
455	2014-07-27 13:11:39.935486-06	10	11	138	Karen Paola Morales Bonilla	2	Añadido/a "71 - $75" abono.
456	2014-07-27 13:12:02.964966-06	10	11	119	Irina Lucia Orantes Regalado	2	Añadido/a "74 - $23" abono.
457	2014-07-27 13:12:36.024777-06	10	11	41	Ludwing Alfredo Contreras Menjívar	2	Añadido/a "75 - $50" abono.
458	2014-07-27 13:13:21.232206-06	10	11	42	Katherine Haydee Contreras Menjívar	2	Añadido/a "76 - $50" abono.
459	2014-07-27 13:14:30.20806-06	10	11	159	Denise Elizabeth Hernández Pineda	2	Añadido/a "77 - $28" abono.
460	2014-07-27 13:15:21.495603-06	10	11	190	Allison Michel Santos	2	Añadido/a "78 - $20" abono.
461	2014-07-27 13:16:27.249185-06	10	11	122	Edi Lineth Caseros Cubias	2	Añadido/a "79 - $75" abono.
462	2014-07-27 13:17:17.99604-06	10	11	79	Alexia Rosibel Ochoa González	2	Añadido/a "80 - $68" abono.
463	2014-07-27 13:22:53.399143-06	10	11	116	Josué Israel Guevara Aguilar	2	Añadido/a "226 - $5" abono. Eliminado/a "152b - $20.00" abono.
464	2014-07-27 13:23:33.622601-06	10	11	45	Doris Esmeralda Alfaro  Castillo	2	Añadido/a "227 - $40" abono.
465	2014-07-27 13:23:56.405281-06	10	11	190	Allison Michel Santos	2	Añadido/a "228 - $20" abono.
466	2014-07-27 13:24:25.119601-06	10	11	8	Diana Saraí Santos Martir	2	Añadido/a "229 - $15" abono.
467	2014-07-27 13:26:18.980933-06	10	12	2	José David Nery Maravilla	2	Añadido/a "156 - $50" abono.
468	2014-07-27 13:26:52.154621-06	10	11	108	Melany Sofia Bonilla Beltrán	2	Añadido/a "157 - $70" abono.
469	2014-07-27 13:28:23.066927-06	10	11	203	Gabriel Alejandro Gómez Elías	1	
470	2014-07-27 13:40:31.783229-06	10	12	5	Ricardo Josué Medrano Guerrero	2	Añadido/a "195 - $70" abono.
471	2014-07-27 16:49:43.435832-06	10	11	81	Carlos  Raúl Dominguez Hernández	2	Añadido/a "230 - $4" abono.
472	2014-07-27 16:50:17.172068-06	10	11	35	Javier Alfonso Martínez Portillo	2	Añadido/a "231 - $78" abono.
473	2014-07-27 16:51:03.362621-06	10	15	53	232 - $60.00 (Egreso)	1	
474	2014-07-27 16:51:28.918051-06	10	15	54	233 - $3.00 (Egreso)	1	
475	2014-07-27 16:52:16.672977-06	10	15	53	232 - $60.00 (Egreso)	2	Modificado/a destination.
476	2014-07-27 16:52:53.584096-06	10	15	55	234 - $30.00 (Egreso)	1	
477	2014-07-27 16:53:37.55946-06	10	12	7	Andrea Saraí Navarrete Pérez	2	Añadido/a "235 - $10" abono.
478	2014-07-27 17:15:39.346611-06	10	12	36	Gerardo Josué Osorio Portillo	2	Modificados amount para "51 - $55" abono.
479	2014-07-27 17:17:01.563106-06	10	12	36	Gerardo Josué Osorio Portillo	2	Modificados receipt_id para "051 - $55.00" abono.
480	2014-07-27 17:22:49.937967-06	10	11	137	Mónica  María Morales Bonilla	2	Añadido/a "72 - $75" abono.
481	2014-07-27 17:47:37.02548-06	10	12	11	Laura Patricia Santillana Meléndez	2	Añadido/a "128.1 - $75" abono.
482	2014-07-27 17:49:35.481938-06	1	11	59	David Josué Mejía	3	
483	2014-07-27 17:54:00.341414-06	10	11	110	Rodrigo Alberto Martinez Renderos	2	Añadido/a "171 - $73" abono.
484	2014-07-28 06:49:32.638625-06	10	11	179	Iker Gabriel Pérez Andrade	2	Modificado/a counselor.
485	2014-07-28 06:49:38.113326-06	10	11	179	Iker Gabriel Pérez Andrade	2	No ha cambiado ningún campo.
486	2014-07-28 23:17:57.885134-06	10	15	46	002 - $10.00 (Ingreso)	3	
487	2014-07-28 23:17:57.890395-06	10	15	45	001 - $310.00 (Ingreso)	3	
488	2014-07-28 23:17:57.891017-06	10	15	44	 - $1007.00 (Ingreso)	3	
489	2014-07-29 00:47:50.907433-06	10	15	56	1b - $5449.75 (Ingreso)	1	
490	2014-07-29 00:48:15.163299-06	10	15	57	2b - $5449.75 (Ingreso)	1	
491	2014-07-29 00:49:31.79984-06	10	15	56	1b - $5449.75 (Ingreso)	3	
492	2014-07-29 00:49:31.805769-06	10	15	57	2b - $5449.75 (Ingreso)	3	
493	2014-07-29 01:31:32.364669-06	10	15	58	1b - $169.05 (Ingreso)	1	
494	2014-07-29 01:32:04.74614-06	10	15	59	2b - $20.30 (Ingreso)	1	
495	2014-07-30 14:43:55.76886-06	1	11	203	Gabriel Alejandro Gómez Elías	3	
496	2014-07-30 14:44:38.728369-06	1	11	144	David Alejandro Gómez Elias	2	Añadido/a "158 - $35" abono.
497	2014-07-30 14:57:42.534781-06	1	11	146	Ana Elizabeth Montoya Ardón	2	Modificado/a counselor.
498	2014-08-02 00:55:23.613547-06	8	14	4	Samuel	2	Modificado/a bus.
499	2014-08-16 18:15:58.078955-06	10	11	204	Yanira Rodriguez	1	
500	2014-08-16 18:16:46.040411-06	10	11	55	Jorge Antonio Campos Miranda	2	Añadido/a "241 - $68" abono.
501	2014-08-16 18:17:11.446243-06	10	12	19	Pamela Alejandra Chacón Rodríguez	2	Añadido/a "242 - $15" abono.
502	2014-08-16 18:18:38.577253-06	10	11	39	Marlon Edgardo Figueroa Martínez	2	Añadido/a "243 - $13" abono.
503	2014-08-16 18:19:40.74429-06	10	12	31	Geovanny Ernesto Lainez Castro	2	Añadido/a "244 - $55" abono.
504	2014-08-16 18:20:43.973892-06	10	11	187	José Carlos Sequeira Alvarado	2	Añadido/a "245 - $30" abono.
505	2014-08-16 18:21:47.867459-06	10	11	142	Sara Ester Martínez Francia	2	Añadido/a "246 - $15" abono.
506	2014-08-16 18:22:25.569154-06	10	11	102	William Rodrigo Huezo Orantes	2	Añadido/a "247 - $70" abono.
507	2014-08-16 18:23:09.932495-06	10	12	14	Griselda Beatriz Martínez Cornejo	2	Añadido/a "248 - $75" abono.
508	2014-08-16 18:23:37.278714-06	10	12	6	Gloria Raquel González Galdamez	2	Añadido/a "249 - $75" abono.
509	2014-08-16 18:24:27.105589-06	10	11	163	Daniel Alberto Alcoleas Jaime	2	Añadido/a "250 - $55" abono.
510	2014-08-16 18:24:47.489718-06	10	11	77	Raúl  David Yanes Peña	2	Añadido/a "251 - $65" abono.
511	2014-08-16 18:25:03.498812-06	10	11	73	Carmen Elena Yanes Peña	2	Añadido/a "252 - $65" abono.
512	2014-08-16 18:25:32.975747-06	10	11	82	Alejandra Poulette Montalvo Meza	2	Añadido/a "253 - $50" abono.
513	2014-08-16 18:25:55.398328-06	10	11	115	Nicole Azucena Barahona Castro	2	Añadido/a "254 - $65" abono.
514	2014-08-16 18:26:13.337055-06	10	11	190	Allison Michel Santos	2	Añadido/a "255 - $20" abono.
515	2014-08-16 18:27:15.310892-06	10	11	205	Amanda Gisselle Franco	1	
516	2014-08-16 18:27:33.267061-06	10	11	66	Emely Nohemi Sevillano Platero	2	Añadido/a "257 - $50" abono.
517	2014-08-16 18:27:51.338402-06	10	11	87	Alejandra Maria Claros Burgos	2	Añadido/a "258 - $70" abono.
518	2014-08-16 18:28:14.128212-06	10	12	29	René Moisés Sevillano Platero	2	Añadido/a "259 - $60" abono.
519	2014-08-16 18:28:51.669166-06	10	12	23	Priscila Saraí Sevillano Platero	2	Añadido/a "260 - $43" abono.
520	2014-08-16 18:29:24.941798-06	10	12	33	Tarquino Aldair Hernández Cañenguez	2	Añadido/a "261 - $70" abono.
521	2014-08-16 18:29:59.429007-06	10	13	10	Javier Ernesto Santillana Meléndez	2	Añadido/a "262 - $37.50" abono.
522	2014-08-16 18:30:53.833191-06	10	11	27	Christian Alessandro Calderón Castillo	2	Añadido/a "269 - $35" abono.
523	2014-08-16 18:31:21.208786-06	10	11	86	Carlos Ernesto Medrano Guerrero	2	Añadido/a "270 - $5" abono.
524	2014-08-16 18:35:43.831214-06	10	11	206	Norma Berenice Sigarun Ortiz	1	
525	2014-08-16 18:36:22.6028-06	10	11	162	José Eduardo Pacheco Guerrero	2	Añadido/a "237 - $73" abono.
526	2014-08-16 18:36:37.970694-06	10	11	160	Diana Marcela Pacheco Guerrero	2	Añadido/a "237.1 - $73" abono.
527	2014-08-16 18:38:37.922295-06	10	11	161	Mauricio Alejandro Pacheco Guerrero	2	Añadido/a "237.2 - $73" abono.
528	2014-08-16 18:39:05.479246-06	10	11	91	Rene Rafael Campos Fernández	2	Añadido/a "238 - $20" abono.
529	2014-08-16 18:39:29.715232-06	10	11	91	Rene Rafael Campos Fernández	2	Añadido/a "238.1 - $10" abono.
530	2014-08-16 18:40:25.047693-06	10	11	92	Gloria María Campos Fernández	2	Añadido/a "238.2 - $20" abono.
531	2014-08-16 18:41:05.319637-06	10	11	92	Gloria María Campos Fernández	2	Añadido/a "238b - $10" abono.
532	2014-08-16 18:41:36.790268-06	10	11	91	Rene Rafael Campos Fernández	3	
533	2014-08-16 18:42:17.221101-06	10	11	92	Gloria María Campos Fernández	3	
534	2014-08-16 18:43:38.937982-06	10	11	207	Gloria  Maria Campos Fernández	1	
535	2014-08-16 18:44:41.700045-06	10	11	208	Rene Campos Fernández	1	
536	2014-08-16 18:45:15.437705-06	10	11	22	Marcela Alejandra Mendoza Orellana	2	Añadido/a "239 - $10" abono.
537	2014-08-16 20:06:06.339133-06	10	11	195	Frances Melana García Díaz	2	Añadido/a "271 - $170" abono.
538	2014-08-16 20:06:57.9776-06	10	11	80	Evelyn Janet Trinidad García	2	Añadido/a "272 - $70" abono.
539	2014-08-16 20:12:07.064199-06	10	11	142	Sara Ester Martínez Francia	2	Añadido/a "273 - $20" abono.
540	2014-08-16 20:12:41.732305-06	10	12	7	Andrea Saraí Navarrete Pérez	2	Añadido/a "274 - $65" abono.
541	2014-08-16 20:12:59.137754-06	10	12	7	Andrea Saraí Navarrete Pérez	2	Añadido/a "275 - $65" abono.
542	2014-08-16 20:39:08.958468-06	10	11	195	Frances Melana García Díaz	2	Modificados amount para "271 - $70.00" abono.
543	2014-08-17 00:16:27.10109-06	10	11	188	Bryan Dennis Castillo Flores	2	Eliminado/a "65 - $5.00" abono.
544	2014-08-17 00:16:59.878984-06	10	12	1	José Eduardo Rivas Melgar	2	Modificados amount para "107b - $75.00" abono.
545	2014-08-17 00:28:40.432689-06	10	12	7	Andrea Saraí Navarrete Pérez	2	Eliminado/a "275 - $65.00" abono.
546	2014-08-17 00:32:46.132169-06	10	13	12	Julia de Paz	1	
547	2014-09-04 08:18:15.326112-06	10	12	20	Maricela Nohemy Flores de León	2	Añadido/a "300 - $20" abono.
548	2014-09-04 08:18:38.347678-06	10	12	25	Erik Emmanuel Miranda Hernández	2	Añadido/a "301 - $75" abono.
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 548, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	content type	contenttypes	contenttype
5	session	sessions	session
6	site	sites	site
7	log entry	admin	logentry
8	migration history	south	migrationhistory
9	Payment	signup	payment
10	Parent	signup	parent
11	Camper	signup	camper
12	Counselor	signup	counselor
13	Guest	signup	guest
14	Small Group	logistics	smallgroup
15	Transaction	finances	transaction
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('django_content_type_id_seq', 15, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
jaj5qhvkg0qxj6p7f5cfq89a5ak31evf	NDcwNDYwYzEwNDM1MDNjNzBmZGQ4ZTc2MWMwNWZiMjgzMmVjYzYzMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-12 14:32:06.452948-06
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Data for Name: finances_transaction; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY finances_transaction (id, transaction_id, transaction_type, transaction_date, amount, origin, destination) FROM stdin;
47	092b	egress	2014-07-05	30.00	Inscripciones	Recreativa
48	115	egress	2014-07-13	255.00	Inscripciones	Carpeta y gafete
49	140	egress	2014-07-20	40.00	Inscripción	Decoracion Cena especial
50	146	egress	2014-07-27	10.00	Inscripción	Decoración
51	183	egress	2014-07-27	70.00	Inscripciones	Logística
52	186	egress	2014-07-27	50.00	Inscripciones	Migración
54	233	egress	2014-07-27	3.00	Inscripciones	Devolución Abel Magaña
53	232	egress	2014-07-27	60.00	Inscripciones	Decoración Oliver
55	234	egress	2014-07-27	30.00	Inscripciones	Nocturna
58	1b	income	2014-07-29	169.05	CINE	Pago Montesión, comisiones y buses
59	2b	income	2014-07-29	20.30	Ofrendas preju	Pago Montesión, comisiones y buses
\.


--
-- Name: finances_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('finances_transaction_id_seq', 59, true);


--
-- Data for Name: logistics_smallgroup; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY logistics_smallgroup (id, title, generation, cabin, bus, structure) FROM stdin;
1	Abiel	5	belen	2	preju
14	Ester	4	koinonia4	2	preju
30	Keilah	3	agape3	2	preju
29	Mati	3	nueva1	2	preju
28	Kyrios	3	nueva1	2	preju
27	Kadisha	3	agape3	2	preju
26	Febe	3	agape3	2	preju
20	Jezreel	3	agape3	2	preju
19	Zabdi	4	koinonia4	3	preju
15	Abdiel	4	nueva2	3	preju
3	Eliana	4	koinonia1	2	preju
18	Abigail	5	koinonia3	3	preju
16	Elyon	5	juda	3	preju
13	Ithiel	5	koinonia3	3	preju
43	Asael	1	horeb1	1	josias
40	Elí	1	horeb1	1	josias
34	Manos	2	horeb2	1	josias
33	Adriel	2	horeb2	1	josias
42	Magdiel	1	anakaino1	1	josias
41	Dodava	1	anakaino2	1	josias
32	Karmi	2	anakaino3	1	josias
31	Zuria	2	anakaino4	1	josias
5	Migdal	5	koinonia3	3	preju
2	Abiatar	5	belen	3	preju
38	Uriel	4	nueva2	3	preju
12	Abdi	6	agape2	4	preju
11	Yoel	6	gerizim	4	preju
10	Bitia	6	agape2	4	preju
6	Jesed	6	huespedes2	4	preju
4	Samuel	6	moab	4	preju
\.


--
-- Name: logistics_smallgroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('logistics_smallgroup_id_seq', 43, true);


--
-- Data for Name: signup_camper; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_camper (id, first_name, second_name, first_surname, second_surname, gender, birth_date, state, province, occupation, balance, no_pay, badge_name, cabin, passport, birth_cert_num, birth_cert_fol, birth_cert_book, registrar, mother_id, father_id, counselor_id, generation, structure, bus, small_group_id, registrar_title, registrar_position, reg_state, reg_province, permission_status, lawyer, signed_up) FROM stdin;
15	Marco	Stefano	Barrientos	Melgar	m	\N				75.00	f	Marco	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
70	Adriana	María 	Rodríguez	Monge	f	\N				75.00	f	Adri	koinonia3		\N	\N	\N		\N	\N	14	5	preju	3	13					0		t
56	Julieta	Elizabeth	Ponce	Martir	f	\N				75.00	f	Julieta	koinonia4		\N	\N	\N		\N	\N	20	4	preju	3	19					0		t
36	Gabriela	María	Melara	Rodríguez	f	\N				75.00	f	Gaby	huespedes2		\N	\N	\N		\N	\N	7	6	preju	4	6					0		t
45	Doris	Esmeralda	Alfaro 	Castillo	f	\N				78.00	f	Esmi	agape3		\N	\N	\N		\N	\N	23	3	preju	2	27					0		t
100	Margareth	Rachelle	Escamilla	Zuniga	f	\N				78.00	f	Rachelle	agape3		\N	\N	\N		\N	\N	22	3	preju	2	26					0		t
44	Yohalmo	Obdulio	Pérez	De León	m	\N				0.00	f	Yohalmo	belen		\N	\N	\N		\N	\N	2	5	preju	3	2					0		f
60	Alejandra	Guadalupe	Cruz	Vásquez	f	\N				0.00	f	Alejandra	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		f
68	Cristian	Alexis	Amaya	Cortéz	m	\N				0.00	f	Cristian	juda		\N	\N	\N		\N	\N	17	5	preju	3	16					0		f
46	Katherine	Rebeca	Medrano	Guerrero	f	\N				75.00	f	Rebe	agape3		\N	\N	\N		\N	\N	21	3	preju	2	20					0		t
1	Jacqueline	Pamela	Rodríguez	Pineda	f	2000-03-25 16:19:00-06	lal	Santa Tecla	Estudiante	75.00	f	Pamelonga	agape3	M00818435	246	248	3	MIGUEL ANGEL CRUZ LOPEZ	5	6	23	3	preju	2	27	m	subchief	sas	San Salvador	0	jorge	t
58	Nicole	Jasmin	Mata	Salinas	f	1997-09-23 07:40:00-06	lal	Antiguo Cuscatlán	Estudiante	78.00	f	Nicole	agape2	A50130681	84	86	62	Donaldo Francisco Salazar Ruballo	10	11	11	6	preju	4	10	m	subchief	sas	San Salvador	0	jorge	t
21	Roxana	Abigail	Comandari	Rodríguez	f	\N				75.00	f	Roxy	anakaino3		\N	\N	\N		\N	\N	28	2	josias	1	32					0		t
25	Dalia	Marcela	Huezo	Pacheco	f	\N				75.00	f	Dalia	agape2		\N	\N	\N		\N	\N	13	6	preju	4	12					0		t
61	Andrea	Fernanda	Matínez	González	f	\N				5.00	f	Andrea	agape3		\N	\N	\N		\N	\N	26	3	preju	2	30					0		t
55	Jorge	Antonio	Campos	Miranda	m	\N				78.00	f	Jorge	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
18	Adriana		Coello	Gómez	f	\N				75.00	f	Adri	koinonia4		\N	\N	\N		\N	\N	20	4	preju	3	19					0		t
108	Melany	Sofia	Bonilla	Beltrán	m	\N				78.00	f	Melany	agape3		\N	\N	\N		\N	\N	26	3	preju	2	30					0		t
12	Eugenia	Beatriz	Alvarado	Araujo	f	\N				75.00	f	Eu	anakaino3		\N	\N	\N		\N	\N	28	2	josias	1	32					0		t
125	Emilio	Armando	Aguilar	Obando	m	\N				78.00	f	Emilio	nueva2		\N	\N	\N		\N	\N	16	4	preju	3	15					0		t
136	Carlos		Salazar		m	\N				0.00	f	Carlos	nueva2		\N	\N	\N		\N	\N	16	4	preju	3	15					0		f
39	Marlon	Edgardo	Figueroa	Martínez	m	\N				73.00	f	Marlon	nueva2		\N	\N	\N		\N	\N	31	4	preju	3	38					0		t
2	Adriana	Saraí	Vasquez  	Rodríguez	f	\N				75.00	f	Adri	agape3		\N	\N	\N		\N	\N	23	3	preju	2	27					0		t
43	Natalia	Daniela	González	Tobar	f	\N				75.00	f	Naty	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		t
8	Diana	Saraí	Santos	Martir	f	\N				75.00	f	Diana	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
54	David	Godofredo	Campos 	Aguilar	m	\N				75.00	f	David	horeb2		\N	\N	\N		\N	\N	30	2	josias	1	34					0		t
73	Carmen	Elena	Yanes	Peña	f	\N				75.00	f	Carmen	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
24	Andrea	Lizzeth	Letona	Hernández	f	\N				78.00	f	Andrea	agape2		\N	\N	\N		\N	\N	13	6	preju	4	12					0		t
7	Angélica	Yamileth	López	Pérez	f	\N				75.00	f	Angélica	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
57	Sara	Eunice	Arteaga	Funes	f	\N				75.00	f	Sarita	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		t
101	Daniel	Andrés	Bonilla	Montes	m	\N				0.00	f	Dany	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		f
69	Rolando 	Javier	Guardado	Alvarado	m	\N				0.00	f	Rolando	belen		\N	\N	\N		\N	\N	2	5	preju	3	2					0		f
71	Jonathan	Eduardo	Hernández	Díaz	m	\N				75.00	f	Jonathan	juda		\N	\N	\N		\N	\N	17	5	preju	3	16					0		t
67	Melvin	Alexi	Pérez	Pérez	m	\N				0.00	f	Alexi	nueva1		\N	\N	\N		\N	\N	25	3	preju	2	29					0		f
64	Luis	Hernán 	Orellana	Reyes	m	\N				75.00	f	Luis	nueva1		\N	\N	\N		\N	\N	25	3	preju	2	29					0		t
38	Laura	Celina	Gil	Henríquez	f	\N				78.00	f	Laurita	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		t
79	Alexia	Rosibel	Ochoa	González	f	\N				78.00	f	Alexia	anakaino4		\N	\N	\N		\N	\N	27	2	josias	1	31					0		t
42	Katherine	Haydee	Contreras	Menjívar	f	\N				75.00	f	Katherine	huespedes2		\N	\N	\N		\N	\N	7	6	preju	4	6					0		t
16	María	José	Rivera	Recinos	f	\N				75.00	f	María	huespedes2		\N	\N	\N		\N	\N	7	6	preju	4	6					0		t
53	Jonathan	Alexander	Arteaga	Segovia	f	\N				75.00	f	Jonathan	juda		\N	\N	\N		\N	\N	17	5	preju	3	16					0		t
35	Javier	Alfonso	Martínez	Portillo	m	\N				78.00	f	Alfonso	nueva2		\N	\N	\N		\N	\N	31	4	preju	3	38					0		t
63	Roberto	Benjamín	Coello	Gómez	m	\N				75.00	f	Roberto	gerizim		\N	\N	\N		\N	\N	12	6	preju	4	11					0		t
81	Carlos 	Raúl	Dominguez	Hernández	m	\N				79.00	f	Raul	nueva2		\N	\N	\N		\N	\N	31	4	preju	3	38					0		t
41	Ludwing	Alfredo	Contreras	Menjívar	m	\N				75.00	f	Ludwing	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
37	Raúl 	Ernesto	López	Hernández	m	\N				75.00	f	Raúl	juda		\N	\N	\N		\N	\N	17	5	preju	3	16					0		t
17	Florence	Natalia	Perdomo	de la O	f	\N				78.00	f	Florence	huespedes2		\N	\N	\N		\N	\N	7	6	preju	4	6					0		t
98	Alessandra	Jeanneth	Vega	Hernández	f	\N				75.00	f	Alessandra	koinonia4		\N	\N	\N		\N	\N	20	4	preju	3	19					0		t
128	Carlos 	Samuel	Flores	Olivares	m	\N				78.00	f	Carlos	nueva1		\N	\N	\N		\N	\N	25	3	preju	2	29					0		t
9	Adriana	Elizabeth	Gutiérrez	Padilla	f	\N				75.00	f	Adriana	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
72	Josué	 Alejandro	Pérez	Linares	m	\N				0.00	f	Josué	belen		\N	\N	\N		\N	\N	2	5	preju	3	2					0		f
120	Eduardo	Enrique	Herrera		m	\N				75.00	f	Eduardo	belen		\N	\N	\N		\N	\N	2	5	preju	3	2					0		t
143	Irma	Elizabeth	Claros	Alemán	f	\N				75.00	f	Irma	anakaino2		\N	\N	\N		\N	\N	34	1	josias	1	41					0		t
109	Rodrigo	Eduardo	Zelaya	Fuentes	m	\N				0.00	f	Rodrigo	gerizim		\N	\N	\N		\N	\N	12	6	preju	4	11					0		f
94	Cinthya	Gissellie	Pineda 	Bonilla	f	\N				78.00	f	Cinthya	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		t
48	Ivy	Vanessa	Gutiérrez	Padilla	f	\N				75.00	f	Ivy	anakaino3		\N	\N	\N		\N	\N	28	2	josias	1	32					0		t
147	Rebeca	Aracely	Alvarado	Granados	f	\N				78.00	f	Rebeca	anakaino1		\N	\N	\N		\N	\N	35	1	josias	1	42					0		t
112	Astrid	Nicolle	Rivas	Cruz	f	\N				0.00	f	Nicolle	koinonia3		\N	\N	\N		\N	\N	14	5	preju	3	13					0		f
22	Marcela	Alejandra	Mendoza	Orellana	f	\N				75.00	f	Marcela	anakaino3		\N	\N	\N		\N	\N	28	2	josias	1	32					0		t
52	Jorge 	Daniel	Cruz	Vásquez	m	2001-02-16 22:50:00-06	sas	Tonacatepeque	Estudiante	0.00	f	Jorge	horeb2	M00623981	113	\N	\N	RAFAEL ANTONIO RIVAS QUINTANILLA	3	4	29	2	josias	1	33	m	chief	sas	Ilopango	0	jorge	f
127	Diego	Alfredo	Ochoa	Gómez	m	\N				75.00	f	Diego	nueva2		\N	\N	\N		\N	\N	16	4	preju	3	15					0		t
95	Paola	Gabriela	Magaña	Peña	f	\N				0.00	f	Paola	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		f
89	Carlos	Rodrigo	Cornejo	González	m	\N				0.00	f	Carlos Rodrigo	belen		\N	\N	\N		\N	\N	1	5	preju	2	1					0		f
145	Ariel	Josué	Martínez	Márquez	f	\N				75.00	f	Ariel	horeb1		\N	\N	\N		\N	\N	36	1	josias	1	43					0		t
138	Karen	Paola	Morales	Bonilla	f	\N				75.00	f	Paola	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		t
126	Alejandro	Alfredo	Ochoa	Gómez	m	\N				75.00	f	Alejandro	nueva2		\N	\N	\N		\N	\N	16	4	preju	3	15					0		t
20	Stephanie	Elizabeth	Ramos	Ramirez	f	\N				75.00	f	Elizabeth	anakaino4		\N	\N	\N		\N	\N	27	2	josias	1	31					0		t
114	David	Gonzalo	Castillo	Dimas	m	\N				75.00	f	Gonzo	juda		\N	\N	\N		\N	\N	17	5	preju	3	16					0		t
142	Sara	Ester	Martínez	Francia	f	\N				75.00	f	Sara	huespedes2		\N	\N	\N		\N	\N	7	6	preju	4	6					0		t
123	Jessica	Estelisa	Lemus	Alas	f	\N				0.00	f	Jessica	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		f
103	Carlos	Eduardo 	Escobar	Iraheta	m	\N				0.00	f	Carlos	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		f
78	Carmen	Patricia	Sánchez	García	f	\N				0.00	f	Carmen	koinonia3		\N	\N	\N		\N	\N	6	5	preju	3	5					0		f
137	Mónica 	María	Morales	Bonilla	f	\N				75.00	f	Mónica	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		t
80	Evelyn	Janet	Trinidad	García	f	\N				75.00	f	Evelyn	koinonia3		\N	\N	\N		\N	\N	6	5	preju	3	5					0		t
96	Ana	Margarita	Santamaría	Hernández	f	\N				75.00	f	Ana	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		t
121	Débora	Michelle	Pérez	Castillo	m	\N				0.00	f	Debbie	koinonia4		\N	\N	\N		\N	\N	20	4	preju	3	19					0		f
141	Krisia		Díaz		f	\N				75.00	f	Krisia	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
119	Irina	Lucia	Orantes	Regalado	f	\N				78.00	f	Lucy	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		t
99	Cristian	Alexander	Ayala	Serrano	m	\N				75.00	f	Cristian	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
139	Roger	Ellebien	Torres	Díaz	m	\N				75.00	f	Roger	nueva1		\N	\N	\N		\N	\N	25	3	preju	2	29					0		t
102	William	Rodrigo	Huezo	Orantes	m	\N				75.00	f	Rodrigo	belen		\N	\N	\N		\N	\N	1	5	preju	2	1					0		t
23	Karla	Tatiana	Duke	Monchez	f	\N				75.00	f	Karla	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		t
140	Jonathan	Josué	González	Sosa	m	\N				75.00	f	Jonathan	horeb1		\N	\N	\N		\N	\N	36	1	josias	1	43					0		t
87	Alejandra	Maria	Claros	Burgos	f	\N				75.00	f	Ale	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		t
107	Diego	Andrés	Velado	Peñate	m	\N				0.00	f	Diego	belen		\N	\N	\N		\N	\N	1	5	preju	2	1					0		f
77	Raúl 	David	Yanes	Peña	m	\N				75.00	f	Raúl	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
149	Karla	Iliana	Baires	Escobar	f	\N				75.00	f	Ili	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
122	Edi	Lineth	Caseros	Cubias	f	\N				75.00	f	Titi	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
105	Josué	David	Lainez	Castro	m	\N				75.00	f	Josué	gerizim		\N	\N	\N		\N	\N	12	6	preju	4	11					0		t
150	Luis	Rene	Baires	Escobar	m	\N				75.00	f	Luis	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
151	Juan 	Carlos	Morales	Sosa	m	\N				75.00	f	Sosa	horeb2		\N	\N	\N		\N	\N	30	2	josias	1	34					0		t
85	Bianca		Gavidia		f	\N				0.00	f	Bianca	koinonia3		\N	\N	\N		\N	\N	6	5	preju	3	5					0		f
13	Guillermo	Arturo	Alvarado	Araujo	m	1998-08-18 08:05:00-06	sas	Cuscatancingo	Estudiante	75.00	f	Guille	belen	M00707888	478	480	53	Jesus Douglas Henriquez Rodriguez	1	2	2	5	preju	3	2		subchief	sas	San Salvador	0	silvia	t
83	Miguel	Alejandro	Soriano	Beltrán	m	\N				75.00	f	Ale	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
148	Andrea	Roxana	Ponce	Martir	f	\N				75.00	f	Andrea	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
115	Nicole	Azucena	Barahona	Castro	f	\N				75.00	f	Nicole	koinonia4		\N	\N	\N		\N	\N	20	4	preju	3	19					0		t
146	Ana	Elizabeth	Montoya	Ardón	f	\N				75.00	f	Elizabeth	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		t
144	David	Alejandro	Gómez	Elias	m	\N				75.00	f	Alejandro	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
129	Aldo	Andrés	Palacios	Escamilla	m	\N				75.00	f	Andrés	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
84	Raúl 	Alexander	Mata	Peña	m	\N				0.00	f	Raul	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		f
134	Josue	Ariel 	Umanzor		m	\N				0.00	f	Ariel	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		f
76	Mónica	Gabriela	Hernández	Villacorta	f	\N				78.00	f	Mónica	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
135	Ernesto	Alexander	Figueroa	Dominguez	m	\N				0.00	f	Alex	horeb2		\N	\N	\N		\N	\N	29	2	josias	1	33					0		f
165	Gloria	Raquel	Gutiérrez	Quinteros	f	\N				78.00	f	Gloria	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
19	Francisco	Ariel	Linares	Melgar	m	\N				75.00	f	Ariel	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
110	Rodrigo	Alberto	Martinez	Renderos	m	\N				78.00	f	Chino	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
152	Adriana		Contreras	Pujol	f	\N				75.00	f	Adriana Pujol	anakaino1		\N	\N	\N		\N	\N	35	1	josias	1	42					0		t
184	Pablo	Ricardo	Rodriguez	Paz	m	\N				75.00	f	Pablo	horeb2		\N	\N	\N		\N	\N	30	2	josias	1	34					0		t
153	Nicole		Contreras	Pujol	f	\N				75.00	f	Nicole Pujol	agape3		\N	\N	\N		\N	\N	26	3	preju	2	30					0		t
185	Abel	Ernesto	Magaña	Rivera	m	\N				78.00	f		nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
154	Emilton	Daniel	Alvarenga	Flores	m	\N				75.00	f	Emilton	horeb2		\N	\N	\N		\N	\N	30	2	josias	1	34					0		t
86	Carlos	Ernesto	Medrano	Guerrero	m	\N				75.00	f	Neto	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
158	Carlos	Alejandro	Montoya	Cáceres	m	\N				5.00	f	Alejandro	nueva1		\N	\N	\N		\N	\N	25	3	preju	2	29					0		t
161	Mauricio	Alejandro	Pacheco	Guerrero	m	\N				78.00	f	Mauricio	nueva2		\N	\N	\N		\N	\N	16	4	preju	3	15					0		t
65	Mauricio	Javier	Castellón	Cerritos	m	\N				75.00	f	Mauri	nueva2		\N	\N	\N		\N	\N	31	4	preju	3	38					0		t
162	José	Eduardo	Pacheco	Guerrero	m	\N				78.00	f	Eduardo	horeb1		\N	\N	\N		\N	\N	36	1	josias	1	43					0		t
172	Cindy	Nayeli	Bonilla	Beltran	f	\N				78.00	f	Cindy	anakaino3		\N	\N	\N		\N	\N	28	2	josias	1	32					0		t
164	María	Fernanda	Balibrerra	Barahona	f	\N				78.00	f	Mafer	agape3		\N	\N	\N		\N	\N	21	3	preju	2	20					0		t
47	Astrid	Margarita	Hernández	Villacorta	f	\N				78.00	f	Astrid	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
156	Paola	Rebeca	Lara	Cruz	f	\N				78.00	f	Paola	anakaino2		\N	\N	\N		\N	\N	34	1	josias	1	41					0		t
155	María	José	Alvarado	Argueta	f	\N				75.00	f	María José	anakaino2		\N	\N	\N		\N	\N	34	1	josias	1	41					0		t
183	Rafaela	Nicole	Guardado	Zelaya	f	\N				75.00	f	Nicole	anakaino1		\N	\N	\N		\N	\N	35	1	josias	1	42					0		t
27	Christian	Alessandro	Calderón	Castillo	m	\N				75.00	f	Christian	belen		\N	\N	\N		\N	\N	2	5	preju	3	2					0		t
176	Nelson	Edgardo	Linares	Arias	m	\N				75.00	f	Nelson	gerizim		\N	\N	\N		\N	\N	12	6	preju	4	11					0		t
160	Diana	Marcela	Pacheco	Guerrero	f	\N				78.00	f	Marce	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
157	Karen	Adriana	Recinos	Orellana	f	\N				78.00	f	Karen	anakaino2		\N	\N	\N		\N	\N	34	1	josias	1	41					0		t
163	Daniel	Alberto	Alcoleas	Jaime	m	\N				75.00	f	Daniel	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
187	José	Carlos	Sequeira	Alvarado	m	\N				74.00	f	Sequeira	horeb1		\N	\N	\N		\N	\N	36	1	josias	1	43					0		t
191	Josué	David	Mejía		m	\N				78.00	f	Josué	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
82	Alejandra	Poulette	Montalvo	Meza	f	\N				75.00	f	Poulette	anakaino3		\N	\N	\N		\N	\N	28	2	josias	1	32					0		t
190	Allison	Michel	Santos		f	\N				65.00	f	Allison	koinonia1		\N	\N	\N		\N	\N	4	4	preju	2	3					0		t
169	Karla	Veronica	Bonilla	Peña	f	\N				75.00	f	Karla	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
181	Mayra	Fabiola	Monterrosa		f	\N				78.00	f	Fabiola	anakaino2		\N	\N	\N		\N	\N	34	1	josias	1	41					0		t
159	Denise	Elizabeth	Hernández	Pineda	f	\N				78.00	f	Denise	anakaino1		\N	\N	\N		\N	\N	35	1	josias	1	42					0		t
66	Emely	Nohemi	Sevillano	Platero	f	1998-11-26 04:30:00-06	sas	Soyapango	Estudiante	60.00	f	Emely	koinonia4	A50022654	326	326	77	Juan Jose Armando Azucena Catan	7	8	20	4	preju	3	19	m	chief	sas	San Salvador	0	jorge	t
182	Raquel	Alejandra	Pérez	Martínez	f	\N				78.00	f	Raquel	koinonia3		\N	\N	\N		\N	\N	6	5	preju	3	5					0		t
166	Katherine	Lisbeth	Vásquez	Chávez	f	\N				78.00	f	Kathy	anakaino4		\N	\N	\N		\N	\N	27	2	josias	1	31					0		t
168	Tania	Gisselle	Cárcamo	Hernández	f	\N				75.00	f	Exodo 	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
173	Nicole	Estefania	Rodas	Chávez	f	\N				78.00	f	Nicole	anakaino4		\N	\N	\N		\N	\N	27	2	josias	1	31					0		t
186	Ronald		Navas	López	m	\N				5.00	f	Ronalds	horeb2		\N	\N	\N		\N	\N	30	2	josias	1	34					0		t
171	Moisés	Daniel	Mejía	Henríquez	m	\N				78.00	f	Daniel	horeb1		\N	\N	\N		\N	\N	33	1	josias	1	40					0		t
177	Debora	Elizabeth	Romero	Martínez	f	\N				75.00	f	Debby	anakaino2		\N	\N	\N		\N	\N	34	1	josias	1	41					0		t
178	Nicole	Astrid	Rivas	Cruz	f	\N				75.00	f	Nicole	koinonia3		\N	\N	\N		\N	\N	14	5	preju	3	13					0		t
180	Jose 	Luis	Monterrosa		m	\N				78.00	f	Jose Luis	horeb2		\N	\N	\N		\N	\N	30	2	josias	1	34					0		t
40	Andrés	Gerardo	López	Guevara	m	\N				78.00	f	Andrés 	horeb2		\N	\N	\N		\N	\N	29	2	josias	1	33					0		t
167	María	Beatriz	Zuniga	Ramirez	f	\N				75.00	f	Bea	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
188	Bryan	Dennis	Castillo	Flores	m	\N				0.00	f	Bryan	belen		\N	\N	\N		\N	\N	1	5	preju	2	1					0		f
189	David	Alejandro	Torres	Andino	m	\N				83.00	f	Ale Torres	nueva1		\N	\N	\N		\N	\N	24	3	preju	2	28					0		t
170	Reina	Dolores	Barrera	Mijano	f	\N				75.00	f	Reina	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
179	Iker	Gabriel	Pérez	Andrade	m	\N				78.00	f	Iker	horeb2		\N	\N	\N		\N	\N	30	2	josias	1	34					0		t
193	Bryan	Josué	Andrade	Delgado	m	\N				78.00	f	Bryan	gerizim		\N	\N	\N		\N	\N	12	6	preju	4	11					0		t
174	Joaquin		Cornejo	Viches	m	\N				10.00	f	Joaquin	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
194	Alejandro		Orellana		m	\N				75.00	f	Alejandro	horeb1		\N	\N	\N		\N	\N	33	1	josias	1	40					0		t
196	Margorie		Prieto	Castro	f	\N				78.00	f	Margorie	agape3		\N	\N	\N		\N	\N	26	3	preju	2	30					0		t
197	Ana	Marcela	Chavarría	Hernández	f	\N				78.00	f	Marce	koinonia4		\N	\N	\N		\N	\N	15	4	preju	2	14					0		t
198	Patricia	Elizabeth	Chavarría	Hernández	f	\N				78.00	f	Paty	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
200	Karla	Gabriela	Aguilar	Pérez	f	\N				75.00	f	Gabby	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		t
116	Josué	Israel	Guevara	Aguilar	m	2001-08-20 11:29:00-06	sas	San Salvador	Estudiante	75.00	f	Josué	horeb2	A50026996	221	223	44	Juan Jose Armando Azucena Catan	9	\N	29	2	josias	1	33	m	chief	sas	San Salvador	0	jorge	t
199	Victor	Josué	Yanez	López	m	\N				25.00	f	Victor	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
201	Oscar	Daniel	Renderos		m	\N				75.00	f	Oscar	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
202	Boris	Emilio	Quixada		m	\N				78.00	f	Boris	moab		\N	\N	\N		\N	\N	5	6	preju	4	4					0		t
204	Yanira		Rodriguez		f	\N				78.00	f	Yanira	koinonia3		\N	\N	\N		\N	\N	19	5	preju	3	18					0		t
205	Amanda	Gisselle	Franco		f	\N				50.00	f		agape3		\N	\N	\N		\N	\N	26	3	preju	2	30					0		t
206	Norma	Berenice	Sigarun	Ortiz	f	\N				75.00	f	Bernice	agape2		\N	\N	\N		\N	\N	11	6	preju	4	10					0		t
207	Gloria	 Maria	Campos	Fernández	f	\N				75.00	f	Gloria	huespedes2		\N	\N	\N		\N	\N	7	6	preju	4	6					0		t
208	Rene		Campos	Fernández	m	\N				75.00	f		gerizim		\N	\N	\N		\N	\N	12	6	preju	4	11					0		t
195	Frances	Melana	García	Díaz	f	\N				75.00	f	Frances	koinonia3		\N	\N	\N		\N	\N	6	5	preju	3	5					0		t
\.


--
-- Name: signup_camper_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_camper_id_seq', 208, true);


--
-- Data for Name: signup_counselor; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_counselor (id, first_name, second_name, first_surname, second_surname, gender, balance, no_pay, badge_name, cabin, small_group_id, generation, structure, bus, signed_up) FROM stdin;
28	Sara	Carolina	Moreno	Sandoval	f	75.00	f	Sarita	anakaino3	32	2	josias	1	t
1	José	Eduardo	Rivas	Melgar	m	75.00	f	Choche	belen	1	5	preju	2	t
16	Milton	Josué	Méndez	Alfaro	m	75.00	f	Méndez	nueva2	15	4	preju	3	t
4	María	Alejandra	Durán	Castellanos	f	75.00	f	Ale	koinonia1	3	4	preju	2	t
7	Andrea	Saraí	Navarrete	Pérez	f	75.00	f	Saraí	huespedes2	6	6	preju	4	t
20	Maricela	Nohemy	Flores	de León	f	20.00	f	Maricela	koinonia4	19	4	preju	3	t
26	Imelda	Margarita	Aguilar	Palma	f	75.00	f	Margarita	agape3	30	3	preju	2	t
25	Erik	Emmanuel	Miranda	Hernández	m	75.00	f	Erik	nueva1	29	3	preju	2	t
13	Elisa	Imelda	Echegoyén	Díaz	f	0.00	f	Elisa	agape2	12	6	preju	4	f
12	Jacob	Benjamín	Zelaya	Chicas	m	70.00	f	Jake	gerizim	11	6	preju	4	t
2	José	David	Nery	Maravilla	m	75.00	f	Nery	belen	2	5	preju	3	t
15	Jacqueline	Beatriz	Aquino	Fuentes	f	75.00	f	Jacqui	koinonia4	14	4	preju	2	t
36	Gerardo	Josué	Osorio	Portillo	m	75.00	f	Gerardo	horeb1	43	1	josias	1	t
17	Miguel	Antonio	Guardado	Salmerón	m	75.00	f	Mike	juda	16	5	preju	3	t
11	Laura	Patricia	Santillana	Meléndez	f	75.00	f	Laura	agape2	10	6	preju	4	t
5	Ricardo	Josué	Medrano	Guerrero	m	75.00	f	Ricardo	moab	4	6	preju	4	t
19	Pamela	Alejandra	Chacón	Rodríguez	f	75.00	f	Pame	koinonia3	18	5	preju	3	t
35	Elia	Fernanda	Carranza	Ríos	f	75.00	f	Elia	anakaino1	42	1	josias	1	t
31	Geovanny	Ernesto	Lainez	Castro	m	55.00	f	Geo	nueva2	38	4	preju	3	t
27	Karen	Noemi	López	Dimas	f	75.00	f	Karencita	anakaino4	31	2	josias	1	t
30	Oliver	Stanley	Larín	Aguirre	m	75.00	f	Oliver	horeb2	34	2	josias	1	t
14	Griselda	Beatriz	Martínez	Cornejo	f	75.00	f	Gris	koinonia3	13	5	preju	3	t
22	Ruth	Abigail	Méndez	Alfaro	f	75.00	f	Abby	agape3	26	3	preju	2	t
21	Clarissa	Esmeralda	Rodriguez	Monge	f	75.00	f	Clari	agape3	20	3	preju	2	t
6	Gloria	Raquel	González	Galdamez	f	75.00	f	Raque	koinonia3	5	5	preju	3	t
34	Marcela	Roxana	Melara	Rodríguez	f	75.00	f	Marcela	anakaino2	41	1	josias	1	t
29	René	Moisés	Sevillano	Platero	m	65.00	f	René	horeb2	33	2	josias	1	t
23	Priscila	Saraí	Sevillano	Platero	f	55.00	f	Priscy	agape3	27	3	preju	2	t
33	Tarquino	Aldair	Hernández	Cañenguez	m	75.00	f	Tarki	horeb1	40	1	josias	1	t
24	Christian	Steve	Domínguez	Vallecillos	m	75.00	f	Tivi	nueva1	28	3	preju	2	t
\.


--
-- Name: signup_counselor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_counselor_id_seq', 36, true);


--
-- Data for Name: signup_guest; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_guest (id, first_name, second_name, first_surname, second_surname, gender, balance, no_pay, badge_name, cabin, signed_up) FROM stdin;
9	Mauricio	Alberto	Paz	Herrera	m	75.00	f	Mou		t
11	Grisel	Abigail	González	de Santillana	f	75.00	f	Aby 		t
10	Javier	Ernesto	Santillana	Meléndez	m	75.00	f	Javo		t
12	Julia		de Paz		f	75.00	f			t
\.


--
-- Name: signup_guest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_guest_id_seq', 12, true);


--
-- Data for Name: signup_parent; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_parent (id, first_name, second_name, first_surname, second_surname, gender, birth_date, state, province, occupation, gov_id, known_as) FROM stdin;
1	Ana	Mercedes	Araujo	de Alvarado	f	1965-10-13 00:00:00-06	sas	Cuscatancingo	Empleada	02106986-5	
2	Carlos	Arturo	Alvarado	Valencia	m	1966-08-29 00:00:00-06	sas	Cuscatancingo	Empleado	01596605-9	
5	Paula	Maritza	Pineda	de Rodriguez	f	1961-11-18 00:00:00-06	lal	Santa Tecla	Ingeniera Quimica	02738005-7	
6	Jorge	Dante	Rodriguez	Pineda	m	1954-08-15 00:00:00-06	lal	Santa Tecla	Ingeniero Civil	01664314-1	
7	Marta	Luz	Platero	de Sevillano	f	1968-04-29 00:00:00-06	sas	Soyapango	Contador	00975440-2	
9	Marta	Celia	Guevara	Aguilar	f	1976-03-12 00:00:00-06	sas	San Salvador	Cosmetóloga	03061993-6	
11	Salvador		Mata	Iraheta	m	1967-08-08 00:00:00-06	lal	Antiguo Cuscatlán	Ingeniero Industrial	02830060-2	
4	Vicente		Cruz	García	m	1956-08-09 00:00:00-06	sas	Tonacatepeque	Comerciante	01697230-4	
10	Blanca	Gloria Elizabeth	Salinas	de Mata	f	1963-01-12 00:00:00-06	lal	Antiguo Cuscatlán	Licenciada en Idioma Inglés	02428318-3	
3	Sara	Noemy	Vásquz	de Cruz	f	1976-09-25 00:00:00-06	sas	Tonacatepeque	Modista	02025969-5	
8	Rene	Moisés	Sevillano	Martinez	m	1966-12-25 00:00:00-06	sas	Soyapango	Empleado	00058806-6	
\.


--
-- Name: signup_parent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_parent_id_seq', 11, true);


--
-- Data for Name: signup_payment; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_payment (id, receipt_id, payment_date, amount, notes, content_type_id, object_id) FROM stdin;
377	001	2014-05-25	5.00		12	5
378	002	2014-05-18	5.00		11	23
379	003	2014-05-18	10.00		11	139
380	004	2014-05-18	5.00		11	140
381	006	2014-05-18	40.00		11	141
382	007	2014-05-18	5.00		11	20
383	008	2014-06-01	5.00		11	71
384	009	2014-06-01	20.00		12	21
385	010	2014-06-08	5.00		11	142
386	011	2014-06-08	5.00		11	2
387	012	2014-06-08	5.00		11	83
388	014	2014-06-15	5.00		12	2
389	015	2014-06-15	5.00		12	22
390	016	2014-06-15	20.00		11	15
391	017	2014-06-15	10.00		12	19
392	018	2014-06-20	20.00		12	4
393	019	2014-06-15	15.00		11	13
394	020	2014-06-15	50.00		11	105
395	021	2014-06-22	5.00		11	102
396	022	2014-06-22	75.00		11	53
397	023	2014-06-22	30.00		11	143
398	024	2014-06-22	20.00		11	12
399	025	2014-06-22	60.00		11	13
400	026	2014-06-22	40.00		11	144
401	027	2014-06-22	5.00		11	70
402	028	2014-06-22	75.00		12	24
403	029	2014-06-22	20.00		12	34
404	030	2014-06-22	20.00		11	86
405	031	2014-06-22	20.00		11	36
406	041	2014-06-22	5.00		11	61
407	042	2014-06-22	10.00		11	39
408	043	2014-06-22	5.00		11	96
409	044	2014-06-22	30.00		11	145
410	045	2014-06-22	5.00		11	119
411	046	2014-06-22	5.00		11	146
412	047	2014-06-22	10.00		11	21
413	048	2014-06-22	7.00		11	2
414	1b	2014-06-22	75.00		11	127
415	2b	2014-06-22	75.00		11	126
416	3b	2014-06-22	20.00		11	147
417	5b	2014-06-22	5.00		11	56
418	4b	2014-06-22	5.00		11	148
419	6b	2014-06-22	10.00		11	139
420	7b	2014-06-22	75.00		11	149
421	8b	2014-06-22	45.00		11	150
422	9b	2014-06-22	5.00		11	99
423	081	2014-06-28	5.00		13	9
426	084	2014-06-28	5.00		11	151
427	085	2014-06-28	10.00		11	152
428	086	2014-06-28	10.00		11	153
429	087	2014-06-28	40.00		11	154
430	088	2014-06-28	5.00		11	48
431	089	2014-06-28	20.00		11	22
432	090	2014-06-28	5.00		12	30
433	091	2014-06-28	5.00		12	27
435	032	2014-06-28	20.00		13	9
436	033	2014-06-28	20.00		11	65
437	034	2014-06-28	20.00		11	27
438	036	2014-06-28	20.00		11	142
439	049	2014-06-29	25.00		11	41
440	050	2014-06-29	25.00		11	42
434	035	2014-06-28	70.00		12	12
441	081b	2014-06-29	10.00		11	54
442	082	2014-06-29	70.00		11	155
443	083.1	2014-06-29	40.00		11	140
444	084b	2014-06-29	40.00		11	147
445	085b	2014-06-29	5.00		11	94
446	086b	2014-06-29	5.00		11	25
447	087b	2014-06-29	5.00		11	8
448	088b	2014-06-29	78.00		11	156
449	089b	2014-06-29	26.80		11	2
450	090b	2014-06-29	37.50		13	10
451	091b	2014-06-29	37.50		13	11
452	093b	2014-07-06	5.00		11	157
453	094b	2014-07-06	20.00		12	2
454	095b	2014-07-06	5.00		11	46
455	096b	2014-07-06	5.00		11	17
456	097	2014-07-06	20.00		11	65
457	098	2014-07-06	75.00		11	120
458	099	2014-07-06	40.00		11	21
459	100	2014-07-06	30.00		11	17
460	101	2014-07-06	5.00		11	155
461	102	2014-07-06	5.00		11	128
462	103	2014-07-06	5.00		11	158
463	104	2014-07-06	25.00		11	8
464	105	2014-07-06	5.00		11	87
465	106	2014-07-06	10.00		11	73
466	107	2014-07-06	10.00		11	77
467	108	2014-07-06	5.00		11	27
468	109	2014-07-06	10.00		11	159
469	110	2014-07-06	5.00		11	160
470	111	2014-07-06	5.00		11	161
471	94	2014-07-06	5.00		11	162
472	112	2014-07-13	20.00		11	163
473	113	2014-07-13	10.00		11	66
474	114	2014-07-13	50.00		11	164
475	037	2014-07-16	10.00		11	38
476	038	2014-07-16	50.00		13	9
477	039	2014-07-16	78.00		11	24
478	040	2014-07-16	20.00		11	145
424	082b	2014-06-28	5.00		11	82
425	083	2014-06-28	20.00		12	36
479	120	2014-07-16	5.00		11	19
480	121	2014-07-16	15.00		11	165
481	122	2014-07-16	10.00		11	55
482	123	2014-07-16	70.00		11	70
483	124	2014-07-16	78.00		11	166
484	125	2014-07-16	75.00		11	9
485	126	2014-07-16	60.00		11	146
486	130	2014-07-16	30.00		11	167
487	130.1	2014-07-16	30.00		11	168
488	130.2	2014-07-16	30.00		11	169
489	130.3	2014-07-16	30.00		11	170
490	131	2014-07-17	78.00		11	47
491	131.b	2014-07-17	78.00		11	76
492	132	2014-07-17	43.00		11	17
493	133	2014-07-17	20.00		11	159
494	134	2014-07-17	78.00		11	171
495	135	2014-07-17	8.00		11	172
496	136	2014-07-17	8.00		11	108
497	137	2014-07-17	10.00		11	173
498	138	2014-07-17	20.00		11	140
499	139	2014-07-17	10.00	INVITADO	11	174
500	140	2014-07-17	55.00		11	12
501	141	2014-07-17	20.00		11	58
502	116	2014-07-17	70.00		11	46
503	117	2014-07-17	70.00		11	23
504	118	2014-07-17	50.00		11	86
506	124.1	2014-07-17	12.00		12	23
507	125.1	2014-07-17	5.00		12	29
509	120b	2014-07-23	5.00		11	168
510	121b	2014-07-23	5.00		11	169
511	122b	2014-07-23	5.00		11	170
512	123b	2014-07-23	30.00		12	4
513	126B	2014-07-13	75.00		11	176
514	127	2014-07-23	10.00		11	43
515	128	2014-07-23	30.00		11	150
516	129	2014-07-23	5.00		12	33
517	130B	2014-07-23	70.00		11	48
518	131B	2014-07-23	10.00		11	79
519	132B	2014-07-23	15.00		11	177
520	133b	2014-07-23	73.00		11	157
521	134b	2014-07-23	65.00		11	152
522	135b	2014-07-23	65.00		11	153
523	136b	2014-07-23	50.00		11	81
524	137b	2014-07-23	5.00		11	40
525	138b	2014-07-23	70.00		11	37
526	139b	2014-07-23	20.00		11	159
527	141b	2014-07-23	5.00		11	178
528	142b	2014-07-23	50.00		11	57
529	143b	2014-07-23	68.00		11	38
530	144b	2014-07-23	45.00		11	143
531	147	2014-07-23	5.00		12	16
532	145b	2014-07-23	30.00		12	21
533	148b	2014-07-23	5.00		12	28
534	91b	2014-07-25	70.00		12	30
535	92b	2014-07-25	20.00		11	82
536	93b	2014-07-25	10.00		11	18
537	95b	2014-07-25	10.00		11	63
538	96b	2014-07-25	25.00		11	145
539	97	2014-07-25	78.00		11	179
540	98b	2014-07-25	15.00		11	22
541	99b	2014-07-25	70.00		11	20
542	100b	2014-07-25	78.00		11	180
543	101b	2014-07-25	78.00		11	181
544	102b	2014-07-25	38.00		11	45
547	105b	2014-07-25	35.00		11	141
548	106b	2014-07-25	5.00		11	37
550	129b	2014-07-25	78.00		11	125
551	142	2014-07-25	15.00		11	27
552	142.1	2014-07-25	10.00		11	140
553	143	2014-07-25	40.00		11	182
554	144.1	2014-07-25	15.00		11	105
555	145	2014-07-25	5.00		11	183
556	146	2014-07-25	5.00		11	110
557	147.1	2014-07-25	25.00		11	21
558	148	2014-07-25	10.00		11	146
559	149	2014-07-25	5.00		11	184
560	150	2014-07-25	68.00		11	173
561	151	2014-07-25	5.00		11	185
562	152	2014-07-26	20.00		11	116
564	153	2014-07-26	75.00		11	98
565	154	2014-07-26	5.00		11	186
566	155	2014-07-26	75.00		12	15
567	63	2014-07-26	10.00		11	115
568	62	2014-07-26	70.00		11	99
569	61	2014-07-26	5.00		11	187
570	60	2014-07-26	9.10		11	2
571	59	2014-07-26	55.00		11	15
572	58	2014-07-26	50.00		11	119
573	57	2014-07-26	5.00	5	12	35
574	056	2014-07-26	15.00		11	142
576	55	2014-07-26	5.00		11	80
577	54	2014-07-26	5.00		11	189
578	53	2014-07-26	5.00		11	100
579	52	2014-07-26	5.00		11	1
581	64	2014-07-26	5.00		11	190
582	151b	2014-07-27	40.00		11	167
583	200	2014-07-27	65.00		11	63
584	149.1	2014-07-27	70.00		11	114
585	201	2014-07-27	65.00		11	18
586	202	2014-07-27	5.00		11	114
587	150.1	2014-07-27	25.00		11	81
588	203	2014-07-27	78.00		11	189
589	119	2014-07-27	5.00		11	167
590	108.1	2014-07-27	40.00		11	168
591	109.1	2014-07-27	40.00		11	169
592	204	2014-07-27	78.00		11	191
593	110.1	2014-07-27	40.00		11	170
594	111.1	2014-07-27	75.00		12	17
596	207	2014-07-27	18.00		11	147
597	112.1	2014-07-27	78.00		11	193
598	208	2014-07-27	30.00		11	22
599	113.1	2014-07-27	10.00		11	105
600	209	2014-07-27	50.00		11	116
601	114.1	2014-07-27	50.00		12	19
602	115.1	2014-07-27	25.00		11	57
604	210	2014-07-27	73.00		11	128
605	116.1	2014-07-27	38.00		11	182
606	211	2014-07-27	35.00		11	154
607	212	2014-07-27	75.00		11	64
608	213	2014-07-27	75.00		11	194
609	214	2014-07-27	60.00		11	177
610	117.1	2014-07-27	5.00		11	195
611	215	2014-07-27	78.00		11	196
612	216	2014-07-27	39.00		11	187
613	217	2014-07-27	70.00		12	35
614	218	2014-07-27	70.00		11	151
615	159	2014-07-27	73.00		11	100
616	219	2014-07-27	70.00		12	27
617	220	2014-07-27	73.00		11	40
618	160	2014-07-27	70.00		11	25
619	221	2014-07-27	58.00		11	58
620	161	2014-07-27	75.00		11	7
621	222	2014-07-27	70.00		12	22
622	162	2014-07-27	73.00		11	94
623	223	2014-07-27	70.00		11	19
624	163	2014-07-27	28.00		11	164
625	224	2014-07-27	37.50		13	11
628	166	2014-07-27	25.00		12	21
629	167	2014-07-27	70.00		11	56
630	168	2014-07-27	78.00		11	197
631	169	2014-07-27	78.00		11	198
632	170	2014-07-27	70.00		11	83
603	205	2014-07-27	65.00		11	43
633	172	2014-07-27	50.00		11	39
634	173	2014-07-27	70.00		11	184
635	174	2014-07-27	55.00		11	36
636	174.1	2014-07-27	55.00		12	34
637	175	2014-07-27	70.00		11	71
638	176	2014-07-27	25.00		11	199
639	177	2014-07-27	70.00		11	178
640	178	2014-07-27	20.00		11	148
641	179	2014-07-27	75.00		11	16
642	180	2014-07-27	75.00		11	129
643	181	2014-07-27	65.00		11	54
644	182	2014-07-27	70.00		11	1
645	184	2014-07-27	50.00		11	148
646	185	2014-07-27	73.00		11	185
647	187	2014-07-27	75.00		11	200
549	107b	2014-07-25	75.00		12	1
580	051	2014-07-26	55.00		12	36
648	188	2014-07-27	35.00		11	65
649	225	2014-07-27	70.00		12	28
650	189	2014-07-27	70.00		11	96
651	190	2014-07-27	70.00		11	183
652	073	2014-07-27	27.10		11	2
653	191	2014-07-27	70.00		12	16
654	193	2014-07-27	25.00		12	4
655	192	2014-07-27	30.00		11	8
656	194	2014-07-27	63.00		11	165
657	66	2014-07-27	75.00		12	26
658	67	2014-07-27	55.00		11	139
659	68	2014-07-27	75.00		11	201
660	69	2014-07-27	78.00		11	202
661	70	2014-07-27	70.00		11	172
662	71	2014-07-27	75.00		11	138
663	74	2014-07-27	23.00		11	119
664	75	2014-07-27	50.00		11	41
665	76	2014-07-27	50.00		11	42
666	77	2014-07-27	28.00		11	159
667	78	2014-07-27	20.00		11	190
668	79	2014-07-27	75.00		11	122
669	80	2014-07-27	68.00		11	79
670	226	2014-07-27	5.00		11	116
671	227	2014-07-27	40.00		11	45
672	228	2014-07-27	20.00		11	190
673	229	2014-07-27	15.00		11	8
674	156	2014-07-27	50.00		12	2
675	157	2014-07-27	70.00		11	108
677	195	2014-07-27	70.00		12	5
678	230	2014-07-27	4.00		11	81
679	231	2014-07-27	78.00		11	35
680	235	2014-07-27	10.00		12	7
681	72	2014-07-27	75.00		11	137
682	128.1	2014-07-13	75.00		12	11
683	171	2014-07-27	73.00		11	110
684	158	2014-07-30	35.00		11	144
685	240	2014-08-16	78.00		11	204
686	241	2014-08-16	68.00		11	55
687	242	2014-08-16	15.00		12	19
688	243	2014-08-16	13.00		11	39
689	244	2014-08-16	55.00		12	31
690	245	2014-08-16	30.00		11	187
691	246	2014-08-16	15.00		11	142
692	247	2014-08-16	70.00		11	102
693	248	2014-08-16	75.00		12	14
694	249	2014-08-16	75.00		12	6
695	250	2014-08-16	55.00		11	163
696	251	2014-08-16	65.00		11	77
697	252	2014-08-16	65.00		11	73
698	253	2014-08-16	50.00		11	82
699	254	2014-08-16	65.00		11	115
700	255	2014-08-16	20.00		11	190
701	256	2014-08-16	50.00		11	205
702	257	2014-08-16	50.00		11	66
703	258	2014-08-16	70.00		11	87
704	259	2014-08-16	60.00		12	29
705	260	2014-08-16	43.00		12	23
706	261	2014-08-16	70.00		12	33
707	262	2014-08-16	37.50		13	10
708	269	2014-08-16	35.00		11	27
709	270	2014-08-16	5.00		11	86
710	236	2014-08-16	75.00		11	206
711	237	2014-08-16	73.00		11	162
712	237.1	2014-08-16	73.00		11	160
713	237.2	2014-08-16	73.00		11	161
718	238	2014-08-16	75.00		11	207
719	238.1	2014-08-16	75.00		11	208
720	239	2014-08-16	10.00		11	22
722	272	2014-08-16	70.00		11	80
723	273	2014-08-16	20.00		11	142
724	274	2014-08-16	65.00		12	7
721	271	2014-08-16	70.00		11	195
726	281	2014-08-17	75.00		13	12
727	300	2014-09-04	20.00		12	20
728	301	2014-09-04	75.00		12	25
\.


--
-- Name: signup_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_payment_id_seq', 728, true);


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	logistics	0001_initial	2014-05-29 17:51:04.132161-06
2	logistics	0002_auto__del_generation__add_field_smallgroup_structure__chg_field_smallg	2014-05-29 17:51:04.134904-06
3	logistics	0003_auto__add_unique_smallgroup_title	2014-05-29 17:51:04.137056-06
4	logistics	0004_auto__chg_field_smallgroup_bus__chg_field_smallgroup_structure__chg_fi	2014-05-29 17:51:04.139157-06
5	signup	0001_initial	2014-05-29 17:51:04.152066-06
6	signup	0002_auto__add_field_counselor_generation__add_field_counselor_structure__a	2014-05-29 17:51:04.154569-06
7	signup	0003_auto__chg_field_counselor_generation__chg_field_camper_generation__chg	2014-05-29 17:51:04.156824-06
8	signup	0004_auto__add_unique_counselor_second_surname_first_surname_first_name_sec	2014-05-29 17:51:04.159203-06
9	signup	0005_auto__chg_field_counselor_second_surname__chg_field_camper_second_surn	2014-05-29 17:51:04.161368-06
10	signup	0006_auto__chg_field_payment_receipt_id	2014-05-29 17:51:04.163551-06
11	signup	0007_auto__chg_field_counselor_bus__chg_field_counselor_badge_name__chg_fie	2014-05-29 17:51:04.165717-06
12	signup	0008_auto__del_field_camper_docs_signed__add_field_camper_registrar_title__	2014-05-29 17:51:04.167866-06
13	signup	0009_auto__add_unique_payment_receipt_id	2014-05-29 17:51:04.170098-06
14	signup	0010_auto__add_field_camper_documents_ready	2014-05-29 17:51:04.172438-06
15	signup	0011_auto__del_field_camper_documents_ready__del_field_camper_perm_printed_	2014-05-29 17:51:04.174526-06
16	signup	0012_auto__del_field_camper_special_case	2014-05-29 17:51:04.176545-06
17	signup	0013_auto__add_field_camper_lawyer	2014-05-29 17:51:04.178528-06
18	finances	0001_initial	2014-05-29 17:51:04.190468-06
19	finances	0002_auto__add_field_budget_active	2014-05-29 17:51:04.192448-06
20	finances	0003_auto__del_budget__del_field_transaction_budget	2014-05-29 17:51:04.194738-06
21	finances	0004_auto__chg_field_transaction_origin__chg_field_transaction_destination_	2014-05-29 17:51:04.196935-06
22	finances	0005_auto__chg_field_transaction_transaction_id	2014-05-29 17:51:04.198947-06
23	finances	0006_auto__chg_field_transaction_origin__chg_field_transaction_destination_	2014-05-29 17:51:04.201173-06
24	finances	0007_auto__add_unique_transaction_transaction_id	2014-05-29 17:51:04.203003-06
25	signup	0014_auto__add_field_counselor_signed_up__add_field_camper_signed_up__add_f	2014-06-03 13:44:34.80784-06
\.


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 25, true);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: finances_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY finances_transaction
    ADD CONSTRAINT finances_transaction_pkey PRIMARY KEY (id);


--
-- Name: finances_transaction_transaction_id_uniq; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY finances_transaction
    ADD CONSTRAINT finances_transaction_transaction_id_uniq UNIQUE (transaction_id);


--
-- Name: logistics_smallgroup_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY logistics_smallgroup
    ADD CONSTRAINT logistics_smallgroup_pkey PRIMARY KEY (id);


--
-- Name: logistics_smallgroup_title_uniq; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY logistics_smallgroup
    ADD CONSTRAINT logistics_smallgroup_title_uniq UNIQUE (title);


--
-- Name: signup_camper_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_camper
    ADD CONSTRAINT signup_camper_pkey PRIMARY KEY (id);


--
-- Name: signup_camper_second_surname_775aa7ab6c60a9a_uniq; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_camper
    ADD CONSTRAINT signup_camper_second_surname_775aa7ab6c60a9a_uniq UNIQUE (second_surname, first_surname, first_name, second_name);


--
-- Name: signup_counselor_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_counselor
    ADD CONSTRAINT signup_counselor_pkey PRIMARY KEY (id);


--
-- Name: signup_counselor_second_surname_106e01f18eefbfe5_uniq; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_counselor
    ADD CONSTRAINT signup_counselor_second_surname_106e01f18eefbfe5_uniq UNIQUE (second_surname, first_surname, first_name, second_name);


--
-- Name: signup_counselor_small_group_id_key; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_counselor
    ADD CONSTRAINT signup_counselor_small_group_id_key UNIQUE (small_group_id);


--
-- Name: signup_guest_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_guest
    ADD CONSTRAINT signup_guest_pkey PRIMARY KEY (id);


--
-- Name: signup_guest_second_surname_21743c26046e2ab_uniq; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_guest
    ADD CONSTRAINT signup_guest_second_surname_21743c26046e2ab_uniq UNIQUE (second_surname, first_surname, first_name, second_name);


--
-- Name: signup_parent_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_parent
    ADD CONSTRAINT signup_parent_pkey PRIMARY KEY (id);


--
-- Name: signup_parent_second_surname_2a109ed0dea39ab8_uniq; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_parent
    ADD CONSTRAINT signup_parent_second_surname_2a109ed0dea39ab8_uniq UNIQUE (second_surname, first_surname, first_name, second_name);


--
-- Name: signup_payment_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_payment
    ADD CONSTRAINT signup_payment_pkey PRIMARY KEY (id);


--
-- Name: signup_payment_receipt_id_uniq; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY signup_payment
    ADD CONSTRAINT signup_payment_receipt_id_uniq UNIQUE (receipt_id);


--
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: campmanager; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_like; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_group_name_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_like; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX auth_user_username_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_like; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX django_session_session_key_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: signup_camper_counselor_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX signup_camper_counselor_id ON signup_camper USING btree (counselor_id);


--
-- Name: signup_camper_father_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX signup_camper_father_id ON signup_camper USING btree (father_id);


--
-- Name: signup_camper_mother_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX signup_camper_mother_id ON signup_camper USING btree (mother_id);


--
-- Name: signup_camper_small_group_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX signup_camper_small_group_id ON signup_camper USING btree (small_group_id);


--
-- Name: signup_payment_content_type_id; Type: INDEX; Schema: public; Owner: campmanager; Tablespace: 
--

CREATE INDEX signup_payment_content_type_id ON signup_payment USING btree (content_type_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_8e48ac9d; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_payment
    ADD CONSTRAINT content_type_id_refs_id_8e48ac9d FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_d043b34a; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_d043b34a FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: counselor_id_refs_id_f4105043; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_camper
    ADD CONSTRAINT counselor_id_refs_id_f4105043 FOREIGN KEY (counselor_id) REFERENCES signup_counselor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: father_id_refs_id_893a30d9; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_camper
    ADD CONSTRAINT father_id_refs_id_893a30d9 FOREIGN KEY (father_id) REFERENCES signup_parent(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_f4b32aac; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_f4b32aac FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: mother_id_refs_id_893a30d9; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_camper
    ADD CONSTRAINT mother_id_refs_id_893a30d9 FOREIGN KEY (mother_id) REFERENCES signup_parent(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: small_group_id_refs_id_5dce26c4; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_camper
    ADD CONSTRAINT small_group_id_refs_id_5dce26c4 FOREIGN KEY (small_group_id) REFERENCES logistics_smallgroup(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: small_group_id_refs_id_82ce3c39; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY signup_counselor
    ADD CONSTRAINT small_group_id_refs_id_82ce3c39 FOREIGN KEY (small_group_id) REFERENCES logistics_smallgroup(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_40c41112; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_40c41112 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_4dc23c39; Type: FK CONSTRAINT; Schema: public; Owner: campmanager
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_4dc23c39 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

