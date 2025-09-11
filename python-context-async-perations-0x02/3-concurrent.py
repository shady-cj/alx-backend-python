import aiosqlite
import asyncio


async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users WHERE id > ?", (2,)) as cursor:
            return await cursor.fetchall()


async def fetch_concurrently():
    results = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    for result in results:
        for row in result:
            print(dict(row))


asyncio.run(fetch_concurrently())
