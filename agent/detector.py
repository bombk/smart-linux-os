from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.trained = False

    def train(self, data):
        self.model.fit(data)
        self.trained = True

    def detect(self, vector):
        if not self.trained:
            return False
        return self.model.predict([vector])[0] == -1
