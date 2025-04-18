SUBTREE = """
    WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id
    FROM categories
    WHERE parent_id :condition1
    
    UNION ALL

    SELECT c.id, c.name, c.parent_id
    FROM categories c
    INNER JOIN category_tree ct ON c.parent_id = ct.id
    )
    SELECT * FROM category_tree;"""
