
class ZeroFingersAreUpRule:
    def __init__(self, hand, detector):
        self.hand = hand
        self.detector = detector
        self.fingersUp = detector.fingersUp(hand)

    @staticmethod
    def passes(self):
        # all fingers are up
        fingersUp = [0,0,0,0,0]
        return self.fingersUp == fingersUp


class ClosedFist():
    def __init__(self, hand, detector):
        self.hand = hand
        self.detector = detector
        self.rules = [ZeroFingersAreUpRule(hand, detector)]

    def isShowing(self):
        # a rule is just a condition that must be true for the hand sign to be showing
        for rule in self.rules:
            if not rule.passes(rule):
                return False
        print('closed fist')
        return True

