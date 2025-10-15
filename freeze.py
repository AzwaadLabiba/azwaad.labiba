# freeze.py
from flask_frozen import Freezer
from app import app, db, Professor, Student, Project, Publication, LabInfo

# Configure freezer
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)

# Generate URLs for all dynamic routes
@freezer.register_generator
def project_detail():
    """Generate URLs for all project detail pages"""
    with app.app_context():
        projects = Project.query.all()
        for project in projects:
            yield {'project_id': project.id}

if __name__ == '__main__':
    with app.app_context():
        freezer.freeze()
    print("\n" + "="*60)
    print("Site frozen successfully!")
    print("Output directory: build/")
    print("="*60)