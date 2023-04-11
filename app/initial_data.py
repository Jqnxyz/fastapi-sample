"""
Put here any Python code that must be runned before application startup.
It is included in `init.sh` script.

By defualt `main` create a superuser if not exists
"""

import asyncio


async def main() -> None:
    print("Start initial data")
    # async with async_session() as session:
    #     print("Initial data created")


if __name__ == "__main__":
    asyncio.run(main())
