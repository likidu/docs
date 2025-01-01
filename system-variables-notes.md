---
title: System Variables Analysis Notes
summary: Progress tracking and issues for system variables reference analysis
---

# System Variables Analysis Notes

## Progress

1. Initial setup
   - ✅ Created system-variables-references.md
   - ✅ Created system-variables-notes.md
   - ⏳ Extracting variables from system-variables.md (in progress)
   - ✅ Processed variables starting with 'a' through 't'
   - ⏳ Searching for references (in progress)

## Progress Updates

- Processed `ssl_ca` variable (YYYY-MM-DD)
  - Found references in 16 different files
  - Most references are in development guides and vector search integration docs
  - References include both configuration examples and actual usage patterns
- Processed `max_allowed_packet` variable
  - Found references in 12 different files
  - References include configuration files, error handling docs, release notes, and feature documentation
  - Updated system-variables-references.md with the findings
- Processed `tidb_auto_analyze_start_time`: Found 5 references across the documentation
- Processed `tidb_constraint_check_in_place`:
  - Found 8 direct references across the documentation
  - References include configuration files, transaction documentation, and release notes
  - Successfully updated system-variables-references.md with the findings
- Processed `tidb_constraint_check_in_place_pessimistic`
  - Found 9 files with direct references
  - References include documentation, release notes, and configuration files
  - All references appear to be properly linked
- Processed `tidb_ddl_disk_quota`: Found in 3 files (excluding system-variables.md)
  - Found in release notes (6.3.0) where it was introduced
  - Found in feature documentation
  - Found in cloud-specific limitations
- Analyzed `tidb_ddl_enable_fast_reorg`: Found 17 references across documentation, including feature descriptions, release notes, and configuration guides.
- Processed `tidb_ddl_flashback_concurrency`: Found references in limited SQL features documentation and release notes (6.3.0, 6.4.0)
- Completed reference search for `tidb_ddl_reorg_worker_cnt`
  - Found 17 unique files referencing this variable
  - References include documentation, release notes, and various SQL-related guides
  - Variable is frequently mentioned in context of DDL operations and performance tuning
- Processed `tidb_ddl_reorg_max_write_speed`
  - Found in 4 files (excluding system-variables.md)
  - References added to system-variables-references.md
  - Variable is new in v8.5.0
- Processed `tidb_window_concurrency`: Found 1 reference in sql-statement-show-variables.md

## Variables Processed
- ✅ allow_auto_random_explicit_insert
- ✅ authentication_ldap_* (all LDAP variables)
- ✅ auto_increment_* (all auto increment variables)
- ✅ autocommit
- ✅ block_encryption_mode
- ✅ character_set_* (all character set variables)
- ✅ collation_* (all collation variables)
- ✅ cte_max_recursion_depth
- ✅ datadir
- ✅ ddl_slow_threshold
- ✅ default_* (all default variables)
- ✅ disconnect_on_expired_password
- ✅ div_precision_increment
- ✅ error_count
- ✅ foreign_key_checks
- ✅ group_concat_max_len
- ✅ have_* (SSL-related variables)
- ✅ hostname
- ✅ identity
- ✅ init_connect
- ✅ innodb_lock_wait_timeout
- ✅ interactive_timeout
- ✅ last_* (all last-related variables)
- ✅ license
- ✅ max_* (all max-related variables)
- ✅ mpp_* (all MPP-related variables)
- ✅ password_* (all password-related variables)
- ✅ pd_enable_follower_handle_region
- ✅ plugin_dir
- ✅ plugin_load
- ✅ port
- ✅ rand_seed* (all rand seed variables)
- ✅ require_secure_transport
- ✅ skip_name_resolve
- ✅ socket
- ✅ sql_* (all SQL-related variables)
- ✅ ssl_* (all SSL-related variables)
- ✅ system_time_zone
- ✅ time_zone
- ✅ tidb_adaptive_closest_read_threshold
- ✅ tidb_allow_* (all allow-related variables)
- ✅ tidb_analyze_* (all analyze-related variables)
- ✅ tidb_auto_* (all auto-related variables)
- ✅ tidb_backoff_* (all backoff-related variables)
- ✅ tidb_batch_* (all batch-related variables)
- ✅ tidb_broadcast_join_threshold_* (all broadcast join threshold variables)
- ✅ tidb_build_* (all build-related variables)
- ✅ tidb_capture_plan_baselines
- ✅ tidb_cdc_write_source
- ✅ tidb_check_mb4_value_in_utf8
- ✅ tidb_checksum_table_concurrency
- ✅ tidb_committer_concurrency
- ✅ tidb_config
- ✅ tidb_constraint_check_* (all constraint check variables)
- ✅ tidb_cost_model_version
- ✅ tidb_current_ts
- ✅ tidb_ddl_* (all DDL-related variables)
- ✅ tidb_enable_dist_task
- ✅ tidb_cloud_storage_uri
- ✅ tidb_default_string_match_selectivity
- ✅ tidb_disable_txn_auto_retry
- ✅ tidb_distsql_scan_concurrency
- ✅ tidb_dml_batch_size
- ✅ tidb_dml_type
- ✅ tidb_enable_1pc
- ✅ tidb_enable_async_commit
- ✅ tidb_enable_analyze_snapshot
- ✅ tidb_enable_auto_analyze
- ✅ tidb_enable_auto_analyze_priority_queue
- ✅ tidb_enable_auto_increment_in_generated
- ✅ tidb_enable_batch_dml
- ✅ tidb_enable_cascades_planner
- ✅ tidb_enable_check_constraint
- max_execution_time
  - Found 11 unique references across the documentation
  - Notable mentions in connection parameters, timeouts, and release notes
  - Variable behavior changed in v6.4.0 to only affect read-only statements
- Completed analysis of `last_insert_id` variable:
  - Found references in 8 different files
  - Updated system-variables-references.md with the findings
  - References include documentation, release notes, and sample applications
- Need to continue with next batch of variables
- tidb_auto_build_stats_concurrency
  - Found in release-6.5.0.md (introduced as new feature)
  - References updated in system-variables-references.md

## Issues
- None so far

## Next Steps
1. Continue reading system-variables.md to extract more variables
2. Process next batch of variables:
   - Read the next section of variables from system-variables.md
   - Search for references using `rg`
   - Update references.md with findings 