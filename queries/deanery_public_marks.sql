create table marks
(
    id         serial  not null
        constraint "MARKS_PK"
            primary key,
    student_id integer not null
        constraint marks_student_id_fkey
            references people,
    subject_id integer not null
        constraint marks_subject_id_fkey
            references subject,
    teacher_id integer not null
        constraint marks_teacher_id_fkey
            references people,
    value      integer not null
);

alter table marks
    owner to postgres;

INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (2, 6, 2, 2, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (3, 6, 3, 3, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (4, 6, 4, 4, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (5, 6, 5, 5, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (6, 7, 2, 2, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (7, 7, 3, 3, 3);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (8, 7, 4, 4, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (9, 7, 5, 5, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (10, 8, 2, 2, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (11, 8, 3, 3, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (12, 8, 4, 4, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (13, 8, 5, 5, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (14, 9, 2, 2, 3);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (15, 9, 3, 3, 3);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (16, 9, 4, 4, 3);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (17, 9, 5, 5, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (18, 10, 2, 2, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (19, 10, 3, 3, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (20, 10, 4, 4, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (21, 10, 5, 5, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (22, 11, 2, 2, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (23, 11, 3, 3, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (24, 11, 4, 4, 5);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (25, 11, 5, 5, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (26, 12, 2, 2, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (27, 12, 3, 3, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (28, 12, 4, 4, 4);
INSERT INTO public.marks (id, student_id, subject_id, teacher_id, value) VALUES (29, 12, 5, 5, 4);