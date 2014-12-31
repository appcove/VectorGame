--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: Main; Type: SCHEMA; Schema: -; Owner: VectorGame
--

CREATE SCHEMA "Main";


ALTER SCHEMA "Main" OWNER TO "VectorGame";

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = "Main", pg_catalog;

--
-- Name: Seq; Type: SEQUENCE; Schema: Main; Owner: VectorGame
--

CREATE SEQUENCE "Seq"
    START WITH 1026750
    INCREMENT BY 10
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Main"."Seq" OWNER TO "VectorGame";

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Player; Type: TABLE; Schema: Main; Owner: VectorGame; Tablespace: 
--

CREATE TABLE "Player" (
    "Player_MNID" integer DEFAULT nextval('"Seq"'::regclass) NOT NULL,
    "User_MNID" integer NOT NULL,
    "Name" character varying(32) NOT NULL,
    "Health" integer NOT NULL,
    "Location_Current" point,
    "Location_Next" point,
    "Color" character varying(16) NOT NULL
);


ALTER TABLE "Main"."Player" OWNER TO "VectorGame";

--
-- Name: User; Type: TABLE; Schema: Main; Owner: VectorGame; Tablespace: 
--

CREATE TABLE "User" (
    "User_MNID" integer DEFAULT nextval('"Seq"'::regclass) NOT NULL,
    "User_GSID" character varying(64) NOT NULL,
    "CreateDate" timestamp(6) with time zone DEFAULT now() NOT NULL,
    "FirstName" character varying(35) DEFAULT NULL::character varying NOT NULL,
    "LastName" character varying(35) DEFAULT NULL::character varying NOT NULL,
    "Email" character varying(100) DEFAULT NULL::character varying NOT NULL,
    "Phone" character varying(30) DEFAULT NULL::character varying NOT NULL,
    "Login_Username" character varying(40),
    "Login_Password_Hash" character varying(40) DEFAULT NULL::character varying,
    "Login_Password_Salt" character varying(60) DEFAULT NULL::character varying NOT NULL,
    "Perm_Active" boolean NOT NULL,
    "Perm_Super" boolean DEFAULT false NOT NULL
);


ALTER TABLE "Main"."User" OWNER TO "VectorGame";

--
-- Name: Player_pkey; Type: CONSTRAINT; Schema: Main; Owner: VectorGame; Tablespace: 
--

ALTER TABLE ONLY "Player"
    ADD CONSTRAINT "Player_pkey" PRIMARY KEY ("Player_MNID");


--
-- Name: User_GSID_Unique; Type: CONSTRAINT; Schema: Main; Owner: VectorGame; Tablespace: 
--

ALTER TABLE ONLY "User"
    ADD CONSTRAINT "User_GSID_Unique" UNIQUE ("User_GSID");


--
-- Name: User_Login_Username_Unique; Type: CONSTRAINT; Schema: Main; Owner: VectorGame; Tablespace: 
--

ALTER TABLE ONLY "User"
    ADD CONSTRAINT "User_Login_Username_Unique" UNIQUE ("Login_Username");


--
-- Name: User_pkey; Type: CONSTRAINT; Schema: Main; Owner: VectorGame; Tablespace: 
--

ALTER TABLE ONLY "User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY ("User_MNID");


--
-- Name: Player>>User; Type: FK CONSTRAINT; Schema: Main; Owner: VectorGame
--

ALTER TABLE ONLY "Player"
    ADD CONSTRAINT "Player>>User" FOREIGN KEY ("User_MNID") REFERENCES "User"("User_MNID") ON UPDATE CASCADE ON DELETE CASCADE;


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

