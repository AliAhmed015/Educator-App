from graphviz import Digraph

# Create a directed graph for Student user journey
dot_student = Digraph(comment='Student User Journey Flow')

# Nodes for the flow
dot_student.node('Start', 'Start')
dot_student.node('RateLimit', 'Rate Limiting', shape='rect')  # Renamed the node
dot_student.node('Login', 'Log In', shape='rect')  # Moved Login after Rate Limit
dot_student.node('Auth', 'Verify Credentials', shape='rect')
dot_student.node('RoleCheck', 'Check Student Role', shape='diamond', style='filled', color='lightgray', width='2.5', height='1.5', fixedsize='true')
dot_student.node('Dashboard', 'Student Dashboard', shape='rect')
dot_student.node('ViewDetails', 'View Their Details', shape='rect')  # Added View Details node
dot_student.node('Browse', 'Browse Courses', shape='rect')
dot_student.node('End', 'Complete / Log Out', shape='rect')

# Connect the nodes
dot_student.edge('Start', 'RateLimit', label='Open App')  # Start to Rate Limiting
dot_student.edge('RateLimit', 'Login', label='Not Exceeding')  # Rate Limit to Login with "Not Exceeding"
dot_student.edge('Login', 'Auth', label='Submit Login')
dot_student.edge('Auth', 'RoleCheck', label='Check Requests')
dot_student.edge('RoleCheck', 'Dashboard', label='Student Role Verified')
dot_student.edge('Dashboard', 'ViewDetails', label='View Their Details')  # View Their Details
dot_student.edge('ViewDetails', 'Browse', label='Browse Courses')
dot_student.edge('Browse', 'End', label='Finish Tasks')

# Visual settings
dot_student.attr(dpi='300', rankdir='TB', size='10,15', nodesep='0.7')

# Render the Student diagram
dot_student.render('lms_student_user_journey_flow', format='png', cleanup=True)
