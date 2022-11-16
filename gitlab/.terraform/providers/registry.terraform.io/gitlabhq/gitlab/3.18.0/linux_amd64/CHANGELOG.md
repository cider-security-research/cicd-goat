## 3.18.0 (2022-09-05)

This release was tested against GitLab 15.1, 15.2 and 15.3 for both CE and EE.

FEATURES

* **New Resource:** `gitlab_group_saml_link` ([#1243](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1243))

## 3.17.0 (2022-08-24)

This release was tested against GitLab 15.1, 15.2 and 15.3 for both CE and EE.

FEATURES:

* **New Data Source:** `gitlab_project_hook` ([#1204](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1204))
* **New Data Source:** `gitlab_project_hooks` ([#1204](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1204))
* **New Data Source:** `gitlab_project_membership` ([#593](https://github.com/gitlabhq/terraform-provider-gitlab/pull/593))
* **New Data Source:** `gitlab_repository_tree` ([#1198](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1198))
* **New Data Source:** `gitlab_group_hook` ([#1221](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1221))
* **New Data Source:** `gitlab_group_hooks` ([#1221](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1221))
* **New Resource:** `gitlab_group_hook` ([#1221](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1221))
* **New Resource:** `gitlab_application_settings` (experimental) ([#1201](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1201))
* **New Resource:** `gitlab_project_issue_board` ([#1173](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1173))
* **New Resource:** `gitlab_user_gpgkey` ([#1181](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1181))

IMPROVEMENTS:

* resource/gitlab_service_jira: Support `jira_issue_transition_id` attribute for GitLab 15.2 ([#1188](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1188))
* resource/gitlab_project_protected_environment: Add docs that users and groups must be shared with the project ([#1210](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1210))
* resource/gitlab_branch_protection: Automatically take ownership of projects default branch without an import ([#1216](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1216))
* resource/gitlab_group_ldap_link: Clarify value for `ldap_provider` attribute ([#1220](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1220))
* resource/gitlab_group_membership: Support `skip_subresources_on_destroy` and `unassign_issuables_on_destroy` removal option attributes ([#1209](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1209))
* resource/gitlab_project: Reference doc for required `gitlab_group_project_template` resource when using `template_project_id` attribute ([#1223](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1223))

BUG FIXES:

* resource/gitlab_user_sshkey: Ignore leading and trailing whitespaces in key ([#1175](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1175))
* resource/gitlab_project: Fix setting `ci_forward_deployment_enabled` to `false` during creation ([#1218](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1218))

## 3.16.1 (2022-07-11)

This release was tested against GitLab 14.10, 15.0 and 15.1 for both CE and EE.

BUG FIXES:

* resource/gitlab_project: Fix admin token requirement to check default branch protection ([#1169](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1169))

## 3.16.0 (2022-07-07)

This release was tested against GitLab 14.10, 15.0 and 15.1 for both CE and EE.

FEATURES:

* **New Data Source:** `gitlab_current_user` ([#1118](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1118))
* **New Data Source:** `gitlab_release_link` ([#1131](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1131))
* **New Data Source:** `gitlab_release_links` ([#1131](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1131))
* **New Resource:** `gitlab_release_link` ([#1131](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1131))
* **New Resource:** `gitlab_cluster_agent_token` ([#1147](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1147))

IMPROVEMENTS:

* resource/gitlab_project_protected_environment: Add `required_approval_count` attribute ([#1097](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1097))
* resource/gitlab_project_access_token: Add `owner` as possible value to `access_level` ([#1145](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1145))
* resource/gitlab_project_membership: Add `owner` as possible value to `access_level` ([#1145](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1145))
* resource/gitlab_project_share_group: Add `owner` as possible value to `access_level` ([#1145](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1145))
* resource/gitlab_project: Add `ci_default_git_depth` attribute ([#1146](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1146))
* datasource/gitlab_project: Add `ci_default_git_depth` attribute ([#1146](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1146))
* datasource/gitlab_projects: Add `ci_default_git_depth` attribute ([#1146](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1146))

BUG FIXES:

* resource/gitlab_project: Fix project creation when default branch protection is disabled on instance-level ([#1128](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1128))
* resource/gitlab_project: Fix a case where a change to a project in terraform can never apply when certain fields are modified ([#1158](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1158))
* resource/gitlab_project: Fix passing `false` to API for explicitly set optional attributes ([#1152](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1152))
* resource/gitlab_group: Fix passing false to API for explicitly set optional attributes ([#1152](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1152))

## 3.15.1 (2022-06-08)

This release was tested against GitLab 14.9, 14.10 and 15.0 for both CE and EE.

BUG FIXES:

* resource/gitlab_service_microsoft_teams: Fix removal from state when integration is not found ([#1113](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1113))

## 3.15.0 (2022-05-29)

This release was tested against GitLab 14.9, 14.10 and 15.0 for both CE and EE.

FEATURES:

* **New Data Source:** `gitlab_cluster_agent` ([#1073](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1073))
* **New Data Source:** `gitlab_cluster_agents` ([#1073](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1073))
* **New Data Source:** `gitlab_project_milestone` ([#1044](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1044))
* **New Data Source:** `gitlab_project_milestones` ([#1044](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1044))
* **New Resource:** `gitlab_project_milestone` ([#1044](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1044))
* **New Resource:** `gitlab_runner` ([#1049](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1049))
* **New Resource:** `gitlab_cluster_agent` ([#1073](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1073))

IMPROVEMENTS:

* resource/gitlab_group: Allow value `3` for `default_branch_protection` attribute ([#1070](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1070))
* resource/gitlab_project_badge: Add `name` attribute ([#1052](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1052))
* resource/gitlab_group: Transfer a subgroup does not longer re-create the group ([#1078](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1078))
* resource/gitlab_topic: Add `name` attribute ([#1095](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1095))

BUG FIXES:

* resource/gitlab_project_issue: Remove `Optional` from `Computed`-only attributes ([#1081](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1081))
* datasource/gitlab_project_issues: Fix type of `not_milestone` attribute from list of strings to a single string ([#1095](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1095))


## 3.14.0 (2022-05-02)

FEATURES:

* **New Data Source:** `gitlab_project_variable` ([#990](https://github.com/gitlabhq/terraform-provider-gitlab/pull/990))
* **New Data Source:** `gitlab_project_variables` ([#990](https://github.com/gitlabhq/terraform-provider-gitlab/pull/990))
* **New Data Source:** `gitlab_group_variable` ([#990](https://github.com/gitlabhq/terraform-provider-gitlab/pull/990))
* **New Data Source:** `gitlab_group_variables` ([#990](https://github.com/gitlabhq/terraform-provider-gitlab/pull/990))
* **New Data Source:** `gitlab_instance_variable` ([#990](https://github.com/gitlabhq/terraform-provider-gitlab/pull/990))
* **New Data Source:** `gitlab_instance_variables` ([#990](https://github.com/gitlabhq/terraform-provider-gitlab/pull/990))
* **New Resource:** `gitlab_group_project_file_template` ([#971](https://github.com/gitlabhq/terraform-provider-gitlab/pull/971))
* **New Resource:** `gitlab_service_external_wiki` ([#1003](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1003))
* **New Resource:** `gitlab_project_runner_enablement` ([#1016](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1016))
* **New Resource:** `gitlab_personal_access_token` ([#1007](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1007))

IMPROVEMENTS:

* resource/gitlab_deploy_key: Fully support `can_push` attribute ([#1009](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1009))
* resource/gitlab_deploy_key_enable: Fully support `can_push` attribute ([#1009](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1009))
* resource/gitlab_group_access_token: Support `owner` as access level ([#999](https://github.com/gitlabhq/terraform-provider-gitlab/pull/999))
* resource/gitlab_pipeline_trigger: Mark `token` attribute as sensitive ([#1034](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1034))
* resource/gitlab_project: Deprecate `build_coverage_regex` ([#1036](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1036))
* resource/gitlab_project_access_token: Add `access_level` attribute ([#997](https://github.com/gitlabhq/terraform-provider-gitlab/pull/997))
* resource/gitlab_project_protected_environment: Support multiple `deploy_access_levels` ([#1004](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1004))
* resource/gitlab_project_mirror: Support deletion on destroy ([#988](https://github.com/gitlabhq/terraform-provider-gitlab/pull/988))
* resource/gitlab_repository_file: Add `execute_filemode` attribute ([#1038](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1038))
* resource/gitlab_user: Add `namespace_id` attribute ([#987](https://github.com/gitlabhq/terraform-provider-gitlab/pull/987))
* datasource/gitlab_user: Add `namespace_id` attribute ([#987](https://github.com/gitlabhq/terraform-provider-gitlab/pull/987))
* datasource/gitlab_users: Add `namespace_id` attribute ([#987](https://github.com/gitlabhq/terraform-provider-gitlab/pull/987))

BUG FIXES:

* resource/gitlab_service_slack: Fix a resource ID bug that causes `gitlab_service_slack` resources that were created before provider version 3.9.0 to return an error. ([#1013](https://github.com/gitlabhq/terraform-provider-gitlab/pull/1013))

## 3.13.0 (2022-03-30)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

FEATURES:

* **New Data Source:** `gitlab_instance_deploy_keys` ([#870](https://github.com/gitlabhq/terraform-provider-gitlab/pull/870))
* **New Data Source:** `gitlab_project_tags` ([#963](https://github.com/gitlabhq/terraform-provider-gitlab/pull/963))
* **New Data Source:** `gitlab_repository_file` ([#939](https://github.com/gitlabhq/terraform-provider-gitlab/pull/939))
* **New Resource**: `gitlab_project_environment` ([#938](https://github.com/gitlabhq/terraform-provider-gitlab/pull/938))
* **New Resource**: `gitlab_project_protected_environment` ([#938](https://github.com/gitlabhq/terraform-provider-gitlab/pull/938))
* **New Resource**: `gitlab_system_hook` ([#929](https://github.com/gitlabhq/terraform-provider-gitlab/pull/929))
* resource/gitlab_topic: Support deletion ([#967](https://github.com/gitlabhq/terraform-provider-gitlab/pull/967))
* resource/gitlab_topic: Support avatar images ([#968](https://github.com/gitlabhq/terraform-provider-gitlab/pull/968))
* resource/gitlab_repository_file: Support using plain text `content` to beautify plans ([#972](https://github.com/gitlabhq/terraform-provider-gitlab/pull/972))

IMPROVEMENTS:

* resource/gitlab_branch_protection: Make `push_access_level` and `merge_access_level` optional ([#934](https://github.com/gitlabhq/terraform-provider-gitlab/pull/934))
* resource/gitlab_branch_protection: Add `unprotect_access_level` and `allowed_to_unprotect` attributes ([#934](https://github.com/gitlabhq/terraform-provider-gitlab/pull/934))
* resource/gitlab_pipeline_schedule: Use single GET API to read resource details to increase performance ([#955](https://github.com/gitlabhq/terraform-provider-gitlab/pull/955))
* resource/gitlab_project_variable: Use single GET API to read resource details to increase performance ([#953](https://github.com/gitlabhq/terraform-provider-gitlab/pull/953))
* resource/gitlab_deploy_token: Support `terraform import` ([#960](https://github.com/gitlabhq/terraform-provider-gitlab/pull/960))
* resource/gitlab_project_access_token: Support `terraform import` ([#960](https://github.com/gitlabhq/terraform-provider-gitlab/pull/960))
* resource/gitlab_project_hook: Support `terraform import` ([#960](https://github.com/gitlabhq/terraform-provider-gitlab/pull/960))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `analytics_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `auto_cancel_pending_pipelines` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `auto_devops_deploy_strategy` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `auto_devops_enabled` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `autoclose_referenced_issues` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `build_git_strategy` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `builds_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `container_expiration_policy` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `container_registry_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `emails_disabled` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `external_authorization_classification_label` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `forking_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `issues_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `merge_commit_template` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `merge_requests_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `operations_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `public_builds` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `repository_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `repository_storage` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `requirements_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `resolve_outdated_diff_discussions` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `security_and_compliance_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `squash_commit_template` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `topics` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_project, datasource/gitlab_project, datasource/gitlab_projects: Add `wiki_access_level` attribute ([#917](https://github.com/gitlabhq/terraform-provider-gitlab/pull/917))
* resource/gitlab_managed_license: Add support for "allowed" and "denied" to align with upcoming GitLab 15.0 deprecations ([#952](https://github.com/gitlabhq/terraform-provider-gitlab/pull/952))

BUG FIXES:

* resource/gitlab_deploy_token: Implement pagination when reading tokens to find all existing tokens ([#941](https://github.com/gitlabhq/terraform-provider-gitlab/pull/941))
* resource/gitlab_project_approval_rule: Implement pagination when reading approval rules to find all existing ones ([#950](https://github.com/gitlabhq/terraform-provider-gitlab/pull/950))
* resource/gitlab_repository_file: Implement locking and retry within the provider to mitigate parallelism limits ([#964](https://github.com/gitlabhq/terraform-provider-gitlab/pull/964))

## 3.12.0 (2022-03-08)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

FEATURES:

* **New Resource:** `gitlab_project_tag` ([#910](https://github.com/gitlabhq/terraform-provider-gitlab/pull/910))
* **New Resource:** `gitlab_project_issue` ([#891](https://github.com/gitlabhq/terraform-provider-gitlab/pull/891))
* **New Data Source:** `gitlab_project_tag` ([#910](https://github.com/gitlabhq/terraform-provider-gitlab/pull/910))
* **New Data Source:** `gitlab_project_issue` ([#891](https://github.com/gitlabhq/terraform-provider-gitlab/pull/891))
* **New Data Source:** `gitlab_project_issues` ([#891](https://github.com/gitlabhq/terraform-provider-gitlab/pull/891))

IMPROVEMENTS:

* datasource/gitlab_group: Add `prevent_forking_outside_group` attribute ([#914](https://github.com/gitlabhq/terraform-provider-gitlab/pull/914))
* resource/gitlab_group: Add `prevent_forking_outside_group` attribute ([#914](https://github.com/gitlabhq/terraform-provider-gitlab/pull/914))
* resource/gitlab_project_approval_rule: Add `rule_type` attribute ([#916](https://github.com/gitlabhq/terraform-provider-gitlab/pull/916))

BUG FIXES:

* resource/gitlab_project: Fix deletion drift handling ([#924](https://github.com/gitlabhq/terraform-provider-gitlab/pull/924))
* resource/gitlab_project_badge: Fix deletion drift handling ([#924](https://github.com/gitlabhq/terraform-provider-gitlab/pull/924))
* resource/gitlab_group_badge: Fix deletion drift handling ([#924](https://github.com/gitlabhq/terraform-provider-gitlab/pull/924))

## 3.11.1 (2022-03-02)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

BUG FIXES:

* resource/gitlab_project: fix waiting for default branch protection during creation ([#908](https://github.com/gitlabhq/terraform-provider-gitlab/pull/908))

## 3.11.0 (2022-03-01)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

FEATURES:

* **New Resource:** `resource/gitlab_user_sshkey` ([#903](https://github.com/gitlabhq/terraform-provider-gitlab/pull/903))

IMPROVEMENTS:

* resource/gitlab_instance_variable: better error message for invalid masked variable values ([#895](https://github.com/gitlabhq/terraform-provider-gitlab/pull/895))
* resource/gitlab_group_variable: better error message for invalid masked variable values ([#895](https://github.com/gitlabhq/terraform-provider-gitlab/pull/895))
* resource/gitlab_project: Add `merge_pipelines_enabled` and `merge_trains_enabled` attributes ([#900](https://github.com/gitlabhq/terraform-provider-gitlab/pull/900))
* resource/gitlab_project_level_mr_approvals: Add `required_password_to_approve` attribute ([#808](https://github.com/gitlabhq/terraform-provider-gitlab/pull/808))
* resource/gitlab_user: Add support for `deactivated` user state ([#899](https://github.com/gitlabhq/terraform-provider-gitlab/pull/899))

BUG FIXES:

* resource/gitlab_branch_protection: fix issue claiming that no valid access level([#892](https://github.com/gitlabhq/terraform-provider-gitlab/pull/892))

## 3.10.1 (2022-02-24)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

BUG FIXES:

* resource/gitlab_branch_protection: Fix issue which claimed that `no valid access level` can be found ([#892](https://github.com/gitlabhq/terraform-provider-gitlab/pull/892))

## 3.10.0 (2022-02-23)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

FEATURES:

* **New Resource:** `gitlab_group_access_token` ([#860](https://github.com/gitlabhq/terraform-provider-gitlab/pull/860))
* **New Resource:** `gitlab_topic` ([#871](https://github.com/gitlabhq/terraform-provider-gitlab/pull/871))

IMPROVEMENTS:

* datasource/gitlab_project: Add `printing_merge_request_link_enabled` attribute ([#783](https://github.com/gitlabhq/terraform-provider-gitlab/pull/783))
* datasource/gitlab_project: Add `ci_forward_deployment_enabled` attribute ([#732](https://github.com/gitlabhq/terraform-provider-gitlab/pull/732))
* datasource/gitlab_projects: Add `ci_forward_deployment_enabled` attribute ([#732](https://github.com/gitlabhq/terraform-provider-gitlab/pull/732))
* datasource/gitlab_group_membership: Support pagination ([#858](https://github.com/gitlabhq/terraform-provider-gitlab/pull/858))
* resource/gitlab_group_ldap_link: Add import support ([#771](https://github.com/gitlabhq/terraform-provider-gitlab/pull/771))
* resource/gitlab_project: Add `ci_forward_deployment_enabled` attribute ([#732](https://github.com/gitlabhq/terraform-provider-gitlab/pull/732))
* resource/gitlab_project: Add `printing_merge_request_link_enabled` attribute ([#783](https://github.com/gitlabhq/terraform-provider-gitlab/pull/783))
* resource/gitlab_project_hook: Add `releases_events` attribute ([#773](https://github.com/gitlabhq/terraform-provider-gitlab/pull/773))
* resource/gitlab_branch_protection: Add `allow_force_push` attribute ([#877](https://github.com/gitlabhq/terraform-provider-gitlab/pull/877))
* resource/gitlab_service_jira: Add `api_url` attribute ([#597](https://github.com/gitlabhq/terraform-provider-gitlab/pull/597))
* resource/gitlab_user: Add `state` attribute to allow blocking users ([#762](https://github.com/gitlabhq/terraform-provider-gitlab/pull/762))

BUG FIXES:

* datasource/gitlab_projects: Allow to get archived and unarchived repositories ([#855](https://github.com/gitlabhq/terraform-provider-gitlab/pull/855))
* resource/gitlab_group: Support setting `default_branch_protection` to `0` ([#856](https://github.com/gitlabhq/terraform-provider-gitlab/pull/856))
* resource/gitlab_group_ldap_link: Fix panic when setting group access level ([#873](https://github.com/gitlabhq/terraform-provider-gitlab/pull/873))
* resource/gitlab_project: Correctly handle push rules add and edit ([#838](https://github.com/gitlabhq/terraform-provider-gitlab/pull/838))
* resource/gitlab_project: Support creating project in group without default branch protection ([#856](https://github.com/gitlabhq/terraform-provider-gitlab/pull/856))
* resource/gitlab_project: Fix backwards-compatibility with 14.1 regarding the `squash_option` ([#867](https://github.com/gitlabhq/terraform-provider-gitlab/pull/867))
* resource/gitlab_project: Re-compute `path_with_namespace`, `ssh_url_to_repo`, `http_url_to_repo` and `web_url` attributes if `path` changes ([#875](https://github.com/gitlabhq/terraform-provider-gitlab/pull/875))

## 3.9.1 (2022-02-06)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

BUGFIXES:

* Fix crash in `gitlab_user` data source

## 3.9.0 (2022-02-04)

NOTES:

* resource/gitlab_service_slack: There was a breaking change to this resource in version 3.9.0 which was fixed in 3.14.0. Thus, if you have `gitlab_service_slack` resources that were created before 3.9.0, you should skip this version.

FEATURES:

* 0519c96 - Add `gitlab_repository_file` resource (#724)
* a915ccb - Add the `gitlab_project_access_token` resource (#588)
* 8564a07 - Add `gitlab_group_custom_attribute`, `gitlab_project_custom_attribute`, and `gitlab_user_custom_attribute` (#731)
* 39b0b6d - Add support for `gitlab_group_badge` resource (#673)
* dd0da2b - Implement configuration of the integration "Microsoft Teams" (#308) (#784)
* febe745 - Add `gitlab_project_protected_branch` and `gitlab_project_protected_branches` data sources (#551)
* b4d4f8d - Support `early_auth_check` flag in provider config (#787)
* 1455db0 - Add `gitlab_managed_license` resource (#700)
* be59cd1 - New `archive_on_destroy` attribute for `gitlab_project` (#816)

ENHANCEMENTS:

* 9863a61 - Add missing attributes to documentation (#802)
* 84d729e - Improve documentation around authentication with GitLab (#803)
* a9edc4a - Add environment scope to `gitlab_group_variable` (#717)
* c5a2f34 - Support `issues_template` and `merge_requests_template` attributes in project resource (#796)
* 65b8e9c - Add minimal access level permissions (#747)
* 12ae791 - Added missing scopes to deploy token (#769)
* 1455db0 - Update allowed access levels in `gitlab_branch_protection`, `gitlab_group_ldap_link`, `gitlab_group_membership`, `gitlab_group_share_group`, `gitlab_project_membership`, `gitlab_project_share_group`, and `gitlab_tag_protection` (#819)
* 1455db0 - New attribute `group_access` in `gitlab_project_share_group` and `gitlab_group_ldap_link` (attribute `access_level` is now considered deprecated on those resources) (#819)

BUGFIXES:

* f3b0f31 - Handle manually removed resources (#318)
* fc84cc3 - Properly allow arguments `id`or `path_with_namespace` for project data source (#806)
* d7059cf - Do not recreate project mirror on every run (#632)
* e57bf1d - Fix branch_protection documentation (#780)
* 912b647 - Fix docs for `gitlab_project_level_mr_approvals` import (#766)
* e89922e - instance_cluster/group_cluster: Suppress whitespace diff for kubernetes_ca_cert (#728)
* edda219 - gitlab_user: Do not set skip_confirmation on read (#491)

## 3.8.0 (Nov 19, 2021)

ENHANCEMENTS:
* More examples and better documentation ([#654](https://github.com/gitlabhq/terraform-provider-gitlab/pull/654))
* Adding a first complete example code ([#670](https://github.com/gitlabhq/terraform-provider-gitlab/pull/670))
* Support running the provider using an OAuth token ([#686](https://github.com/gitlabhq/terraform-provider-gitlab/pull/686))
* Allow merge on skipped pipeline ([#705](https://github.com/gitlabhq/terraform-provider-gitlab/pull/705))
* support default_branch_protection on group ([#706](https://github.com/gitlabhq/terraform-provider-gitlab/pull/706))
* Bump github.com/xanzy/go-gitlab from 0.50.0 to 0.51.1 ([#718](https://github.com/gitlabhq/terraform-provider-gitlab/pull/718))
* Add squash option ([#719](https://github.com/gitlabhq/terraform-provider-gitlab/pull/719))

BUGFIXES:
* Suppress whitespace diffs for kubernetes_ca_cert attribute ([#665](https://github.com/gitlabhq/terraform-provider-gitlab/pull/665))
* Fix GitLab project membership example ([#684](https://github.com/gitlabhq/terraform-provider-gitlab/pull/684))
* Improve tests for initializing a project without README ([#730](https://github.com/gitlabhq/terraform-provider-gitlab/pull/730))


## 3.7.0 (July 20, 2021)

FEATURES:

* Add protected_branch_ids to gitlab_project_approval_rule ([#542](https://github.com/gitlabhq/terraform-provider-gitlab/pull/542))
* Add most Premium features for gitlab_branch_protection ([#556](https://github.com/gitlabhq/terraform-provider-gitlab/pull/556))
* Adds support for gitlab project badges ([#648](https://github.com/gitlabhq/terraform-provider-gitlab/pull/648))

ENHANCEMENTS:

* Add CustomCIPath to resource gitlab_project ([#662](https://github.com/gitlabhq/terraform-provider-gitlab/pull/662))
* add build coverage regex ([#627](https://github.com/gitlabhq/terraform-provider-gitlab/pull/627))
* Add tfproviderlint linter to CI ([#653](https://github.com/gitlabhq/terraform-provider-gitlab/pull/653))
* Documentation improvements ([#642](https://github.com/gitlabhq/terraform-provider-gitlab/pull/642))
* chore: add error handling to resourceGitlabProjectSetToState ([#649](https://github.com/gitlabhq/terraform-provider-gitlab/pull/649))
* Missing documentation for gitlab_instance_variable ([#602](https://github.com/gitlabhq/terraform-provider-gitlab/pull/602))
* Add support for importing Pipeline Schedules and Triggers ([#618](https://github.com/gitlabhq/terraform-provider-gitlab/pull/618))
* update reference to master branch to main ([#612](https://github.com/gitlabhq/terraform-provider-gitlab/pull/612))

BUGFIXES:

* Fix project approval rule tests ([#660](https://github.com/gitlabhq/terraform-provider-gitlab/pull/660))
* Fix markdown linter errors in branch_protection.md ([#656](https://github.com/gitlabhq/terraform-provider-gitlab/pull/656))
* fix: update default branch name to "main" ([#643](https://github.com/gitlabhq/terraform-provider-gitlab/pull/643))
* gitlab_project: Wait for template projects to be cloned/imported ([#621](https://github.com/gitlabhq/terraform-provider-gitlab/pull/621))



## 3.6.0 (Apr 6, 2021)

ENHANCEMENTS:

* Support the Note field in the User resource/data ([#572](https://github.com/gitlabhq/terraform-provider-gitlab/pull/572))
* add diffSuppressFunc for 'expires_at' attribute in 'deploy_token' ([#575](https://github.com/gitlabhq/terraform-provider-gitlab/pull/575))
* Update to Go 1.16 and terraform-plugin-sdk 1.16 ([#579](https://github.com/gitlabhq/terraform-provider-gitlab/pull/579))
* Bump github.com/xanzy/go-gitlab from 0.44.0 to 0.46.0 ([#586](https://github.com/gitlabhq/terraform-provider-gitlab/pull/586))

BUG FIXES:

* Fix "Run failed" on forks ([#565](https://github.com/gitlabhq/terraform-provider-gitlab/pull/565))


## 3.5.0 (Feb 18, 2021)

FEATURES:

* Add resource for project freeze periods ([#516](https://github.com/gitlabhq/terraform-provider-gitlab/pull/516 ))

ENHANCEMENTS:

* Update go version and go-gitlab version ([#523](https://github.com/gitlabhq/terraform-provider-gitlab/pull/523))
* Support additional attributes in `gitlab_project_hook` ([#525](https://github.com/gitlabhq/terraform-provider-gitlab/pull/525))
* Link badges in README to proper workflows ([#527](https://github.com/gitlabhq/terraform-provider-gitlab/pull/527))
* gitlab_project: Check each push rule individually ([#531](https://github.com/gitlabhq/terraform-provider-gitlab/pull/531))
* Allow `full_path` in addition to `id` in gitlab_project data source ([#532](https://github.com/gitlabhq/terraform-provider-gitlab/pull/532))
* Update test fixtures for better usability ([#535](https://github.com/gitlabhq/terraform-provider-gitlab/pull/535))
* Check for state change on user delete ([#539](https://github.com/gitlabhq/terraform-provider-gitlab/pull/539))
* Increase gitlab_project import timeout ([#536](https://github.com/gitlabhq/terraform-provider-gitlab/pull/536))
* Add optional mirror options ([#554](https://github.com/gitlabhq/terraform-provider-gitlab/pull/554))
* Remove vendor folder ([#546](https://github.com/gitlabhq/terraform-provider-gitlab/pull/546))
* Add dependabot config ([#558](https://github.com/gitlabhq/terraform-provider-gitlab/pull/558))
* Fix EE tests actually running against CE ([#564](https://github.com/gitlabhq/terraform-provider-gitlab/pull/564))
* Fix EE test mounting license as a directory ([#568](https://github.com/gitlabhq/terraform-provider-gitlab/pull/568))

BUG FIXES:

* fix deploy_token expiration ([#510](https://github.com/gitlabhq/terraform-provider-gitlab/pull/510))
* Fix group_share_group nil pointer reference ([#555](https://github.com/gitlabhq/terraform-provider-gitlab/pull/555))

## 3.4.0 (Jan 14, 2021)

FEATURES:

* Support sharing a group with another group ([#511](https://github.com/gitlabhq/terraform-provider-gitlab/pull/511))
* Support Project Mirroring ([#512](https://github.com/gitlabhq/terraform-provider-gitlab/pull/512))

## 3.3.0 (Nov 30, 2020)

FEATURES:

* Support instance level CI variables ([#389](https://github.com/gitlabhq/terraform-provider-gitlab/pull/389))

ENHANCEMENTS

*  Add the pages_access_level parameter ([#472](https://github.com/gitlabhq/terraform-provider-gitlab/pull/472))
*  Do not fail when project member does not exist ([#473](https://github.com/gitlabhq/terraform-provider-gitlab/pull/473))
* Make the runners_token on the project secret ([#474](https://github.com/gitlabhq/terraform-provider-gitlab/pull/474))
*  Fix nil pointer dereference importing gitlab_user ([#490](https://github.com/gitlabhq/terraform-provider-gitlab/pull/490))
* Fix unit and acceptance tests not running ([#495](https://github.com/gitlabhq/terraform-provider-gitlab/pull/495))

## 3.2.0 (Nov 20, 2020)

FEATURES:

* Project Approval Rules ([#250](https://github.com/gitlabhq/terraform-provider-gitlab/pull/https://github.com/gitlabhq/terraform-provider-gitlab/pull/250))

ENHANCEMENTS

* Documentation for expires_at ([#482](https://github.com/gitlabhq/terraform-provider-gitlab/pull/482))
* Update set-env github action command ([484](https://github.com/gitlabhq/terraform-provider-gitlab/pull/484))

## 3.1.0 (Oct 16, 2020)

ENHANCEMENTS:

* Enable custom UserAgent ([#451](https://github.com/gitlabhq/terraform-provider-gitlab/pull/451))
* gitlab_project_mirror: Mark URL as sensitive ([#458](https://github.com/gitlabhq/terraform-provider-gitlab/pull/458))
* Remove old-style variable interpolation ([#456](https://github.com/gitlabhq/terraform-provider-gitlab/pull/456))

BUG FIXES:

* add pagination for ListPipelineSchedules ([#454](https://github.com/gitlabhq/terraform-provider-gitlab/pull/454))

## 3.0.0 (Sept 23, 2020)

BREAKING CHANGES:

* Resource `gitlab_project_push_rules` has been removed. You now instead specify project push rules using the `push_rules` attribute on the `gitlab_project` resource.
* The `shared_with_groups` attribute has been removed from the `gitlab_project` resource (but not the data source). You may use the `gitlab_project_share_group` resource instead.

NOTES:

* If you are using the `environment_scope` attribute of `gitlab_project_variable` to manage multiple variables with the same key, it is recommended to use GitLab 13.4+. See [this related GitLab issue](https://gitlab.com/gitlab-org/gitlab/-/issues/9912) for older versions.
* The ID format of the `gitlab_project_variable` resource changed. The upgrade should be automatic.
* The default value of the `gitlab_project_variable` resource's `environment_scope` attribute has changed from `0` to `*`.

FEATURES:

* **New Data Source:** `gitlab_group_membership` ([#264](https://github.com/gitlabhq/terraform-provider-gitlab/issues/264))
* **New Resource:** `gitlab_instance_cluster` ([#367](https://github.com/gitlabhq/terraform-provider-gitlab/issues/367))
* **New Resource:** `gitlab_project_level_mr_approvals` ([#356](https://github.com/gitlabhq/terraform-provider-gitlab/issues/356))
* **New Resource:** `gitlab_project_mirror` ([#358](https://github.com/gitlabhq/terraform-provider-gitlab/issues/358))
* **New Resource:** `gitlab_service_pipelines_email` ([#375](https://github.com/gitlabhq/terraform-provider-gitlab/issues/375))

ENHANCEMENTS:

* data-source/gitlab_project: New attributes `packages_enabled`, `path_with_namespace` and `push_rules` ([#405](https://github.com/gitlabhq/terraform-provider-gitlab/issues/405), [#403](https://github.com/gitlabhq/terraform-provider-gitlab/issues/403), [#422](https://github.com/gitlabhq/terraform-provider-gitlab/issues/422))
* resource/gitlab_branch_protection: New `code_owner_approval_required` attribute ([#380](https://github.com/gitlabhq/terraform-provider-gitlab/issues/380))
* resource/gitlab_project: New attributes `packages_enabled`, `path_with_namespace`, and `push_rules` ([#405](https://github.com/gitlabhq/terraform-provider-gitlab/issues/405), [#403](https://github.com/gitlabhq/terraform-provider-gitlab/issues/403), [#422](https://github.com/gitlabhq/terraform-provider-gitlab/issues/422))
* resource/gitlab_group: New attributes `share_with_group_lock`, `project_creation_level`, `auto_devops_enabled`, `emails_disabled`, `mentions_disabled`, `subgroup_creation_level`, `require_two_factor_authentication`, and `two_factor_grace_period` ([#362](https://github.com/gitlabhq/terraform-provider-gitlab/issues/362))
* resource/gitlab_group: Automatically detect removal ([#267](https://github.com/gitlabhq/terraform-provider-gitlab/issues/267))
* resource/gitlab_group_label: Can now be imported ([#339](https://github.com/gitlabhq/terraform-provider-gitlab/issues/339))
* resource/gitlab_project: New `import_url` attribute ([#381](https://github.com/gitlabhq/terraform-provider-gitlab/issues/381))
* resource/gitlab_project_push_rules: Can now be imported ([#360](https://github.com/gitlabhq/terraform-provider-gitlab/issues/360))
* resource/gitlab_project_variable: Better error message when a masked variable fails validation ([#371](https://github.com/gitlabhq/terraform-provider-gitlab/issues/371))
* resource/gitlab_project_variable: Automatically detect removal ([#409](https://github.com/gitlabhq/terraform-provider-gitlab/issues/409))
* resource/gitlab_service_jira: Automatically detect removal ([#337](https://github.com/gitlabhq/terraform-provider-gitlab/issues/337))
* resource/gitlab_user: The `email` attribute can be changed without forcing recreation ([#261](https://github.com/gitlabhq/terraform-provider-gitlab/issues/261))
* resource/gitlab_user: Require either the `password` or `reset_password` attribute to be set ([#262](https://github.com/gitlabhq/terraform-provider-gitlab/issues/262))

BUG FIXES:

* resource/gitlab_pipeline_schedule: Fix a rare error during deletion ([#364](https://github.com/gitlabhq/terraform-provider-gitlab/issues/364))
* resource/gitlab_pipeline_schedule_variable: Fix a rare error during deletion ([#364](https://github.com/gitlabhq/terraform-provider-gitlab/issues/364))
* resource/gitlab_project: Fix the `default_branch` attribute changing to `null` after first apply ([#343](https://github.com/gitlabhq/terraform-provider-gitlab/issues/343))
* resource/gitlab_project_share_group: Fix the `access_level` attribute not updating ([#421](https://github.com/gitlabhq/terraform-provider-gitlab/issues/421))
* resource/gitlab_project_share_group: Fix the share not working if the project is also managed ([#421](https://github.com/gitlabhq/terraform-provider-gitlab/issues/421))
* resource/gitlab_project_variable: Fix inconsistent reads for variables with non-unique keys ([#409](https://github.com/gitlabhq/terraform-provider-gitlab/issues/409))
* resource/gitlab_project_variable: Change the default `environment_scope` from `0` to `*` ([#409](https://github.com/gitlabhq/terraform-provider-gitlab/issues/409))
* resource/gitlab_service_jira: Fix a rare state inconsistency problem during creation ([#363](https://github.com/gitlabhq/terraform-provider-gitlab/issues/363))
* resource/gitlab_user: Fix some attributes saving incorrectly in state ([#261](https://github.com/gitlabhq/terraform-provider-gitlab/issues/261))

## 2.11.0 (July 24, 2020)

ENHANCEMENTS:
* Improvements to resource `gitlab_user` import
  ([#340](https://github.com/gitlabhq/terraform-provider-gitlab/issues/340))

## 2.10.0 (June 09, 2020)

FEATURES:
* **New Resource:** `gitlab_service_github`
  ([#311](https://github.com/gitlabhq/terraform-provider-gitlab/issues/311))

ENHANCEMENTS:
* add attribute `remove_source_branch_after_merge` to projects
  ([#289](https://github.com/gitlabhq/terraform-provider-gitlab/issues/289))

BUGFIXES:
* fix for flaky `gitlab_group` tests
  ([#320](https://github.com/gitlabhq/terraform-provider-gitlab/issues/320))
* Creating custom skip function for group_ldap_link tests.
  ([#328](https://github.com/gitlabhq/terraform-provider-gitlab/issues/328))

## 2.9.0 (June 01, 2020)

FEATURES:
* **New DataSource:** `gitlab_projects`
  ([#279](https://github.com/gitlabhq/terraform-provider-gitlab/issues/279))
* **New Resource:** `gitlab_deploy_token`
  ([#284](https://github.com/gitlabhq/terraform-provider-gitlab/issues/284))

ENHANCEMENTS:
* Add `management_project_id` for Group and Project Clusters
  ([#301](https://github.com/gitlabhq/terraform-provider-gitlab/issues/301))

## 2.8.0 (May 28, 2020)

FEATURES:
* **New Resource:** `gitlab_group_ldap_link`
  ([#296](https://github.com/gitlabhq/terraform-provider-gitlab/issues/296),
   [#316](https://github.com/gitlabhq/terraform-provider-gitlab/issues/316))

ENHANCEMENTS:

* Update resource gitlab_group_label to read labels from all pages
  ([#302](https://github.com/gitlabhq/terraform-provider-gitlab/issues/302))
* Provide a way to specify client cert and key
  ([#315](https://github.com/gitlabhq/terraform-provider-gitlab/issues/315))

BUGFIXES:
* Increase MaxIdleConnsPerHost in http.Transport
  ([#305](https://github.com/gitlabhq/terraform-provider-gitlab/issues/305))

## 2.7.0 (May 20, 2020)

* Implement `masked` parameters for `gitlab_group_variable`
  ([#271](https://github.com/gitlabhq/terraform-provider-gitlab/issues/271))

## 2.6.0 (April 08, 2020)

ENHANCEMENTS:
* Add jira flags
  ([#274](https://github.com/gitlabhq/terraform-provider-gitlab/issues/274))

## 2.5.1 (April 06, 2020)

BUGFIXES:

* Support for soft-delete of groups and projects in Gitlab Enterprise Edition
  ([#282](https://github.com/gitlabhq/terraform-provider-gitlab/issues/282),
   [#283](https://github.com/gitlabhq/terraform-provider-gitlab/issues/283),
   [#285](https://github.com/gitlabhq/terraform-provider-gitlab/issues/285),
   [#291](https://github.com/gitlabhq/terraform-provider-gitlab/issues/291))

ENHANCEMENTS:
* Switched from Travis CI to Github Actions
  ([#216](https://github.com/gitlabhq/terraform-provider-gitlab/issues/216))

## 2.5.0 (December 05, 2019)

ENHANCEMENTS:
* Implement `lfs_enabled`, `request_access_enabled`, and `pipelines_enabled` parameters for `gitlab_project`
  ([#225](https://github.com/gitlabhq/terraform-provider-gitlab/pull/225),
   [#226](https://github.com/gitlabhq/terraform-provider-gitlab/pull/226),
   [#227](https://github.com/gitlabhq/terraform-provider-gitlab/pull/227))

BUGFIXES:
* Fix label support when there is more than 20 labels on a project
  ([#229](https://github.com/gitlabhq/terraform-provider-gitlab/pull/229))
* Enable `environment_scope` for `gitlab_project_variable` lookup
  ([#228](https://github.com/gitlabhq/terraform-provider-gitlab/pull/229))
* Fix users data source when there is more than 20 users returned
  ([#230](https://github.com/gitlabhq/terraform-provider-gitlab/pull/230))

## 2.4.0 (November 28, 2019)

FEATURES:
* **New Resource:** `gitlab_group_label` ([#186](https://github.com/gitlabhq/terraform-provider-gitlab/pull/186))
* **New Resource:** `gitlab_group_cluster`
  ([#178](https://github.com/gitlabhq/terraform-provider-gitlab/pull/178))
* **New Resource:** `gitlab_pipeline_schedule_variable`
  ([#204](https://github.com/gitlabhq/terraform-provider-gitlab/pull/204))

ENHANCEMENTS:
* Add `runners_token` to gitlab groups ([#218](https://github.com/gitlabhq/terraform-provider-gitlab/pull/218))
* Add `reset_password` to `gitlab_user` ([#127](https://github.com/gitlabhq/terraform-provider-gitlab/pull/127))
* Update `access_level` available values ([#220](https://github.com/gitlabhq/terraform-provider-gitlab/pull/220))
* Make read callbacks graceful for `gitlab_project_share_group`, `gitlab_branch_protection` and
  `gitlab_label` resources ([#223](https://github.com/gitlabhq/terraform-provider-gitlab/pull/223))


BUGFIXES:
* Fix state not being updated for `gitlab_branch_protection`
  ([#166](https://github.com/gitlabhq/terraform-provider-gitlab/pull/166))
* Set ForceNew for `gitlab_pipeline_schedule` `project`
  ([#203](https://github.com/gitlabhq/terraform-provider-gitlab/pull/203))

## 2.3.0 (October 17, 2019)

*We would like to thank Gitlab, which has provided us a EE license. This project
is now tested against Gitlab CE and Gitlab EE.*

FEATURES:
* **New Resource:** `gitlab_project_push_rules` ([#163](https://github.com/gitlabhq/terraform-provider-gitlab/pull/163))
* **New Resource:** `gitlab_deploy_key_enable` ([#176](https://github.com/gitlabhq/terraform-provider-gitlab/pull/176))
* **New Resource:** `gitlab_project_share_group` ([#167](https://github.com/gitlabhq/terraform-provider-gitlab/pull/167))

ENHANCEMENTS:
* Add `initialize_with_readme` to `gitlab_project` ([#179](https://github.com/gitlabhq/terraform-provider-gitlab/issues/179))
* Add support for more variable options ([#169](https://github.com/gitlabhq/terraform-provider-gitlab/issues/169))
* Documentation improvements ([#168](https://github.com/gitlabhq/terraform-provider-gitlab/issues/168), [#187](https://github.com/gitlabhq/terraform-provider-gitlab/issues/187), [#171](https://github.com/gitlabhq/terraform-provider-gitlab/issues/171))

BUGFIXES:
* Fix tag protection URL
  ([#156](https://github.com/gitlabhq/terraform-provider-gitlab/issues/156))
* Properly manage the default branch in a git repo
  ([#158](https://github.com/gitlabhq/terraform-provider-gitlab/issues/158))
* Resolve triggers pagination issue by calling `GetPipelineTrigger`
  ([#173](https://github.com/gitlabhq/terraform-provider-gitlab/issues/173))

## 2.2.0 (June 12, 2019)

FEATURES:
* **New Resource:** `gitlab_service_jira` ([#101](https://github.com/gitlabhq/terraform-provider-gitlab/pull/101))
* **New Resource:** `gitlab_pipeline_schedule` ([#116](https://github.com/gitlabhq/terraform-provider-gitlab/pull/116))

ENHANCEMENTS:
* Add `archived` argument to `gitlab_project` ([#148](https://github.com/gitlabhq/terraform-provider-gitlab/issues/148))
* Add `managed` argument to `gitlab_project_cluster` ([#137](https://github.com/gitlabhq/terraform-provider-gitlab/issues/137))

## 2.1.0 (May 29, 2019)

FEATURES:
* **New Datasource**: `gitlab_group` ([#129](https://github.com/gitlabhq/terraform-provider-gitlab/issues/129))


## 2.0.0 (May 23, 2019)

This is the first release to support Terraform 0.12.

BACKWARDS INCOMPATIBILITIES:
* **all**: Previous versions of this provider silently removed state from state when
  Gitlab returned an error 404. Now we error on this and you must reconciliate
  the state (e.g. `terraform state rm`). We have done this because we can not
  make the difference between permission denied and resources removed outside of
  terraform (gitlab returns 404 in both cases)
  ([#130](https://github.com/gitlabhq/terraform-provider-gitlab/pull/130))


FEATURES:
* **New Resource:** `gitlab_tag_protection` ([#125](https://github.com/gitlabhq/terraform-provider-gitlab/pull/125))


ENHANCEMENTS:
* Add `container_registry_enabled` argument to `gitlab_project` ([#115](https://github.com/gitlabhq/terraform-provider-gitlab/issues/115))
* Add `shared_runners_enabled` argument to `gitlab_project` ([#134](https://github.com/gitlabhq/terraform-provider-gitlab/issues/134) [#104](https://github.com/gitlabhq/terraform-provider-gitlab/issues/104))

## 1.3.0 (May 03, 2019)

FEATURES:
* **New Resource:** `gitlab_service_slack` ([#96](https://github.com/gitlabhq/terraform-provider-gitlab/issues/96))
* **New Resource:** `gitlab_branch_protection` ([#68](https://github.com/gitlabhq/terraform-provider-gitlab/issues/68))

ENHANCEMENTS:
* Support for request/response logging when >`DEBUG` severity is set ([#93](https://github.com/gitlabhq/terraform-provider-gitlab/issues/93))
* Datasource `gitlab_user` supports user_id, email lookup and return lots of new attributes ([#102](https://github.com/gitlabhq/terraform-provider-gitlab/issues/102))
* Resource `gitlab_deploy_key` can now be imported ([#197](https://github.com/gitlabhq/terraform-provider-gitlab/issues/97))
* Add `tags` attribute for `gitlab_project` ([#106](https://github.com/gitlabhq/terraform-provider-gitlab/pull/106))


BUGFIXES:
* Documentation fixes ([#108](https://github.com/gitlabhq/terraform-provider-gitlab/issues/108), [#113](https://github.com/gitlabhq/terraform-provider-gitlab/issues/113))

## 1.2.0 (February 19, 2019)

FEATURES:

* **New Datasource:** `gitlab_users` ([#79](https://github.com/gitlabhq/terraform-provider-gitlab/issues/79))
* **New Resource:** `gitlab_pipeline_trigger` ([#82](https://github.com/gitlabhq/terraform-provider-gitlab/issues/82))
* **New Resource:** `gitlab_project_cluster` ([#87](https://github.com/gitlabhq/terraform-provider-gitlab/issues/87))

ENHANCEMENTS:

* Supports "No one" and "maintainer" permissions ([#83](https://github.com/gitlabhq/terraform-provider-gitlab/issues/83))
* `gitlab_project.shared_with_groups` is now order-independent ([#86](https://github.com/gitlabhq/terraform-provider-gitlab/issues/86))
* add `merge_method`, `only_allow_merge_if_*`, `approvals_before_merge` parameters to `gitlab_project` ([#72](https://github.com/gitlabhq/terraform-provider-gitlab/issues/72), [#88](https://github.com/gitlabhq/terraform-provider-gitlab/issues/88))


## 1.1.0 (January 14, 2019)

FEATURES:

* **New Resource:** `gitlab_project_membership`
* **New Resource:** `gitlab_group_membership` ([#8](https://github.com/gitlabhq/terraform-provider-gitlab/issues/8))
* **New Resource:** `gitlab_project_variable` ([#47](https://github.com/gitlabhq/terraform-provider-gitlab/issues/47))
* **New Resource:** `gitlab_group_variable` ([#47](https://github.com/gitlabhq/terraform-provider-gitlab/issues/47))

BACKWARDS INCOMPATIBILITIES:

`gitlab_project_membership` is not compatible with a previous *unreleased* version due to an id change resource will need to be reimported manually
e.g
```bash
terraform state rm gitlab_project_membership.foo
terraform import gitlab_project_membership.foo 12345:1337
```

## 1.0.0 (October 06, 2017)

BACKWARDS INCOMPATIBILITIES:

* This provider now uses the v4 api. It means that if you set up a custom API url, you need to update it to use the /api/v4 url. As a side effect, we no longer support Gitlab < 9.0. ([#20](https://github.com/gitlabhq/terraform-provider-gitlab/issues/20))
* We now support Parent ID for `gitlab_groups`. However, due to a limitation in
  the gitlab API, changing a Parent ID requires destroying and recreating the
  group. Since previous versions of this provider did not support it, there are
  chances that terraform will try do delete all your nested group when you
  update to 1.0.0. A workaround to prevent this is to use the `ignore_changes`
  lifecycle parameter. ([#28](https://github.com/gitlabhq/terraform-provider-gitlab/issues/28))

```
resource "gitlab_group" "nested_group" {
  name = "bar-name-%d"
  path = "bar-path-%d"
  lifecycle {
    ignore_changes = ["parent_id"]
  }
}
```

FEATURES:

* **New Resource:** `gitlab_user` ([#23](https://github.com/gitlabhq/terraform-provider-gitlab/issues/23))
* **New Resource:** `gitlab_label` ([#22](https://github.com/gitlabhq/terraform-provider-gitlab/issues/22))

IMPROVEMENTS:

* Add `cacert_file` and `insecure` options to the provider. ([#5](https://github.com/gitlabhq/terraform-provider-gitlab/issues/5))
* Fix race conditions with `gitlab_project` deletion. ([#19](https://github.com/gitlabhq/terraform-provider-gitlab/issues/19))
* Add `parent_id` argument to `gitlab_group`. ([#28](https://github.com/gitlabhq/terraform-provider-gitlab/issues/28))
* Add support for `gitlab_project` import. ([#30](https://github.com/gitlabhq/terraform-provider-gitlab/issues/30))
* Add support for `gitlab_groups` import. ([#31](https://github.com/gitlabhq/terraform-provider-gitlab/issues/31))
* Add `path` argument for `gitlab_project`. ([#21](https://github.com/gitlabhq/terraform-provider-gitlab/issues/21))
* Fix indempotency issue with `gitlab_deploy_key` and white spaces. ([#34](https://github.com/gitlabhq/terraform-provider-gitlab/issues/34))

## 0.1.0 (June 20, 2017)

NOTES:

* Same functionality as that of Terraform 0.9.8. Repacked as part of [Provider Splitout](https://www.hashicorp.com/blog/upcoming-provider-changes-in-terraform-0-10/)
