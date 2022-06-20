from typing import Tuple
import psycopg2
from urllib.parse import urlparse




result = urlparse("postgres://nofufthy:we3Erf889-HjVtanL4MF7mS0UsRvGf1T@dumbo.db.elephantsql.com/nofufthy")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port
db_connection = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname,
    port = port
)

print(f"DB DEBUG DATA: username: {username}. password: {password}. database: {database}. hostname: {hostname}. port: {port}.")

def db_action(action: str):
    print("DB ACTION: " + action)
    try:
        with db_connection.cursor() as cur:
            
            cur.execute(action)
            db_connection.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print("SQL do_action Error: ", error)
    
def db_fetch(sql: str):
    print("DB FETCH: " + sql)
    try:
        with db_connection.cursor() as cur:
            
            cur.execute(sql)
            db_connection.commit() 
            
            res = tuple(cur.fetchall())
            return res

    except (Exception, psycopg2.DatabaseError) as error:
        print("SQL db_fetch Error: ", error)
        return Tuple()

def insert_app_to_db(id: int, name: str, description: str, category: str, rating: float, **kw):
    
    sql = f"""INSERT INTO public.apps(id, name, description, rating, category) VALUES ({id}, '{name}', '{description}', {rating}, '{category}') ON CONFLICT DO NOTHING;"""
    
    db_action(sql)
    
def add_purchase_do_db(app_addr: str, creator_addr: str, purchaser_addr: str, **kw):
    sql = f"""INSERT INTO public.purchases(app_addr, creator_addr, purchaser_addr) VALUES ('{app_addr}', '{creator_addr}', '{purchaser_addr}') ON CONFLICT DO NOTHING;"""
    db_action(sql)

def get_filtered_app_ids(offset, length, textFilter, categoryFilter, ratingFilter):

    sql = f"""SELECT id 
            FROM public.apps 
            WHERE 
                (name ILIKE '%{textFilter}%' OR description ILIKE '%{textFilter}%')
                AND
                category ILIKE '%{categoryFilter}%' 
                AND 
                rating >= {ratingFilter} 
            ORDER BY id ASC
            OFFSET {offset} 
            LIMIT {length};   
        """
    raw_res = db_fetch(sql)
    print("raw res: ", raw_res)
    ids = [res[0] for res in raw_res]
    
    print("ids: ", ids)
    return ids

def update_app_rating_db(app_id: int, rating: float):
    sql = f"""UPDATE public.apps SET rating = {rating} WHERE id = {app_id};"""
    db_action(sql)
    
def update_app_name_description_db(app_id: int, name: str, description: str):
    sql = f"""UPDATE public.apps SET name = '{name}', description = '{description}' WHERE id = {app_id};"""
    db_action(sql)
