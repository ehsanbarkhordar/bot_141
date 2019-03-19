from main_config import BotConfig
import os


class FileAddress:
    unresolved_request = None
    resolved_request_jazb = os.path.join(BotConfig.project_path, "bot/files/jazb_resolved_request.xlsx")
