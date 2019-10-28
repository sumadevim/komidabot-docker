import requests
from typing import List

from komidabot.app import get_app

from komidabot.facebook.message_sender import MessageSender
from komidabot.facebook.message import Message
from komidabot.message_receiver import MessageReceiver
from komidabot.util import check_exceptions

TYPE_REPLY = 'RESPONSE'
TYPE_SUBSCRIPTION = 'NON_PROMOTIONAL_SUBSCRIPTION'


# TODO: Deprecated
class Messenger:
    def __init__(self, page_access_token: str, admin_ids: List[str]):
        self.session = requests.Session()
        self.base_endpoint = "https://graph.facebook.com/v4.0/"
        self.locale_parameters = {
            'access_token': page_access_token,
            'fields': 'locale'
        }
        self.admin_ids = admin_ids

    @check_exceptions
    def send_message(self, message: 'Message'):
        return get_app().bot_interfaces['facebook']['api_interface'].post_send_api(message.get_data())

    @staticmethod
    def multicast_message(message: 'Message', recipients: List[MessageReceiver]):
        original_recipient = message.recipient

        for recipient in recipients:
            recipient.send_message(message)

        message.recipient = original_recipient

    @check_exceptions
    def mark_read(self, sender: MessageSender):
        return get_app().bot_interfaces['facebook']['api_interface'].post_send_api({
            'recipient': {'id': sender.user_id},
            'sender_action': 'mark_seen'
        })

    def is_admin(self, user_id):
        return user_id in self.admin_ids

    def lookup_locale(self, user_id):
        return get_app().bot_interfaces['facebook']['api_interface'].lookup_locale(user_id)
