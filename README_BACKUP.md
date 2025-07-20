## Introduction

The goal of this project is to d---

## **Project Overview**

### **Main Objective**

The One Billion Row Challenge 2025 is a comprehensive benchmarking project that demonstrates and compares different approaches to processing massive datasets efficiently. This project specifically focuses on processing a 1 billion row dataset (~14GB) containing temperature measurements from weather stations worldwide, showcasing the performance characteristics of various modern data processing technologies and frameworks in Python.

### **Key Objectives**

- **Performance Benchmarking**: Compare execution times and resource utilization across different data processing technologies
- **Technology Evaluation**: Assess the strengths and weaknesses of modern data processing libraries including:
  - **DuckDB**: In-memory analytical database with CSV and Parquet support
  - **Polars**: Fast DataFrame library with lazy evaluation and streaming capabilities  
  - **PySpark**: Distributed computing framework for big data processing
  - **Pandas**: Traditional data manipulation library with multiprocessing optimization
  - **Apache Airflow**: Workflow orchestration with DuckDB and PostgreSQL integration
- **File Format Analysis**: Compare performance between CSV and Parquet file formats
- **Optimization Techniques**: Explore parallel processing, chunking, streaming, and memory management strategies
- **Real-world Application**: Demonstrate practical data engineering workflows for large-scale analytics
- **Community Learning**: Share performance insights and best practices with the data engineering community

### **Data Generation and Formats**

The project includes sophisticated data generation capabilities to create realistic test datasets:

#### **CSV Dataset Generation** (`criar_dataset_csv.py`)
- Generates synthetic temperature measurements from 10,000+ real weather station names
- Creates CSV files with format: `<station_name>;<temperature_value>`
- Temperature range: -99.9°C to +99.9°C with 1 decimal precision
- Batch processing for memory efficiency during generation
- Sample data sourced from `data/amostra_44k.csv` containing real weather station names

#### **Parquet Dataset Generation** (`criar_dataset_parquet.py`)
- Converts data to optimized Parquet format for columnar analytics
- Partitioned storage for improved query performance
- Uses Apache Arrow for efficient data serialization
- Significantly smaller file sizes compared to CSV (~3-5x compression)
- Supports parallel processing and predicate pushdown

#### **Generated Files Structure**
```
data/generated/
├── medicoes_1000000000.txt          # 14GB CSV file with 1B rows
└── medicoes_1000000000.parquet/     # ~3-4GB Parquet directory
    ├── part-001.parquet             # Multiple partitioned files
    ├── part-002.parquet             # for optimal parallel processing
    └── ...
```w to efficiently process a massive data file containing 1 billion rows (~14GB), specifically to compute statistics (including aggregation and sorting, which are heavy operations) using Python.

This challenge was inspired by the [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originally proposed for Java.

The data file consists of temperature measurements from various weather stations. Each record follows the format `<string: station name>;<double: measurement>`, with the temperature presented to one decimal place of precision.

Here are ten sample lines from the file:

```
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
```

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

## **Today’s Overview**

### **Main Objective**

The One Billion Challenge is a project that explores different approaches to processing a massive volume of data, reaching 1 billion rows. The goal is to test and compare the performance of technologies and frameworks for optimizing large-scale data processing.

#### Objectives

- Test and compare different tools for processing large volumes of data.
- Explore new libraries such as Databricks, DuckDB, FireDucks, Polars, and others.
- Share learnings and benchmarks with the data engineering community.
