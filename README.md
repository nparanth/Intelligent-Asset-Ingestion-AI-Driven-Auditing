# **Intelligent Asset Ingestion & Functionless AI-Driven Auditing**

## Project Overview
The project is a mission-critical ingestion pipeline designed for data ingestion. It automates the auditing of technical assets (3D CAD models) using a **Functionless Serverless Architecture**. 

By leveraging **Amazon Bedrock (Claude 3)** and **EventBridge Pipes**, this system eliminates the overhead of managing Lambda functions, providing a highly scalable, secure, and cost-effective registry for engineering data.

---

##  Architecture: The 4-Phase Strategy

### **Phase 1: Secure Edge Ingestion & Control**
*   **Hardened S3 "Raw Zone":** Private bucket utilizing **SSE-KMS** and **S3 Bucket Keys** to reduce cryptographic overhead costs by up to 90% during bulk uploads.
*   **Object Lock (Governance Mode):** Ensures data immutability for 30 days, meeting strict maritime compliance and anti-ransomware standards.

### **Phase 2: Resilient Event Buffering**
*   **EventBridge Integration:** Captures `Object Created` events directly from S3.
*   **SQS (The Shock Absorber):** Decouples ingestion from processing. This protects the **Amazon Bedrock** model from being throttled by queuing requests during high-volume data dumps.

### **Phase 3: The "AI-Powered" Brain (Functionless Orchestration)**
*   **EventBridge Pipes:** A modern "glue" component that polls SQS and triggers the workflow without custom Lambda code.
*   **Step Functions (Standard Workflow):** The mission controller that manages the logic natively.
    *   **Task 1: Amazon Bedrock Integration:** Directly passes metadata and prompts to **Claude 3** for technical validation.
    *   **Task 2: DynamoDB Asset Registry:** Writes the "Golden Record"—linking the file metadata to its AI-generated audit score.

### **Phase 4: Real-Time Governance**
*   **DynamoDB Registry:** Stores the final analysis, including timestamps and AI-driven results for immediate engineering review.
*   **SNS:** Dispatches an "Action Required" alert to lead engineers with a summary of the AI-generated audit results the moment a record is finalized.
   
---

## Technical Stack
| Category | Service |
| :--- | :--- |
| **Infrastructure** | AWS CloudFormation (IaC) |
| **AI / ML** | Amazon Bedrock (Anthropic Claude 3 Sonnet) |
| **Orchestration** | AWS Step Functions & EventBridge Pipes |
| **Messaging** | Amazon SQS & EventBridge |
| **Database** | Amazon DynamoDB (On-Demand) |
| **Security** | AWS KMS |

---

##  Key Performance Features
*   **Minimized Lambda Footprint:** While a lightweight Lambda handles secure pre-signed URL generation for frontend uploads, the entire data processing and AI orchestration logic is 100% functionless, using native service-to-service integrations to eliminate cold starts in the mission-critical path.
*   **Cost Optimization:** Leverages DynamoDB `PAY_PER_REQUEST` and S3 Bucket Keys to ensure costs only scale with actual activity.
*   **Intelligent Retries:** Built-in Exponential Backoff within the State Machine handles transient AI model API errors automatically.

---

##  Deployment & Setup

### **Prerequisites**
*   **Model Access:** You must manually enable **Claude 3 Sonnet** access in the AWS Bedrock Console (e.g., in `us-east-1`).
*   **AWS CLI:** Installed and configured with appropriate IAM permissions.

### **Standard Deployment**
1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>

2. **Deploy via CloudFormation:**
    ```
    aws cloudformation deploy \
     --template-file template.yaml \
     --stack-name ShipyardEngineeringVault \
     --capabilities CAPABILITY_NAMED_IAM

