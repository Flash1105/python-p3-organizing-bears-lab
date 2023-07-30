select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex='F';
"""

select_young_bears_return_name_and_temperament = """
    SELECT
        name,
        temperament
    FROM bears
    WHERE age < 5;
"""

select_bears_by_colors_return_name_and_color = """
    SELECT
        name,
        color
    FROM bears
    WHERE color IN ('Brown', 'Black');
"""

select_dead_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 0;
"""
