from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Application Flow Diagram')

# Add components (nodes)
dot.node('Client', 'Client (User)')
dot.node('FastAPI', 'FastAPI Main App (main.py)', shape='rect')
dot.node('Middleware', 'Middleware (Rate Limiting)', shape='rect')
dot.node('Routers', 'Routers (admin_router, auth_router, etc.)', shape='rect')
dot.node('AuthRouter', 'auth_router (Handles Login/Registration)', shape='rect')
dot.node('Controller', 'Controllers (auth_controller, etc.)', shape='rect')
dot.node('Repository', 'Repositories (Database Queries)', shape='rect')
dot.node('Database', 'Database (Models: Student, Admin, etc.)', shape='rect')
dot.node('Services', 'Services (auth.py, helping_functions.py)', shape='rect')
dot.node('JWT', 'JWT Token Verification', shape='ellipse')

# Define the main flow of data
dot.edge('Client', 'FastAPI', label='HTTP Request')
dot.edge('FastAPI', 'Middleware', label='Apply Rate Limiting')
dot.edge('Middleware', 'Routers', label='Forward Request')
dot.edge('Routers', 'AuthRouter', label='Routing Request')
dot.edge('AuthRouter', 'Controller', label='Forward Request to Controller')

# Add Authentication and Role Validation
dot.edge('Controller', 'JWT', label='Verify Token')
dot.edge('JWT', 'Services', label='Validate JWT Token')
dot.edge('Services', 'Database', label='Query for User Info')

# Controller interacts with Repositories and Database
dot.edge('Controller', 'Repository', label='Call Repository Functions')
dot.edge('Repository', 'Database', label='Query Database')

# Return response
dot.edge('Controller', 'Client', label='Return Response')

# Additional information for the admin and student
dot.node('Admin', 'Admin Role Logic', shape='diamond', style='filled', color='lightgray', width='1.5', height='1.0', fixedsize='true')
dot.node('Student', 'Student Role Logic', shape='diamond', style='filled', color='lightgray', width='1.5', height='1.0', fixedsize='true')

# Role check based on user role
dot.edge('AuthRouter', 'Admin', label='Check Admin Role')
dot.edge('AuthRouter', 'Student', label='Check Student Role')

# Visual adjustments for layout (Spiral and Downward)
dot.attr(dpi='300', rankdir='TB', size='10,15', nodesep='0.7')

# Render the diagram
dot.render('cms_flow_diagram', format='png', cleanup=True)
