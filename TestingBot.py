import re
import requests
import base64

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

def report_testingbot_status(name, status, credentials):
	selenium = BuiltIn().get_library_instance('Selenium2Library')
	session_id = selenium.driver.session_id

	token = base64.b64encode(credentials)
	payload = {'test[name]': name, 'test[success]': int(status == 'PASS')}
	headers = {'Authorization': 'Basic {0}'.format(token)}

	url = 'https://api.testingbot.com/v1/tests/{0}'.format(session_id)
	response = requests.put(url, data=payload, headers=headers)
	assert response.status_code == 200, response.text