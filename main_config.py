import os


class BotConfig:
    daily_report_filename = None
    full_report_filename = None
    root_admin = os.environ.get('BOT_ADMIN_ID', '1471278867')
    reports_route = "files/"
    base_url = os.environ.get('BASE_URL', "wss://api.bale.ai/v1/bots/")
    # bot_token = os.environ.get('TOKEN', "4de3376eb96e3c0c4905778ae22065dfefe10b7f")

    bot_token = os.environ.get('TOKEN', "da5b2817e583c88fa4a736d481693a6fcdbce700")
    system_local = os.environ.get('SYSTEM_LOCAL', "fa_IR")
    resending_max_try = int(os.environ.get('RESENDING_MAX_TRY', 5))
    reuploading_max_try = int(os.environ.get('REUPLOADING_MAX_TRY', 5))


class DbConfig:
    # database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name) or None
    database_url = "sqlite:///bot/files/foo.db"
