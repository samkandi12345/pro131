from turtle import distance
import pandas as pd
import csv

df = pd.read_csv("final.csv")
mass = df[3]*1.989e+30
radius = df[10]*6.957e+8
gravity = 6.67*10^-11*(mass/(radius*radius))

print(gravity)
