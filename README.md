## Introduction

The goal of this project is to demonstrate how to efficiently process a massive data file containing 1 billion rows (~14GB), specifically to compute statistics (including aggregation and sorting, which are heavy operations) using Python.

This challenge was inspired by the [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originally proposed for Java.

The data file consists of temperature measurements from various weather stations. Each record follows the format `<string: station name>;<double: measurement>`, with the temperature presented to one decimal place of precision.

Here are ten sample lines from the file:

Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0


The challenge is to develop a Python program capable of reading this file and calculating the minimum, average (rounded to one decimal), and maximum temperature for each station, displaying the results in a table sorted by station name.

| station       | min_temperature | mean_temperature | max_temperature |
|---------------|-----------------|------------------|-----------------|
| Abha          | -31.1           | 18.0             | 66.5            |
| Abidjan       | -25.9           | 26.0             | 74.6            |
| Abéché        | -19.8           | 29.4             | 79.9            |
| Accra         | -24.8           | 26.4             | 76.3            |
| Addis Ababa   | -31.8           | 16.0             | 63.9            |
| Adelaide      | -31.8           | 17.3             | 71.5            |
| Aden          | -19.6           | 29.1             | 78.3            |
| Ahvaz         | -24.0           | 25.4             | 72.6            |
| Albuquerque   | -35.0           | 14.0             | 61.9            |
| Alexandra     | -40.1           | 11.0             | 67.9            |
| ...           | ...             | ...              | ...             |
| Yangon        | -23.6           | 27.5             | 77.3            |
| Yaoundé       | -26.2           | 23.8             | 73.4            |
| Yellowknife   | -53.4           | -4.3             | 46.7            |
| Yerevan       | -38.6           | 12.4             | 62.8            |
| Yinchuan      | -45.2           | 9.0              | 56.9            |
| Zagreb        | -39.2           | 10.7             | 58.1            |
| Zanzibar City | -26.5           | 26.0             | 75.2            |
| Zürich        | -42.0           | 9.3              | 63.6            |
| Ürümqi        | -42.1           | 7.4              | 56.7            |
| İzmir         | -34.4           | 17.9             | 67.9            |

---

**Project diagram:** [app.excalidraw.com](https://link.excalidraw.com/l/8pvW6zbNUnD/AOSRHr9dKWd)

---

## **Today’s Overview**

### **Main Objective**

The One Billion Challenge is a project that explores different approaches to processing a massive volume of data, reaching 1 billion rows. The goal is to test and compare the performance of technologies and frameworks for optimizing large-scale data processing.

#### Objectives

- Test and compare different tools for processing large volumes of data.
- Explore new libraries such as Databricks, DuckDB, FireDucks, Polars, and others.
- Share learnings and benchmarks with the data engineering community.
