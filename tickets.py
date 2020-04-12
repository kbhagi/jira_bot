from atlassian import Jira

#auth_jira = JIRA()

jira = Jira(url='http://company.atlassian.net',username='', password='',)


# for issue in jac.search_issues('project = SUP AND issuetype in ("Access request", "Clarification / Query / Request", "Data Change Request", "New Bug") AND status = To_Do AND assignee in (currentUser()) ORDER BY assignee ASC, reporter DESC, priority DESC, created DESC, component ASC, resolution ASC, issuetype DESC, cf[10900] ASC, due ASC, cf[10005] ASC, project ASC, status ASC, labels ASC, key ASC', maxResults=3):
#     print('{}: {} {}'.format(issue.key, issue.fields.summary,issue.fields.description,issue.fields.comment))
#issue = jac.issue('SUP-33232', fields='summary,comment,description')
#print issue
jql_str_unassigned = 'project = SUP AND issuetype in ("Access request", "Clarification / Query / Request", "Data Change Request", "New Bug") AND status in (In_progress, Reopened, To_Do) AND assignee in (EMPTY) ORDER BY assignee ASC, reporter DESC, priority DESC, created DESC, component ASC, resolution ASC, issuetype DESC, cf[10900] ASC, due ASC, cf[10005] ASC, project ASC, status ASC, labels ASC, key ASC'
issues=jira.jql(jql_str_unassigned,start=0,limit=50)
print issues

# for issue in issues:
#     print jira.issue(issue[3])
