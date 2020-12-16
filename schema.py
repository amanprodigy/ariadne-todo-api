from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
    ObjectType,
)
from api.query import resolve_todos, resolve_todo

query = ObjectType("Query")
query.set_field("todos", resolve_todos)
query.set_field("todo", resolve_todo)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)
