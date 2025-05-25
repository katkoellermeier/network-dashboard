```
This app is a sample of a network dashboard. The following are features and skills included:

Feature	                                    Skills Practiced
Pull device info via Netmiko	            SSH automation, Python logic
Poll Meraki/DNA/Webex API for metrics	    REST APIs, token auth
Handle missing credentials/errors	        Error handling, retry logic
Multithreaded polling	                    concurrent.futures
Store secrets in .env	                    Secure config
Log successes/failures to file	            Logging best practices
Create Docker container	                    App deployment
GitHub Actions for lint + test	            CI/CD workflow
YAML inventory parsing	                    IaC readiness
Optional Flask front end	                Web dev + API integration


# Clone repo
git clone https://github.com/youruser/device-dashboard.git
cd device-dashboard

# Set up virtualenv
python3 -m venv venv && source venv/bin/activate

# Install deps
pip install -r requirements.txt

# Run CLI or web app
python app.py


Bonus Add-ons (Optional)

# Webex bot alert if a device is down

# Use genie learn or pyATS for deeper config comparison

# Grafana/InfluxDB integration via Telegraf export

# Jenkinsfile for local Jenkins pipeline