--������� ������
--����� ���� ������ ��� ������ ������

--�	������������� �������:
--1.	������� ��� ������, ���������� �� � �������� ������� �� ���� � � ������ ������� �� ������������.
SELECT * from GROUPS ORDER BY NAME DESC ASC;

SELECT * from GROUPS ORDER BY NAME;

--1.	������� ����� ���������, �� ������� ���� ������ � ������, �������� �� ������������.
SELECT  Count(distinct SUBJECT_ID) FROM MARKS, people p, groups
WHERE P.GROUP_ID = (SELECT ID FROM GROUPS WHERE NAME = '3084/2_2018');

--�	���������� ������ (join):

--1.	������� ��������� � ������������ ���������, ������� ��������,
-- ������� �� �������� ��������� � ���������, ������� �� �������� �� ����� ������.


SELECT  p.first_name, p.last_name, p.pather_name, s.name FROM MARKS M
        FULL JOIN PEOPLE P ON P.ID = M.STUDENT_ID
        LEFT JOIN GROUPS G ON G.ID = P.GROUP_ID
        FULL Join subject s on M.subject_id = s.id;

--2.	������� ��� ������ � ������� ���� ��������� ������.
SELECT G.name, avg(COALESCE(value, 0)) FROM people p
    FULL JOIN marks m on p.id = m.student_id
    RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
GROUP BY G.id; -- ���� ������ �� ����������, ��������� �� 0

--Hints: select, count, join, where, in, exists, order by, group by, having
--
--������� ������
--�	������������� �������:
--1.	�������� ������ ��������.
INSERT INTO people (first_name, last_name, pather_name, group_id, type)
VALUES ('�������', '�����', '����������', 6, 'S');

DELETE from marks WHERE student_id = (SELECT id from people WHERE first_name = '�������' and last_name = '�����' and
        pather_name = '����������');
DELETE FROM PEOPLE WHERE first_name = '�������' and last_name = '�����' and
 pather_name = '����������';
--2.	�������� ������ �� ���������� �������� �������� �� �.1.
INSERT INTO marks (student_id, subject_id, teacher_id, value)
VALUES ((SELECT id from People WHERE first_name = '�������' and
last_name = '�����' and pather_name = '����������'), 8, 2, 4);

--�	�������������� ������� � ������ ����������:
--1.	������� ����� �������� ������ (�� ����������) � ����������� ����� �� 1.
--����� ������� �����
BEGIN transaction ;
    INSERT INTO groups (name)
    VALUES ('4084/1_2018');
    UPDATE people SET group_id = (SELECT id from groups where name = '4084/1_2018')
    WHERE group_id = (SELECT id from groups where name = '3084/1_2018');
COMMIT transaction ;

--�������� ����������
BEGIN transaction;
UPDATE people SET group_id = (SELECT id from groups where name = '3084/1_2018')
WHERE group_id = (SELECT id from groups where name = '4084/1_2018');
DELETE from groups where name = '4084/1_2018';
COMMIT transaction;

--2.	�� �� ��� �.1. ���� ������ � ���������� ������������� ��� ���������� � ���������� ��������.
--���� name unique

--Hints: insert, where, in, exists, commit, rollback
--�������� ������
--�	�������� �� ������� � �������� �� ��������� ������:
--1.	������� ���������, � ������� ������� ���� ���� ���������.

SELECT G.name, avg(COALESCE(value, 0)) FROM people1 p
                                                FULL JOIN marks m on p.id = m.student_id
                                                RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
GROUP BY G.id; -- ���� ������ �� ����������, ��������� �� 0

DELETE from People1 p
    where id in (Select id from (Select student_id as id, avg(COALESCE(value, 0)) as avg_mark from marks
        FULL JOIN people1 p2 on marks.student_id = p2.id
    GROUP BY student_id) as ia where avg_mark < 4);

--2.	������� �������� ������ � ���������, ������������� ��.
--�	�������� � ������ ����������:
--1.	������� � ������ ���������� ������ � ����� ��������� ������� ������ � ���������,������������� ��.
begin transaction ;
DELETE from groups1 where id in (Select id from (
    SELECT G.id as id, avg(COALESCE(value, 0)) as avg_mark FROM people p
    FULL JOIN marks m on p.id = m.student_id
    RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
GROUP BY G.id ORDER BY avg_mark
    Limit 1) as table_name
);
commit transaction ;

--2.	�� ��, ��� � �.1, ��, ���� � ��������� ������ �������� 3 �������� � ���������� ��������.
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
    THEN RAISE EXCEPTION '� ���� ������ �������� 3 ��������'
        USING HINT = '������� ��� ������ �������?';
    ELSE
        DELETE from groups1 where id = candidateondeleting;
        RETURN TRUE;
    END IF;
END $_$ LANGUAGE 'plpgsql';

SELECT * from deleteandcheckfor3subjects();

--����������� ������
--�	����������� �� �������:
--1.	��������� �������� ������ �� ������.
UPDATE groups SET name = '3084/1_2021'
WHERE group_id = (SELECT id from groups where name = '3084/1_2018');
--������
UPDATE groups SET name = '3084/1_2018'
WHERE group_id = (SELECT id from groups where name = '3084/1_2021');

--�	����������� � ������ ����������:

--1.	�������� �� ���� ������������ ������� �������� ������� �� ������ � ������� ���� ������� �� ������� ���������.
DO $do$
declare
    old_name  varchar(30) = '���������������';
    new_name varchar(30) = '����';
    old_id integer;
    new_id integer;

begin

Select id into old_id from subject where name = old_name;
Select id into new_id from subject where name = new_name;

update marks set subject_id = new_id where subject_id = old_id;
delete from subject where id = old_id;
END;
    $do$;

insert into subject (name) values ('���������������');
update marks set subject_id = (Select id from subject where name = '���������������') where subject_id = (select id from subject where name = '������������');
delete from subject where id = 11;


--2.	�� ��, ��� � �.1, �� � ������, ���� �������������, �������� ��������� �������, ������ ������ �� ������ � �������� ����������.
DROP function avoidDeletingTeachers(old_subject varchar, new_subject varchar);
CREATE OR REPLACE FUNCTION avoidDeletingTeachers(old_subject varchar(30), new_subject varchar(30))
                                                                            RETURNS BOOLEAN AS $_$
BEGIN
    create temp table if not exists curriculum1 as (SELECT teacher_id, subject_id FROM people p
        LEFT JOIN marks m on p.id = m.teacher_id
        LEFT JOIN subject s on m.subject_id = s.id
       GROUP BY teacher_id, subject_id); -- ���� ������ �� ����������, ��������� �� 0

    if(select count(teacher_id) from curriculum1 where subject_id = (select id from subject where name = old_subject)) < 2
    then
        RAISE EXCEPTION '���� ������� ��������� � �������������'
            USING HINT = '�� �������?';
           ELSE
        insert into subject (name) values (new_subject);
        update marks set subject_id = (Select id from subject where name = new_subject)
        where subject_id = (select id from subject where name = old_subject);
        delete from subject where id = (select id from subject where name = old_subject);
    END IF;
    RETURN TRUE;

END $_$ LANGUAGE 'plpgsql';

select * from avoidDeletingTeachers('����', '��');
--
--Hints: update, where, in, exists, commit, rollback


