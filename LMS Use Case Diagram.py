from graphviz import Digraph

# Create a new directed graph for the Use Case Diagram
dot = Digraph(comment='Complete Use Case Diagram')

# Set the title for the graph
dot.attr(label='Use Case Diagram: System, Student and Admin Operations', labelloc='t', fontsize='16', fontweight='bold')

# Add actors as nodes
dot.node('S', 'Student', shape='actor', fontsize='16')
dot.node('A', 'Admin', shape='actor', fontsize='16')
dot.node('Sys', 'System (App)', shape='actor', fontsize='16')

# Add use cases as nodes
dot.node('Login', 'Login', shape='ellipse', fontsize='16')
dot.node('Register', 'Register', shape='ellipse', fontsize='16')
dot.node('View_Courses', 'View Courses', shape='ellipse', fontsize='16')
dot.node('Enroll_Courses', 'Enroll in Courses', shape='ellipse', fontsize='16')
dot.node('Manage_Courses', 'Manage Courses (Admin)', shape='ellipse', fontsize='16')
dot.node('Manage_Students', 'Manage Students (Admin)', shape='ellipse', fontsize='16')
dot.node('JWT_Auth', 'JWT Authentication', shape='ellipse', fontsize='16')
dot.node('Rate_Limiting', 'Rate Limiting (Redis)', shape='ellipse', fontsize='16')
dot.node('Database_Operations', 'Database Operations (CRUD)', shape='ellipse', fontsize='16')
dot.node('Seed_Database', 'Seed Database', shape='ellipse', fontsize='16')
dot.node('Role_Validation', 'Role Validation', shape='ellipse', fontsize='16')

# Define relationships between actors and use cases
dot.edge('S', 'Login')
dot.edge('S', 'Register')
dot.edge('S', 'View_Courses')
dot.edge('S', 'Enroll_Courses')
dot.edge('A', 'Login')
dot.edge('A', 'Register')
dot.edge('A', 'Manage_Courses')
dot.edge('A', 'Manage_Students')

# Relationships between use cases and system functions
dot.edge('Sys', 'JWT_Auth')
dot.edge('Sys', 'Rate_Limiting')
dot.edge('Sys', 'Database_Operations')
dot.edge('Sys', 'Seed_Database')
dot.edge('Sys', 'Role_Validation')

# Visual adjustments for the diagram
dot.attr(dpi='300', rankdir='LR', size='14,10', nodesep='0.7', ranksep='5')

# Render the diagram to a file
dot.render('cms_use_case_diagram', format='png', cleanup=True)
