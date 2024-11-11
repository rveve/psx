locals {
     buckets_set = toset(split(",", var.bucket_names))
}
