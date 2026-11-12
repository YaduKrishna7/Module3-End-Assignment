from django.shortcuts import render
def resume_view(request):

    # Resume information stored in a Python dictionary
    resume = {
        'name': 'Yadu Krishna',
        'age': 23,
        'gender': 'Male',
        'email': 'yaduvalsaraj1007.11@gmail.com',

        # Skills stored in a list
        'skills': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'JavaScript',
            'REST APIs',
            'PostgreSQL',
            'MySQL',
            'Sqlite'
        ],
        # Education details stored in a dictionary
        'education': {
            'degree': 'B.Tech Information Technology',
            'institution': 'Calicut University Institute of Engineering and Technology',
            'year': '2026',
            'grade': '7.2'
        }
    }

    # Pass resume dictionary to HTML template
    return render(request, 'myapp/resume.html', {'resume': resume})
