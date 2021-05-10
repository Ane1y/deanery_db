select current_database()


CREATE TABLE SUBJECT
( ID       integer     not null
      constraint "SUBJECT_PK"
          primary key,
  NAME VARCHAR(50));

CREATE TABLE GROUPS
( ID       integer     not null
      constraint "GROUPS_PK"
          primary key,
  NAME VARCHAR(50)
);

CREATE TABLE PEOPLE
( ID       integer     not null
      constraint "PEOPLE_PK"
          primary key,
  FIRST_NAME VARCHAR(30),
  LAST_NAME VARCHAR(30),
  PATHER_NAME VARCHAR(30),
  GROUP_ID integer references GROUPS not null,
  TYPE CHAR
);


CREATE TABLE MARKS
(ID       integer     not null
     constraint "MARKS_PK"
         primary key,
  STUDENT_ID integer references PEOPLE NOT NULL,
  SUBJECT_ID integer references SUBJECT NOT NULL,
  TEACHER_ID integer references PEOPLE NOT NULL
);

INSERT INTO GROUPS (name)
VALUES ('3084/1_2018');

INSERT INTO GROUPS (name)
VALUES ('3084/2_2018');
INSERT INTO GROUPS (name)
VALUES ('1084/1_2020');
INSERT INTO GROUPS (name)
VALUES ('1084/2_2020');
INSERT INTO GROUPS (name)
VALUES ('2084/1_2019');
INSERT INTO GROUPS (name)
VALUES ('2084/2_2019');


INSERT INTO SUBJECT (name)
VALUES ('Цифровая обработка сигналов');
INSERT INTO SUBJECT (name)
VALUES ('Микропроцессоры');
INSERT INTO SUBJECT (name)
VALUES ('СУБД');
INSERT INTO SUBJECT (name)
VALUES ('Физика');
INSERT INTO SUBJECT (name)
VALUES ('Высшая математика');



Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Борисов','Антон','Алексеевич',null,'P');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Кротов','Леонид','Петрович',null,'P');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Мохаев','Константин','Александрович',null,'P');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Сямочкин','Анатолий','Григорьевич',null,'P');

Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Петрова','Антонина','Александровна','1','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Краснов','Валерий','Александрович','1','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Замакова','Зарина','Алексеевна','1','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Гурьев', 'Аким', 'Станиславович', '1','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Овчинников', 'Леонтий', 'Протасьевич', '1','S');

Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Артемьева', 'Октябрина', 'Руслановна', '2','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Большаков', 'Евдоким', 'Еремеевич','2','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Пономарёв', 'Гавриил', 'Демьянович','2','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Лыткин', 'Валерий', 'Феликсович','2','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Киселёв', 'Святослав', 'Тимофеевич','2','S');

Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Мартынов', 'Ким', 'Владимирович', '3','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Васильев', 'Глеб', 'Федотович','3','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Васильева', 'Серафима', 'Альбертовна','3','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Ширяева', 'Харитина', 'Романовна','3','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Герасимова', 'Мартина', 'Романовна','3','S');

Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Кудряшова', 'Элина', 'Дмитриевна', '4','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Иванкова', 'Дарьяна', 'Григорьевна','4','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Максимов', 'Лазарь', 'Семёнович','4','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Крюкова', 'Розалия', 'Игнатьевна','4','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Смирнов', 'Игорь', 'Антонинович','4','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Игнатьева', 'Анна', 'Еремеевна','5','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Мишина', 'Любовь', 'Фроловна','5','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Уварова', 'Дарья', 'Филипповна','5','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Яковлев', 'Роман', 'Еремеевич', '5','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Самсонов', 'Орест', 'Ильяович', '5','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Ильин', 'Иннокентий', 'Павлович', '5','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Артемьев', 'Руслан', 'Вениаминович', '6','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Максимов', 'Василий', 'Русланович', '6','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Фомин', 'Модест', 'Евгеньевич', '6','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Игнатьев', 'Родион', 'Сергеевич', '6','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Филиппов', 'Ростислав', 'Анатольевич', '6','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Селиверстов', 'Мартын', 'Викторович', '6','S');
Insert into PEOPLE (FIRST_NAME,LAST_NAME,PATHER_NAME,GROUP_ID,TYPE)
values ('Гусев', 'Юрий', 'Валерьянович', '6','S');


INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (6, 2, 2, 5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (6, 3, 3, 5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (6, 4, 4, 4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (6, 5, 5, 5);

INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (7, 2, 2, 4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (7, 3, 3, 3);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (7, 4, 4, 4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (7, 5, 5, 4);

INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (8, 2, 2, 5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (8, 3, 3, 5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (8, 4, 4, 4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (8, 5, 5, 4);

INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (9, 2, 2, 3);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (9, 3, 3,3);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (9, 4, 4, 3);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (9, 5, 5, 4);

INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (10, 2, 2, 5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (10, 3, 3,5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (10, 4, 4, 5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (10, 5, 5, 5);

INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (11, 2, 2, 4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (11, 3, 3,5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (11, 4, 4, 5);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (11, 5, 5, 4);

INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (12, 2, 2, 4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (12, 3, 3,4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (12, 4, 4, 4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (12, 5, 5, 4);

INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (38, 2, 2, 3);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (38, 3, 3,4);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (38, 4, 4, 3);
INSERT INTO MARKS(STUDENT_ID, SUBJECT_ID, TEACHER_ID, VALUE)
values (38, 5, 5, 3);


create table curriculum
(
    id serial not null
        constraint "curriculum_pk"
        primary key ,
    subject_id integer not null
        constraint curriculum_subject_fkey
            references subject,
    teacher_id integer not null
        constraint curriculum_people_fkey
            references people
);
