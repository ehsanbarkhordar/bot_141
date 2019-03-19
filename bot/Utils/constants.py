class Command:
    del_admin = "/del_admin"
    add_admin = "/add_admin"
    myid = "/myid"
    help = "/help"
    start = "/start"
    menu = "/menu"


class ButtonAction:
    default = 0


class Patterns:
    bale_id = "^\d{3,}$"
    back_to_replied = "^بازگشت به پیام‌های پاسخ داده شده$"
    return_to_main_menu = "^بازگشت به منوی اصلی$"
    phone_number_pattern = "^(\+98|0)?9\d{9}$"  # "(^09[0-9]{9}$)|(^9[0-9]{9}$)"
    fullname = "[\D]{7,130}"  # "^[\sآابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی‬ٌ ‬ًّ ‬َ ‬ِ ‬ُ ‬]{5,30}$"  # "[\u0600-\u06FF\s]{5,30}"


class MimeType:
    image = "image/jpeg"
    csv = "text/csv"
    xlsx = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


class BotMessage:
    state_choosed = "استان *{}*"
    state_coming_soon = "نقشه راه های استان *{}* در حال آماده سازی است..."
    traffic_between_state = "تصویر مروبط به ترافیک بین شهری استان  *{state}*"
    choose_state = "استان مورد نظر را برای مشاهده ترافیک بین شهری *انتخاب* نمایید:"
    add_admin_id = "لطفا آی دی ادمین جدید را وارد کنید:"
    not_found_admin = "آی دی وارد شده در لیست کاربران بازو یافت نشد."
    no_admin_right = "*شما دسترسی ادمین روت ندارید!*"
    del_admin = "ادمین مورد نظر حذف شد"
    add_admin = "ادمین جدید با موفقیت اضافه شد.\n" \
                "نام: *{}*  نام کاربری: *{}*"
    choose_admin = "ادمین مورد نظر را انتخاب کنید:"
    guide_text = "این راهنما است."
    enter_your_pass = "رمز عبور خود را وارد کنید"
    message_sent = "پیام شما ارسال شد"
    choose_from_menu = "یکی از گزینه‌های زیر را انتخاب کنید:"
    greeting = "سلام به بازوی *۱۴۱* خوش آمدید.\n" \
               "می‌توانید با انتخاب استان مورد نظر خود ترافیک جاده‌های بین شهری را مشاهده کنید."


class ConversationData:
    username = "username"
    name = "name"


class ButtonMessage:
    top_state = "{} - {} بازدید"
    update_state = "به روزرسانی {}"
    tehran = "تهران"
    choose_state_most_views = "پربازدیدترین استانها"
    choose_state_alphabetian = "تمام استان ها به ترتیب الفبا"
    return_to_back_step = "بازگشت به مرحله‌ی قبل"
    report = "گزارش"
    yes = "بله"
    return_to_main_menu = "بازگشت به منوی اصلی"
    guide = "راهنما"


class SendingAttempt:
    first = 1


class Step:
    show_guide = "show_guide"
    showing_menu = "showing_menu"
    conversation_starter = "conversation_starter"


class LogMessage:
    failed_report_sending = "failed report sending"
    successful_report_sending = "successful report sending"
    failed_report_upload = "failure report uploading"
    successful_report_upload = "successful report uploading"
    user_register = "successful user register"
    successful_sending = "successful sending of message:"
    failed_sending = "failed sending of message:"
    successful_step_message_sending = "successful step message sending"
    failed_step_message_sending = "failure step message sending"


class UserData:
    record_changes_num = "record_changes_num"
    url = "url"
    file_id = "file_id"
    succedent_message = "succedent_message"
    latitude = "latitude"
    longitude = "longitude"
    bot = "bot"
    send_message = "send_message"
    logger = "logger"
    session = "session"
    message_type = "message_type"
    message_id = "message_id"
    sending_set_time = "sending_set_time"
    base_message = "base_message"
    db_msg = "db_msg"
    random_id = "random_id"
    sending_attempt = "sending_attempt"
    kwargs = "kwargs"
    user_id = "user_id"
    user_peer = "user_peer"
    step_name = "step_name"
    message = "message"
    attempt = "attempt"
    report_attempt = "report_attempt"
    doc_message = "doc_message"
    file_url = "file_url"


class Regex:
    persian_number_regex = '([۰-۹])+'
    number_regex = '^([0-9]+|[۰-۹]+)$'
    persian_regex = "[ء|\s|آ-ی]+"
    any_match = "(.*)"