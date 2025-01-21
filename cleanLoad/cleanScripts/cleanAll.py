import subprocess

def run_script(script_name):
	try:
		result = subprocess.run(["python3", script_name], check =True)
	except Exception as e:
		print(f"fail {e}")

if __name__ == '__main__':
	scripts = [
		'/home/pgill914/ETL-ASG/cleanLoad/cleanScripts/clean_department_table.py',
		'/home/pgill914/ETL-ASG/cleanLoad/cleanScripts/clean_employee_table.py',
		'/home/pgill914/ETL-ASG/cleanLoad/cleanScripts/clean_counciling_table.py',
		'/home/pgill914/ETL-ASG/cleanLoad/cleanScripts/clean_performance_table.py'
	]

	for script in scripts:
		print(f"Running {script}")
		run_script(script)
