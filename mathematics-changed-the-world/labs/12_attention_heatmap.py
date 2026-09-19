import numpy as np
import matplotlib.pyplot as plt


def softmax(x, axis=-1):
    shifted = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(shifted)
    return e / e.sum(axis=axis, keepdims=True)

rng = np.random.default_rng(3)
tokens = ["math", "changes", "how", "we", "see", "world"]
n = len(tokens)
d_model = 8
d_k = 4

X = rng.normal(size=(n, d_model))
Wq = rng.normal(size=(d_model, d_k))
Wk = rng.normal(size=(d_model, d_k))
Wv = rng.normal(size=(d_model, d_k))

Q = X @ Wq
K = X @ Wk
V = X @ Wv

scores = Q @ K.T / np.sqrt(d_k)
attention = softmax(scores, axis=1)
output = attention @ V

print("attention row sums:", attention.sum(axis=1))
print("output shape:", output.shape)

plt.figure()
plt.imshow(attention, aspect="auto")
plt.xticks(range(n), tokens, rotation=45, ha="right")
plt.yticks(range(n), tokens)
plt.xlabel("key/value token")
plt.ylabel("query token")
plt.title("Scaled dot-product attention weights")
plt.colorbar(label="attention weight")
plt.tight_layout()
plt.show()
