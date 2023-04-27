import bittensor
import commune

class Dataset( commune.Module):
    def __init__(self, *args, **kwargs):
        self.dataset = bittensor.dataset(*args, **kwargs)
        
    def getattr(self, key):
        if hasattr(getattr(self, 'dataset'), key):
            return getattr(self.dataset, key)
        else:
            return getattr(self, key)
            
            
    
    def sample(self,*args, **kwargs):
        input_ids =  next(self.dataset)
        sample = {'input_ids': input_ids}
        return sample

Dataset.serve(name='bro', batch_size=32, block_size=256)

        

# Dataset.serve(name='data.bt')