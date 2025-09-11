import aiosqlite
import asyncio


async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users") as cursor:
            async for row in cursor:
                print(dict(row))


async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            async for row in cursor:
                print(dict(row))


async def fetch_concurrently():
    await asyncio.gather(async_fetch_users(), async_fetch_older_users())


asyncio.run(fetch_concurrently())
