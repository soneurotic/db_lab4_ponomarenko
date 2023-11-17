-- Запит 1
-- Вивести character_name та max_atk зброї, якою споряджений кожен з персонажів

-- SELECT has.character_name, weapon.max_atk FROM has
-- LEFT JOIN weapon ON has.weapon_name = weapon.weapon_name


-- Запит 2
-- Вивести weapon_type та кількість зброї цього виду на персонажах, що мають level >= 40

-- SELECT weapon_type, COUNT(weapon_type) FROM is_at 
-- 	LEFT JOIN character ON is_at.character_name = character.character_name
-- 	LEFT JOIN has ON character.character_name = has.character_name
-- 		WHERE is_at.level > 40
-- 			GROUP BY weapon_type


-- Запит 3
-- Вивести ім'я персонажа, його base_atk та max_atk зброї, якою він споряджений. 
-- Результат запиту впорядкувати за сумою (base_atk + max_atk)

-- SELECT is_at.character_name, is_at.base_atk, weapon.max_atk FROM is_at 
-- 	LEFT JOIN character ON is_at.character_name = character.character_name
-- 	LEFT JOIN has ON character.character_name = has.character_name
-- 	LEFT JOIN weapon ON has.weapon_name = weapon.weapon_name
-- 		ORDER BY base_atk + max_atk