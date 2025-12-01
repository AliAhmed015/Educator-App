from graphviz import Digraph

# Create a directed graph for Admin user journey
dot_admin = Digraph(comment='Admin User Journey Flow')

# Nodes for the flow
dot_admin.node('Start', 'Start')
dot_admin.node('RateLimit', 'Rate Limiting', shape='rect')  # Renamed the node
dot_admin.node('Login', 'Log In', shape='rect')  # Moved Login after Rate Limit
dot_admin.node('Auth', 'Verify Credentials', shape='rect')
dot_admin.node('RoleCheck', 'Check Admin Role', shape='diamond', style='filled', color='lightgray', width='2.5', height='1.5', fixedsize='true')
dot_admin.node('Dashboard', 'Admin Dashboard', shape='rect')
dot_admin.node('Manage', 'Manage Students and Courses', shape='rect')  # Renamed the node
dot_admin.node('End', 'Complete / Log Out', shape='rect')

# Connect the nodes
dot_admin.edge('Start', 'RateLimit', label='Open App')  # Start to Rate Limit
dot_admin.edge('RateLimit', 'Login', label='Not Exceeding')  # Rate Limit to Login with "Not Exceeding"
dot_admin.edge('Login', 'Auth', label='Submit Login')
dot_admin.edge('Auth', 'RoleCheck', label='Check Requests')
dot_admin.edge('RoleCheck', 'Dashboard', label='Admin Role Verified')
dot_admin.edge('Dashboard', 'Manage', label='Manage Students and Courses')
dot_admin.edge('Manage', 'End', label='Finish Tasks')

# Visual settings
dot_admin.attr(dpi='300', rankdir='TB', size='10,15', nodesep='0.7')

# Render the Admin diagram
dot_admin.render('lms_admin_user_journey_flow', format='png', cleanup=True)