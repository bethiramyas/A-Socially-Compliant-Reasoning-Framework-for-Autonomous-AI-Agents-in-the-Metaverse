import numpy as np

def affect_encoder(obs_id:int, meta:int=0):
    """
    Toy multimodal encoder: returns a 3-d 'emo' embedding and a class id.
    obs_id ~ {0:neg,1:neutral,2:pos,...}
    """
    base = {
        0: np.array([-1.0, 0.0, 0.0]),
        1: np.array([ 0.0, 1.0, 0.0]),
        2: np.array([ 0.0, 0.0, 1.0]),
    }.get(int(obs_id), np.array([0.0, 0.5, 0.0]))
    z = base + 0.05*np.array([np.sin(meta), np.cos(meta), np.sin(2*meta)])
    emo = int(np.argmax(z))
    return z, emo
