from datetime import datetime
from importlib.metadata import metadata

import metadate
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey, TIMESTAMP, JSON, Table

matadate=MetaData()

roles=Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=True),
    Column("permissions", JSON),

users=Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey="roles_id")),
)
