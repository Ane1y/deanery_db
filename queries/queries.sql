--Выборка данных
--вывод всех данных для каждой оценки

--•	однотабличная выборка:
--1.	Вывести все группы, упорядочив их в обратном порядке по году и в прямом порядке по наименованию.
SELECT * from GROUPS ORDER BY NAME DESC ASC;

SELECT * from GROUPS ORDER BY NAME;

--1.	Вывести число предметов, по которым есть оценки у группы, заданной по наименованию.
SELECT  Count(distinct SUBJECT_ID) FROM MARKS, people p, groups
WHERE P.GROUP_ID = (SELECT ID FROM GROUPS WHERE NAME = '3084/2_2018');

--•	соединение таблиц (join):

--1.	Вывести студентов и наименования предметов, включая предметы,
-- которые не читались студентам и студентов, которые не получили ни одной оценки.


SELECT  p.first_name, p.last_name, p.pather_name, s.name FROM MARKS M
        FULL JOIN PEOPLE P ON P.ID = M.STUDENT_ID
        LEFT JOIN GROUPS G ON G.ID = P.GROUP_ID
        FULL Join subject s on M.subject_id = s.id;

--2.	Вывести все группы и средний балл студентов каждой.
SELECT G.name, avg(COALESCE(value, 0)) FROM people p
    FULL JOIN marks m on p.id = m.student_id
    RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
GROUP BY G.id; -- если оценка не поставлена, считается за 0

--Hints: select, count, join, where, in, exists, order by, group by, having
--
--Вставка данных
--•	однотабличная вставка:
--1.	Добавить нового студента.
INSERT INTO people (first_name, last_name, pather_name, group_id, type)
VALUES ('Смирнов', 'Антон', 'Николаевич', 6, 'S');

DELETE from marks WHERE student_id = (SELECT id from people WHERE first_name = 'Смирнов' and last_name = 'Антон' and
        pather_name = 'Николаевич');
DELETE FROM PEOPLE WHERE first_name = 'Смирнов' and last_name = 'Антон' and
 pather_name = 'Николаевич';
--2.	Добавить оценку по некоторому предмету студенту из п.1.
INSERT INTO marks (student_id, subject_id, teacher_id, value)
VALUES ((SELECT id from People WHERE first_name = 'Смирнов' and
last_name = 'Антон' and pather_name = 'Николаевич'), 8, 2, 4);

--•	многотабличная вставка в рамках транзакции:
--1.	Создать копию заданной группы (со студентами) с увеличением курса на 1.
--нужно создать копию
BEGIN transaction ;
    INSERT INTO groups (name)
    VALUES ('4084/1_2018');
    UPDATE people SET group_id = (SELECT id from groups where name = '4084/1_2018')
    WHERE group_id = (SELECT id from groups where name = '3084/1_2018');
COMMIT transaction ;

--обратная транзакция
BEGIN transaction;
UPDATE people SET group_id = (SELECT id from groups where name = '3084/1_2018')
WHERE group_id = (SELECT id from groups where name = '4084/1_2018');
DELETE from groups where name = '4084/1_2018';
COMMIT transaction;

--2.	То же что п.1. Если группа с полученным наименованием уже существует – транзакцию откатить.
--поле name unique

--Hints: insert, where, in, exists, commit, rollback
--Удаление данных
--•	удаление по фильтру и удаление из связанных таблиц:
--1.	Удалить студентов, у которых средний балл ниже заданного.

SELECT G.name, avg(COALESCE(value, 0)) FROM people1 p
                                                FULL JOIN marks m on p.id = m.student_id
                                                RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
GROUP BY G.id; -- если оценка не поставлена, считается за 0

DELETE from People1 p
    where id in (Select id from (Select student_id as id, avg(COALESCE(value, 0)) as avg_mark from marks
        FULL JOIN people1 p2 on marks.student_id = p2.id
    GROUP BY student_id) as ia where avg_mark < 4);

--2.	Удалить заданную группу и студентов, принадлежащих ей.
--•	удаление в рамках транзакции:
--1.	Удалить в рамках транзакции группу с самым маленьким средним баллом и студентов,принадлежащих ей.
begin transaction ;
DELETE from groups1 where id in (Select id from (
    SELECT G.id as id, avg(COALESCE(value, 0)) as avg_mark FROM people p
    FULL JOIN marks m on p.id = m.student_id
    RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
GROUP BY G.id ORDER BY avg_mark
    Limit 1) as table_name
);
commit transaction ;

--2.	то же, что и п.1, но, если в удаленной группе читались 3 предмета – транзакцию откатить.
CREATE OR REPLACE FUNCTION deleteandcheckfor3subjects() RETURNS BOOLEAN AS $_$
Declare
    candidateondeleting integer;
BEGIN

    Select id from (SELECT G.id as id, avg(COALESCE(value, 0)) as avg_mark FROM people p
                    FULL JOIN marks m on p.id = m.student_id
                    RIGHT JOIN groups1 G ON G.ID = P.GROUP_ID
                    GROUP BY G.id ORDER BY avg_mark
                    Limit 1) as table_name into candidateondeleting;


    IF (Select subj_num from (SELECT group_id, count(distinct subject_id) as subj_num FROM groups1
                    LEFT JOIN people p on groups1.id = p.group_id
                    left join marks m on p.id = m.student_id
                              where groups1.id = candidateondeleting
                              group by group_id) as table_name) > 3
    THEN RAISE EXCEPTION 'в этой группе читалось 3 предмета'
        USING HINT = 'уверены что хотите удалить?';
    ELSE
        DELETE from groups1 where id = candidateondeleting;
        RETURN TRUE;
    END IF;
END $_$ LANGUAGE 'plpgsql';

SELECT * from deleteandcheckfor3subjects();

--Модификация данных
--•	модификация по фильтру:
--1.	Подменить заданную группу на другую.
UPDATE groups SET name = '3084/1_2021'
WHERE group_id = (SELECT id from groups where name = '3084/1_2018');
--отмена
UPDATE groups SET name = '3084/1_2018'
WHERE group_id = (SELECT id from groups where name = '3084/1_2021');

--•	модификация в рамках транзакции:

--1.	Заменить во всех существующих записях заданный предмет на другой и удалить этот предмет из таблицы предметов.
DO $do$
declare
    old_name  varchar(30) = 'Микропроцессоры';
    new_name varchar(30) = 'СУБД';
    old_id integer;
    new_id integer;

begin

Select id into old_id from subject where name = old_name;
Select id into new_id from subject where name = new_name;

update marks set subject_id = new_id where subject_id = old_id;
delete from subject where id = old_id;
END;
    $do$;

insert into subject (name) values ('Микропроцессоры');
update marks set subject_id = (Select id from subject where name = 'Микропроцессоры') where subject_id = (select id from subject where name = 'Схемотехника');
delete from subject where id = 11;


--2.	то же, что и п.1, но в случае, если преподаватель, читающий удаляемый предмет, больше ничего не читает – откатить транзакцию.
DROP function avoidDeletingTeachers(old_subject varchar, new_subject varchar);
CREATE OR REPLACE FUNCTION avoidDeletingTeachers(old_subject varchar(30), new_subject varchar(30))
                                                                            RETURNS BOOLEAN AS $_$
BEGIN
    create temp table if not exists curriculum1 as (SELECT teacher_id, subject_id FROM people p
        LEFT JOIN marks m on p.id = m.teacher_id
        LEFT JOIN subject s on m.subject_id = s.id
       GROUP BY teacher_id, subject_id); -- если оценка не поставлена, считается за 0

    if(select count(teacher_id) from curriculum1 where subject_id = (select id from subject where name = old_subject)) < 2
    then
        RAISE EXCEPTION 'этот предмет последний у преподователя'
            USING HINT = 'вы уверены?';
           ELSE
        insert into subject (name) values (new_subject);
        update marks set subject_id = (Select id from subject where name = new_subject)
        where subject_id = (select id from subject where name = old_subject);
        delete from subject where id = (select id from subject where name = old_subject);
    END IF;
    RETURN TRUE;

END $_$ LANGUAGE 'plpgsql';

select * from avoidDeletingTeachers('СУБД', 'БД');
--
--Hints: update, where, in, exists, commit, rollback


