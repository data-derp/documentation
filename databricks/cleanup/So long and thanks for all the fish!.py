# Databricks notebook source
# MAGIC %md
# MAGIC # Cleanup
# MAGIC Now that we've completed all of the exercise, let's do a little cleanup! Run this notebook to delete all files

# COMMAND ----------

# MAGIC %md
# MAGIC ## Delete data files in Filestore

# COMMAND ----------

# MAGIC %pip uninstall -y databricks_helpers
# MAGIC %pip install git+https://github.com/data-derp/databricks_helpers#egg=databricks_helpers

# COMMAND ----------

from databricks_helpers.databricks_helpers import DataDerpDatabricksHelpers

helper = DataDerpDatabricksHelpers(dbutils, "cleanup")
helper.clean_user_directory()
try:    
    print("Verifying files are deleted...")
    dbutils.fs.ls(helper.working_directory())
except Exception as e:
    print(f"Got an exception, there's probably no files left \o/")



# COMMAND ----------

# MAGIC %md
# MAGIC ## Export all Notebooks
# MAGIC
# MAGIC ![export-notebooks.png](https://github.com/data-derp/documentation/blob/master/databricks/assets/export-notebooks.png?raw=true)

# COMMAND ----------

# MAGIC %md
# MAGIC And now you're done! :) Don't worry about deleting them, we'll handle it later.

# COMMAND ----------


