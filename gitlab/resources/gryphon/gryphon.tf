terraform {
  required_providers {
    gitlab = {
      source = "gitlabhq/gitlab"
      version = "3.18.0"
    }
  }
}

provider "gitlab" {
  token    = "8225526e2656be28b1dfdcb48988746c"
  base_url = "http://gitlab/api/v4/"
}

variable "nest_of_gold_project_id" {
  description = "nest-of-gold project id"
  type        = number
}

variable "awesome_app_project_id" {
  description = "awesome_app project id"
  type        = number
}

variable "pygryphon_project_id" {
  description = "pygryphon project id"
  type        = number
}

### Schedules ###
resource "gitlab_pipeline_schedule" "nest_of_gold_schedule" {
  project     = var.nest_of_gold_project_id
  description = "Schedule main"
  ref         = "main"
  cron        = "*/1 * * * *"
}

resource "gitlab_pipeline_schedule" "awesome_app_schedule" {
  project     = var.awesome_app_project_id
  description = "Schedule main"
  ref         = "main"
  cron        = "*/1 * * * *"
}