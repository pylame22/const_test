#!/bin/sh

set -e
set -u

cd /app
alembic upgrade head
exec python -m uvicorn main:app
