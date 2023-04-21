# conexion a sql server: https://www.youtube.com/watch?v=BzsF1cG6JJU&list=PLWYKfSbdsjJgKIKV-5eixWaNIiB-j_OSI&index=9

# instalacion paquetes necesarios conexion a postgresql
# pip install psycopg2
# pip install pygresql
conexion = psycopg2.connect("dbname=empleados user=neoguias password=pimientos44")
