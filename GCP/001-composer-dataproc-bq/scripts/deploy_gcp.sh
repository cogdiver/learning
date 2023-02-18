#!/bin/bash

read -p "GCP Account: " account
read -p "GCP Project: " project

gcloud config set account $account
gcloud config set project $project

gcloud services disable composer.googleapis.com --force
gcloud services enable composer.googleapis.com

# gcloud composer environments create dev \
#     --location us-east1

# gsutil mb -l us-east1 gs://bucket_1_composer_dataproc
# gsutil mb -l us-east1 gs://bucket_3_composer_dataproc

# gsutil cp dags/*.py gs://$bucket/dags/
