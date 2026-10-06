import numpy as np  # pyright: ignore[reportMissingImports]


class Filter:

    def brightness(self, im: np.ndarray, level: float) -> np.ndarray:
        im = im + level
        return np.clip(im, 0, 1)

    def contrast(self, im: np.ndarray, level: float) -> np.ndarray:
        im = (im - 0.5) * level + 0.5
        return np.clip(im, 0, 1)

    def blur(self, im: np.ndarray, size: int) -> np.ndarray:
        result = im.copy()

        for i in range(size, im.shape[0] - size):
            for j in range(size, im.shape[1] - size):
                result[i, j] = np.mean(
                    im[i-size:i+size+1, j-size:j+size+1],
                    axis=(0, 1)
                )

        return result

    