create table roles (
    id bigserial not null constraint role_key primary key,
    code varchar(9) not null unique, 
    name varchar(200) not null,
    type varchar(40) not null,
    color varchar(7) default '',
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table stages (
    id bigserial not null constraint stage_key primary key,
    code varchar(9) not null unique, 
    name varchar(200) not null,
    color varchar(7) default '',
    sequence smallint default 0, 
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table processes (
    id bigserial not null constraint process_key primary key,
    code varchar(9) not null unique,
    name varchar(200) not null,
    color varchar(7) default '',
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table processes_stages (
    process_id bigint not null, 
    stage_id bigint not null, 
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table activities (
    id bigserial not null constraint activity_key primary key,
    process_id bigint not null default 0, 
    code varchar(9) not null unique, 
    name varchar(200) not null,
    color varchar(7) default '',
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table products (
    id bigserial not null constraint product_key primary key,
    code varchar(9) not null unique, 
    name varchar(200) not null,
    color varchar(7) default '',
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table procedures (
    id bigserial not null constraint procedure_key primary key,
    activity_id bigint,
    product_id bigint,
    code varchar(9) not null unique, 
    name varchar(200) not null,
    color varchar(7) default '',
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table tops (
    id bigserial not null constraint top_key primary key,
    code varchar(9) not null unique, 
    name varchar(200) not null,
    color varchar(7) default '',
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table indicators (
    id bigserial not null constraint indicator_key primary key,
    code varchar(9) not null unique, 
    name varchar(200) not null,
    color varchar(7) default '',
    type varchar(20) default '',
    picture varchar(200) default '',
    additional_information varchar(500) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table procedures_indicators (
    procedure_id bigint not null, 
    indicator_id bigint not null, 
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table procedures_tops (
    procedure_id bigint not null, 
    top_id bigint not null, 
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table companies (
    id bigserial not null constraint companies_key primary key,
    people_id varchar(80) default '', 
    identification_number varchar(14) not null unique, 
    name varchar(80) not null,
    color varchar(7) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table persons (
    id bigserial not null constraint person_key primary key,
    people_id varchar(80) default '', 
    identification_number varchar(14) not null unique, 
    first_name varchar(80) not null,
    last_name varchar(80) not null,
    email varchar(80) not null,
    role varchar(10) not null default 'CLIENT',
    color varchar(7) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table implantations (
    id bigserial not null constraint implantation_key primary key,
    company_id bigint, 
    negotiated_hours varchar(7),
    additional_hours varchar(7),
    color varchar(7) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table implantations_products (
    implantation_id bigint not null, 
    product_id bigint not null, 
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table implantations_procedures (
    implantation_id bigint not null, 
    procedure_id bigint not null, 
    additional_information varchar(1000) default '',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table implantations_persons_roles (
    implantation_id bigint not null, 
    person_id bigint not null, 
    role_id bigint not null, 
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table tasks (
    id bigserial not null constraint task_key primary key,
    person_id bigint not null, 
    implantation_id bigint not null, 
    procedure_id bigint not null, 
    stage_id bigint not null, 
    additional_information varchar(500) default '',
    status varchar(10) default 'PENDING',
    color varchar(7) default '',
    date_to_do  timestamp default null,
    hour_to_start varchar(5) default '08:00',
    hour_to_finish varchar(5) default '08:00',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table orders (
    id bigserial not null constraint order_key primary key,
    person_id bigint not null, 
    implantation_id bigint not null, 
    additional_information varchar(500) default '',
    color varchar(7) default '',
    hour_to_start time default null,
    hour_to_finish time default null,
    hour_to_lunch time default null,
    date_done timestamp default null, 
    status varchar(10) default 'PENDING',
    created_at timestamp default now(),
    updated_at timestamp default now()
);

create table orders_tasks (
    task_id bigint not null, 
    order_id bigint not null, 
    created_at timestamp default now(),
    updated_at timestamp default now()
);

alter table activities add constraint activities_processes_fk foreign key (process_id) references processes (id) on update cascade;
alter table procedures add constraint procedures_actvitys_fk foreign key (activity_id) references activities (id) on update cascade;
alter table procedures add constraint procedures_products_fk foreign key (product_id) references products (id) on update cascade;
alter table procedures_indicators add constraint procedures_indicators_procedure_fk foreign key (procedure_id) references procedures (id) on update cascade;
alter table procedures_indicators add constraint procedures_indicators_indicator_fk foreign key (indicator_id) references indicators (id) on update cascade;
alter table procedures_tops add constraint procedures_indicators_procedure_fk foreign key (procedure_id) references procedures (id) on update cascade;
alter table procedures_tops add constraint procedures_indicators_top_fk foreign key (top_id) references tops (id) on update cascade;
alter table implantations_products add constraint implantations_products_implantation_fk foreign key (implantation_id) references implantations (id) on update cascade;
alter table implantations_products add constraint implantations_products_product_fk foreign key (product_id) references products (id) on update cascade;
alter table implantations_procedures add constraint implantations_procedures_implantation_fk foreign key (implantation_id) references implantations (id) on update cascade;
alter table implantations_procedures add constraint implantations_procedures_procedure_fk foreign key (procedure_id) references procedures (id) on update cascade;
alter table processes_stages add constraint processes_stages_process_fk foreign key (process_id) references processes (id) on update cascade;
alter table processes_stages add constraint processes_stages_stage_fk foreign key (stage_id) references stages (id) on update cascade;
alter table implantations_persons_roles add constraint implantations_persons_roles_implantation_fk foreign key (implantation_id) references implantations (id) on update cascade;
alter table implantations_persons_roles add constraint implantations_persons_roles_person_fk foreign key (person_id) references persons (id) on update cascade;
alter table implantations_persons_roles add constraint implantations_persons_roles_role_fk foreign key (role_id) references roles (id) on update cascade;
alter table tasks add constraint tasks_implantations_fk foreign key (implantation_id) references implantations (id) on update cascade;
alter table tasks add constraint tasks_persons_fk foreign key (person_id) references persons (id) on update cascade;
alter table tasks add constraint tasks_procedures_fk foreign key (procedure_id) references procedures (id) on update cascade;
alter table tasks add constraint tasks_stage_fk foreign key (stage_id) references stages (id) on update cascade;
alter table implantations add constraint implantations_companies_fk foreign key (company_id) references companies (id) on update cascade;
alter table orders_tasks add constraint orders_tasks_order_fk foreign key (order_id) references orders (id) on update cascade;
alter table orders_tasks add constraint orders_tasks_task_fk foreign key (task_id) references tasks (id) on update cascade;

commit;
