#!/usr/bin/python
import psycopg2
from configobj import ConfigObj
from config import config
#from psutil import virtual_memory

#mem = virtual_memory()

filename=['web_pos10_2RAM_2CPU_HDD.txt', 'web_pg9_5_32RAM_4CPU_SDD.txt', 'web_pg9_5_32RAM_4CPU_HDD.txt']

config_values = ConfigObj(filename[2])
#print(config_values)
print(config_values.keys())


def connect():
    """ Connect to the PostgreSQL database server """


    #params_list = ['max_connections', "shared_buffers", "effective_cache_size", "maintenance_work_mem",
    #               "checkpoint_completion_target", "wal_buffers", "default_statistics_target", "random_page_cost",
    #               "effective_io_concurrency", "work_mem", "min_wal_size", "max_wal_size", "max_worker_processes",
    #               "max_parallel_workers_per_gather", "max_parallel_workers"]

    params_list = config_values.keys()

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        param = "server_version"
        paramSQL = "select current_setting('" + param + "')"
        cur.execute(paramSQL)

        # display the PostgreSQL database server version
        pg_param = cur.fetchone()[0]
        print(param + ": ", pg_param)

        for param in params_list:
            paramSQL = "select current_setting('" + param + "')"
            cur.execute(paramSQL)
            # display the PostgreSQL database server version
            pg_param = cur.fetchone()[0]
            print("%-30s %8s %8s"% (param , pg_param, config_values[param]))
            #print(param + ": ", pg_param, " Proposto:", config_values[pg_param])

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
