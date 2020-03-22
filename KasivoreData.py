import psycopg2 as psycopg2
import traceback
import configfile

##postgresql connection string

con_postgresql = psycopg2.connect(user= configfile.DB_USER, password= configfile.DB_PASS, host= configfile.DB_HOST, port= configfile.DB_PORT,
                                  database= configfile.DB_DATABASE)


## postgresql Database fuctions and SP's
# Get User Level
def pgsql_get_scalar(schema, fn_name, paramenters):
    value = 0
    fn_parameters = ''
    Sp_QueryStr = ''
    ##Get Parameters

    try:
        for par in paramenters:
            if fn_parameters == '':
                fn_parameters = fn_parameters + par + ":= '{value}'".format(value= paramenters[par])
            else:
                fn_parameters = fn_parameters + ',' + par + ":= '{value}'".format(value= paramenters[par])

        Sp_QueryStr = 'SELECT {schema}.{function} ({params})'.format(schema='"' + schema + '"', function=fn_name, params=fn_parameters)
        #print(Sp_QueryStr)

        ##Sql Call
        mycursor = con_postgresql.cursor()
        mycursor.execute(Sp_QueryStr)
        user_record = mycursor.fetchone()
        mycursor.close()
        con_postgresql.commit()
        value = user_record
    except Exception:
        traceback.print_exc()
    return value[0]


#This is void SP, can be used for inserts and updates
def pgsql_call_SP(schema, sp_name, paramenters):
    fn_parameters = ''
    Sp_QueryStr = ''
    ##Get Parameters
    try:
        for par in paramenters:
            if fn_parameters == '':
                fn_parameters = fn_parameters + par + ":= '{value}'".format(value=paramenters[par])
            else:
                fn_parameters = fn_parameters + ',' + par['name'] + ":= '{value}'".format(value=par['value'])

        Sp_QueryStr = 'call {schema}.{sp} ({params})'.format(schema='"' + schema + '"', sp=sp_name, params=fn_parameters)
        #print(Sp_QueryStr)
        ##Sql Call
        mycursor = con_postgresql.cursor()
        mycursor.execute(Sp_QueryStr)
        mycursor.close()
        con_postgresql.commit()
    except Exception:
        traceback.print_exc()


# this table value function takes a schema name as string, function name as string and a dictinary list of parameter name and values [{name: name,value: value}]. returns Dataset
def pgsql_call_Tablefunction_P(schema, fn_name, paramenters):
    fn_parameters = ''
    DataSet = []
    fn_QueryStr = ''
    ##Get Parameters
    try:
        for par in paramenters:
            if fn_parameters == '':
                fn_parameters = fn_parameters + par + ":= '{value}'".format(value=paramenters[par])
            else:
                fn_parameters = fn_parameters + ',' + par + ":= '{value}'".format(value=paramenters[par])

        fn_QueryStr = 'SELECT * FROM {schema}.{function} ({params})'.format(schema='"' + schema + '"', function=fn_name,
                                                                            params=fn_parameters)
        #print(fn_QueryStr)
        ##Sql Call
        mycursor = con_postgresql.cursor()
        mycursor.execute(fn_QueryStr)
        DataSet = mycursor.fetchall()
        mycursor.close()
        con_postgresql.commit()
    except Exception:
        traceback.print_exc()
    return DataSet


# this table vale function takes a schema name as string and function name as string returns Dataset
def pgsql_call_Tablefunction(schema, fn_name):
    fn_QueryStr = ''
    DataSet = []
    ##Get Parameters

    fn_QueryStr = 'SELECT * FROM {schema}.{function}()'.format(schema='"' + schema + '"', function=fn_name)
    try:
        #print(fn_QueryStr)
        ##Sql Call
        mycursor = con_postgresql.cursor()
        mycursor.execute(fn_QueryStr)
        DataSet = mycursor.fetchall()
        mycursor.close()
        con_postgresql.commit()

    except Exception:
        traceback.print_exc()

    return DataSet
