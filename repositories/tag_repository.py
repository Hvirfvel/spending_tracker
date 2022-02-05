from db.run_sql import run_sql

from models.tag import Tag

# Save
def save(tag):
    sql = """
    INSERT INTO 
    tags (name) 
    VALUES (%s) 
    RETURNING id
    """
    values = [tag.name]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

# Select all
def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)
    return tags

# Select
def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if tag is not None:
        tag = Tag(result['name'], result['id'])
    return tag

# Update
def update(tag):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = [tag.name, tag.id]
    run_sql(sql, values)

# Delete all
def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)