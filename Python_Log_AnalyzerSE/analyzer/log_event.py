class LogEvent:
    def __init__(self, timestamp, event_id, user, source_ip, message):
        self.timestamp = timestamp
        self.event_id = event_id
        self.user = user
        self.source_ip = source_ip
        self.message = message

    def __repr__(self):
        return (f"LogEvent(timestamp ={self.timestamp}, event_id ={self.event_id}, "
                f"user ={self.user}, source_ip ={self.source_ip}, message ={self.message})")