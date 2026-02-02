from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = 'Seed the database with professional sample courses.'

    def handle(self, *args, **kwargs):
        courses = [
            {
                'title': 'Python for Beginners',
                'description': 'Learn Python from scratch. Variables, loops, functions, and more.',
                'instructor': 'Alice Smith',
                'duration': '6 hours',
                'level': 'Beginner',
            },
            {
                'title': 'Web Development with Django',
                'description': 'Build web applications using Django. Models, views, templates, and deployment.',
                'instructor': 'Bob Johnson',
                'duration': '12 hours',
                'level': 'Intermediate',
            },
            {
                'title': 'JavaScript Fundamentals',
                'description': 'Master JavaScript: DOM manipulation, events, async/await, and ES6+ syntax.',
                'instructor': 'Carol Lee',
                'duration': '8 hours',
                'level': 'Beginner',
            },
            {
                'title': 'Machine Learning Basics',
                'description': 'Introduction to ML. Linear regression, classification, and scikit-learn.',
                'instructor': 'David Kim',
                'duration': '15 hours',
                'level': 'Advanced',
            },
            {
                'title': 'React.js for Frontend',
                'description': 'Build modern UIs with React. Components, hooks, state, and routing.',
                'instructor': 'Eva Brown',
                'duration': '14 hours',
                'level': 'Intermediate',
            },
            {
                'title': 'SQL and Databases',
                'description': 'Learn SQL from scratch. SELECT, JOINs, subqueries, and database design basics.',
                'instructor': 'Frank Green',
                'duration': '5 hours',
                'level': 'Beginner',
            },
            {
                'title': 'REST APIs with Django REST Framework',
                'description': 'Build RESTful APIs with Django REST Framework. Serializers, viewsets, and authentication.',
                'instructor': 'Grace White',
                'duration': '9 hours',
                'level': 'Advanced',
            },
            {
                'title': 'Data Science with Python',
                'description': 'Pandas, NumPy, and Matplotlib. Clean data, analyze it, and visualize results.',
                'instructor': 'Henry Black',
                'duration': '10 hours',
                'level': 'Intermediate',
            },
            {
                'title': 'HTML and CSS',
                'description': 'Build and style web pages. Semantic HTML, Flexbox, Grid, and responsive design.',
                'instructor': 'Ivy Wilson',
                'duration': '7 hours',
                'level': 'Beginner',
            },
            {
                'title': 'Git and GitHub',
                'description': 'Version control with Git. Commit, branch, merge, and collaborate on GitHub.',
                'instructor': 'Jack Brown',
                'duration': '4 hours',
                'level': 'Beginner',
            },
        ]
        for c in courses:
            Course.objects.get_or_create(**c)
        self.stdout.write(self.style.SUCCESS('Successfully seeded professional sample courses.'))
