"""
Management command to seed 10 sample courses with categories and lessons.
Run: python manage.py seed_courses
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from courses.models import Course, Category
from lessons.models import Lesson


SAMPLE_COURSES = [
    {
        'title': 'Python for Beginners',
        'category': 'Programming',
        'description': 'Learn Python from scratch. Variables, loops, functions, and basic data structures. Perfect for absolute beginners.',
        'level': Course.Level.BEGINNER,
        'duration': '6 hours',
        'lessons': [
            {'title': 'Introduction to Python', 'video_url': 'https://www.youtube.com/watch?v=_uQrJ0TkZlc', 'content': 'What is Python and why learn it?'},
            {'title': 'Variables and Data Types', 'video_url': 'https://www.youtube.com/watch?v=khKv-8q7YmY', 'content': 'Strings, numbers, and basic types.'},
            {'title': 'Loops and Conditionals', 'video_url': 'https://www.youtube.com/watch?v=6iF8Xb7Zzpw', 'content': 'if/else, for and while loops.'},
            {'title': 'Functions', 'video_url': 'https://www.youtube.com/watch?v=NSbOtYzIQI0', 'content': 'Defining and calling functions.'},
        ],
    },
    {
        'title': 'Web Development with Django',
        'category': 'Web Development',
        'description': 'Build full-stack web applications with Django. Models, views, templates, and deployment.',
        'level': Course.Level.INTERMEDIATE,
        'duration': '12 hours',
        'lessons': [
            {'title': 'Django Setup', 'video_url': 'https://www.youtube.com/watch?v=rHux0gMZ3Eg', 'content': 'Install Django and create your first project.'},
            {'title': 'Models and Migrations', 'video_url': 'https://www.youtube.com/watch?v=6oRHhDcFqTU', 'content': 'Define models and run migrations.'},
            {'title': 'Views and URLs', 'video_url': 'https://www.youtube.com/watch?v=VOdd7JOhAtc', 'content': 'Write views and wire up URLs.'},
            {'title': 'Templates', 'video_url': 'https://www.youtube.com/watch?v=qn0nB2L1_2w', 'content': 'Django template language and inheritance.'},
        ],
    },
    {
        'title': 'JavaScript Fundamentals',
        'category': 'Programming',
        'description': 'Master JavaScript: DOM manipulation, events, async/await, and modern ES6+ syntax.',
        'level': Course.Level.BEGINNER,
        'duration': '8 hours',
        'lessons': [
            {'title': 'JavaScript Basics', 'video_url': 'https://www.youtube.com/watch?v=W6NZfCO5SIk', 'content': 'Variables, types, and operators.'},
            {'title': 'Functions and Scope', 'video_url': 'https://www.youtube.com/watch?v=N8ap4k_1QEQ', 'content': 'Functions, closures, and scope.'},
            {'title': 'DOM Manipulation', 'video_url': 'https://www.youtube.com/watch?v=5fb2aPlgoys', 'content': 'Select and modify the DOM.'},
            {'title': 'Async JavaScript', 'video_url': 'https://www.youtube.com/watch?v=PoRJizFvM7s', 'content': 'Promises and async/await.'},
        ],
    },
    {
        'title': 'Data Science with Python',
        'category': 'Data Science',
        'description': 'Pandas, NumPy, and Matplotlib. Clean data, analyze it, and visualize results.',
        'level': Course.Level.INTERMEDIATE,
        'duration': '10 hours',
        'lessons': [
            {'title': 'NumPy Basics', 'video_url': 'https://www.youtube.com/watch?v=QUT1VHiLmmI', 'content': 'Arrays and array operations.'},
            {'title': 'Pandas DataFrames', 'video_url': 'https://www.youtube.com/watch?v=vmEHCGofBt8', 'content': 'Loading and manipulating data.'},
            {'title': 'Data Cleaning', 'video_url': 'https://www.youtube.com/watch?v=8qTxF2jTgbk', 'content': 'Handling missing values and outliers.'},
            {'title': 'Visualization with Matplotlib', 'video_url': 'https://www.youtube.com/watch?v=DAQNHzOcO5A', 'content': 'Charts and plots.'},
        ],
    },
    {
        'title': 'SQL and Databases',
        'category': 'Databases',
        'description': 'Learn SQL from scratch. SELECT, JOINs, subqueries, and database design basics.',
        'level': Course.Level.BEGINNER,
        'duration': '5 hours',
        'lessons': [
            {'title': 'Introduction to SQL', 'video_url': 'https://www.youtube.com/watch?v=p3qvj9hO_Bo', 'content': 'What is SQL and relational databases?'},
            {'title': 'SELECT and WHERE', 'video_url': 'https://www.youtube.com/watch?v=2-1XQHAgDsM', 'content': 'Querying data with conditions.'},
            {'title': 'JOINs', 'video_url': 'https://www.youtube.com/watch?v=9yeOJ0ZMUYw', 'content': 'INNER, LEFT, and RIGHT JOINs.'},
            {'title': 'Aggregations and GROUP BY', 'video_url': 'https://www.youtube.com/watch?v=Ww71kcvxmfa', 'content': 'COUNT, SUM, AVG, GROUP BY.'},
        ],
    },
    {
        'title': 'React.js for Frontend',
        'category': 'Web Development',
        'description': 'Build modern UIs with React. Components, hooks, state, and routing.',
        'level': Course.Level.INTERMEDIATE,
        'duration': '14 hours',
        'lessons': [
            {'title': 'React Setup and JSX', 'video_url': 'https://www.youtube.com/watch?v=SqcY0Gl6PgA', 'content': 'Create React App and JSX basics.'},
            {'title': 'Components and Props', 'video_url': 'https://www.youtube.com/watch?v=IYvD9oBCuJI', 'content': 'Functional components and props.'},
            {'title': 'State and Hooks', 'video_url': 'https://www.youtube.com/watch?v=O6P86uwfdR0', 'content': 'useState and useEffect.'},
            {'title': 'React Router', 'video_url': 'https://www.youtube.com/watch?v=Ul3y1LXxzdU', 'content': 'Client-side routing.'},
        ],
    },
    {
        'title': 'Git and GitHub',
        'category': 'DevOps',
        'description': 'Version control with Git. Commit, branch, merge, and collaborate on GitHub.',
        'level': Course.Level.BEGINNER,
        'duration': '4 hours',
        'lessons': [
            {'title': 'Git Basics', 'video_url': 'https://www.youtube.com/watch?v=8JJ101D3knE', 'content': 'Install Git, init, add, commit.'},
            {'title': 'Branching and Merging', 'video_url': 'https://www.youtube.com/watch?v=FyAAIHHClqI', 'content': 'Create branches and merge.'},
            {'title': 'Working with GitHub', 'video_url': 'https://www.youtube.com/watch?v=RGOj5yH7evk', 'content': 'Push, pull, and remote repos.'},
            {'title': 'Pull Requests', 'video_url': 'https://www.youtube.com/watch?v=8lGpZkjnkt4', 'content': 'Collaboration and code review.'},
        ],
    },
    {
        'title': 'Machine Learning Basics',
        'category': 'Data Science',
        'description': 'Introduction to ML. Linear regression, classification, and scikit-learn.',
        'level': Course.Level.ADVANCED,
        'duration': '15 hours',
        'lessons': [
            {'title': 'What is Machine Learning?', 'video_url': 'https://www.youtube.com/watch?v=ukzFI9rgwfU', 'content': 'Supervised vs unsupervised learning.'},
            {'title': 'Linear Regression', 'video_url': 'https://www.youtube.com/watch?v=4b4MUYve_U8', 'content': 'Fitting a line to data.'},
            {'title': 'Classification', 'video_url': 'https://www.youtube.com/watch?v=J4Wdy0Wc_xQ', 'content': 'Logistic regression and decision trees.'},
            {'title': 'Scikit-learn', 'video_url': 'https://www.youtube.com/watch?v=0B5eIE_dsbo', 'content': 'Using the scikit-learn library.'},
        ],
    },
    {
        'title': 'HTML and CSS',
        'category': 'Web Development',
        'description': 'Build and style web pages. Semantic HTML, Flexbox, Grid, and responsive design.',
        'level': Course.Level.BEGINNER,
        'duration': '7 hours',
        'lessons': [
            {'title': 'HTML Structure', 'video_url': 'https://www.youtube.com/watch?v=PlxWf493en4', 'content': 'Tags, headings, lists, links.'},
            {'title': 'CSS Selectors and Box Model', 'video_url': 'https://www.youtube.com/watch?v=1Rs2ND1ryYc', 'content': 'Selectors, margin, padding.'},
            {'title': 'Flexbox', 'video_url': 'https://www.youtube.com/watch?v=K74l26pE4YA', 'content': 'Flexbox layout.'},
            {'title': 'Responsive Design', 'video_url': 'https://www.youtube.com/watch?v=srvUrASNj0s', 'content': 'Media queries and mobile-first.'},
        ],
    },
    {
        'title': 'REST APIs with Django REST Framework',
        'category': 'Web Development',
        'description': 'Build RESTful APIs with Django REST Framework. Serializers, viewsets, and authentication.',
        'level': Course.Level.ADVANCED,
        'duration': '9 hours',
        'lessons': [
            {'title': 'Introduction to REST', 'video_url': 'https://www.youtube.com/watch?v=Q-BpqyOT3a8', 'content': 'REST principles and HTTP methods.'},
            {'title': 'DRF Setup and Serializers', 'video_url': 'https://www.youtube.com/watch?v=c708Nf0cHr0', 'content': 'Install DRF and create serializers.'},
            {'title': 'ViewSets and Routers', 'video_url': 'https://www.youtube.com/watch?v=6VbL_bVlR2E', 'content': 'ModelViewSet and URL routing.'},
            {'title': 'Authentication', 'video_url': 'https://www.youtube.com/watch?v=0d7c4i8ny5E', 'content': 'Token and session auth.'},
        ],
    },
]


class Command(BaseCommand):
    help = 'Seed 10 sample courses with categories and lessons.'

    def handle(self, *args, **options):
        categories_created = {}
        for data in SAMPLE_COURSES:
            cat_name = data['category']
            if cat_name not in categories_created:
                cat, _ = Category.objects.get_or_create(
                    name=cat_name,
                    defaults={'slug': slugify(cat_name)}
                )
                categories_created[cat_name] = cat
            category = categories_created[cat_name]

            slug = slugify(data['title'])
            course, created = Course.objects.update_or_create(
                slug=slug,
                defaults={
                    'title': data['title'],
                    'category': category,
                    'description': data['description'],
                    'level': data['level'],
                    'duration': data['duration'],
                    'status': Course.Status.PUBLISHED,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created course: {course.title}'))
            else:
                self.stdout.write(f'Updated course: {course.title}')

            for i, lesson_data in enumerate(data['lessons'], start=1):
                Lesson.objects.update_or_create(
                    course=course,
                    order=i,
                    defaults={
                        'title': lesson_data['title'],
                        'video_url': lesson_data.get('video_url', ''),
                        'content': lesson_data.get('content', ''),
                    }
                )
            self.stdout.write(f'  -> {len(data["lessons"])} lessons')

        self.stdout.write(self.style.SUCCESS('Seed complete. 10 courses with lessons are ready.'))
