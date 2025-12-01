from graphviz import Digraph

# Create a new directed graph for the updated architecture diagram
dot = Digraph(comment='Updated Application Architecture Diagram')

# Nodes for the components of the architecture
dot.node('Client', 'Client (User)', shape='rect')
dot.node('FastAPI', 'FastAPI Main App (main.py)', shape='rect')
dot.node('Routers', 'Routers (admin_router, auth_router, student_router, course_router)', shape='rect')
dot.node('Middleware', 'Middleware (Rate Limiting)', shape='rect')
dot.node('Controllers', 'Controllers (auth_controller, admin_controller, etc.)', shape='rect')
dot.node('Repositories', 'Repositories (admin_repository, student_repository, etc.)', shape='rect')
dot.node('Database', 'Database (student_model, admin_model, course_model)', shape='rect')
dot.node('Services', 'Services (auth.py, helping_functions.py)', shape='rect')
dot.node('Static', 'Static Files (favicon.png)', shape='rect')

# Define the interactions between components
dot.edge('Client', 'FastAPI', label='HTTP Request')
dot.edge('FastAPI', 'Routers', label='Route Request')
dot.edge('Routers', 'Middleware', label='Apply Rate Limiting')
dot.edge('Middleware', 'Controllers', label='Forward Request to Controller')
dot.edge('Controllers', 'Repositories', label='Query Database')
dot.edge('Repositories', 'Database', label='Perform CRUD Operations')
dot.edge('Controllers', 'Services', label='Use Utility Functions')
dot.edge('Services', 'Repositories', label='Query Database')  # Updated to reflect Services querying Repositories
dot.edge('Services', 'Database', label='Access DB for Data')  # Optional if Services interact directly with DB
dot.edge('FastAPI', 'Static', label='Serve Favicon')

# Add some dependencies between routers and controllers
dot.edge('Routers', 'Controllers', label='Forward Request to Controller Functions')

# Visual adjustments
dot.attr(dpi='300', rankdir='TB', size='10,12', nodesep='0.7', ranksep='1')

# Render the updated diagram to a file
dot.render('cms_architecture_diagram', format='png', cleanup=True)

# Optionally, you can change the path where the diagram is saved or view it after rendering.
