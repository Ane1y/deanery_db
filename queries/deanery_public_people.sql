create table people
(
    id          serial not null
        constraint "PEOPLE_PK"
            primary key,
    first_name  varchar(30),
    last_name   varchar(30),
    pather_name varchar(30),
    group_id    integer
        constraint people_group_id_fkey
            references groups,
    type        char
);

alter table people
    owner to postgres;

INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (2, 'Борисов', 'Антон', 'Алексеевич', null, 'P');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (3, 'Кротов', 'Леонид', 'Петрович', null, 'P');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (4, 'Мохаев', 'Константин', 'Александрович', null, 'P');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (5, 'Сямочкин', 'Анатолий', 'Григорьевич', null, 'P');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (6, 'Петрова', 'Антонина', 'Александровна', 1, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (7, 'Краснов', 'Валерий', 'Александрович', 1, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (8, 'Замакова', 'Зарина', 'Алексеевна', 1, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (9, 'Гурьев', 'Аким', 'Станиславович', 1, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (10, 'Овчинников', 'Леонтий', 'Протасьевич', 1, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (11, 'Артемьева', 'Октябрина', 'Руслановна', 2, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (12, 'Большаков', 'Евдоким', 'Еремеевич', 2, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (13, 'Пономарёв', 'Гавриил', 'Демьянович', 2, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (14, 'Лыткин', 'Валерий', 'Феликсович', 2, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (15, 'Киселёв', 'Святослав', 'Тимофеевич', 2, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (16, 'Мартынов', 'Ким', 'Владимирович', 3, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (17, 'Васильев', 'Глеб', 'Федотович', 3, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (18, 'Васильева', 'Серафима', 'Альбертовна', 3, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (19, 'Ширяева', 'Харитина', 'Романовна', 3, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (20, 'Герасимова', 'Мартина', 'Романовна', 3, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (21, 'Кудряшова', 'Элина', 'Дмитриевна', 4, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (22, 'Иванкова', 'Дарьяна', 'Григорьевна', 4, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (23, 'Максимов', 'Лазарь', 'Семёнович', 4, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (24, 'Крюкова', 'Розалия', 'Игнатьевна', 4, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (25, 'Смирнов', 'Игорь', 'Антонинович', 4, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (26, 'Игнатьева', 'Анна', 'Еремеевна', 5, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (27, 'Мишина', 'Любовь', 'Фроловна', 5, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (28, 'Уварова', 'Дарья', 'Филипповна', 5, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (29, 'Яковлев', 'Роман', 'Еремеевич', 5, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (30, 'Самсонов', 'Орест', 'Ильяович', 5, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (31, 'Ильин', 'Иннокентий', 'Павлович', 5, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (32, 'Артемьев', 'Руслан', 'Вениаминович', 6, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (33, 'Максимов', 'Василий', 'Русланович', 6, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (34, 'Фомин', 'Модест', 'Евгеньевич', 6, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (35, 'Игнатьев', 'Родион', 'Сергеевич', 6, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (36, 'Филиппов', 'Ростислав', 'Анатольевич', 6, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (37, 'Селиверстов', 'Мартын', 'Викторович', 6, 'S');
INSERT INTO public.people (id, first_name, last_name, pather_name, group_id, type) VALUES (38, 'Гусев', 'Юрий', 'Валерьянович', 6, 'S');