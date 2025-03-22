import os

if os.getenv("USE_EMULATOR"):
    from hal_emulator import HAL
else:
    from hal_board import HAL
