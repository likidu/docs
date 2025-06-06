---
title: tiup cluster rename
summary: The `tiup cluster rename` command is used to change the cluster name after it has been deployed. Additional steps are required if the `dashboard_dir` field of `grafana_servers` is configured for the TiUP cluster. The syntax for the command is `tiup cluster rename <old-cluster-name> <new-cluster-name>`. The `-h, --help` option prints help information. The output is the execution log of the tiup-cluster.
---

# tiup cluster rename

The cluster name is specified when [the cluster is deployed](/tiup/tiup-component-cluster-deploy.md). If you want to change the cluster name after the cluster is deployed, you can use the command `tiup cluster rename`.

> **Note:**
>
> If the `dashboard_dir` field of `grafana_servers` is configured for the TiUP cluster, after you execute the command `tiup cluster rename` to rename the cluster, the following additional steps are required:
>
> + For the `*.json` files in the local dashboards directory, update the `datasource` field of each file to the new cluster name, because the value of `datasource` must be the name of the cluster.
> + Execute the command `tiup cluster reload -R grafana`.

## Syntax

```shell
tiup cluster rename <old-cluster-name> <new-cluster-name> [flags]
```

- `<old-cluster-name>`: The old cluster name.
- `<new-cluster-name>`: The new cluster name.

## Options

### -h, --help

- Prints help information.
- Data type: `BOOLEAN`
- This option is disabled by default with the `false` value. To enable this option, add this option to the command, and either pass the `true` value or do not pass any value.

## Outputs

The execution log of the tiup-cluster.

## See also

- [TiUP Common Operations](/maintain-tidb-using-tiup.md)