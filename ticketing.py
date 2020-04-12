from jira import JIRA


user = 'yourrrmail'
apikey = 'bdTjLdnjjdn_'
server = 'https://yourdomain.atlassian.net'

options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user, apikey))

workflow_status = {
    "None":0,
    "Begin Work": 21,
    "In_progress" : 31 ,
    "Close Ticket" : 41,
    "Re-Open": 51,
    "Reopened": 61
    }

    #(u'21', u'Begin Work')
#(u'51', u'Re-Open')
#(u'61', u'Issue reopened')
#(u'31', u'Work Complete')
#(u'41', u'Close Ticket')
#print issue.fields.transitions;
def check_unassigned_issues():
 jql_str_unassigned='project = SUP AND issuetype in ("Access request", "Clarification / Query / Request", "Data Change Request", "New Bug") AND status = To_Do AND assignee in (EMPTY) ORDER BY assignee ASC, reporter DESC, priority DESC, created DESC, component ASC, resolution ASC, issuetype DESC, cf[10900] ASC, due ASC, cf[10005] ASC, project ASC, status ASC, labels ASC, key ASC'
 issues = jira.search_issues(jql_str_unassigned,startAt=0,maxResults=50)
 for issue in issues:
    if str(issue.fields.status) == 'To_Do' or str(issue.fields.assignee) == 'Unassigned':
        print 'Assigning issue '+issue.key+ ' to bhargava.k'
        jira.assign_issue(issue,' bhargava.k')
        jira.transition_issue(issue,'21')

def check_assigned_issues_of_bhargavak():
 jql_str_assigned='project = SUP AND issuetype in ("Access request", "Clarification / Query / Request", "Data Change Request", "New Bug") AND status = To_Do AND assignee in (currentUser()) ORDER BY summary ASC, assignee ASC, reporter DESC, priority DESC, created DESC, component ASC, resolution ASC, issuetype DESC, cf[10900] ASC, due ASC, cf[10005] ASC, project ASC, status ASC, labels ASC, key ASC'
 issues = jira.search_issues(jql_str_assigned,startAt=0,maxResults=50)
 for issue in issues:
     summary=issue.fields.summary
     component=issue.fields.components
     description=issue.fields.description
     if str(issue.fields.status) == 'To_Do' or str(issue.fields.assignee) == 'bhargava.k':
         jira.transition_issue(issue,'21')
      #if str(summary).__contains__('days per cycle') or str(summary).__contains__('Sanction'):

def check_access_requests():
    jql_str_unassigned = 'project = SUP AND issuetype in ("Access request", "Clarification / Query / Request", "Data Change Request", "New Bug") AND status = To_Do AND assignee in (EMPTY) ORDER BY assignee ASC, reporter DESC, priority DESC, created DESC, component ASC, resolution ASC, issuetype DESC, cf[10900] ASC, due ASC, cf[10005] ASC, project ASC, status ASC, labels ASC, key ASC'
    issues = jira.search_issues(jql_str_unassigned)
    for issue in issues:
        #   issue.fields.type
        #resolution_status=issue.fields.transition
        print 'issue_resolution', issue.fields.resolution
        print  'issue status', issue.fields.status.name

        summary=issue.fields.summary
        description=issue.fields.description
        #print str(workflow_status.get(resolution_status) + 10)
        if str(summary).__contains__('Access') or str(description).__contains__('Access') or str(description).__contains__('access'):
            if str(issue.fields.issuetype.name).__contains__('Access request'):
                print 'Access Request'
                print issue.fields.status.name
                existing_resolution_status = issue.fields.status.name
                print existing_resolution_status,' of',issue
                if str(existing_resolution_status).__eq__('TO_DO'):
                    jira.transition_issue(issue, "Begin Work")
                else:
                    issue.update(notify=True, fields={"issuetype": {"name": 'Access request'},
                                                      "priority": {"name": "Medium- Performance issue"}})
                #print 'setting resolution status of '+issue.key+ '',
                print issue.key
                #jira.transition_issue(issue,'2', fields={'assignee':{'name': 'bhargava.k'}, 'resolution':   {'id':new_resolution_status}})
                if str(existing_resolution_status).__eq__('TO_DO'):
                    jira.transition_issue(issue, "Begin Work")
                jira.assign_issue(issue,'bhargava.k')
                #fields = {'summary': 'New summary'}
            else:
                print 'else'
                issue.update(notify=True,fields={"issuetype": {"name": 'Access request'},"priority": {"name": "Medium- Performance issue"}})
                if str(existing_resolution_status).__eq__('TO_DO'):
                    jira.transition_issue(issue, "Begin Work")
                jira.assign_issue(issue, 'bhargava.k')





def check_LMS_OPS_COCKPIT_OPS_BANKING_issues():
    pass


def check_comments_set_workflow_status():
    jql_assigned_to_bhargavak='project = SUP AND issuetype in ("Access request", "Clarification / Query / Request", "Data Change Request", "New Bug") AND status = To_Do AND assignee in (currentUser()) ORDER BY summary ASC, assignee ASC, reporter DESC, priority DESC, created DESC, component ASC, resolution ASC, issuetype DESC, cf[10900] ASC, due ASC, cf[10005] ASC, project ASC, status ASC, labels ASC, key ASC'
    issues = jira.search_issues(jql_assigned_to_bhargavak,startAt=0,maxResults=50,fields = 'comment')
    for issue in issues:
         # summary=issue.fields.summary
         # component=issue.fields.components
         # description=issue.fields.description
          if(jira.comments(issue)>0):
              jira.transition_issue(issue,'21')

def check_App_X_Issues():
    pass

def check_User_Management_Issues():
    pass

def check_App_Y_Issues():
    pass

def check_Issues_by_due_date():
    pass

def check_and_close_resolved_Issues():
    pass

def send_followup_to_developer():
    pass

def check_dev1_Issues():
    pass

def check_dev2_Issues():
    pass

def check_dev3_Issues():
    pass

def check_dev4_issues():
    pass

def check_dev5_Issues():
    pass

def check_dev6_issues():
    pass

def assign_data_change_requests():
    pass

def assign_dev7_deletion_updation_requests():
    pass

def check_in_review_status_and_close_tickets():
    pass

def check_already_assigned_tickets_and_close_them():
    pass



# issue = jira.issue(issue).key
# transitions = jira.transitions(issue)
# for t in transitions:
#      print(t['id'], t['name'])

 # print (issue.key), issue.fields.creator, issue.fields.reporter, issue.fields.created, issue.fields.components,issue.fields.description,issue.fields.summary, issue.fields.issuetype.name, issue.fields.priority.name, issue.fields.resolution,issue.fields.status.name,issue.fields.status.description,  issue.fields.updated, issue.fields.assignee


#{"update":{"priority":[{"set":{"name" : "High- Specific feature issue or Error in app process"}}]}}

#issue.update(notify=True, fields=
                                    #'summary' :'some Text',
                                    #'description': 'some Text- ' +str(test),
                                    #{"priority": {"name": "Medium- Performance issue"}})
                                    #'components': [{'name': 'TestMode'}],
                                    #"issuetype": {"name": 'Requirement'},
                                    #'fixVersions': [{'name': 'test'}])

# print('ticket: ', ticket, summary,description,title)
# if description.__contains__('sop'):
#     print 'contains'
#jira.assign_issue(issue,'smitha.crystal')


if __name__ == '__main__':
    check_access_requests()
