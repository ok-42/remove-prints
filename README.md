This simple tool is intended to remove lines that start with `print` statement. It modifies file inplace with no backup.

Use case: you are testing Python code with `print()` instead of `logging.debug()` and don't want to erase all those statements manually after it is finished.

Add as an external tool to PyCharm:

- Open *Settings &mdash; Tools &mdash; External Tools*.
- Click *Add* button.
- Fill in the following fields:
  - Name: you choose
  - Program: `$ModuleSdkPath$`
  - Arguments: `"C:\full-path-to-project\remove-prints\remove-prints.py" $FilePath$`
  - Working directory: `$ProjectFileDir$`
- Click *OK*.

More info on adding external tools [here](https://github.com/ok-42/pycharm-scp#readme).
