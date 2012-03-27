def getIssuesUrl(user_id, xml=True):
    return "https://factory.ailove.ru/issues"+('.xml' if xml else '')+"?set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%3D&v%5Bassigned_to_id%5D%5B%5D="+str(user_id)

def getProjectsByUser(user_id):
    return "https://factory.ailove.ru/users/"+str(user_id)+".xml?include=memberships"

def getProject (project_id):
    return "https://factory.ailove.ru/projects/"+project_id+".xml"