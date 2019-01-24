class Individual(object):
    
    def __init__(self, hyper, model):
        self.hyper    = hyper
        self.model    = model
        self.val_acc  = 0
        self.tra_acc  = 0
        self.val_loss = 0
        self.tra_loss = 0
        self.score    = 0
         
    def getHyperVec(self):
        return self.hyper
    
    def getHyper(self, i):
        return self.hyper[i]
    
    def setHyper(self, i, value):
        self.hyper[i] = value
    
    def getModel(self):
        return self.model
    
    def getScore(self):
        return self.score
    
    def setScore(self):
        self.score = round((95*self.val_acc + 5*self.tra_acc),2)
        
    def getValAcc(self):
        return self.val_acc
    
    def setValAcc(self, val_acc):
        self.val_acc = val_acc
            
    def getTraAcc(self):
        return self.tra_acc
    
    def setTraAcc(self, tra_acc):
        self.tra_acc = tra_acc
    
    def getValLoss(self):
        return self.val_loss
    
    def setValLoss(self, val_loss):
        self.val_loss = val_loss
    
    def getTraLoss(self):
        return self.tra_loss
    
    def setTraLoss(self, tra_loss):
        self.tra_loss = tra_loss
        
    def fitness(self):
        model = self.getModel()
        metric = model.fit(x=small_data['X_train'], y=small_data['y_train'],epochs=5, verbose=0, 
                           validation_data=(small_data['X_val'], small_data['y_val']))
        self.setValAcc(metric.history['val_acc'][-1])
        self.setTraAcc(metric.history['acc'][-1])
        self.setValLoss(metric.history['val_loss'][-1])
        self.setTraLoss(metric.history['loss'][-1])
        self.setScore()