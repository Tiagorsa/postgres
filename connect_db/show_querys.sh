psql -c "select usename, application_name, query, state from pg_stat_activity where usename<>'' and usename<>'postgres';"
