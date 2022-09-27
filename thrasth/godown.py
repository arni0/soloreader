#storage module
import levelup as lp
# unicode symbols ᛜ ᛭ ៙ ◎ ✧

player_stats = {
    "Total hours": 211,
    "Hours studied previous day": 23,
    "streak": 3,
    "xp": lp.xp,
    "level": lp.lvl,
    "coins": 3,
    "Title": "Monarch of the shadows",
    "status": "In test",
    "Daily_task_completed": True
}

print(player_stats)
