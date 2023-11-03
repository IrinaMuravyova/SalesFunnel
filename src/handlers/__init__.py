from .messages import router_messages
from .lessons import router_lessons
from .reminders import router_reminders
from .reminders import check_status_and_remind, remind_if_lesson_did_not_watch, remind_to_watch_this
router_list = [router_messages, router_lessons, router_reminders]
