import asyncio
from functional.composition import o


# line execute, returns result of task executing
async def exec_line(coroutines: list) -> list:
    match coroutines:
        case []:
            return []
        case coroutines:
            task = asyncio.create_task(coroutines[0])
            future = asyncio.create_task(exec_line(coroutines[1:]))
            exec_task = await task
            exec_future = await future
            return [exec_task] + exec_future


# returns result of async operations
catch_line = o([asyncio.run, exec_line])
