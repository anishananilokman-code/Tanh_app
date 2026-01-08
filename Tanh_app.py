import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title of the application
st.title('Tanh Activation Function Visualization')

# Input range for the plot
x = np.linspace(-10, 10, 100)
y = np.tanh(x)

# Plotting Tanh function
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Tanh(x)')
plt.title('Tanh Activation Function')
st.pyplot(plt)

