--Оставшийся запрос со второй лабы:
--1.	Вывести студентов и наименования предметов, включая предметы,
-- которые не читались студентам и студентов, которые не получили ни одной оценки.


SELECT  p.first_name, p.last_name, p.pather_name, s.name FROM MARKS M
                                                                  FULL JOIN PEOPLE P ON P.ID = M.STUDENT_ID
                                                                  LEFT JOIN GROUPS G ON G.ID = P.GROUP_ID
                                                                  FULL Join subject s on M.subject_id = s.id;
--•	многотабличная вставка в рамках транзакции:
--1.	Создать копию заданной группы (со студентами) с увеличением курса на 1.
--нужно создать копию
Do $DO$
BEGIN
INSERT INTO groups (name)
VALUES ('4084/1_2018');
INSERT INTO people (first_name, last_name, pather_name, group_id, type)
(SELECT  first_name, last_name, pather_name, (SELECT id from groups where name = '4084/1_2018'), type from people
WHERE group_id = (SELECT id from groups where name = '3084/1_2018'));

end;$DO$;

Do $DO$
    BEGIN
        Delete from people  WHERE group_id = (SELECT id from groups where name = '4084/1_2018');
        Delete from groups where name = '4084/1_2018';

    end;$DO$;
-- Представления
-- 1.	Создать представление, отображающее всех преподавателей, предметы и средний балл,
-- выставляемый ими, агрегируя по предметам.
drop view avgMarkByTeacher;
Create  view avgMarkByTeacher as
SELECT s.name, p.first_name, p.last_name, p.pather_name, avg(COALESCE(value, 0)) FROM people p
                                                FULL JOIN marks m on p.id = m.teacher_id
                                                RIGHT JOIN subject s on m.subject_id = s.id
GROUP BY s.id, p.id; -- если оценка не поставлена, считается за 0
select * from avgMarkByTeacher;

-- 2.	Создать представление, отображающее средние баллы, агрегируя оценки по годам.
drop view avgMarkByYears;
Create  view avgMarkByYears as
SELECT extract(year from m.date), avg(COALESCE(value, 0)) FROM people p
                                                FULL JOIN marks m on p.id = m.student_id
                                                RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
GROUP BY extract(year from m.date); -- если оценка не поставлена, считается за 0
select * from avgMarkByYears;

select marks.id, g.name, value, s.name, date from marks
left join people p on p.id = marks.student_id
left join groups g on p.group_id = g.id
left join subject s on s.id = marks.subject_id

-- Hints: select, where, count, max, group by, having, like, create view, drop view



--     Хранимые процедуры
--     •	без параметров:
--     1.	Создать хранимую процедуру, выводящую все предметы, по которым в заданном году были выставлены оценки,
--     и средний балл по каждому из предметов.

drop function subjectsAndAvgMarkInOneYear(year integer);
CREATE OR REPLACE FUNCTION subjectsAndAvgMarkInOneYear(year integer)
    RETURNS TABLE (
                      subject_id              int,
                      avg_marks               numeric
                  ) AS $_$
BEGIN
    IF ((year < 2000) or (year > extract(year from current_date)))
        THEN RAISE EXCEPTION 'Некорректный год';
    END IF;
    drop table if exists temp;
    Create temp table temp as (SELECT s.id as subject_id, round(avg(COALESCE(value, 0)), 2) as avg_marks from marks m
                                                                            RIGHT JOIN subject s on m.subject_id = s.id
                              where extract(year from date) = 2020
                              GROUP BY s.id);
    RETURN QUERY EXECUTE 'Select * from temp';

END $_$ LANGUAGE 'plpgsql';

select s.name, avg_marks from subjectsAndAvgMarkInOneYear(2020)
right join subject s on s.id = subject_id;

--     •	с входными параметрами:
--     1.	Создать хранимую процедуру. Входные параметры задают интервал времени. Процедура должна вернуть выборку
--     средних баллов по группам, попавшим в этот интервал.

drop function intervalAvgMarks(begin_timestamp timestamp, end_timestamp timestamp);

CREATE OR REPLACE FUNCTION intervalAvgMarks(begin_timestamp timestamp, end_timestamp timestamp)
    RETURNS TABLE (
                      subject_id              int,
                      avg_marks               numeric
                  ) AS $_$
BEGIN
    IF ((extract(year from begin_timestamp) < 2000) or (extract(year from begin_timestamp) > extract(year from current_date))
            or ((extract(year from begin_timestamp) > (extract(year from end_timestamp)))))
    THEN RAISE EXCEPTION 'Некорректные года';
    END IF;
    drop table if exists temp;
    Create temp table temp as (SELECT s.id as subject_id, avg(COALESCE(value, 0)) as avg_marks from marks m
                                RIGHT JOIN subject s on m.subject_id = s.id

                               where date > begin_timestamp and date < end_timestamp
                               GROUP BY s.id);
    RETURN QUERY EXECUTE 'Select * from temp';

END $_$ LANGUAGE 'plpgsql';

select s.name, avg_marks from intervalAvgMarks('2019-01-01'::timestamp, '2019-09-01'::timestamp)
                                  right join subject s on s.id = subject_id;
-- COPY (select s.name, avg_marks from intervalAvgMarks('2019-01-01'::timestamp, '2019-09-01'::timestamp)
--                     right join subject s on s.id = subject_id)
--     TO E'C:\\Users\\Owner\\Documents\\intervalAvgMarks1.csv' With CSV DELIMITER ',';
\COPY (select s.name, round(avg_marks, 2),  from intervalAvgMarks('2019-01-01'::timestamp, '2019-09-01'::timestamp) right join subject s on s.id = subject_id) to 'C:\\Users\\Owner\\Documents\\intervalAvgMarks1.csv' DELIMITER ',' CSV HEADER
--номер группы, название группы

--     •	с выходными параметрами:
--     1.	Создать хранимую процедуру с входным параметром «преподаватель» и выходным параметром – группа,
--     с наименьшим средним баллом у этого преподавателя.

drop function minMarksFromOneProf(first_name varchar(20), last_name varchar(20), pather_name varchar(20));

CREATE OR REPLACE FUNCTION minMarksFromOneProf(first varchar(20), last varchar(20), pather varchar(20))
    RETURNS integer AS $_$
declare
        returned_id integer;
BEGIN
    drop table if exists temp;
    select id into returned_id from (SELECT p1.group_id as id, avg(COALESCE(value, 0)) as avg FROM marks m
                                                  left join people p on m.teacher_id = p.id
                                                  left join people p1 on m.student_id = p1.id
                                                  left join groups g on p.group_id = g.id
                                                  where  p.last_name = last and p.first_name = first and p.pather_name = pather
                                                  GROUP BY p1.group_id
                                                    order by avg asc
    limit 1) as temp_table
                                   ;
    RETURN returned_id;

END $_$ LANGUAGE 'plpgsql';

Select name from groups where id = minMarksFromOneProf('Мохаев','Константин','Александрович');

--     Hints: select, where, count, max, group by, having, create procedure, drop procedure
--     Триггера
--     •	Триггера на вставку:
--     1.	Создать триггер, который не позволяет добавить оценку, не попадающую в интервал [2..5].

-- 2
-- Создать хранимую процедуру с входным параметром группа и двумя
-- выходными параметрами, возвращающими предмет с самым низким
-- средним балом у этой группы и самый низкий средний бал по этому
-- предмету среди других групп.

CREATE OR REPLACE FUNCTION bound_mark() returns trigger as $bound_mark_trigger$
    BEGIN
    if (new.value < 2) or (new.value > 5) then
        raise exception 'mark cannot be more than 5 or less than 2';
    end if;

    RETURN NEW;
    END;
$bound_mark_trigger$ LANGUAGE plpgsql;

CREATE TRIGGER bound_mark_trigger
    Before INSERT ON marks
    FOR EACH ROW EXECUTE PROCEDURE bound_mark();

Insert into marks (student_id, subject_id, teacher_id, value) values (8,1,2,1);


--     •	Триггера на модификацию:
--     1.	Создать триггер, который не позволяет изменить наименование предмета, если на него есть ссылки.

--     •	Триггера на удаление:
--     1.	Создать триггер, который при удалении предмета, если на него существуют ссылки – откатывает транзакцию.

CREATE OR REPLACE FUNCTION name_and_link() returns trigger as $name_and_link_trigger$
BEGIN
    if exists(select * from marks where subject_id = old.id) then
        raise exception 'по этому предмету некоторым студентам выставлены оценки, что-нибудь сделать с ним не получится';
    end if;

    RETURN NEW;
END;
$name_and_link_trigger$
    LANGUAGE plpgsql;
CREATE TRIGGER name_and_link_trigger
    Before UPDATe or delete ON subject
    FOR EACH ROW EXECUTE PROCEDURE name_and_link();

--
--     Hints: select, where, in, exists, join, commit, rollback, create trigger, drop trigger
--
--
--     Курсоры
--     •	Хранимая процедура для расчета успеваемости и прироста успеваемости:
CREATE OR REPLACE FUNCTION academic_progress(begin_timestamp timestamp,
                                           end_timestamp timestamp)
    RETURNS TABLE (
                      year integer,
                      subject_id integer,
                      avg_mark          numeric,
                      diff_avg_mark     numeric
                  ) AS
$cursor_test$
DECLARE
    interval_cur CURSOR FOR (SELECT extract(year from m.date) as year ,m.subject_id,  avg(COALESCE(value, 0)) as avg_mark FROM people p
                        FULL JOIN marks m on p.id = m.student_id
                        RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
                        where (m.date > begin_timestamp) and (m.date < end_timestamp)
                    GROUP BY extract(year from m.date), m.subject_id);
    current_avg_mark numeric;
BEGIN
    IF ((extract(year from begin_timestamp) < 2000) or (extract(year from begin_timestamp) > extract(year from current_date))
        or ((extract(year from begin_timestamp) > (extract(year from end_timestamp)))))
    THEN RAISE EXCEPTION 'Некорректные года';
    END IF;

    drop table if exists temp_table;
    Create temp table temp_table(                      year integer,
                                                       subject_id integer,
                                                       avg_mark          numeric,
                                                       diff_avg_mark     numeric);
    drop table if exists current_year_stat;
    Create temp table current_year_stat as (SELECT m.subject_id,  avg(COALESCE(value, 0)) as avg_mark
    FROM people p
        FULL JOIN marks m on p.id = m.student_id
        RIGHT JOIN GROUPS G ON G.ID = P.GROUP_ID
        where (extract(year from m.date) = 2020)--date_part('year', CURRENT_DATE))
        GROUP BY m.subject_id);

    FOR row IN interval_cur LOOP
            Select c.avg_mark into current_avg_mark from current_year_stat c
             where c.subject_id = row.subject_id;
                 INSERT INTO temp_table(year, subject_id, avg_mark, diff_avg_mark)
            VALUES (row.year, row.subject_id, row.avg_mark, abs(current_avg_mark - row.avg_mark));

        END LOOP;
    return query execute 'Select * from temp_table';
END;
$cursor_test$
    LANGUAGE plpgsql VOLATILE;

select * from academic_progress('2019-01-01'::timestamp, '2020-09-01'::timestamp)
\COPY (select * from academic_progress('2019-01-01'::timestamp, '2020-09-01'::timestamp) right join subject s on s.id = subject_id) to 'C:\\Users\\Owner\\Documents\\academic_progress.csv' DELIMITER ',' CSV HEADER

--     Хранимая процедура имеет два параметра, определяющие анализируемый интервал времени.
--     Результатом работы процедуры должна явиться выборка, содержащая средний балл по всем предметам в
--     рассматриваемом интервале времени, и разницу текущего среднего балла и предыдущего.
--     Алгоритм реализации предлагается следующий.
--     Oрганизуется курсор, перебирающий все года, в которых проводилось обучение, попадающие в заданный интервал времени.
--     Средний балл предыдущего года запоминается в переменной. В теле курсора формируется выборка необходимых данных.
--
--     Hints: CURSOR,  %NOTFOUND, FETCH
--
--
