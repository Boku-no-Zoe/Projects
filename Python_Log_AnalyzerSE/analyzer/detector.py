from collections import defaultdict


class SecurityDetector:
    """
    Applies light security detection logic to a list of Logevent objects.
    """

    FAILED_LOGIN_EVENT_ID = "4009"
    FAILED_LOGIN_THRESHOLD = 4


    def __init__(self, events):
        self.events = events
    

    def run_all_checks(self):
        alerts = []
        alerts.extend(self._detect_failed_login_bursts())
        return alerts
    
    def _detect_failed_login_bursts(self):
        """
        Detects users with excessive failed login attempts.
        """
        failed_login_counts = defaultdict(int)

        for event in self.events:
            if event.event_id == self.FAILED_LOGIN_EVENT_ID:
                failed_login_counts[event.user] += 1


        alerts = []

        for user, count in failed_login_counts.items():
            if count > self.FAILED_LOGIN_THRESHOLD:
                alerts.append({
                    "type": "Failed Login Burst",
                    "user": user,
                    "count": count,
                    "severity": "High",
                    "description": f"User {user} had {count} failed login attempts."
                })
        
        return alerts
     