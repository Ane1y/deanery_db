create table groups
(
    id   serial not null
        constraint "GROUPS_PK"
            primary key,
    name varchar(50)
);

alter table groups
    owner to postgres;

INSERT INTO public.groups (id, name) VALUES (1, '3084/1_2018');
INSERT INTO public.groups (id, name) VALUES (2, '3084/2_2018');
INSERT INTO public.groups (id, name) VALUES (3, '1084/1_2020');
INSERT INTO public.groups (id, name) VALUES (4, '1084/2_2020');
INSERT INTO public.groups (id, name) VALUES (5, '2084/1_2019');
INSERT INTO public.groups (id, name) VALUES (6, '2084/2_2019');