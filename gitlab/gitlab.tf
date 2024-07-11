terraform {
  required_providers {
    gitlab = {
      source = "gitlabhq/gitlab"
      version = "17.1.0"
    }
  }
}

### Providers ###
provider "gitlab" {
  token    = "60b6c7ba41475b2ebdded2c0d3b079f0"
  base_url = "http://gitlab/api/v4/"
}

### Modules ###
module "gryphon" {
  source                  = "./resources/gryphon"
  nest_of_gold_project_id = gitlab_project.nest_of_gold_project.id
  awesome_app_project_id = gitlab_project.awesome_app_project.id
  pygryphon_project_id = gitlab_project.pygryphon_project.id
}

### Scripts ###
resource "null_resource" "gryphon_sh" {
  provisioner "local-exec" {
    command = "/bin/sh /setup/resources/gryphon/token.sh"
  }
  depends_on = [gitlab_project_membership.nest_of_gold_membership, gitlab_project_membership.awesome_app_membership]
}

### Users ###
resource "gitlab_user" "alice" {
  name             = "alice"
  username         = "alice"
  password         = "alice1234"
  email            = "alice@wonderland.com"
  is_admin         = false
  projects_limit   = 0
  can_create_group = false
  is_external      = false
  reset_password   = false
}

resource "gitlab_user" "gryphon" {
  name             = "gryphon"
  username         = "gryphon"
  password         = "^SKF$T6c9C1*"
  email            = "gryphon@wonderland.com"
  is_admin         = false
  projects_limit   = 0
  can_create_group = false
  is_external      = false
  reset_password   = false
}

### Groups ###
resource "gitlab_group" "wonderland_group" {
  name             = "Wonderland"
  path             = "wonderland"
  description      = "An pygryphon group"
  visibility_level = "public"
}

resource "gitlab_group" "pygryphon_group" {
  name             = "pygryphon"
  path             = "pygryphon"
  description      = "group for pygrphon"
  visibility_level = "public"
}

### Projects ###
resource "gitlab_project" "pygryphon_project" {
  name                   = "pygryphon"
  description            = "A servant to the Queen who befriends Alice. The Gryphon escorts Alice to see the Mock Turtle"
  namespace_id           = gitlab_group.pygryphon_group.id
  shared_runners_enabled = true
  visibility_level       = "public"
}

resource "gitlab_project" "nest_of_gold_project" {
  name                   = "nest-of-gold"
  namespace_id           = gitlab_group.wonderland_group.id
  shared_runners_enabled = true
  visibility_level       = "public"
}

resource "gitlab_project" "awesome_app_project" {
  name                   = "awesome-app"
  namespace_id           = gitlab_group.wonderland_group.id
  shared_runners_enabled = true
  visibility_level       = "public"
  depends_on             = [
    gitlab_project.pygryphon_project
  ]
}

### Memberships ###
resource "gitlab_project_membership" "nest_of_gold_membership" {
  project   = gitlab_project.nest_of_gold_project.id
  user_id      = gitlab_user.gryphon.id
  access_level = "maintainer"
}

resource "gitlab_project_membership" "awesome_app_membership" {
  project   = gitlab_project.awesome_app_project.id
  user_id      = gitlab_user.gryphon.id
  access_level = "maintainer"
}

resource "gitlab_project_membership" "pgryphon_membership" {
  project   = gitlab_project.pygryphon_project.id
  user_id      = gitlab_user.alice.id
  access_level = "maintainer"
}

### Variables ###
resource "gitlab_group_variable" "nest_of_gold_token_variable" {
  group = gitlab_group.wonderland_group.id
  key     = "TOKEN"
  masked  = true
  value   = "04b6bdf425dbd720a34705a398500937"
}

resource "gitlab_project_variable" "nest_of_gold_flag11_variable" {
  project = gitlab_project.nest_of_gold_project.id
  key     = "FLAG11"
  masked  = true
  value   = "7ED44218-C9CC-4824-BC85-C9841305A642"
}

resource "gitlab_project_variable" "nest_of_gold_key_variable" {
  project = gitlab_project.nest_of_gold_project.id
  key     = "SSH_KEY"
  masked  = true
  value   = "LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05dVpRQUFBQUFBQUFBQkFBQUJsd0FBQUFkemMyZ3RjbgpOaEFBQUFBd0VBQVFBQUFZRUF6S01RWTlUN1IySkJEakZ1eEN4UVd4S0k5TmYzOUVkZXdNcFNZZmdSNEFzbFNjRXpKSlgwCk8zbGZrcTFqYWxMNHpwMDY2YkZrVTIxTTNwNDJoVmdYbkJyY1ZPUjdKVTNGaUVGRHc0cWZFMkNjSlRYRkhMNG9iQXFGaXkKY3A2UnhzSWpSSW9Sejh6ckJJNTdrOEN5aHFaSzEwNHh0NzlYRGtXY0RuQTdsY3RCd3E5RHE5dnhzSzhTcVh2VzRjSlR1Nwpvc295TWl0TzNSUDN4MEVZb2NzTk5uVEROQmoxSklNc2ZtU2tPdTUwM0xGWnFBdXFoY2hLbTdCY25wZU9ZVDJxS1J1RnF2CkJvd2tsZWdDWlJXWk5XU1ZJMWxHaFVRUTN3RGdFazBkcVVQekhsT2hEeDRoTkFlVC9SWHR0bGxZK2x4Y2kwMEVGbWpSczMKWFhnY3VscFhSczNjeUMrVDNJdG40clFvRTVBVjUxOTFtSXV3dWZvelhDaUdnRmhPS2ZPbVllOFpIQ2NJMDlwbVQyeFo5bQpDcHE1VmhhckxLSFIza3U0eXkzTkVZWnJPY052aElmU2xrRkNUWVY1SUtYcjlWY1MzZitLTU5yQmd2RUYwdEVxbzNzeTg3CjFiYlVJbmpDVFZpTXZDUzhHMnVGUWxudk1SaVc0K0ZOeUNjU1VxcEJBQUFGa0F6cGVBRU02WGdCQUFBQUIzTnphQzF5YzIKRUFBQUdCQU15akVHUFUrMGRpUVE0eGJzUXNVRnNTaVBUWDkvUkhYc0RLVW1INEVlQUxKVW5CTXlTVjlEdDVYNUt0WTJwUworTTZkT3VteFpGTnRUTjZlTm9WWUY1d2EzRlRrZXlWTnhZaEJROE9LbnhOZ25DVTF4UnkrS0d3S2hZc25LZWtjYkNJMFNLCkVjL002d1NPZTVQQXNvYW1TdGRPTWJlL1Z3NUZuQTV3TzVYTFFjS3ZRNnZiOGJDdkVxbDcxdUhDVTd1NkxLTWpJclR0MFQKOThkQkdLSExEVFowd3pRWTlTU0RMSDVrcERydWROeXhXYWdMcW9YSVNwdXdYSjZYam1FOXFpa2JoYXJ3YU1KSlhvQW1VVgptVFZrbFNOWlJvVkVFTjhBNEJKTkhhbEQ4eDVUb1E4ZUlUUUhrLzBWN2JaWldQcGNYSXROQkJabzBiTjExNEhMcGFWMGJOCjNNZ3ZrOXlMWitLMEtCT1FGZWRmZFppTHNMbjZNMXdvaG9CWVRpbnpwbUh2R1J3bkNOUGFaazlzV2ZaZ3FhdVZZV3F5eWgKMGQ1THVNc3R6UkdHYXpuRGI0U0gwcFpCUWsyRmVTQ2w2L1ZYRXQzL2lqRGF3WUx4QmRMUktxTjdNdk85VzIxQ0o0d2sxWQpqTHdrdkJ0cmhVSlo3ekVZbHVQaFRjZ25FbEtxUVFBQUFBTUJBQUVBQUFHQVJlc1JGb3NXci9VcU5TYytxVmhhdkVOQStDCmN5V1F4cG00V0ZVR1BwOTVyWFNyUHdQWGZlMHROTmpGZ2h0NXBSMklad01waWhwcitabkJhQ21selc5RWRaTU1oQUt5YS8KYnlhZGVKcE1iOXA2ZjF3MzFQSkQ3V1pLNnBpZkFUN3MwMkw1emRLUnJpMGRPODlXYkptS2dJdWpmRlZQclRTOVVNMVFJVAoyY0p3M1l2MG15dXpFS05BeFJmQys2L2gzQ3BvUmZValRwNVMrRllWY2tpMk5OU0dYc3JFZzZ1aGIzaE5mdUpSU0VhVU5QClZ0TmxtQUF2UGJLc2NxTmx5bU8rdTFFUDlXMzRVRFJDTnFHZExaeEZzNjUxYTUwcW1tUXZUQU1ZSENPVEZVRTNDaEduRUkKQkdMRXRzT2tZS2xFblFnNXFRSUhLTEpFeEgwYTJiMGZWRnJHSzdkY1ZLM2tjN3hMZ0d3dnh1RnZLbDREZU1nQ1g1cTg1ZwowMk11OU9kY3Npbzd0NkdvNnNYVGlCM1YvSWRiemNwM3piTzNCNzZBUUR6aGp6VHRHWU9OUFIrYUR0aGZuSklKaHl4UkpnCm1hRTlJSFdJcGlXZTBnempuU3M0SEJHcUYwRjZSci9YSWJqTi81M3dCbXlNTzZlVnEyd0FIYlJ1L05FZ2lzY3RmaEFBQUEKd1FDdUltZVRuTDhmR29mYjNqVEFZZWNrVFBpVXNNMlJzc2hTYndsWmFYM1RSNFRXTnUwbWNjOTRoWUJ1dEljRzJTTVZYYwpGNGk5amw2Y2RnQWZmNDN1b1B5OEdLaUdjOWpGNGV5bGt5NGM0Zmd3N0V6YnRGTVBtcEZudGVBL09oMFN4bHhobVVEVkhVCm14Umtzc0RTSTdaaWY2ejJLYVQzWjl5SzkyeS8yNjVTbTJna0lVc2htMkJOcGxnc3NDZElrTnRxWmFlUEJtSHI2LzA5b0oKaFJTSm1tZ2tlc3g3VEo5QnFWdXVpWmRuM0U3MVhOSHNiQk95RDA4Y0xyWkVvTnRqa0FBQURCQVBLVzh0clhVL0g4NURPbAptOVpONlZHSWJuRmd0SXRVTjhudHNTMnNySjNONVZ5Zk5pR2czcE0zcDBwV3RPbVNnalRQanJiZUV0YjQ0TzczLzB6MzhXCkhmenBoc2JnSGcwVFZWRUZOMjhON3lMSFlwTVJrTFB6NzBoL1JJQkxSbWFacklZS3VRK0tnU0FQQUt5ZG5IYVY4SkpWNzUKdWJPVGI2SUVHY1I5akZPanduRWUrN3BDM0FaT3dka3N0UXFDTThtVVdVeXdxS1ZRMmo0aUZlQ1d5R2MyaldHcTN0cFQ5QwpvUnExV2l2NTZLTzhJSkdIZklBY3pLeVR5THdyeGd4d0FBQU1FQTEvTUZibGwrN2ZpcjdlTmFKdUQybmh2T1ZxMEJsQlRqCktMT2xDZ1puQnNXaGgrdUwrLzdoelBRSmRHOXFaeWprMm5rUGVVemd3Z2ZidHNqRGhwMThkMXJOK1p2UDdtWGd0elMwMksKb3duQ0RjUXord2VPL0JoQUZGbDZJa0RQQjBYbkM4b0MwUE5LczlQcDlTS2xraUR0VEtjdkZDT0JhcTVMT24zWEZRZGFaUgpsRkFlQ3RwTEZaZDFhcW96TCtXeGRoSitPbFVNV2V4QUhOVkluWDN2TTI0NVIyaGlTRUhKZkNNS3dLbWRRMm5rcHlDak16Cm5GWDJZTEVGZTlCcVMzQUFBQUYyRnphVUJCYzJGbUxrZHlaV1Z1YUc5c2RITXRUVUpRQVFJRAotLS0tLUVORCBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0K"
}

### Job token ###
resource "gitlab_project_job_token_scopes" "explicit_deny" {
  project_id         = gitlab_project.awesome_app_project.id
  target_project_ids = []
}

### Branch Protection Rules ###
resource "gitlab_branch_protection" "bpr_pygryphon" {
  project                      = gitlab_project.pygryphon_project.id
  branch                       = "main"
  push_access_level            = "maintainer"
  merge_access_level           = "maintainer"
  unprotect_access_level       = "maintainer"
  allow_force_push             = false
}
