BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "maths_math" (
	"id"	integer NOT NULL,
	"operation"	varchar(5) NOT NULL,
	"a"	integer NOT NULL,
	"b"	integer NOT NULL,
	"created"	datetime NOT NULL,
	"result_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("result_id") REFERENCES "maths_result"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "maths_result" (
	"id"	integer NOT NULL,
	"value"	real UNIQUE,
	"error"	varchar(255) UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "posts_author" (
	"id"	integer NOT NULL,
	"nick"	varchar(15) NOT NULL,
	"email"	varchar(254) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "posts_post" (
	"id"	integer NOT NULL,
	"title"	varchar(50) NOT NULL,
	"content"	text NOT NULL,
	"created"	datetime NOT NULL,
	"modified"	datetime NOT NULL,
	"author_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("author_id") REFERENCES "posts_author"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2023-05-17 21:54:15.254002');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2023-05-17 21:54:15.282610');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2023-05-17 21:54:15.295884');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2023-05-17 21:54:15.309917');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2023-05-17 21:54:15.317899');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2023-05-17 21:54:15.337130');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2023-05-17 21:54:15.350437');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2023-05-17 21:54:15.364400');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2023-05-17 21:54:15.372408');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2023-05-17 21:54:15.385343');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2023-05-17 21:54:15.390311');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2023-05-17 21:54:15.398935');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2023-05-17 21:54:15.412862');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2023-05-17 21:54:15.425826');
INSERT INTO "django_migrations" VALUES (15,'auth','0010_alter_group_name_max_length','2023-05-17 21:54:15.437793');
INSERT INTO "django_migrations" VALUES (16,'auth','0011_update_proxy_permissions','2023-05-17 21:54:15.448793');
INSERT INTO "django_migrations" VALUES (17,'auth','0012_alter_user_first_name_max_length','2023-05-17 21:54:15.461736');
INSERT INTO "django_migrations" VALUES (18,'sessions','0001_initial','2023-05-17 21:54:15.472703');
INSERT INTO "django_migrations" VALUES (19,'maths','0001_initial','2023-05-20 08:55:39.957587');
INSERT INTO "django_migrations" VALUES (20,'maths','0002_alter_math_operation','2023-05-20 08:55:39.962610');
INSERT INTO "django_migrations" VALUES (21,'maths','0003_result_math_result','2023-05-20 21:09:56.808413');
INSERT INTO "django_migrations" VALUES (22,'posts','0001_initial','2023-05-20 21:41:30.180415');
INSERT INTO "django_migrations" VALUES (23,'maths','0004_alter_math_options','2023-05-29 21:48:23.631267');
INSERT INTO "auth_group_permissions" VALUES (1,1,40);
INSERT INTO "auth_group_permissions" VALUES (2,1,37);
INSERT INTO "auth_group_permissions" VALUES (3,1,38);
INSERT INTO "auth_group_permissions" VALUES (4,1,39);
INSERT INTO "auth_user_groups" VALUES (1,2,1);
INSERT INTO "django_admin_log" VALUES (1,'3','value: 5484.0 | error: None',1,'[{"added": {}}]',8,1,'2023-05-20 22:37:20.445075');
INSERT INTO "django_admin_log" VALUES (2,'4','id:4, a=6, b=914, op=mul',1,'[{"added": {}}]',7,1,'2023-05-20 22:37:22.654448');
INSERT INTO "django_admin_log" VALUES (3,'5','Post object (5)',3,'',10,1,'2023-05-22 11:42:10.261118');
INSERT INTO "django_admin_log" VALUES (4,'4','Post object (4)',3,'',10,1,'2023-05-22 11:42:10.266280');
INSERT INTO "django_admin_log" VALUES (5,'2','matematyk',1,'[{"added": {}}]',4,1,'2023-05-28 20:55:29.357881');
INSERT INTO "django_admin_log" VALUES (6,'1','authors',1,'[{"added": {}}]',3,1,'2023-05-29 21:23:23.303257');
INSERT INTO "django_admin_log" VALUES (7,'2','matematyk',2,'[{"changed": {"fields": ["Groups"]}}]',4,1,'2023-05-29 21:24:18.452928');
INSERT INTO "django_admin_log" VALUES (8,'3','mietek',1,'[{"added": {}}]',4,1,'2023-05-29 21:25:18.238748');
INSERT INTO "django_admin_log" VALUES (9,'3','mietek',2,'[]',4,1,'2023-05-29 21:27:11.890063');
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'auth','user');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'maths','math');
INSERT INTO "django_content_type" VALUES (8,'maths','result');
INSERT INTO "django_content_type" VALUES (9,'posts','author');
INSERT INTO "django_content_type" VALUES (10,'posts','post');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_math','Can add math');
INSERT INTO "auth_permission" VALUES (26,7,'change_math','Can change math');
INSERT INTO "auth_permission" VALUES (27,7,'delete_math','Can delete math');
INSERT INTO "auth_permission" VALUES (28,7,'view_math','Can view math');
INSERT INTO "auth_permission" VALUES (29,8,'add_result','Can add result');
INSERT INTO "auth_permission" VALUES (30,8,'change_result','Can change result');
INSERT INTO "auth_permission" VALUES (31,8,'delete_result','Can delete result');
INSERT INTO "auth_permission" VALUES (32,8,'view_result','Can view result');
INSERT INTO "auth_permission" VALUES (33,9,'add_author','Can add author');
INSERT INTO "auth_permission" VALUES (34,9,'change_author','Can change author');
INSERT INTO "auth_permission" VALUES (35,9,'delete_author','Can delete author');
INSERT INTO "auth_permission" VALUES (36,9,'view_author','Can view author');
INSERT INTO "auth_permission" VALUES (37,10,'add_post','Can add post');
INSERT INTO "auth_permission" VALUES (38,10,'change_post','Can change post');
INSERT INTO "auth_permission" VALUES (39,10,'delete_post','Can delete post');
INSERT INTO "auth_permission" VALUES (40,10,'view_post','Can view post');
INSERT INTO "auth_group" VALUES (1,'authors');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$600000$CuyRCzDUEvat9sUME2CbYZ$1UfUay15UjUnA+tIteDxVA4g7lmi3Mci+lNmqrL4Vqo=','2023-05-29 21:19:16.301116',1,'rpodn','','r.podnajmer@gmail.com',1,1,'2023-05-20 22:31:10.964112','');
INSERT INTO "auth_user" VALUES (2,'pbkdf2_sha256$600000$lPMtfwqHxBhZwWr5AZAmQn$uoXK5g4UoCA1NlJIERSNa/FeDcwl2v0bcoS6G+MxQlI=','2023-05-29 21:31:28.699918',0,'matematyk','','',0,1,'2023-05-28 20:55:28','');
INSERT INTO "auth_user" VALUES (3,'pbkdf2_sha256$600000$iqMAH6mKFUBZbhSVY75Ehu$rDfV3LJgzJauG+UbL46QRVoc04eQNHZ9q1A4n3dTnvw=','2023-05-29 21:32:13.911715',0,'mietek','','',0,1,'2023-05-29 21:25:17','');
INSERT INTO "django_session" VALUES ('mibmo58v79vsiiby1crci55qx16c81s6','.eJxVjEEOwiAQRe_C2hApCOjKGLeeoRmGQdCWJtCujHcXTWPS5bz_3rxYzTASO7HrA_J9YjtWaYQ0NOJ_5Fwo5QjFc5zGNvewzLFfKpU--WaJLXOAT8r-n7cqzyU5_lX4ulZ-mzwNl9XdPIhQY6s78p4USQpBIerg0HRSSNMOQ5YUarKhM0ZqDVaY4MAeJR7Iib0TkhR7fwBy00j6:1q0V78:cBj7A9_k-w6Euko1lTtuIoXtyUoDBayW_TeUot_IfVU','2023-06-03 22:31:50.922168');
INSERT INTO "django_session" VALUES ('wufri953gn0fzhczmyrcquy0z5p14p8m','.eJxVjMEOwiAQRP-FsyHCIqBH734D2V0WqRqalPZk_HfbpAc9zrw381YJl7mmpcuUhqwuyqjDb0fIT2kbyA9s91Hz2OZpIL0peqdd38Ysr-vu_h1U7HVdW8lZnICU4ph9IQ4WDIQ1BIni2EssNgTwHqMJhTCegU9C5kgGxKnPFxnwOM8:1q0opX:OCK7Vle1AvdhdbtCd-eePAeBbxDOdzwkHCc5O6OktK0','2023-06-04 19:34:59.680231');
INSERT INTO "django_session" VALUES ('pw4y8atvep8h9ckvlw1s0t86a4y0o16j','.eJxVjEEOwiAQRe_C2hBggLYu3XsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwkzgLI06_W8T04LoDumO9NZlaXZc5yl2RB-3y2oifl8P9OyjYy7e2frKaVXROpYENEDFYpKwBEwMgAbthcmrMZAmtchHBgTVep8yj9-L9AedfN_U:1q3k3g:HCa3GaDMmzcJjr7PUeJD2HRL0mFBO-FMBD_BAI2MU38','2023-06-12 21:05:40.207882');
INSERT INTO "django_session" VALUES ('th18shuga8varjet78rf3ue8ph9xnwm2','.eJxVjMEOwiAQRP-FsyHCIqBH734D2V0WqRqalPZk_HfbpAc9zrw381YJl7mmpcuUhqwuyqjDb0fIT2kbyA9s91Hz2OZpIL0peqdd38Ysr-vu_h1U7HVdW8lZnICU4ph9IQ4WDIQ1BIni2EssNgTwHqMJhTCegU9C5kgGxKnPFxnwOM8:1q3kGq:pBUNekN-28Nh8mpyxoCMfLaPUi7tUgJolaeEuFusxQU','2023-06-12 21:19:16.306154');
INSERT INTO "django_session" VALUES ('t1vym4atji7qziivr2d7jrhz9734sc5j','.eJxVjEEOwiAQRe_C2hBggLYu3XsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwkzgLI06_W8T04LoDumO9NZlaXZc5yl2RB-3y2oifl8P9OyjYy7e2frKaVXROpYENEDFYpKwBEwMgAbthcmrMZAmtchHBgTVep8yj9-L9AedfN_U:1q3kPA:VY3UJxaBQDZwrxjqrgTEyn1aAF2AazeM2cXNBpR4ecA','2023-06-12 21:27:52.115026');
INSERT INTO "django_session" VALUES ('peew8bjc3cxv4y8eoo062b1sx2jueg1i','.eJxVjMEOwiAQBf-FsyEUlgIevfsNhIVFqgaS0p5M_7026UGvb2beh_mwLsWvnWY_JXZlil1-NwzxRfUA6Rnqo_HY6jJPyA-Fn7Tze0v0vp3u30EJvXxrh8rQkNAiUYRBOBezFgDCWJmRjBYu2zFI0hmNAiQtBSYiGGNWYCzbdvOcOEU:1q3kTN:lVWAS4IR7dOSb63SSJ1w603PUOzBPprpvBa4Q_UWU5o','2023-06-12 21:32:13.918776');
INSERT INTO "maths_math" VALUES (1,'add',1,2,'2023-05-20 09:00:00.042000',2);
INSERT INTO "maths_math" VALUES (2,'sub',10,20,'2023-05-20 09:01:03.506000',NULL);
INSERT INTO "maths_math" VALUES (3,'div',11,2,'2023-05-20 09:02:24.834000',NULL);
INSERT INTO "maths_math" VALUES (4,'mul',6,914,'2023-05-20 22:37:22.643000',3);
INSERT INTO "maths_math" VALUES (5,'mul',88,88,'2023-05-21 09:50:56.501000',5);
INSERT INTO "maths_math" VALUES (6,'mul',88,88,'2023-05-21 11:30:16.813000',5);
INSERT INTO "maths_math" VALUES (7,'add',16,32,'2023-05-22 10:58:28.661000',6);
INSERT INTO "maths_math" VALUES (8,'sub',8,4,'2023-05-24 00:03:28.661000',4);
INSERT INTO "maths_math" VALUES (9,'div',100,50,'2023-05-22 00:06:44.661000',2);
INSERT INTO "maths_math" VALUES (10,'sub',32,2,'2023-05-22 00:11:32.581000',2);
INSERT INTO "maths_math" VALUES (11,'add',500,223,'2023-05-22 00:12:32.581000',5);
INSERT INTO "maths_math" VALUES (12,'sub',20,30,'2023-05-24 21:38:43.234245',10);
INSERT INTO "maths_math" VALUES (13,'add',1,2,'2023-05-26 22:47:48.113422',2);
INSERT INTO "maths_result" VALUES (1,NULL,'ZeroDivisionError');
INSERT INTO "maths_result" VALUES (2,3.0,NULL);
INSERT INTO "maths_result" VALUES (3,5484.0,NULL);
INSERT INTO "maths_result" VALUES (4,55.0,NULL);
INSERT INTO "maths_result" VALUES (5,7744.0,NULL);
INSERT INTO "maths_result" VALUES (6,48.0,NULL);
INSERT INTO "maths_result" VALUES (7,634.0,NULL);
INSERT INTO "maths_result" VALUES (8,16.0,NULL);
INSERT INTO "maths_result" VALUES (9,723.0,NULL);
INSERT INTO "maths_result" VALUES (10,-10.0,NULL);
INSERT INTO "posts_author" VALUES (1,'Ziemowit','ziemniak@grund.pl');
INSERT INTO "posts_author" VALUES (2,'andromeda','esmeralda@mamayao.su');
INSERT INTO "posts_author" VALUES (3,'maupa','maupa@djungla.pl');
INSERT INTO "posts_author" VALUES (4,'dziedziczka','czertoryska@hrabina.pl');
INSERT INTO "posts_post" VALUES (1,'czy można mieszać łyżką herbatę?','można, ale trzeba mieć dobrą łyżkę','2023-05-20 22:08:58.773360','2023-05-20 22:08:58.773360',1);
INSERT INTO "posts_post" VALUES (2,'jak wybrać dobrą łyżkę?','na stronie internetowej ziemowita','2023-05-20 22:11:34.692575','2023-05-20 22:12:28.139732',1);
INSERT INTO "posts_post" VALUES (3,'kupiłeś łyżkę? zrobiłeś to źle!111!','jak wyżej homo homini lyzkus nie ma takiej strony nie istnieje dobra łyżka do mieszkania poza światem zewnętrznym albowiem słowo przeciwko słowu a człowiek człowiekowi człowiek','2023-05-20 22:15:04.926227','2023-05-20 22:15:04.926227',2);
INSERT INTO "posts_post" VALUES (6,'karambol','na drodze krajowo życiowej','2023-05-22 11:43:20.682154','2023-05-22 11:43:20.682154',3);
INSERT INTO "posts_post" VALUES (7,'elo','pierwwszy post tego typu','2023-05-22 12:00:37.369427','2023-05-22 12:00:37.369427',4);
INSERT INTO "posts_post" VALUES (8,'asa','ala ma kota','2023-05-23 19:30:06.617119','2023-05-23 19:30:06.617119',3);
INSERT INTO "posts_post" VALUES (9,'asd','asdasad','2023-05-29 21:26:04.399302','2023-05-29 21:26:04.399302',1);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "maths_math_result_id_1f6fb015" ON "maths_math" (
	"result_id"
);
CREATE INDEX IF NOT EXISTS "posts_post_author_id_fe5487bf" ON "posts_post" (
	"author_id"
);
COMMIT;
