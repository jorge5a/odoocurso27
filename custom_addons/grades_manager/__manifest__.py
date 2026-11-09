
{
'name': 'Grades Manager',
'version': '1.0',
'description': 'Módulo para gestionar las calificaciones de los estudiantes',
'category': 'Tools',
'depends': ['base'],
'data': [
    'security/ir.access.csv',
    'views/grades_course_views.xml',
    'views/grades_teachers_views.xml',
    'views/grades_manager_menus.xml',
],

'application': True,
}