import csv
from analyzer.log_event import  LogEvent


class LogParser:
    """
    Responsible for reading raw log files and 
    converting them into Log Event Objects
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        """
        Entry point for parsing logs.
        Currently supports CSV.
        """
        return self._parse_csv()
    
    def _parse_csv(self):
        events = []

        with open(self.file_path, newline='', encoding= "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    event = LogEvent(
                       timestamp=row.get("timestamp"),
                       event_id=row.get("event_id"), 
                       user=row.get("user"),
                       source_ip=row.get("source_ip"),
                       message=row.get("message")
                    )
                    events.append(event)
                except Exception:
                    # Skip bad rows for now
                    continue

        return events