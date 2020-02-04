from jira import JIRA
import fnmatch
import os

def find_txt():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            return file


jira = JIRA(basic_auth=(str(os.environ('LOGIN')), str(os.environ('PASSWORD'))), server=str(os.environ('SERVER')))

with open('./{}'.format(find_txt()), 'r') as report:
    description = report.read()
    new_issue = jira.create_issue(project='FAST', summary='Automatic report from FAST Security testing',
                                  description=description, issuetype={'name': 'Task'}, labels=['FAST', 'WALLARM'])
