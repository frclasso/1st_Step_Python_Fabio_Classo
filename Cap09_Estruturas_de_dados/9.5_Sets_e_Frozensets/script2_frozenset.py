
tecnologias = {'Python', 'Django', 'Big Data', 'Data Science','SQL', 'NoSQl'}
print(type(tecnologias))
tecnologias.add('Django')
tecnologias.add('Big Data')
print(tecnologias)

tecnologias_2 = frozenset(tecnologias)
#tecnologias_2.add('Python') # AttributeError: 'frozenset' object has no attribute 'add'
print(type(tecnologias_2))

# simulando um frozenset
tech = tuple({'Python', 'Django', 'Python', 'Django'})
print(f'Simulando um frozenset: {type(tech)}: {tech}')
