class TwoFingersUpRule:
    def __init__(self, hand, detector):
        self.hand = hand
        self.detector = detector
        self.fingersUp = detector.fingersUp(hand)

    @staticmethod
    def passes(self):
        # four fingers are up
        fingersUp = [0, 1, 1, 0, 0]
        return self.fingersUp == fingersUp

class FingersApartRule:
    def __init__(self, hand, detector):
        self.hand = hand
        self.detector = detector
        self.landmarks = hand["lmList"]


    @staticmethod
    def passes(self):
        normalizer, info = self.detector.findDistance(self.landmarks[0][0:2], self.landmarks[9][0:2])
        fingerDistances = [
            self.detector.findDistance(self.landmarks[8][0:2], self.landmarks[12][0:2])
        ]

        for distance in fingerDistances:
            if distance[0] / normalizer < .36:
                return False
        return True

class Peace():
    def __init__(self, hand, detector):
        self.hand = hand
        self.detector = detector
        self.rules = [TwoFingersUpRule(hand, detector), FingersApartRule(hand, detector)]

    def isShowing(self):
        for rule in self.rules:
            if not rule.passes(rule):
                return False
        print('peace sign')
        return True

