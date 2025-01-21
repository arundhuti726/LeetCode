# Databricks notebook source
df.filter(df['conditions'].str.match(r'\sDIAB1'))
