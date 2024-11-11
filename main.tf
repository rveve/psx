resource "aws_s3_bucket" "b" {
  for_each = local.buckets_set
    bucket = each.key
    force_destroy = true
}
