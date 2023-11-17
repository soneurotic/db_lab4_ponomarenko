import psycopg2

username = 'postgres'
password = 'postgres'
database = 'lab_3'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT has.character_name, weapon.max_atk FROM has
LEFT JOIN weapon ON has.weapon_name = weapon.weapon_name
'''
query_2 = '''
SELECT weapon_type, COUNT(weapon_type) FROM is_at 
	LEFT JOIN character ON is_at.character_name = character.character_name
	LEFT JOIN has ON character.character_name = has.character_name
		WHERE is_at.level > 40
			GROUP BY weapon_type
'''

query_3 = '''
SELECT is_at.character_name, is_at.base_atk, weapon.max_atk FROM is_at 
	LEFT JOIN character ON is_at.character_name = character.character_name
	LEFT JOIN has ON character.character_name = has.character_name
	LEFT JOIN weapon ON has.weapon_name = weapon.weapon_name
		ORDER BY base_atk + max_atk
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    print("Database 'lab_3' opened successfully", end='\n\n')
    def output(cur):
        for row in cur:
            print(row)
        print('\n')

    cur = conn.cursor()

    print('Запит 1:', 'Вивести character_name та max_atk зброї, якою споряджений кожен з персонажів', sep='\n')
    cur.execute(query_1)
    output(cur)

    print('Запит 2:', 'Вивести weapon_type та кількість зброї цього виду на персонажах, що мають level >= 40', sep='\n')
    cur.execute(query_2)
    output(cur)

    print('Запит 3:')
    print("Вивести ім'я персонажа, його base_atk та max_atk зброї, якою він споряджений.",
          "Результат запиту впорядкувати за сумою (base_atk + max_atk)", sep='\n')
    cur.execute(query_3)
    output(cur)