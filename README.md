# Youtube Data Analysis Project

### Brief

A Data Engineering project aiming to manage, streamline and produce reports from the Youtube videos data.

### Project Goals
1. **Data Ingestion:** Building a mechanism to ingest data from different sources.

2. **ETL System:** Transforming the raw unformatted data (Json) into structured and processed data (Apache Parquet).

3. **Data Lake:** Setting up a storage schema using Amazon S3 to facilitate incoming data from various sources.

4. **Scalability:** As the size of our data increases, we need to make sure our system scales with it.

5. **Cloud:** Using AWS, creating a scalable and cost effective system to store, manage and analyse data.

### AWS Services leveraged
1. **Amazon S3:** S3 is used to create a data lake for facilitating incoming raw data. Data from sources will be stored in the S3 buckets provisioned for the source.

2. **AWS IAM:** Using Identity Access Manager, I am ensuring the least privildge methodology. Any service used is only given the required access to function.

3. **AWS Glue:** Glue is being used to crawl through the data and provide us a Catalog for the data.

4. **AWS Lambda:** Using Lambda, I am cleaning and transforming the raw json data and converting it into Apache Parquet format for easy analysis.

5. **AWS Athena:** Athena is used to query the cleaned and transformed data.

6. **AWS CloudFormation:** Using Cloudformation stacks and templates, I am ensuring a robust and efficient architecture in which the user can create and leverage the AWS service usage in an automated way without using the AWS Console itself.

7. **AWS CodePipeline:** CodePipeline is being used to integrate the codespace (GitHub) with the AWS environment for managing and ensuring safe working of the system.

### Dataset Used
 - https://www.kaggle.com/datasets/datasnaek/youtube-new
 
   - This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months.
   - There are up to 200 trending videos published every day for many locations.
   - The data for each region is in its own file.
   - The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data.
   - A category_id field, which differs by area, is also included in the JSON file linked to the region.

### Architecture Diagram
<img src="architecture.jpeg">

**Disclaimer/Credits:** 
- This project is inspired by a Data Engineering Tutorial from Youtube Creator Darshil Parmar.

  - Darshil Parmar's Youtube Channel: https://www.youtube.com/@DarshilParmar

- However, there have been some enhancements added at my end such as the CI/CD implementation using CloudFormation and CodePipeline.
