#1
short_messages = ['this is short message', 'hi post this message', 'can you delete this message?']

def read_short_messages(messages):
    for message in messages:
        print(message)

read_short_messages(short_messages)

#2
print("\n")
chat_messages = ['How are you?', 'Here good', 'Alright!', 'Chat later!']

def send_messages(messages, sent_messages):
    for message in messages:
        print(f"sending... {message}")
        sent_messages.append(message)

    return sent_messages


#print all sent messages
sent_messages_done = send_messages(chat_messages, [])
print("\nSent Messages:")
for message in sent_messages_done:
    print(message)

#3
print("\n")
print(f"New:{sent_messages_done}\n")
print(f"Original:{chat_messages}\n")