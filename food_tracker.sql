#File that creates the tables on our Database 

-- Keeping track of dates
create table log_date(
	id integer primary key autoincrement,
	entry_date date not null
);

-- Keeping track if list of foods
create table food(
	id integer primary key autoincrement,
	name text not null,
	carbobydrates integer not null,
	fat integer not null,
	calories integer not null
);
-- Keeping track of food being added to a date.
create table foo_date(
	food_id integer  not null,
	log_date_id integer not null,
	primary key(food_id, log_date_id)
);