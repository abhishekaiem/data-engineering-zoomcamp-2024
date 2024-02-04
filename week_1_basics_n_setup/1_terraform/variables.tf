variable "credentials" {
  description = "My GCP credentials"
  default     = "../keys/my-creds.json"

}

variable "bq_dataset_name" {
  description = "My big query dataset name"
  default     = "trips_all_data"

}

variable "gcs_bucket_name" {
  description = "My bucket name"
  default     = "hardy-pattern-413201-de-zoomcamp"
}

variable "gcs_project_id" {
  description = "Project Name"
  default     = "hardy-pattern-413201"
}

variable "region" {
  description = "Project Location"
  default     = "asia-south1"
}

variable "location" {
  description = "Project Location"
  default     = "asia-south1"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
