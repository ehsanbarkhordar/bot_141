import asyncio
import sys

import persian
from balebot.filters import *
from balebot.handlers import MessageHandler
from balebot.models.messages import *
from bot.DataBase.logic.StateCounter import up_state_counter, get_5_top_state
from bot.DataBase.logic.user import is_user
from bot.DataBase.models.base import Base, engine
from bot.ImageDownloader.downloader import async_request
from bot.Utils.States import States
from bot.Utils.base_bot import Bot
from bot.Utils.callbacks import *

from bot.Utils.constants import *

template_bot = Bot()
bot = template_bot.bot
updater = template_bot.updater
dispatcher = template_bot.dispatcher
loop = template_bot.loop
main_loop = asyncio.get_event_loop()
Base.metadata.create_all(engine)


#################################### Meta Functions ################################


def _get_peer(update):
    return update.get_effective_user()


def _get_msg(update):
    return update.get_effective_message()


def _formatter(id):
    return persian.convert_en_numbers(str(id))


def _return_to_back_step_check_up(msg):
    if isinstance(msg, TemplateResponseMessage):
        if msg.get_json_object()['textMessage'] == ButtonMessage.return_to_back_step:
            return True
    else:
        return False


def send_message(message, peer, step, succedent_message=None):
    kwargs = {UserData.user_peer: peer, UserData.step_name: step, UserData.succedent_message: succedent_message,
              UserData.message: message, UserData.attempt: SendingAttempt.first, UserData.bot: bot}
    bot.send_message(message=message, peer=peer, success_callback=step_success, failure_callback=step_failure,
                     kwargs=kwargs)


def check_message(msg, update):
    send_message(TextMessage("Check Message : {}".format(msg)), update.get_effective_user(),
                 sys._getframe().f_code.co_name)


######################## conversation ###################
@dispatcher.message_handler(TemplateResponseFilter(pattern=Patterns.return_to_main_menu))
@dispatcher.command_handler([Command.start])
@dispatcher.default_handler()
def showing_menu(bot, update):
    user = _get_peer(update)
    message = _get_msg(update)
    if isinstance(message, TextMessage) and message.text == Command.start:
        text_msg = TextMessage(BotMessage.greeting)
    else:
        text_msg = TextMessage(BotMessage.choose_from_menu)
    _is_user = is_user(user.peer_id)
    my_logger.info("is User : {}".format(_is_user))
    if is_user(user.peer_id):
        btn = [

            TemplateMessageButton(ButtonMessage.choose_state_alphabetian, ButtonMessage.choose_state_alphabetian,
                                  ButtonAction.default),
            TemplateMessageButton(ButtonMessage.choose_state_most_views, ButtonMessage.choose_state_most_views,
                                  ButtonAction.default),
            # TemplateMessageButton(ButtonMessage.tehran, ButtonMessage.tehran,
            #                       ButtonAction.default),
        ]
        msg = TemplateMessage(text_msg, btn)
        send_message(msg, _get_peer(update), Step.conversation_starter)
        dispatcher.register_conversation_next_step_handler(update, [
            MessageHandler(TemplateResponseFilter(keywords=ButtonMessage.tehran), send_state_road_map),
            MessageHandler(TemplateResponseFilter(keywords=ButtonMessage.choose_state_most_views), state_most_views),
            MessageHandler(DefaultFilter(), choose_state)
        ])
    else:
        btn = [

            TemplateMessageButton(ButtonMessage.choose_state_alphabetian, ButtonMessage.choose_state_alphabetian,
                                  ButtonAction.default),
            TemplateMessageButton(ButtonMessage.choose_state_most_views, ButtonMessage.choose_state_most_views,
                                  ButtonAction.default),
            # TemplateMessageButton(ButtonMessage.tehran, ButtonMessage.tehran,
            #                       ButtonAction.default),
        ]
        msg = TemplateMessage(text_msg, btn)
        send_message(msg, _get_peer(update), Step.conversation_starter)
        dispatcher.register_conversation_next_step_handler(update, [
            MessageHandler(TemplateResponseFilter(keywords=ButtonMessage.tehran), send_state_road_map),
            MessageHandler(TemplateResponseFilter(keywords=ButtonMessage.choose_state_most_views), state_most_views),
            MessageHandler(DefaultFilter(), choose_state)
        ])


def state_most_views(bot, update):
    states = get_5_top_state()
    btns = []
    for state in states:
        state_name = get_state_name_fa(state.state_name)
        btns.append(TemplateMessageButton(state_name, state_name, 0))
    btns.append(TemplateMessageButton(ButtonMessage.return_to_main_menu))
    text_msg = TextMessage(BotMessage.choose_state)
    msg = TemplateMessage(text_msg, btns)
    send_message(msg, _get_peer(update), Step.conversation_starter)
    dispatcher.finish_conversation(update)


def choose_state(bot, update):
    txt_msg = TextMessage(BotMessage.choose_state)
    btn = []
    for name in States.states_views:
        btn.append(TemplateMessageButton(name, name, 0))
    btn.append(TemplateMessageButton(ButtonMessage.return_to_main_menu))
    msg = TemplateMessage(txt_msg, btn)
    send_message(msg, _get_peer(update), Step.conversation_starter)
    dispatcher.register_conversation_next_step_handler(update, [
        MessageHandler(TemplateResponseFilter(keywords=States.states_views), send_state_road_map),
        MessageHandler(DefaultFilter(), showing_menu)
    ])


def send_state_road_map(bot, update):
    state = _get_msg(update).get_json_object()['textMessage']
    state_name = ""
    state_name = get_state_name_en(state)
    if state_name:
        up_state_counter(state_name)

        def send_done(_, __):
            def callback(future):
                result = future.result()
                response = result.get('content')
                img_data = response

                def success_send_photo_message(result, user_data):
                    text_msg = TextMessage(BotMessage.state_choosed.format(state))
                    btn = [
                        TemplateMessageButton(ButtonMessage.update_state.format(state),
                                              state,
                                              ButtonAction.default),
                        TemplateMessageButton(ButtonMessage.return_to_main_menu, ButtonMessage.return_to_main_menu,
                                              ButtonAction.default),
                    ]
                    msg = TemplateMessage(text_msg, btn)
                    send_message(msg, _get_peer(update), Step.conversation_starter)
                    dispatcher.finish_conversation(update)

                def failure_send_message(result, user_data):
                    showing_menu(bot, update)

                bot.send_photo(user_peer=_get_peer(update), image=img_data,
                               name="bale.jpg", file_storage_version=1, mime_type="image/jpeg",
                               success_callback=success_send_photo_message, failure_callback=failure_send_message)

            main_loop.create_task(async_request(callback=callback, state=state_name))

        def send_fail(_, __):
            showing_menu(bot, update)

        my_logger.info("\n\n\n{}\n\n\n".format(state))
        bot.send_message(message=TextMessage(BotMessage.state_coming_soon.format(state)),
                         peer=_get_peer(update),
                         success_callback=send_done,
                         failure_callback=send_fail
                         )
    else:
        showing_menu(bot, update)


def get_state_name_en(state):
    state_counter = 0
    state_name = ""
    for i in States.states_views:
        if i == state:
            state_name = States.states_names[state_counter]
            break
        else:
            state_counter += 1
    return state_name


def get_state_name_fa(state):
    state_counter = 0
    state_name = ""
    for i in States.states_names:
        if i == state:
            state_name = States.states_views[state_counter]
            break
        else:
            state_counter += 1
    return state_name


dispatcher.add_handler(
    MessageHandler(
        [
            TemplateResponseFilter(
                pattern=Regex.persian_regex
            )
        ],
        send_state_road_map))
