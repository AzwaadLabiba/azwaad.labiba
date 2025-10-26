from flask_frozen import Freezer
from app import app

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_FILES'] = True

# Add this line:
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore']

freezer = Freezer(app)

# Add URL generators to append .html
@freezer.register_generator
def page_urls():
    for page in ['education', 'experience', 'publications', 'achievements']:
        yield 'page', {'page': page}
