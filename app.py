from flask import Flask, render_template, request,redirect,url_for
import jenkinsapi
import subprocess
app = Flask(__name__)
from jenkinsapi.jenkins import Jenkins
@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/configure', methods=['POST'])
# def configure():
#     template = request.form['template']
#     config = request.form['config']
    
#     # Perform any necessary validation or processing here
    
#     # Trigger CI action (mock)
#     ci_result = trigger_ci(template, config)
    
#     return render_template('result.html', template=template, config=config, ci_result=ci_result)
@app.route('/configure', methods=['POST'])
def configure():
    template = request.form['template']
    
    # Redirect to the template configuration page
    return redirect(url_for('configure_template', template=template))

# @app.route('/configure/<template>', methods=['GET', 'POST'])
# def configure_template(template):
#     if request.method == 'POST':
#         # Handle the submitted configuration here
#         config = request.form['config']
#         #   Trigger CI action (mock)
#         ci_result = trigger_ci(template, config)
#         # Perform any necessary processing or CI actions
        
#         # trigger_ci(template, config)

#         return render_template('result.html', template=template, config=config,ci_result=ci_result)
    
#     # Render the template configuration page
#     return render_template(f'{template}.html')
@app.route('/configure/<template>', methods=['GET', 'POST'])
def configure_template(template):
    if request.method == 'POST':
        # Handle the submitted configuration here
        config = request.form['config']
        #   Trigger CI action (mock)
        ci_result = trigger_ci(template, config)
        # Perform any necessary processing or CI actions
        jenkins_url = 'http://localhost:8080/'
        jenkins_username = 'samarpit'
        jenkins_password = 'samarpit'
        #  trigger_ci(template, config)
        # Create a new Jenkins job using JJB
        job_name = f'template_{template}'
        # jjb_command = f'jenkins-jobs --conf jjb_config.yaml update {template}.yaml'
        jjb_command = f'python -m jenkins_jobs --conf jjb_config.yaml update {template}.yaml'
        subprocess.run(jjb_command, shell=True, check=True)
        
        # Trigger the Jenkins job with the configuration parameter
       
        
        # Replace 'parameter_name' with the name of the parameter in your Jenkins job
        # that corresponds to the configuration value
        job_url = f'{jenkins_url}/job/{job_name}'
        jenkins_cli_command = f'java -jar jenkins-cli.jar -s {jenkins_url} build -p parameter_name={config} {job_name}'
        subprocess.run(jenkins_cli_command, shell=True, check=True)
        
        return render_template('result.html', template=template, config=config, job_url=job_url,ci_result=ci_result)
    
    # Render the template configuration page
    return render_template(f'{template}.html')

def trigger_ci(template, config):
    # jenkins_url = 'http://localhost:8080/'  # Replace with the actual URL of your Jenkins server
    # jenkins_username = 'samarpit'
    # jenkins_password = 'samarpit'
    # Perform template-specific CI actions here
    if template == 'template1':
        # Placeholder replacement or other template-specific actions for template1
        ci_result = 'CI action triggered for template1!'
    elif template == 'template2':
        # Placeholder replacement or other template-specific actions for template2
        ci_result = 'CI action triggered for template2!'
    elif template == 'template3':
        # Placeholder replacement or other template-specific actions for template3
        ci_result = 'CI action triggered for template3!'
    else:
        # Handle an unrecognized template or other error scenario
        ci_result = 'Error: Invalid template!'

    # server = Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)
    
    # Replace 'job_name' with the name of the Jenkins job you want to trigger
    # job = server.get_job('job_name')
    
    # Replace 'parameter_name' with the name of the parameter in your Jenkins job
    # that corresponds to the configuration value
    # job.invoke(build_params={'parameter_name': config})    
    
    return ci_result

# def trigger_ci(template, config):
#     jenkins_url = 'http://jenkins_server_url'  # Replace with the actual URL of your Jenkins server
#     jenkins_username = 'your_username'
#     jenkins_password = 'your_password'
    
#     server = Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)
    
#     # Replace 'job_name' with the name of the Jenkins job you want to trigger
#     job = server.get_job('job_name')
    
#     # Replace 'parameter_name' with the name of the parameter in your Jenkins job
#     # that corresponds to the configuration value
#     job.invoke(build_params={'parameter_name': config})

if __name__ == '__main__':
    app.run(debug=True)