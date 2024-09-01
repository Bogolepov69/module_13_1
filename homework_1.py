import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    await asyncio.sleep(1 / power)
    return name

async def lift_ball(strongman, ball_number):
    await asyncio.sleep(1)  # Задержка для имитации подъема шара
    print(f'Силач {strongman} поднял {ball_number} шар')

async def end_competition(strongman):
    print(f'Силач {strongman} закончил соревнования.')

async def start_tournament():
    names = ['Apollon', 'Denis', 'Pasha']
    power = [3, 4, 5]
    # Начало соревнований
    strongmen = await asyncio.gather(*(start_strongman(name, power) for name, power in zip(names, [5, 4, 3])))

    for ball_number in range(1, 6):
        for strongman in strongmen:
            await lift_ball(strongman, ball_number)

    for strongman in strongmen:
        await end_competition(strongman)

if __name__ == "__main__":
    asyncio.run(start_tournament())