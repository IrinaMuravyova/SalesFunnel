from .messages import router_messages
from .lessons import router_lessons
from .reminders import router_reminders
# from .fsm import router_quiz
from .reminders import check_status_and_remind_through_10_min, check_status_and_remind_through_3_hour, remind_to_watch_this
router_list = [router_messages, router_lessons, router_reminders]#, router_quiz]
