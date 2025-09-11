import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["python", target_file], capture_output=True, text=True, timeout=30, check=True)

        if result.returncode != 0:
            return f"Process exited with code {result.returncode}."
        
        if result.stdout or result.stderr:
            output = []
            if result.stdout:
                output.append(f"STDOUT: {result.stdout.strip()}\n")
            if result.stderr:
                output.append(f"STDERR: {result.stderr.strip()}\n")
            return "\n".join(output)
        else:
            return "No output produced."
        
    except Exception as e:
        return f"Error: executing Python file: {e}"



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file and returns its output, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
