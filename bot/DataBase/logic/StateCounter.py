from bot.DataBase.models.StateCounter import StateCounter
from bot.DataBase.models.base import Session
from bot.Utils.callbacks import my_logger

session = Session()


def up_state_counter(state_name):
    try:
        state = session.query(StateCounter).filter(StateCounter.state_name == state_name).first()
        if state:
            state.counter += 1
            session.commit()
            my_logger.info("\n\n\n\n\n\n\n\n\nUp Counter for State  :{}\n\n\n\n\n\n\n\n".format(state_name))
        else:
            state_counter = StateCounter(state_name=state_name)
            session.add(state_counter)
            session.commit()
            my_logger.info("\n\n\n\n\n\n\n\n\nNew State Counter added : {}\n\n\n\n\n\n\n\n\n".format(state_name))
    except Exception as e:
        session.rollback()
        my_logger.info("Fail to Up state : {}, for : {}".format(state_name, e))


def get_5_top_state():
    try:
        states = session.query(StateCounter).order_by(StateCounter.counter.desc()).limit(5).all()
        my_logger.info("5 Top states: {}".format(states))
        return states
    except Exception as e:
        session.rollback()
        my_logger.info("Fail to loaf 5 top state for  :{}".format(e))