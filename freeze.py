from flask_frozen import Freezer
from app import app

# Configure freezer
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

# No need to register generators for static routes - they're auto-discovered!
# Only register if you have dynamic routes like /blog/<slug>

if __name__ == '__main__':
    freezer.freeze()
    print("\n" + "="*60)
    print("Site frozen successfully!")
    print("Output directory: build/")
    print("="*60)