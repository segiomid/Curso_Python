from sqlite3 import DatabaseError


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    
    # List Comprehensions
    all_python_devs = [worker['name'] for worker in DATA if worker['language']=='python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization']=='Platzi']
    
    all_adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    all_old_people = [worker | {"old": worker["age"]> 70} for worker in DATA]

    # High order functions
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))

    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

    all_python_devs_func = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_func = list(map(lambda worker: worker['name'], all_python_devs_func))

    all_platzi_workers_func = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_func = list(map(lambda worker: worker['name'], all_platzi_workers_func))

    for worker in all_old_people:
        print(worker)

if __name__=='__main__':
    run()