


import numpy as np  # type: ignore[import-not-found]



class : 
    
    
    def brightness(im: np.ndarray, level: float) -> np.ndarray:
        im = im + level
        return np.clip(im, 0, 1)


    def contrast(im: np.ndarray, level: float) -> np.ndarray:
        im = (im - 0.5) * level + 0.5
        return np.clip(im, 0, 1)


def blur(im: np.ndarray, size: int) -> np.ndarray:
    result = im.copy()

    for i in range(size, im.shape[0] - size):
        for j in range(size, im.shape[1] - size):
            result[i, j] = np.mean(
                im[i-size:i+size+1, j-size:j+size+1],
                axis=(0, 1)
            )

    return result