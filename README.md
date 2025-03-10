# Serverless TODO Task Manager

A scalable serverless web application built using Google Cloud Platform (GCP) services, providing efficient task management with CRUD operations and CSV export functionality.

## Overview

The Serverless TODO Task Manager leverages the power of:
- **Cloud Functions** for serverless computing.
- **Firestore** as a scalable NoSQL database.
- **Cloud Storage** for exporting tasks in CSV format.

## Key Features

- **Task Creation:** Create tasks with details like name, description, status, and due date.
- **Task Retrieval:** Fetch all tasks efficiently in JSON format.
- **Task Update:** Seamlessly update task details using task IDs.
- **Task Deletion:** Remove tasks securely using task IDs.
- **Export Tasks:** Automatically export all tasks to Cloud Storage as a CSV file for backup and analytics.

## APIs Available

| Method  | Endpoint           | Description                                    |
| ------- | ------------------ | ---------------------------------------------- |
| **POST**   | `/createTask`      | Create a new task                              |
| **GET**    | `/GetAllTasks`     | Retrieve all tasks                             |
| **PUT**    | `/updateTask`      | Update an existing task                        |
| **DELETE** | `/removeTask`      | Delete a specific task                         |
| **POST**   | `/exportTasksCSV`  | Export all tasks to Cloud Storage as CSV       |

## Technologies Used

- Google Cloud Functions
- Google Firestore (NoSQL)
- Google Cloud Storage
- RESTful APIs
- Postman (for testing)

## Deployment and Testing

Deployed APIs are tested using Postman to ensure reliability. cURL examples are provided in the repository for easy API interaction.

Clone the repository, configure your GCP credentials, and deploy Cloud Functions using the Google Cloud CLI:

```bash
gcloud functions deploy [FUNCTION_NAME] --runtime nodejs20 --trigger-http --allow-unauthenticated
