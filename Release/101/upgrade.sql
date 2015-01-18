--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: Pello; Type: SCHEMA; Schema: -; Owner: VectorGame
--

CREATE SCHEMA "Pello";


ALTER SCHEMA "Pello" OWNER TO "VectorGame";

SET search_path = "Pello", pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Board; Type: TABLE; Schema: Pello; Owner: VectorGame; Tablespace: 
--

CREATE TABLE "Board" (
    "Board_GSID" character varying(16) NOT NULL,
    "User_MNID" integer,
    "CreateDate" timestamp(6) with time zone DEFAULT now() NOT NULL,
    "CreateAddr" character varying(128) NOT NULL,
    "Name" character varying(64) NOT NULL
);


ALTER TABLE "Pello"."Board" OWNER TO "VectorGame";

--
-- Name: Task; Type: TABLE; Schema: Pello; Owner: VectorGame; Tablespace: 
--

CREATE TABLE "Task" (
    "Task_MNID" integer DEFAULT nextval('"Main"."Seq"'::regclass) NOT NULL,
    "Board_GSID" character varying(16) NOT NULL,
    "Name" character varying(255) NOT NULL,
    "Position" point,
    "Color" character varying(16),
    "Size" integer,
    "Note" text
);


ALTER TABLE "Pello"."Task" OWNER TO "VectorGame";

--
-- Data for Name: Board; Type: TABLE DATA; Schema: Pello; Owner: VectorGame
--

COPY "Board" ("Board_GSID", "User_MNID", "CreateDate", "CreateAddr", "Name") FROM stdin;
\.


--
-- Data for Name: Task; Type: TABLE DATA; Schema: Pello; Owner: VectorGame
--

COPY "Task" ("Task_MNID", "Board_GSID", "Name", "Position", "Color", "Size", "Note") FROM stdin;
\.


--
-- Name: Board_pkey; Type: CONSTRAINT; Schema: Pello; Owner: VectorGame; Tablespace: 
--

ALTER TABLE ONLY "Board"
    ADD CONSTRAINT "Board_pkey" PRIMARY KEY ("Board_GSID");


--
-- Name: Task_pkey; Type: CONSTRAINT; Schema: Pello; Owner: VectorGame; Tablespace: 
--

ALTER TABLE ONLY "Task"
    ADD CONSTRAINT "Task_pkey" PRIMARY KEY ("Task_MNID");


--
-- Name: Board_Board_GSID_key; Type: INDEX; Schema: Pello; Owner: VectorGame; Tablespace: 
--

CREATE UNIQUE INDEX "Board_Board_GSID_key" ON "Board" USING btree ("Board_GSID");


--
-- Name: Task>>Board; Type: FK CONSTRAINT; Schema: Pello; Owner: VectorGame
--

ALTER TABLE ONLY "Task"
    ADD CONSTRAINT "Task>>Board" FOREIGN KEY ("Board_GSID") REFERENCES "Board"("Board_GSID") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

