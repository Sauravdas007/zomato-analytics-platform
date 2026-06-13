# Why These Technologies Were Chosen

## Why Azure Data Lake Storage Gen2?

### Alternatives Considered
- Azure Blob Storage
- Azure SQL Database
- Local File Storage

### Why ADLS Gen2 Was Selected
- Native integration with Azure Synapse Analytics  
- Supports hierarchical folder structures required for Medallion Architecture  
- Cost-effective storage for large-scale analytical datasets  
- Optimized for Spark workloads and Parquet files  

### Trade-off
ADLS Gen2 requires additional transformation layers before business users can consume data directly, but provides significantly better scalability and flexibility for analytics workloads.

---

## Why Azure Synapse Analytics?

### Alternatives Considered
- Azure Databricks  
- Azure SQL Database  
- Microsoft Fabric  
- Local Apache Spark  

### Why Synapse Was Selected
- Unified analytics platform integrating Spark, SQL, and Data Lake  
- Native connectivity with Azure Data Lake Gen2  
- Suitable for enterprise-scale analytics architectures  
- Simplified management compared to maintaining separate Spark clusters  

### Trade-off
Databricks offers a richer Spark ecosystem, but Synapse provides tighter Azure integration and a lower operational overhead for this project.

---

## Why Apache Spark (PySpark)?

### Alternatives Considered
- Pandas  
- SQL-only transformations  
- Azure Data Factory Mapping Data Flows  

### Why PySpark Was Selected
- Handles large-scale transformations efficiently  
- Supports distributed processing  
- Industry-standard framework for data engineering workloads  
- Enables scalable ETL pipelines and future machine learning extensions  

### Trade-off
PySpark introduces additional complexity compared to Pandas, but offers significantly better scalability.

---

## Why Parquet Format?

### Alternatives Considered
- CSV  
- JSON  
- Excel  

### Why Parquet Was Selected
- Columnar storage format  
- Faster analytical queries  
- Reduced storage consumption through compression  
- Native optimization for Spark and Power BI  

### Trade-off
Parquet is not human-readable, but provides superior performance for analytical workloads.

---

## Why Medallion Architecture?

### Alternatives Considered
- Single-layer data lake  
- Traditional ETL into a warehouse  

### Why Bronze → Silver → Gold Was Selected
- **Bronze Layer**: Stores raw source data without modifications.  
- **Silver Layer**: Contains cleansed and standardized business entities.  
- **Gold Layer**: Contains business-ready analytical marts optimized for reporting.  

### Benefits
- Improved data quality  
- Clear lineage  
- Easier debugging  
- Enterprise-standard architecture  

---

## Why Spark Pools Instead of Dedicated SQL Pools?

### Alternatives Considered
- Dedicated SQL Pool  
- Serverless SQL Pool  

### Why Spark Pool Was Selected
The project required:  
- Data cleansing  
- Schema correction  
- Type casting  
- Data quality validation  
- Aggregation pipelines  
- Forecast preparation  

These operations are naturally suited to Spark.  

Dedicated SQL Pools are optimized for high-concurrency enterprise warehouses but introduce additional costs and administration overhead.

### Trade-off
Dedicated SQL Pools provide faster SQL analytics at scale, but Spark offers greater flexibility for ETL and feature engineering workloads.

---

## Why Not Use Dedicated SQL Pool?

### Reason 1: Cost
Azure for Students credits are limited.  
Dedicated SQL Pools incur continuous compute costs even when not actively used.  

### Reason 2: Project Requirements
The project focused on:  
- Data engineering  
- Analytics engineering  
- Dashboarding  

rather than enterprise data warehousing.  

### Reason 3: Existing Gold Layer
Gold marts generated through Spark already provided curated business datasets for Power BI consumption.  
Adding a dedicated warehouse would increase complexity without delivering meaningful analytical value.

---

## Why Power BI?

### Alternatives Considered
- Tableau  
- Looker  
- Apache Superset  

### Why Power BI Was Selected
- Native Azure integration  
- Industry adoption  
- Rich visualization ecosystem  
- Strong dashboarding capabilities  
- Widely used in enterprise analytics environments  

### Trade-off
Tableau offers greater visualization flexibility, but Power BI provides better integration within the Microsoft ecosystem.

---

## Why Directly Connect Power BI to ADLS Gold Layer?

### Alternatives Considered
- Dedicated SQL Pool  
- Synapse Serverless SQL Views  

### Why Direct ADLS Access Was Selected
The Gold layer already contained business-ready analytical marts stored in Parquet format.  

Connecting Power BI directly to Gold datasets:  
- Reduced architecture complexity  
- Eliminated unnecessary query layers  
- Avoided additional SQL maintenance  
- Leveraged Parquet's optimized analytical performance  

### Trade-off
A SQL semantic layer can simplify business-user access in larger organizations, but direct Gold-layer access is sufficient and efficient for this project's scope.
