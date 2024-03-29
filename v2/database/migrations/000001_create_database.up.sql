-- Add new schema named "public"
CREATE SCHEMA IF NOT EXISTS "public";
-- Set comment to schema: "public"
COMMENT ON SCHEMA "public" IS 'standard public schema';
-- Create "quran_text_sura" table
CREATE TABLE "public"."quran_text_sura" ("index" integer NOT NULL, "name" character varying(20) NOT NULL, PRIMARY KEY ("index"), CONSTRAINT "quran_text_sura_index_check" CHECK (index >= 0));
-- Create index "quran_text_sura_name_281c3867_like" to table: "quran_text_sura"
CREATE INDEX "quran_text_sura_name_281c3867_like" ON "public"."quran_text_sura" ("name" varchar_pattern_ops);
-- Create index "quran_text_sura_name_key" to table: "quran_text_sura"
CREATE UNIQUE INDEX "quran_text_sura_name_key" ON "public"."quran_text_sura" ("name");
-- Create "quran_text_ayah" table
CREATE TABLE "public"."quran_text_ayah" ("id" serial NOT NULL, "number" integer NOT NULL, "text" text NOT NULL, "sura_id" integer NOT NULL, PRIMARY KEY ("id"), CONSTRAINT "quran_text_ayah_sura_id_46e9de77_fk_quran_text_sura_index" FOREIGN KEY ("sura_id") REFERENCES "public"."quran_text_sura" ("index") ON UPDATE NO ACTION ON DELETE NO ACTION, CONSTRAINT "quran_text_ayah_number_check" CHECK (number >= 0));
-- Create index "quran_text_ayah_number_sura_id_9df8698f_uniq" to table: "quran_text_ayah"
CREATE UNIQUE INDEX "quran_text_ayah_number_sura_id_9df8698f_uniq" ON "public"."quran_text_ayah" ("number", "sura_id");
-- Create index "quran_text_ayah_sura_id_46e9de77" to table: "quran_text_ayah"
CREATE INDEX "quran_text_ayah_sura_id_46e9de77" ON "public"."quran_text_ayah" ("sura_id");
-- Create "quran_tafseer_tafseer" table
CREATE TABLE "public"."quran_tafseer_tafseer" ("id" serial NOT NULL, "name" character varying(20) NOT NULL, "author" character varying(50) NOT NULL, "book_name" character varying(50) NOT NULL, "language" character varying(2) NOT NULL, PRIMARY KEY ("id"));
-- Create "quran_tafseer_tafseertext" table
CREATE TABLE "public"."quran_tafseer_tafseertext" ("id" serial NOT NULL, "text" text NOT NULL, "ayah_id" integer NOT NULL, "tafseer_id" integer NOT NULL, PRIMARY KEY ("id"), CONSTRAINT "quran_tafseer_tafsee_ayah_id_0750b184_fk_quran_tex" FOREIGN KEY ("ayah_id") REFERENCES "public"."quran_text_ayah" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION, CONSTRAINT "quran_tafseer_tafsee_tafseer_id_2d0a7f5e_fk_quran_taf" FOREIGN KEY ("tafseer_id") REFERENCES "public"."quran_tafseer_tafseer" ("id") ON UPDATE NO ACTION ON DELETE NO ACTION);
-- Create index "quran_tafseer_tafseertext_ayah_id_0750b184" to table: "quran_tafseer_tafseertext"
CREATE INDEX "quran_tafseer_tafseertext_ayah_id_0750b184" ON "public"."quran_tafseer_tafseertext" ("ayah_id");
-- Create index "quran_tafseer_tafseertext_tafseer_id_2d0a7f5e" to table: "quran_tafseer_tafseertext"
CREATE INDEX "quran_tafseer_tafseertext_tafseer_id_2d0a7f5e" ON "public"."quran_tafseer_tafseertext" ("tafseer_id");