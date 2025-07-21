## **Project Overview**

### **Main Objective**

The One Billion Row Challenge 2025 is a comprehensive benchmarking project that demonstrates and compares different approaches to processing massive datasets efficiently. This project specifically focuses on processing a 1 billion row dataset (~14GB) containing temperature measurements from weather stations worldwide, showcasing the performance characteristics of various modern data processing technologies and frameworks in Python.

This challange was inspired by [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc).


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
- **Community Learning**: Share performance insights and best practices with the data engineering community

### **Data Generation and Formats**

The project includes data generation capabilities to create realistic test datasets:

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
```

---

## **Implementation Approaches**

### **Available Solutions**

The project includes multiple implementations to compare different technologies and optimization strategies:

#### **1. DuckDB Solutions**
- **`src/usando_duckdb.py`**: Direct CSV processing using DuckDB's native SQL engine
- **`src/usando_duckdb_parquet.py`**: Optimized Parquet processing with columnar analytics

#### **2. Polars Implementation**
- **`src/usando_polars.py`**: High-performance DataFrame processing with lazy evaluation

#### **3. PySpark Solutions**
- **`src/usando_pyspark.py`**: Distributed processing for CSV data
- **`src/usando_pyspark_parquet.py`**: Spark SQL with Parquet optimization

#### **4. Pandas Implementation**
- **`src/usando_pandas.py`**: Traditional DataFrame processing with multiprocessing optimization

---

## **Performance Benchmark Results**

### **Execution Time Comparison**

Fill in your benchmark results here:

| Implementation | File Format | Execution Time (sec) |
|----------------|-------------|----------------|
| **DuckDB (CSV)** | CSV | `_____` | 
| **DuckDB (Parquet)** | Parquet | `_____` | 
| **Polars** | CSV | `_____` | 
| **PySpark (CSV)** | CSV | `_____` |
| **PySpark (Parquet)** | Parquet | `_____` |
| **Pandas (Multiprocessing)** | CSV | `_____` |

### **File Format Comparison**

| Format | File Size | Compression |
|--------|-----------|-------------------|
| **CSV** | `~14 GB` | `1.0x (baseline)` |
| **Parquet** | `~3-4 GB` | `~3.5x smaller` |

### **Technology Analysis**

#### **🏆 Performance Champions**
- **Fastest Overall**: `DuckDB`


#### **� Tool Comparison: When to Use What?**

| Tool | Best For | Data Size | Performance | Parallelism | Disk/Memory | Ideal Use Cases |
|------|----------|-----------|-------------|-------------|-------------|-----------------|
| **Python** | Small tasks, custom logic | 💾 < 10MB | 😐 Slow | ❌ Single-threaded | Memory only | Scripts, ETL glue code, testing |
| **Pandas** | Tabular data, exploratory work | 💾 < 1GB RAM | ⚡ Fast (in-memory) | ❌ Single-threaded | Memory only | Data wrangling, ML pipelines |
| **DuckDB** | Analytics on medium data | 💾 < 100GB (local) | ⚡ Very fast (vectorized) | ✅ Multi-threaded | Memory + temp disk | Interactive SQL, file-based ETL |
| **Polars** | Fast tabular ops | 💾 1GB – 100GB | ⚡ Super fast (Rust backend) | ✅ Multi-threaded | Memory (with chunked exec) | Replacement for Pandas |
| **PySpark** | Distributed big data | 🏢 10GB – 100TB+ | 🚀 High (with cluster) | ✅ Yes (clustered) | Can spill to disk | Batch jobs, lakehouse ETL |

---

## **Getting Started**

### **Prerequisites**
```bash
# Install Python dependencies
pip install -r requirements.txt

# Or using Poetry
poetry install
```

### **Generate Dataset**
```bash
# Create 1 billion row CSV file (~14GB)
python criar_dataset_csv.py

# Create optimized Parquet version (~3-4GB)
python criar_dataset_parquet.py
```

### **Run Benchmarks**
```bash
# Test each implementation
python src/usando_duckdb.py
python src/usando_duckdb_parquet.py
python src/usando_polars.py
python src/usando_pyspark.py
python src/usando_pyspark_parquet.py
python src/usando_pandas.py
```

### **Hardware Specifications**
Document your testing environment:
- Macbook Pro - M4 Pro - 24Gb RAM

---

## **Contributing**

Feel free to contribute new implementations, optimizations, or benchmark results! Areas for improvement:
- Additional data processing libraries (Ray, Dask, etc.)
- Cloud-based solutions
- Performance optimizations
- Memory profiling and analysis

---

## **References**

- [Original One Billion Row Challenge (Java)](https://github.com/gunnarmorling/1brc)
- [DuckDB Documentation](https://duckdb.org/)
- [Polars Documentation](https://pola.rs/)
- [Apache Spark Documentation](https://spark.apache.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
