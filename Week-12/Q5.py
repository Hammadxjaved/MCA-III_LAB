import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x1 = np.random.rand(1000, 1)
x2 = np.random.rand(1000, 1)

c = np.random.rand(1000, 1)

y = (x1 ** 2) + (3 * x2) + c

X = np.hstack((x1, x2))

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)
score = r2_score(y, y_pred)

print("R^2 Score:", score)
