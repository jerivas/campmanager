--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
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
    cabin character varying(16) NOT NULL
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
1	pbkdf2_sha256$12000$rmZHayexS4ei$Mhmx3oHGH29OV5Ccc9/ocs+8kSKc/h+ByMeHMb1s+Zw=	2014-05-29 20:32:06.441+00	t	jerivas	Eduardo	Rivas	e@jerivas.com	t	t	2013-05-29 18:23:50+00
3	pbkdf2_sha256$10000$5V8PwSkpRY0U$e1AaDTTHR7w76u7SOmi9xhvV/qEcQJ8zej5nGi3eotk=	2013-07-16 16:23:16+00	f	clari	Clarissa	Rodriguez		t	t	2013-06-02 03:15:56+00
4	pbkdf2_sha256$10000$WcOrxnEGbMut$NDmhxA+kYwWxPi2VyjaUeWVWxSw0Mg1/AUnwgnJmUlc=	2013-06-09 20:41:22+00	f	erik	Erik	Miranda		t	t	2013-06-02 03:17:04+00
5	pbkdf2_sha256$10000$dDM6IuCwWtqa$/c9AH1EzC+HLftaTlizpeIzeUW6390wQYx2Mw1XPSKY=	2013-08-01 15:28:23+00	f	ale	Ale	Durán		t	t	2013-06-02 03:17:32+00
6	pbkdf2_sha256$10000$rbz83N7UrAkF$wDzZPys+M3TRVNwtWMoKLhvnqDIZXKKmL7uvIaHnwgw=	2013-07-31 21:10:25+00	f	maricela	Maricela	de León		t	t	2013-06-02 03:18:23+00
7	pbkdf2_sha256$10000$UIjIub2rH21k$AIim9uk4x4iTUYVLjgUZw5bFzVi1nHMh6iPw2rtNUWU=	2013-08-02 06:01:55+00	f	ricardo	Ricardo	Medrano		t	t	2013-06-02 22:34:34+00
8	pbkdf2_sha256$10000$4YsOacIZl9M3$Unl83vJcWZmCYyqp1A7u8EDxWadx+gCKmHtwdjeCll8=	2013-08-02 03:53:54+00	f	mike	Mike	Guardado		t	t	2013-07-10 12:28:40+00
9	pbkdf2_sha256$10000$9odbORFWiW72$4mpnp8kF0/P21F2k/tGDrhUflFroDmNpW/9enuIwMjg=	2013-07-22 21:11:03+00	f	sarai	Saraí	Navarrete		t	t	2013-07-17 05:47:14+00
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
17	8	5
18	9	6
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 18, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('auth_user_id_seq', 9, true);


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
7	2014-05-30 00:02:23.414956+00	1	3	2	rebe	3	
8	2014-05-30 00:03:34.095102+00	1	10	4	Vicente Cruz García	2	Modificado/a first_name, first_surname y second_surname.
9	2014-05-30 00:03:53.207148+00	1	10	10	Blanca Gloria Elizabeth Salinas de Mata	2	Modificado/a known_as y occupation.
10	2014-05-30 00:04:21.454003+00	1	10	3	Sara Noemy Vásquz de Cruz	2	Modificado/a first_name, second_name, first_surname, second_surname y occupation.
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 10, true);


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
jaj5qhvkg0qxj6p7f5cfq89a5ak31evf	NDcwNDYwYzEwNDM1MDNjNzBmZGQ4ZTc2MWMwNWZiMjgzMmVjYzYzMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-12 20:32:06.452948+00
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
1	001	income	2013-06-02	152.25	Ofrendas	Ofrendas
2	002	income	2013-05-12	8.76	Ventas	Ventas
3	003	income	2013-06-16	46.98	Ofrendas	Ofrendas
4	004	income	2013-06-16	48.13	Ventas	Ventas
5	168	egress	2013-07-07	40.00	Inscripción	Comisión Migración
6	164	income	2013-07-07	3.00	Multa	Comisión Migración
7	114	income	2013-07-07	3.00	Multa	Comisión Migración
8	119	income	2013-07-07	3.00	Multa	Comisión Migración
9	165	income	2013-07-07	3.00	Multa	Comisión Migración
10	006	income	2013-07-07	16.50	Ofrendas	Ofrendas
11	007	income	2013-07-07	10.76	Ofrendas	Ofrendas
12	008	income	2013-07-07	242.00	Cine	Ventas
13	009	income	2013-07-14	21.43	Ofrendas	Ofrendas
14	010	egress	2013-07-17	177.00	Abonos	Pago de vuelo de predicador
15	011	egress	2013-07-14	60.00	Inscripción	Decoración
16	012	income	2013-07-14	3.00	Multa	Migración
17	014	income	2013-07-14	2.25	Multa	Migración
18	204	income	2013-07-17	3.00	Multa	Migración
19	224	egress	2013-07-21	60.00	Inscripción	Comisión Recreativa
21	127	income	2013-07-21	3.00	Multa	Comisión Migración
22	137 B	income	2013-07-21	3.00	Multa	Comisión Migración
23	208	income	2013-07-21	3.00	Multa	Comisión Migración
24	015	income	2013-07-21	33.25	Ofrendas	Ofrendas
25	016	egress	2013-07-18	3397.15	Inscripciones, ventas y ofrendas	Deposito en la iglesia
26	259	egress	2013-07-28	50.00	Inscripción	Comisión Logística
27	147	egress	2013-07-24	24.00	Multas	Comisión Migración
28	229	income	2013-07-24	3.00	Multa	Comisión Migración
29	234	egress	2013-07-24	244.00	Inscripción	Comisión carpeta y gafete
30	235	egress	2013-07-24	40.00	Inscripción	Comisión Decoración para cena especial
31	236	egress	2013-07-24	200.00	Inscripción	Comisión Migración Abogados
32	286	egress	2013-07-28	60.00	Inscripción	Comisión Nocturna
33	017	income	2013-07-28	38.70	Ofrendas	Presupuesto
34	018	income	2013-07-31	1000.00	Iglesia ayuda campamentos	Presupuesto
35	019	income	2013-07-31	60.00	Ofrenda Josias	Presupuesto
36	020	egress	2013-08-01	800.00	Inscripción	Buses
37	021	egress	2013-08-02	167.62	Ofrendas	Ayuda para pagos campamentos de jóvenes
38	022	egress	2013-08-02	100.00	Inscripción	Devolución Hnos. Paz
39	023	income	2013-08-02	182.25	La Red	Pago hospedaje de invitados
40	024	egress	2013-08-02	54.00	Inscripción	Migración
41	025	egress	2013-08-02	54.00	Inscripción	Migración
42	026	egress	2013-08-02	54.00	Inscripción	Migración pago abogados
43	002b	egress	2013-07-29	5807.89	Inscripción	Iglesia
\.


--
-- Name: finances_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('finances_transaction_id_seq', 43, true);


--
-- Data for Name: logistics_smallgroup; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY logistics_smallgroup (id, title, generation, cabin, bus, structure) FROM stdin;
1	Abiel	4	sinai	2	preju
2	Abiatar	4	sinai	3	preju
3	Eliana	3	koinonia1	2	preju
4	Samuel	5	moab	3	preju
5	Migdal	4	koinonia3	3	preju
6	Jesed	5	agape4	3	preju
7	Leví	6	nueva4	4	preju
8	Rabí	6	nueva4	4	preju
9	Déborah	6	agape3	4	preju
10	Bitia	5	agape4	4	preju
11	Yoel	5	moab	3	preju
12	Abdi	5	agape4	4	preju
13	Ithiel	4	koinonia3	3	preju
14	Ester	3	koinonia4	2	preju
15	Abdiel	3	gerizim	2	preju
16	Elyon	4	juda	2	preju
17	Mical	6	agape3	4	preju
18	Abigail	4	koinonia3	3	preju
19	Zabdi	3	koinonia4	2	preju
20	Jezreel	2	anakaino4	1	josias
26	Febe	2	anakaino4	1	josias
27	Kadisha	2	anakaino3	1	josias
28	Kyrios	2	horeb2	1	josias
29	Mati	2	horeb1	1	josias
30	Keilah	2	anakaino2	1	josias
31	Zuria	1	anakaino1	1	josias
32	Karmi	1	anakaino1	1	josias
33	Adriel	1	horeb1	1	josias
34	Manos	1	horeb1	1	josias
38	Uriel	3	gerizim	2	preju
39	Sabaoth	6	ebal	4	preju
\.


--
-- Name: logistics_smallgroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('logistics_smallgroup_id_seq', 39, true);


--
-- Data for Name: signup_camper; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_camper (id, first_name, second_name, first_surname, second_surname, gender, birth_date, state, province, occupation, balance, no_pay, badge_name, cabin, passport, birth_cert_num, birth_cert_fol, birth_cert_book, registrar, mother_id, father_id, counselor_id, generation, structure, bus, small_group_id, registrar_title, registrar_position, reg_state, reg_province, permission_status, lawyer) FROM stdin;
1	Jacqueline	Pamela	Rodríguez	Pineda	f	2000-03-25 22:19:00+00	lal	Santa Tecla	Estudiante	75.00	f	Pame	anakaino3	M00818435	246	248	3	MIGUEL ANGEL CRUZ LOPEZ	5	6	23	2	josias	1	27	m	subchief	sas	San Salvador	2	jorge
2	Adriana	Saraí	Vasquez  	Rodríguez	f	\N				75.00	f	Adri	anakaino3		\N	\N	\N		\N	\N	23	2	josias	1	27					0	
5	Alejandra	Estefany	Martínez	Orantes	f	\N				40.00	f	Mc´Ale	agape3		\N	\N	\N		\N	\N	10	6	preju	4	9					0	
7	Angélica	Yamileth	López	Pérez	f	\N				61.50	f	Angélica	koinonia1		\N	\N	\N		\N	\N	4	3	preju	2	3					0	
8	Diana	Saraí	Santos	Martir	f	\N				75.00	f	Diana	koinonia1		\N	\N	\N		\N	\N	4	3	preju	2	3					0	
9	Adriana	Elizabeth	Gutiérrez	Padilla	f	\N				38.00	f	Adriana	koinonia1		\N	\N	\N		\N	\N	4	3	preju	2	3					0	
10	Gustavo	Enrique	Chacón	Rodríguez	m	\N				75.00	f	Gustavo	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
12	Eugenia	Beatriz	Alvarado	Araujo	f	\N				75.00	f	Beatriz	anakaino1		\N	\N	\N		\N	\N	28	1	josias	1	32					0	
13	Guillermo	Arturo	Alvarado	Araujo	m	1998-08-18 14:05:00+00	sas	Cuscatancingo	Estudiante	75.00	f	Guille	sinai	M00707888	478	480	53	Jesus Douglas Henriquez Rodriguez	1	2	2	4	preju	3	2		subchief	sas	San Salvador	2	silvia
14	Andrea	de Jesús	Torres	Alas	f	\N				75.00	f	Mc´Andrea	agape3		\N	\N	\N		\N	\N	10	6	preju	4	9					0	
15	Marco	Stefano	Barrientos	Melgar	m	\N				75.00	f	Marco	moab		\N	\N	\N		\N	\N	5	5	preju	3	4					0	
16	María	José	Rivera	Recinos	f	\N				75.00	f	María	agape4		\N	\N	\N		\N	\N	7	5	preju	3	6					0	
17	Florence	Natalia	Perdomo	de la O	f	\N				75.00	f	Florence	agape4		\N	\N	\N		\N	\N	7	5	preju	3	6					0	
18	Adriana		Coello	Gómez	f	\N				75.00	f	Adri	koinonia4		\N	\N	\N		\N	\N	20	3	preju	2	19					0	
19	Francisco	Ariel	Linares	Melgar	m	\N				75.00	f	Ariel	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
20	Stephanie	Elizabeth	Ramos	Ramirez	f	\N				75.00	f	Elizabeth	anakaino1		\N	\N	\N		\N	\N	27	1	josias	1	31					0	
21	Roxana	Abigail	Comandari	Rodríguez	f	\N				5.00	f	Roxy	anakaino1		\N	\N	\N		\N	\N	28	1	josias	1	32					0	
22	Marcela	Alejandra	Mendoza	Orellana	f	\N				75.00	f	Marcela	anakaino1		\N	\N	\N		\N	\N	28	1	josias	1	32					0	
23	Karla	Tatiana	Duke	Monchez	f	\N				75.00	f	Karla	koinonia4		\N	\N	\N		\N	\N	15	3	preju	2	14					0	
24	Andrea	Lizzeth	Letona	Hernández	f	\N				75.00	f	Andrea	agape4		\N	\N	\N		\N	\N	13	5	preju	4	12					0	
25	Dalia	Marcela	Huezo	Pacheco	f	\N				75.00	f	Dalia	agape4		\N	\N	\N		\N	\N	13	5	preju	4	12					0	
26	Gloria	Evelia	Pérez	Girón	f	\N				75.00	f	Mc´Gloria	agape3		\N	\N	\N		\N	\N	10	6	preju	4	9					0	
27	Christian	Alessandro	Calderón	Castillo	m	\N				75.00	f	Christian	sinai		\N	\N	\N		\N	\N	2	4	preju	3	2					0	
28	Andrea	Carolina	Morales	Sosa	f	\N				75.00	f	Andrea	agape3		\N	\N	\N		\N	\N	18	6	preju	4	17					0	
30	Steven	José	Martínez	Márquez	m	\N				75.00	f	Steven	nueva4		\N	\N	\N		\N	\N	9	6	preju	4	8					0	
31	Erika	Marcela	Carias	Renderos	f	\N				75.00	f	Erika	agape3		\N	\N	\N		\N	\N	18	6	preju	4	17					0	
33	Gabriela	Nicole	Meléndez	Peñalba	f	\N				75.00	f	Mc´Gaby	agape3		\N	\N	\N		\N	\N	10	6	preju	4	9					0	
34	America	Alejandra	Moreno	Meléndez	f	\N				75.00	f	Mc´America	agape3		\N	\N	\N		\N	\N	10	6	preju	4	9					0	
35	Javier	Alfonso	Martínez	Portillo	m	\N				75.00	f	Alfonso	gerizim		\N	\N	\N		\N	\N	31	3	preju	2	38					0	
36	Gabriela	María	Melara	Rodríguez	f	\N				75.00	f	Gaby	agape4		\N	\N	\N		\N	\N	7	5	preju	3	6					0	
37	Raúl 	Ernesto	López	Hernández	m	\N				70.00	f	Raúl	juda		\N	\N	\N		\N	\N	17	4	preju	2	16					0	
38	Laura	Celina	Gil	Henríquez	f	\N				75.00	f	Laurita	koinonia4		\N	\N	\N		\N	\N	15	3	preju	2	14					0	
39	Marlon	Edgardo	Figueroa	Martínez	m	\N				75.00	f	Marlon	gerizim		\N	\N	\N		\N	\N	31	3	preju	2	38					0	
40	Andrés	Gerardo	López	Guevara	m	\N				75.00	f	Andrés	horeb1		\N	\N	\N		\N	\N	29	1	josias	1	33					0	
41	Ludwing	Alfredo	Contreras	Menjívar	m	\N				75.00	f	Lud	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
42	Katherine	Haydee	Contreras	Menjívar	f	\N				75.00	f	Katherine	agape4		\N	\N	\N		\N	\N	7	5	preju	3	6					0	
43	Natalia	Daniela	González	Tobar	f	\N				75.00	f	Naty	koinonia4		\N	\N	\N		\N	\N	15	3	preju	2	14					0	
44	Yohalmo	Obdulio	Pérez	De León	m	\N				10.00	f	Yohalmo	sinai		\N	\N	\N		\N	\N	2	4	preju	3	2					0	
45	Doris	Esmeralda	Alfaro 	Castillo	f	\N				75.00	f	Esmi	anakaino3		\N	\N	\N		\N	\N	23	2	josias	1	27					0	
46	Katherine	Rebeca	Medrano	Guerrero	f	\N				75.00	f	Rebe	anakaino4		\N	\N	\N		\N	\N	21	2	josias	1	20					0	
47	Astrid	Margarita	Hernández	Villacorta	f	\N				75.00	f	Astrid	koinonia1		\N	\N	\N		\N	\N	4	3	preju	2	3					0	
48	Ivy	Vanessa	Gutiérrez	Padilla	f	\N				75.00	f	Ivy	anakaino1		\N	\N	\N		\N	\N	28	1	josias	1	32					0	
49	Jonathan 	Eliud	Ayala	Serrano	m	\N				75.00	f	Jonathan	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
50	Everth	Ariel	Sánchez	Barrientos	m	\N				5.00	f	Everth	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
51	Angela	Berenice	Soriano	Beltrán	f	\N				75.00	f	Mc´Angiie	agape3		\N	\N	\N		\N	\N	10	6	preju	4	9					0	
52	Jorge 	Daniel	Cruz	Vásquez	m	2001-02-17 04:50:00+00	sas	Tonacatepeque	Estudiante	50.00	f	Jorge	horeb1	M00623981	113	\N	\N	RAFAEL ANTONIO RIVAS QUINTANILLA	3	4	29	1	josias	1	33	m	chief	sas	Ilopango	2	jorge
53	Jonathan	Alexander	Arteaga	Segovia	f	\N				75.00	f	Jonathan	juda		\N	\N	\N		\N	\N	17	4	preju	2	16					0	
54	David	Godofredo	Campos 	Aguilar	m	\N				75.00	f	David	horeb1		\N	\N	\N		\N	\N	30	1	josias	1	34					0	
55	Jorge	Antonio	Campos	Miranda	m	\N				75.00	f	Jorge	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
56	Julieta	Elizabeth	Ponce	Martir	f	\N				75.00	f	Julieta	koinonia4		\N	\N	\N		\N	\N	20	3	preju	2	19					0	
57	Sara	Eunice	Arteaga	Funes	f	\N				35.00	f	Sarita	koinonia3		\N	\N	\N		\N	\N	19	4	preju	3	18					0	
58	Nicole	Jasmin	Mata	Salinas	f	1997-09-23 13:40:00+00	lal	Antiguo Cuscatlán	Estudiante	5.00	f	Nicole	agape4	A50130681	84	86	62	Donaldo Francisco Salazar Ruballo	10	11	11	5	preju	4	10	m	subchief	sas	San Salvador	2	jorge
59	David	Josué	Mejía		m	\N				75.00	f	Josue	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
60	Alejandra	Guadalupe	Cruz	Vásquez	f	\N				50.00	f	Alejandra	koinonia4		\N	\N	\N		\N	\N	15	3	preju	2	14					0	
61	Andrea	Fernanda	Matínez	González	f	\N				75.00	f	Andrea	anakaino2		\N	\N	\N		\N	\N	26	2	josias	1	30					0	
63	Roberto	Benjamín	Coello	Gómez	m	\N				75.00	f	Roberto	moab		\N	\N	\N		\N	\N	12	5	preju	3	11					0	
64	Luis	Hernán 	Orellana	Reyes	m	\N				75.00	f	Luis	horeb1		\N	\N	\N		\N	\N	25	2	josias	1	29					0	
65	Mauricio	Javier	Castellón	Cerritos	m	\N				20.00	f	Mauri	gerizim		\N	\N	\N		\N	\N	31	3	preju	2	38					0	
66	Emely	Nohemi	Sevillano	Platero	f	1998-11-26 10:30:00+00	sas	Soyapango	Estudiante	75.00	f	Emely	koinonia4	A50022654	326	326	77	Juan Jose Armando Azucena Catan	7	8	20	3	preju	2	19	m	chief	sas	San Salvador	2	jorge
67	Melvin	Alexi	Pérez	Pérez	m	\N				75.00	f	Alexi	horeb1		\N	\N	\N		\N	\N	25	2	josias	1	29					0	
68	Cristian	Alexis	Amaya	Cortéz	m	\N				55.00	f	Cristian	juda		\N	\N	\N		\N	\N	17	4	preju	2	16					0	
69	Rolando 	Javier	Guardado	Alvarado	m	\N				5.00	f	Rolando	sinai		\N	\N	\N		\N	\N	2	4	preju	3	2					0	
70	Adriana	María 	Rodríguez	Monge	f	\N				75.00	f	Adri	koinonia3		\N	\N	\N		\N	\N	14	4	preju	3	13					0	
71	Jonathan	Eduardo	Hernández	Díaz	m	\N				5.00	f	Jonathan	juda		\N	\N	\N		\N	\N	17	4	preju	2	16					0	
72	Josué	 Alejandro	Pérez	Linares	m	\N				75.00	f	Josué	sinai		\N	\N	\N		\N	\N	2	4	preju	3	2					0	
73	Carmen	Elena	Yanes	Peña	f	\N				75.00	f	Carmen	koinonia1		\N	\N	\N		\N	\N	4	3	preju	2	3					0	
74	José	Luis	Arriola	Villalta	m	\N				75.00	f	Jose Luis	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
75	Marcelo	José	Dominguez	Toledo	m	\N				75.00	f	Marcelo	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
76	Mónica	Gabriela	Hernández	Villacorta	f	\N				75.00	f	Monica	agape4		\N	\N	\N		\N	\N	11	5	preju	4	10					0	
77	Raúl 	David	Yanes	Peña	m	\N				75.00	f	Raul	moab		\N	\N	\N		\N	\N	5	5	preju	3	4					0	
78	Carmen	Patricia	Sánchez	García	f	\N				75.00	f	Carmen	koinonia3		\N	\N	\N		\N	\N	6	4	preju	3	5					0	
79	Alexia	Rosibel	Ochoa	González	f	\N				70.00	f	Alexia	anakaino1		\N	\N	\N		\N	\N	27	1	josias	1	31					0	
80	Evelyn	Janet	Trinidad	García	f	\N				75.00	f	Evelyn	koinonia3		\N	\N	\N		\N	\N	6	4	preju	3	5					0	
81	Carlos 	Raúl	Dominguez	Hernández	m	\N				60.00	f	Carlos Raul	gerizim		\N	\N	\N		\N	\N	31	3	preju	2	38					0	
82	Alejandra	Poulette	Montalvo	Meza	f	\N				70.00	f	Poulette	anakaino1		\N	\N	\N		\N	\N	28	1	josias	1	32					0	
83	Miguel	Alejandro	Soriano	Beltrán	m	\N				75.00	f	Ale	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
84	Raúl 	Alexander	Mata	Peña	m	\N				75.00	f	Raul	moab		\N	\N	\N		\N	\N	5	5	preju	3	4					0	
85	Bianca		Gavidia		f	\N				65.00	f	Bianca	koinonia3		\N	\N	\N		\N	\N	6	4	preju	3	5					0	
86	Carlos	Ernesto	Medrano	Guerrero	m	\N				75.00	f	Neto	moab		\N	\N	\N		\N	\N	5	5	preju	3	4					0	
87	Alejandra	Maria	Burgos		f	\N				75.00	f	Burgos	koinonia4		\N	\N	\N		\N	\N	15	3	preju	2	14					0	
88	Elvin	Abdonel	De León	De León	m	\N				75.00	f	Elvin	nueva4		\N	\N	\N		\N	\N	8	6	preju	4	7					0	
89	Carlos	Rodrigo	Cornejo	González	m	\N				50.00	f	Carlos Rodrigo	sinai		\N	\N	\N		\N	\N	1	4	preju	2	1					0	
90	Luis	Alonso	Chavarría	Rivera	m	\N				75.00	f	Luis	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
91	Rene	Rafael	Campos	Fernández	m	\N				50.00	f	Rene	moab		\N	\N	\N		\N	\N	12	5	preju	3	11					0	
92	Gloria	María	Campos	Fernández	f	\N				50.00	f	Glo	agape4		\N	\N	\N		\N	\N	7	5	preju	3	6					0	
93	Ricardo	Alberto	Meléndez	Bertrán	m	\N				75.00	f	Ricardo	nueva4		\N	\N	\N		\N	\N	9	6	preju	4	8					0	
94	Cinthya	Gissellie	Pineda 	Bonilla	f	\N				75.00	f	Cinthya	koinonia3		\N	\N	\N		\N	\N	19	4	preju	3	18					0	
95	Paola	Gabriela	Magaña	Peña	f	\N				75.00	f	Paola	koinonia1		\N	\N	\N		\N	\N	4	3	preju	2	3					0	
96	Ana	Margarita	Santamaría	Hernández	f	\N				75.00	f	Anita	koinonia4		\N	\N	\N		\N	\N	15	3	preju	2	14					0	
97	Danilo	Alejandro	Vega	Hernández	m	\N				75.00	f	Danilo	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
98	Alessandra	Jeanneth	Vega	Hernández	f	\N				75.00	f	Alessandra	koinonia4		\N	\N	\N		\N	\N	20	3	preju	2	19					0	
99	Cristian	Alexander	Ayala	Serrano	m	\N				75.00	f	Cristian	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
100	Margareth	Rachelle	Escamilla	Zuniga	f	\N				75.00	f	Rachelle	anakaino4		\N	\N	\N		\N	\N	22	2	josias	1	26					0	
101	Daniel	Andrés	Bonilla	Montes	m	\N				75.00	f	Dany	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
102	William	Rodrigo	Huezo	Orantes	m	\N				75.00	f	Rodrigo	sinai		\N	\N	\N		\N	\N	1	4	preju	2	1					0	
103	Carlos	Eduardo 	Escobar	Iraheta	m	\N				75.00	f	Carlos	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
104	Rafael	Andrés	Huezo	Huezo	m	\N				75.00	f	Rafa	ebal		\N	\N	\N		\N	\N	32	6	preju	4	39					0	
105	Josué	David	Lainez	Castro	m	\N				75.00	f	Josué	moab		\N	\N	\N		\N	\N	12	5	preju	3	11					0	
106	Karla	Jeanette	Gutierrez	Tejada	f	\N				75.00	f	Mc'Karla	agape3		\N	\N	\N		\N	\N	10	6	preju	4	9					0	
107	Diego	Andrés	Velado	Peñate	m	\N				50.00	f	Diego	sinai		\N	\N	\N		\N	\N	1	4	preju	2	1					0	
108	Melany	Sofia	Bonilla	Beltrán	m	\N				75.00	f	Melany	anakaino2		\N	\N	\N		\N	\N	26	2	josias	1	30					0	
109	Rodrigo	Eduardo	Zelaya	Fuentes	m	\N				75.00	f	Rodrigo	moab		\N	\N	\N		\N	\N	12	5	preju	3	11					0	
110	Rodrigo	Alberto	Martinez	Renderos	m	\N				75.00	f	Rodrigo	horeb2		\N	\N	\N		\N	\N	24	2	josias	1	28					0	
111	Josué	David	Rivas	Cruz	m	\N				75.00	f	Josué	nueva4		\N	\N	\N		\N	\N	9	6	preju	4	8					0	
112	Astrid	Nicolle	Rivas	Cruz	f	\N				75.00	f	Nicolle	koinonia3		\N	\N	\N		\N	\N	14	4	preju	3	13					0	
114	David	Gonzalo	Castillo	Dimas	m	\N				5.00	f	Gonzo	juda		\N	\N	\N		\N	\N	17	4	preju	2	16					0	
115	Nicole	Azucena	Barahona	Castro	f	\N				55.00	f	Nicole	koinonia4		\N	\N	\N		\N	\N	20	3	preju	2	19					0	
116	Josué	Israel	Guevara	Aguilar	m	2001-08-20 17:29:00+00	sas	San Salvador	Estudiante	70.00	f	Josué	horeb1	A50026996	221	223	44	Juan Jose Armando Azucena Catan	9	\N	29	1	josias	1	33	m	chief	sas	San Salvador	0	jorge
119	Irina	Lucia	Orantes	Regalado	f	\N				75.00	f	Lucia	koinonia4		\N	\N	\N		\N	\N	15	3	preju	2	14					0	
120	Eduardo	Enrique	Herrera		m	\N				75.00	f	Eduardo	sinai		\N	\N	\N		\N	\N	2	4	preju	3	2					0	
121	Débora	Michelle	Pérez	Castillo	m	\N				75.00	f	Debbie	koinonia4		\N	\N	\N		\N	\N	20	3	preju	2	19					0	
122	Edi	Lineth	Caseros	Cubias	f	\N				75.00	f	Titi	koinonia1		\N	\N	\N		\N	\N	4	3	preju	2	3					0	
123	Jessica	Estelisa	Lemus	Alas	f	\N				75.00	f	Jessica	koinonia3		\N	\N	\N		\N	\N	19	4	preju	3	18					0	
124	Reina	Dolores	Barrera	Mijango	f	\N				5.00	f	Reina	agape4		\N	\N	\N		\N	\N	11	5	preju	4	10					0	
125	Emilio	Armando	Aguilar	Obando	m	\N				75.00	f	Emilio	gerizim		\N	\N	\N		\N	\N	16	3	preju	2	15					0	
126	Alejandro	Alfredo	Ochoa	Gómez	m	\N				75.00	f	Alejandro	gerizim		\N	\N	\N		\N	\N	16	3	preju	2	15					0	
127	Diego	Alfredo	Ochoa	Gómez	m	\N				75.00	f	Diego	gerizim		\N	\N	\N		\N	\N	16	3	preju	2	15					0	
128	Carlos 	Samuel	Flores	Olivares	m	\N				75.00	f	Samu	horeb1		\N	\N	\N		\N	\N	25	2	josias	1	29					0	
129	Aldo	Andrés	Palacios	Escamilla	m	\N				75.00	f	Andrés	moab		\N	\N	\N		\N	\N	5	5	preju	3	4					0	
131	Vanessa	Pamela	Huezo	Orantes	f	\N				75.00	f	VPHuezo	agape3		\N	\N	\N		\N	\N	18	6	preju	4	17					0	
132	Catherine	Irene	Pérez	Cader	f	\N				75.00	f	Cath	agape3		\N	\N	\N		\N	\N	18	6	preju	4	17					0	
133	Nelson	Jonathan	Cárcamo	Cuestas	m	\N				75.00	f	Jonathan	nueva4		\N	\N	\N		\N	\N	9	6	preju	4	8					0	
134	Josue	Ariel 	Umanzor		m	\N				75.00	f	Ariel	moab		\N	\N	\N		\N	\N	5	5	preju	3	4					0	
135	Ernesto	Alexander	Figueroa	Dominguez	m	\N				75.00	f	Alex	horeb1		\N	\N	\N		\N	\N	29	1	josias	1	33					0	
136	Carlos		Salazar		m	\N				75.00	f	Carlos	gerizim		\N	\N	\N		\N	\N	16	3	preju	2	15					0	
137	Mónica 	María	Morales	Bonilla	f	\N				75.00	f	Mónica	koinonia3		\N	\N	\N		\N	\N	19	4	preju	3	18					0	
138	Karen	Paola	Morales	Bonilla	f	\N				75.00	f	Paola	koinonia3		\N	\N	\N		\N	\N	19	4	preju	3	18					0	
\.


--
-- Name: signup_camper_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_camper_id_seq', 138, true);


--
-- Data for Name: signup_counselor; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_counselor (id, first_name, second_name, first_surname, second_surname, gender, balance, no_pay, badge_name, cabin, small_group_id, generation, structure, bus) FROM stdin;
1	José	Eduardo	Rivas	Melgar	m	75.00	f	Choche	sinai	1	4	preju	2
2	José	David	Nery	Maravilla	m	75.00	f	Nery	sinai	2	4	preju	3
4	María	Alejandra	Durán	Castellanos	f	75.00	f	Ale	koinonia1	3	3	preju	2
5	Ricardo	Josué	Medrano	Guerrero	m	10.00	f	Ricardo	moab	4	5	preju	3
6	Gloria	Raquel	González	Galdamez	f	75.00	f	Raque	koinonia3	5	4	preju	3
7	Andrea	Saraí	Navarrete	Pérez	f	75.00	f	Saraí	agape4	6	5	preju	3
8	Daniel	Alfonso	Nery	Maravilla	m	75.00	f	Nery	nueva4	7	6	preju	4
9	Andrés	Fabricio	Larios	Revelo	m	10.00	f	Andrés	nueva4	8	6	preju	4
10	Nelly	Rebeca	Romero	Sánchez	f	75.00	f	Mc´Rebe	agape3	9	6	preju	4
11	Laura	Patricia	Santillana	Meléndez	f	5.00	f	Laura	agape4	10	5	preju	4
12	Jacob	Benjamín	Zelaya	Chicas	m	75.00	f	Jake	moab	11	5	preju	3
13	Elisa	Imelda	Echegoyén	Díaz	f	75.00	f	Elisa	agape4	12	5	preju	4
14	Griselda	Beatriz	Martínez	Cornejo	f	55.00	f	Gris	koinonia3	13	4	preju	3
15	Jacqueline	Beatriz	Aquino	Fuentes	f	75.00	f	Jacqui	koinonia4	14	3	preju	2
16	Milton	Josué	Méndez	Alfaro	m	75.00	f	Méndez	gerizim	15	3	preju	2
17	Miguel	Antonio	Guardado	Salmerón	m	70.00	f	Mike	juda	16	4	preju	2
18	Jacqueline	Andrea	Romero	Vanegas	f	45.00	f	Andrea	agape3	17	6	preju	4
19	Pamela	Alejandra	Chacón	Rodríguez	f	75.00	f	Pame	koinonia3	18	4	preju	3
20	Maricela	Nohemy	Flores	de León	f	75.00	f	Maricela	koinonia4	19	3	preju	2
21	Clarissa	Esmeralda	Rodriguez	Monge	f	75.00	f	Clari	anakaino4	20	2	josias	1
22	Ruth	Abigail	Méndez	Alfaro	f	75.00	f	Abby	anakaino4	26	2	josias	1
23	Priscila	Saraí	Sevillano	Platero	f	75.00	f	Priscy	anakaino3	27	2	josias	1
24	Christian	Steve	Domínguez	Vallecillos	m	75.00	f	Tivi	horeb2	28	2	josias	1
25	Erik	Emmanuel	Miranda	Hernández	m	75.00	f	Erik	horeb1	29	2	josias	1
26	Imelda	Margarita	Aguilar	Palma	f	36.00	f	Margarita	anakaino2	30	2	josias	1
27	Karen	Noemi	López	Dimas	f	75.00	f	Karen	anakaino1	31	1	josias	1
28	Sara	Carolina	Moreno	Sandoval	f	75.00	f	Sarita	anakaino1	32	1	josias	1
29	René	Moisés	Sevillano	Platero	m	25.00	f	René	horeb1	33	1	josias	1
30	Oliver	Stanley	Larín	Aguirre	m	75.00	f	Oliver	horeb1	34	1	josias	1
31	Geovanny	Ernesto	Lainez	Castro	m	0.00	f	Geo	gerizim	38	3	preju	2
32	Marcos	Alejandro Alberto	Martínez	Morales	m	54.00	f	Marcos	ebal	39	6	preju	4
\.


--
-- Name: signup_counselor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_counselor_id_seq', 32, true);


--
-- Data for Name: signup_guest; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_guest (id, first_name, second_name, first_surname, second_surname, gender, balance, no_pay, badge_name, cabin) FROM stdin;
1	Javier	Ernesto	Santillana	Meléndez	m	30.00	f	Javo	
2	Mauricio	Alberto	Paz	Herrera	m	75.00	f	Mou	
3	Juliana		Paz	(Madre)	f	75.00	f		
4	Juliana		Paz		f	75.00	f		
5	Mauricio		Paz	(Padre)	m	75.00	f		
6	Grisel	Abigail	González	Galdamez	f	75.00	f	Aby	
7	Lilian		Herrera	de Esperanza	f	54.00	f	Lily de Hope	
8	Juan 	Ramón	Esperanza		f	54.00	f	Juan Ra	
\.


--
-- Name: signup_guest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_guest_id_seq', 8, true);


--
-- Data for Name: signup_parent; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_parent (id, first_name, second_name, first_surname, second_surname, gender, birth_date, state, province, occupation, gov_id, known_as) FROM stdin;
1	Ana	Mercedes	Araujo	de Alvarado	f	1965-10-13 06:00:00+00	sas	Cuscatancingo	Empleada	02106986-5	
2	Carlos	Arturo	Alvarado	Valencia	m	1966-08-29 06:00:00+00	sas	Cuscatancingo	Empleado	01596605-9	
5	Paula	Maritza	Pineda	de Rodriguez	f	1961-11-18 06:00:00+00	lal	Santa Tecla	Ingeniera Quimica	02738005-7	
6	Jorge	Dante	Rodriguez	Pineda	m	1954-08-15 06:00:00+00	lal	Santa Tecla	Ingeniero Civil	01664314-1	
7	Marta	Luz	Platero	de Sevillano	f	1968-04-29 06:00:00+00	sas	Soyapango	Contador	00975440-2	
8	Rene	Moises	Sevillano	Martinez	m	1966-12-25 06:00:00+00	sas	Soyapango	Empleado	00058806-6	
9	Marta	Celia	Guevara	Aguilar	f	1976-03-12 06:00:00+00	sas	San Salvador	Cosmetóloga	03061993-6	
11	Salvador		Mata	Iraheta	m	1967-08-08 06:00:00+00	lal	Antiguo Cuscatlán	Ingeniero Industrial	02830060-2	
4	Vicente		Cruz	García	m	1956-08-09 06:00:00+00	sas	Tonacatepeque	Comerciante	01697230-4	
10	Blanca	Gloria Elizabeth	Salinas	de Mata	f	1963-01-12 06:00:00+00	lal	Antiguo Cuscatlán	Licenciada en Idioma Inglés	02428318-3	
3	Sara	Noemy	Vásquz	de Cruz	f	1976-09-25 06:00:00+00	sas	Tonacatepeque	Modista	02025969-5	
\.


--
-- Name: signup_parent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_parent_id_seq', 11, true);


--
-- Data for Name: signup_payment; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY signup_payment (id, receipt_id, payment_date, amount, notes, content_type_id, object_id) FROM stdin;
24	001	2013-05-26	5.00		11	1
25	002	2013-05-26	10.00		11	2
28	005	2013-06-02	40.00		11	5
30	007	2013-06-02	5.00		11	7
31	008	2013-06-02	5.00		11	8
32	009	2013-06-02	5.00		11	9
33	010	2013-06-02	5.00		11	10
35	006	2013-06-02	5.00		12	7
36	011	2013-06-02	5.00		12	24
37	004	2013-05-26	15.00		12	22
38	003	2013-05-26	5.00		12	23
39	013	2013-06-02	5.00		11	12
40	014	2013-06-02	5.00		11	13
41	016	2013-06-05	5.00		11	14
42	015	2013-06-02	10.00		13	1
43	017	2013-06-09	15.00		11	8
44	018	2013-06-09	5.00		11	15
45	019	2013-06-09	5.00		11	16
46	020	2013-06-09	5.00		11	17
47	021	2013-06-09	5.00		11	18
48	022	2013-06-09	10.00		11	19
49	041	2013-06-09	5.00		11	20
50	042	2013-06-09	75.00		13	2
51	043	2013-06-09	5.00		11	21
52	044	2013-06-16	20.00		12	22
53	045	2013-06-16	5.00		12	30
54	046	2013-06-16	10.00		12	16
55	081	2013-06-16	10.00		11	22
56	082	2013-06-16	5.00		11	23
57	083	2013-06-16	5.00		11	24
58	084	2013-06-16	5.00		11	25
59	023	2013-06-16	75.00		12	10
60	024	2013-06-16	5.00		11	26
61	025	2013-06-16	5.00		11	27
62	026	2013-06-16	5.00		11	28
64	028	2013-06-16	70.00		11	15
65	029	2013-06-16	30.00		11	30
66	030	2013-06-16	20.00		11	31
68	032	2013-06-16	5.00		11	33
69	033	2013-06-16	5.00		11	34
70	034	2013-06-16	20.00		12	20
71	035	2013-06-16	5.00		11	35
72	036	2013-06-16	5.00		11	36
73	037	2013-06-16	20.00		11	37
74	038	2013-06-16	10.00		11	38
75	039	2013-06-16	5.00		11	39
76	012	2013-06-02	5.00		11	40
77	085	2013-06-19	50.00		11	41
78	086	2013-06-19	50.00		11	42
79	040	2013-06-19	5.00		11	43
80	047	2013-06-23	30.00		12	18
81	048	2013-06-23	55.00		11	8
82	049	2013-06-23	10.00		11	44
83	050	2013-06-23	16.00		11	45
84	051	2013-06-23	5.00		11	46
85	052	2013-06-23	5.00		11	47
86	053	2013-06-23	5.00		11	48
87	054	2013-06-23	5.00	Marcos debe los $5.00	11	49
88	055	2013-06-23	5.00	Marcos debe los $5.00	11	50
89	056	2013-06-23	60.00		11	23
90	057	2013-06-23	20.00		13	1
91	058	2013-06-23	5.00		11	51
92	059	2013-06-23	5.00		11	52
93	060	2013-06-23	75.00		11	53
94	061	2013-06-23	5.00		11	54
95	062	2013-06-23	5.00		11	55
96	063	2013-06-23	5.00		11	56
97	064	2013-06-23	35.00		11	57
98	065	2013-06-23	5.00		11	58
99	066	2013-06-23	5.00	Falta segundo apellido, consultar!	11	59
100	067	2013-06-23	28.00		11	36
101	068	2013-06-23	5.00		11	60
102	069	2013-06-23	5.00		11	61
104	071	2013-06-23	70.00		11	18
105	072	2013-06-23	75.00		11	63
106	073	2013-06-23	5.00		11	64
107	074	2013-06-23	20.00		11	65
108	075	2013-06-23	10.00		12	27
109	076	2013-06-23	5.00		11	66
110	077	2013-06-26	5.00	los otros $5.00 para Rene Sevillano	11	67
111	078	2013-06-26	5.00		11	68
112	079	2013-06-30	5.00		12	2
113	080	2013-06-30	5.00		11	69
114	087	2013-06-30	5.00		11	70
115	088	2013-06-30	5.00		11	71
116	139	2013-07-21	75.00		11	72
117	090	2013-06-30	5.00		11	73
118	091	2013-06-30	5.00		11	74
119	092	2013-06-30	20.00		11	75
120	093	2013-06-30	70.00		11	47
121	094	2013-06-30	75.00		11	76
122	095	2013-06-30	50.00		11	26
123	096	2013-06-30	5.00		11	77
124	097	2013-06-30	20.00		11	78
125	098	2013-06-30	20.00		11	79
126	107	2013-06-30	5.00		11	79
127	099	2013-06-30	30.00		11	19
128	100	2013-06-30	5.00		11	80
129	101	2013-06-30	40.00		11	81
130	102	2013-06-30	35.00		11	61
131	103	2013-06-30	5.00		11	82
132	104	2013-06-30	45.00	Cheque de $50.00 le devolví $5.00 vuelto 	11	30
133	105	2013-06-30	5.00		11	83
134	106	2013-06-30	5.00		11	84
135	108	2013-06-30	30.00		11	27
136	109	2013-06-30	5.00	Falta el nombre completo	11	85
137	121	2013-06-30	5.00		11	86
138	123	2013-06-30	5.00		11	87
139	125	2013-06-30	10.00		11	88
140	122	2013-06-30	10.00		11	23
141	124	2013-06-30	20.00		11	24
142	110	2013-07-07	10.00		11	89
143	111	2013-07-07	5.00		11	90
144	112	2013-07-07	25.00		11	91
145	113	2013-07-07	5.00	Verificar nombre de gafete	11	92
146	115	2013-07-07	15.00		11	93
147	116	2013-07-07	5.00		11	94
148	117	2013-07-07	5.00		11	95
149	118	2013-07-07	20.00		11	96
150	120	2013-07-07	70.00		11	97
151	161	2013-07-07	70.00		11	98
152	162	2013-07-07	20.00		11	99
153	163	2013-07-07	5.00		11	100
154	166	2013-07-07	5.00		11	101
155	167	2013-07-07	5.00	$5.00 para andres del agape	11	102
156	170	2013-07-07	10.00		11	103
157	171	2013-07-07	25.00		11	104
158	203	2013-07-17	50.00		11	105
159	172	2013-07-10	25.00		11	42
160	173	2013-07-10	25.00		11	41
161	174	2013-07-14	75.00		11	106
162	175	2013-07-14	5.00		12	19
163	176	2013-07-14	5.00		11	107
164	177	2013-07-14	75.00		12	1
165	178	2013-07-14	35.00		11	61
166	179	2013-07-14	5.00		11	108
167	180	2013-07-14	36.00		12	26
168	181	2013-07-14	5.00		11	109
169	182	2013-07-14	20.00		11	110
170	183	2013-07-14	60.00		11	111
171	184	2013-07-14	40.00		11	112
172	185	2013-07-14	15.00		11	70
174	187	2013-07-14	40.00		11	82
175	188	2013-07-14	30.00		12	17
176	189	2013-07-14	5.00		11	114
177	190	2013-07-14	5.00		11	115
178	191	2013-07-14	20.00		11	116
181	194	2013-07-14	15.00		11	27
182	196	2013-07-14	55.00		11	96
183	197	2013-07-14	5.00		11	119
184	198	2013-07-14	65.00		11	103
185	199	2013-07-14	70.00		11	49
186	200	2013-07-14	55.00		11	99
187	201	2013-07-14	5.00		12	5
188	202	2013-07-14	5.00		11	120
189	241	2013-07-14	5.00		11	121
190	242	2013-07-14	20.00		11	60
191	243	2013-07-14	10.00		11	89
192	245	2013-07-14	70.00		11	43
193	247	2013-07-17	25.00		12	15
194	169	2013-07-07	20.00		11	66
195	126	2013-07-21	75.00		11	122
196	128	2013-07-21	5.00		11	123
197	129	2013-07-21	20.00		11	14
198	130	2013-07-21	70.00		11	51
199	131	2013-07-21	5.00		11	124
200	132	2013-07-21	5.00		12	11
201	133	2013-07-21	75.00		11	125
202	134	2013-07-21	5.00		11	126
203	135	2013-07-21	5.00		11	127
204	136	2013-07-21	45.00		11	24
205	137	2013-07-21	75.00		11	128
206	138	2013-07-21	35.00		11	119
207	140	2013-07-21	20.00		11	52
208	141 A	2013-07-21	75.00		13	3
209	141 C	2013-07-21	75.00		13	4
210	141 B	2013-07-21	75.00		13	5
211	142	2013-07-21	5.00		11	129
212	143	2013-07-21	55.00		11	38
214	249	2013-07-21	50.00		11	70
215	250	2013-07-21	50.00		12	14
216	205	2013-07-21	10.00		12	4
217	206	2013-07-21	30.00		11	121
218	207	2013-07-21	10.00		12	9
219	209	2013-07-21	5.00		13	6
220	210	2013-07-21	70.00		11	90
221	211	2013-07-21	70.00		11	102
222	212	2013-07-21	75.00		11	131
223	213	2013-07-21	5.00		11	132
224	214	2013-07-21	10.00		12	25
225	215	2013-07-21	35.00		11	31
226	216	2013-07-21	33.00		11	9
227	217	2013-07-21	65.00		11	22
228	218	2013-07-21	70.00		11	17
229	219	2013-07-21	50.00		12	15
230	220	2013-07-21	15.00		11	82
231	221	2013-07-21	70.00		11	1
232	222	2013-07-21	45.00		11	92
233	223	2013-07-21	25.00		11	91
234	225	2013-07-21	40.00		12	21
235	226	2013-07-21	70.00		12	30
236	227	2013-07-21	18.00		12	7
237	228	2013-07-21	75.00		12	28
238	144	2013-07-21	60.00		11	133
241	252	2013-07-28	55.00		11	75
242	253	2013-07-28	70.00		11	127
243	254	2013-07-28	70.00		11	126
244	255	2013-07-28	75.00		11	134
245	256	2013-07-28	55.00		12	20
246	257	2013-07-28	30.00		11	89
247	258	2013-07-28	32.00		11	36
248	260	2013-07-28	75.00		12	13
249	261	2013-07-28	70.00		11	77
250	262	2013-07-28	70.00		11	73
251	263	2013-07-28	70.00		11	84
252	264	2013-07-28	70.00		11	95
253	265	2013-07-28	40.00		11	110
254	145	2013-07-24	70.00		11	13
255	146	2013-07-24	70.00		11	12
256	148	2013-07-28	70.00		12	2
257	149	2013-07-28	70.00		11	87
258	150	2013-07-28	40.00		11	121
259	151	2013-07-28	50.00		11	14
260	152	2013-07-28	75.00		12	8
261	153	2013-07-28	70.00		11	34
262	154	2013-07-28	70.00		11	33
263	155	2013-07-28	15.00		11	111
264	156	2013-07-28	35.00		11	112
265	157	2013-07-28	40.00		12	17
266	158	2013-07-28	70.00		11	123
267	159	2013-07-28	38.27		11	80
268	160	2013-07-28	60.00		11	93
269	230	2013-07-28	50.00		11	104
270	231	2013-07-28	35.00		11	19
271	232	2013-07-24	70.00		11	20
272	233	2013-07-24	40.00		11	107
274	238	2013-07-28	15.00		11	110
275	239	2013-07-28	70.00		11	64
276	240	2013-07-28	70.00		11	48
277	266	2013-07-28	70.00		11	108
278	267	2013-07-28	75.00		11	135
279	268	2013-07-28	54.00		13	7
280	268b	2013-07-28	54.00		13	8
281	269	2013-07-28	10.00		11	38
282	270	2013-07-28	70.00		11	28
283	271	2013-07-28	70.00		11	56
284	272	2013-07-28	5.00		11	24
285	273	2013-07-28	37.50		11	7
286	274	2013-07-28	55.00		11	78
287	275	2013-07-28	70.00		11	25
288	031	2013-07-28	5.00	este recibo era de la inscripcion de Marcela Baracath	11	31
289	186A	2013-07-28	15.00	este recibo era de Alejandra Cisneros de $30.00- $15.00 para Erika y $15.00 Andrea Romero	11	31
290	186B	2013-07-28	15.00	este recibo era de Marcela Baracath de $30.00. $15.00 para erika Carias y $15.00 para Andrea	12	18
291	276	2013-07-29	59.00		11	45
292	277	2013-07-29	35.00		11	119
293	278	2013-07-29	70.00		11	59
294	279	2013-07-29	75.00	Confirmar ágape y nombre completo	11	136
295	280	2013-07-29	70.00		11	67
297	282	2013-07-29	75.00		11	137
298	282b	2013-07-28	75.00		11	138
299	283	2013-07-28	50.00		11	115
300	284	2013-07-28	70.00		11	94
301	285	2013-07-28	5.00		12	29
302	287	2013-07-28	10.00		11	81
303	288	2013-07-28	70.00		11	16
304	289	2013-07-28	50.00		11	2
305	290	2013-07-28	20.00		11	86
306	291	2013-07-28	70.00		12	19
307	292	2013-07-28	70.00		11	10
308	293	2013-07-28	70.00		11	129
309	294	2013-07-28	70.00		11	83
310	295	2013-07-28	70.00		11	74
311	296	2013-07-28	5.00		11	70
312	297	2013-07-28	35.00		12	21
313	298	2013-07-28	20.00		11	26
314	299	2013-07-28	70.00		11	54
315	300	2013-07-28	45.00		11	79
316	302	2013-07-28	70.00		11	109
317	303	2013-07-28	65.00		12	27
318	304	2013-07-28	70.00		11	40
319	305	2013-07-28	15.00		12	16
320	306	2013-07-28	30.00		12	22
321	307	2013-07-28	70.00		11	101
322	308	2013-07-28	70.00		11	120
323	309	2013-07-28	25.00		11	27
324	310	2013-07-28	50.00		11	86
325	311	2013-07-28	70.00		11	132
326	312	2013-07-28	50.00		11	46
327	313	2013-07-28	25.00		11	105
328	314	2013-07-28	15.00		11	133
330	316	2013-07-28	20.00		11	46
331	317	2013-07-28	50.00		12	23
332	318	2013-07-28	5.00		12	29
334	320	2013-07-28	5.00		11	97
336	330	2013-07-28	15.00		11	2
337	331	2013-07-28	5.00		11	98
338	321	2013-07-28	70.00		12	24
339	315	2013-07-28	5.00		11	66
340	319	2013-07-28	5.00		11	66
341	052b	2013-07-31	50.00		11	37
342	053b|	2013-07-31	70.00		11	35
343	54b	2013-07-31	70.00		11	100
344	55b	2013-07-31	10.00		11	81
345	056b	2013-07-31	50.00		12	16
346	057b	2013-07-31	10.00		12	22
347	58b	2013-07-31	75.00		12	6
348	59b	2013-07-31	70.00		13	6
349	322	2013-07-31	70.00		11	39
350	325	2013-07-31	19.00		11	7
351	324	2013-07-31	75.00		12	12
352	323	2013-07-31	65.00		12	4
353	328	2013-08-01	50.00		11	116
354	329	2013-08-01	10.00		11	82
355	060b	2013-07-31	25.00		11	52
356	061b	2013-07-31	25.00		11	60
357	062b	2013-07-31	65.00		12	25
358	063b	2013-07-31	70.00		11	55
359	064b	2013-07-31	5.00		12	14
360	065b	2013-07-31	65.00		11	88
361	066b	2013-07-31	50.00		11	68
362	067b	2013-07-31	10.00		11	36
363	248	2013-08-01	5.00		12	5
364	237	2013-08-01	10.00		12	23
365	193	2013-08-01	5.00		12	23
366	192	2013-08-01	5.00		12	23
367	077b	2013-08-01	5.00		12	29
368	070	2013-08-01	5.00		12	29
369	027	2013-08-01	5.00		12	29
370	167b	2013-08-01	5.00	$5.00 de Rodrigo Huezo	11	107
371	332b	2013-08-02	40.00		11	66
372	400	2013-07-31	5.00		11	85
373	401	2013-08-02	55.00		11	85
374	402	2013-08-02	31.73		11	80
375	403	2013-08-02	52.00		12	7
376	404	2013-08-02	54.00		12	32
\.


--
-- Name: signup_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('signup_payment_id_seq', 376, true);


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: campmanager
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	logistics	0001_initial	2014-05-29 23:51:04.132161+00
2	logistics	0002_auto__del_generation__add_field_smallgroup_structure__chg_field_smallg	2014-05-29 23:51:04.134904+00
3	logistics	0003_auto__add_unique_smallgroup_title	2014-05-29 23:51:04.137056+00
4	logistics	0004_auto__chg_field_smallgroup_bus__chg_field_smallgroup_structure__chg_fi	2014-05-29 23:51:04.139157+00
5	signup	0001_initial	2014-05-29 23:51:04.152066+00
6	signup	0002_auto__add_field_counselor_generation__add_field_counselor_structure__a	2014-05-29 23:51:04.154569+00
7	signup	0003_auto__chg_field_counselor_generation__chg_field_camper_generation__chg	2014-05-29 23:51:04.156824+00
8	signup	0004_auto__add_unique_counselor_second_surname_first_surname_first_name_sec	2014-05-29 23:51:04.159203+00
9	signup	0005_auto__chg_field_counselor_second_surname__chg_field_camper_second_surn	2014-05-29 23:51:04.161368+00
10	signup	0006_auto__chg_field_payment_receipt_id	2014-05-29 23:51:04.163551+00
11	signup	0007_auto__chg_field_counselor_bus__chg_field_counselor_badge_name__chg_fie	2014-05-29 23:51:04.165717+00
12	signup	0008_auto__del_field_camper_docs_signed__add_field_camper_registrar_title__	2014-05-29 23:51:04.167866+00
13	signup	0009_auto__add_unique_payment_receipt_id	2014-05-29 23:51:04.170098+00
14	signup	0010_auto__add_field_camper_documents_ready	2014-05-29 23:51:04.172438+00
15	signup	0011_auto__del_field_camper_documents_ready__del_field_camper_perm_printed_	2014-05-29 23:51:04.174526+00
16	signup	0012_auto__del_field_camper_special_case	2014-05-29 23:51:04.176545+00
17	signup	0013_auto__add_field_camper_lawyer	2014-05-29 23:51:04.178528+00
18	finances	0001_initial	2014-05-29 23:51:04.190468+00
19	finances	0002_auto__add_field_budget_active	2014-05-29 23:51:04.192448+00
20	finances	0003_auto__del_budget__del_field_transaction_budget	2014-05-29 23:51:04.194738+00
21	finances	0004_auto__chg_field_transaction_origin__chg_field_transaction_destination_	2014-05-29 23:51:04.196935+00
22	finances	0005_auto__chg_field_transaction_transaction_id	2014-05-29 23:51:04.198947+00
23	finances	0006_auto__chg_field_transaction_origin__chg_field_transaction_destination_	2014-05-29 23:51:04.201173+00
24	finances	0007_auto__add_unique_transaction_transaction_id	2014-05-29 23:51:04.203003+00
\.


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: campmanager
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 24, true);


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

