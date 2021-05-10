create table subject
(
    id   serial not null
        constraint "SUBJECT_PK"
            primary key,
    name varchar(50)
);

alter table subject
    owner to postgres;

INSERT INTO public.subject (id, name) VALUES (1, 'Цифровая обработка сигналов');
INSERT INTO public.subject (id, name) VALUES (2, 'Микропроцессоры');
INSERT INTO public.subject (id, name) VALUES (3, 'СУБД');
INSERT INTO public.subject (id, name) VALUES (4, 'Физика');
INSERT INTO public.subject (id, name) VALUES (5, 'Высшая математика');