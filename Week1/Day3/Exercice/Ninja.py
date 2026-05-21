class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        self.call_history.append(other_phone)

    def show_call_history(self):
        print(f"Call history from {self.phone_number} : ")
        if not self.call_history:
            print("No calls made.")
        for call in self.call_history:
            print(f" - {call.phone_number}")

    def send_message(self, other_phone, message, content):
        message = {
            "to" : other_phone.phone_number,
            "from" : self.phone_number,
            "content" : content
        }
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: \"{content}\"")
        self.messages.append(message)
        other_phone.messages.append(message)
    
    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number} : ")
        if not self.messages:
            print("No messages sent.")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(f" - To {message['to']}: \"{message['content']}\"")
    
    def show_incoming_messages(self):
        print(f"Incoming messages to {self.phone_number} : ")
        if not self.messages:
            print("No messages received.")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(f" - From {message['from']}: \"{message['content']}\"")
    
    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number} to {self.phone_number} : ")
        if not self.messages:
            print("No messages received.")
        for message in self.messages:
            if message["to"] == self.phone_number and message["from"] == other_phone.phone_number:
                print(f" - From {message['from']}: \"{message['content']}\"")